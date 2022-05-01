import asyncio
import hashlib
import os
import pathlib

import discord
import dotenv

from horny_police import detection
from horny_police import logging

dotenv.load_dotenv()


class HornyPoliceClient(discord.Client):
    logger = logging.get_logger()
    REPLY_IMAGE = pathlib.Path("/workspaces/horny-police/reply_image.png")

    if not os.getenv("TEMP_SAVE_DIRECTORY"):
        logger.error(
            "temp directory for saving files not configured, "
            "please configure in environment variables."
        )
        raise FileExistsError()

    temporary_directory = pathlib.Path(os.getenv("TEMP_SAVE_DIRECTORY"))  # type: ignore

    async def on_ready(self) -> None:
        HornyPoliceClient.logger.info("bot ready for tasking...")
    
    async def on_message(self, message: discord.Message) -> None:
        attachments = message.attachments

        if not attachments:
            return

        if message.author.id == self.user.id: # type: ignore
            return

        HornyPoliceClient.logger.info("detected message with attachments, scanning...")

        for attachment in attachments:
            
            HornyPoliceClient.logger.info(
                f"checking {attachment.content_type} file of name {attachment.filename}"
            )

            if not detection.attachment_can_be_checked(attachment.content_type):
                continue

            HornyPoliceClient.logger.info(
                f"file {attachment.filename} can be checked, proceeding to check..."
            )

            attachment_content = await attachment.read()

            attachment_hash = hashlib.md5(attachment_content).hexdigest()

            attachment_file_path = HornyPoliceClient.temporary_directory / (
                attachment_hash + "." + attachment.filename.split(".")[1]
            )

            attachment_file_path.write_bytes(attachment_content)

            HornyPoliceClient.logger.info(
                f"attachment {attachment.filename} "
                f"saved to local path {attachment_file_path.absolute()}"
            )

            result = detection.detect_nsfw(attachment_file_path)

            if result["unsafe"] >= 0.40:
                HornyPoliceClient.logger.info(
                    f"file {attachment.filename} likely nsfw, deleting"
                )

                await message.reply(
                    f"deleted <@{message.author.id}>'s nsfw message.",   # type: ignore
                    file=discord.File(HornyPoliceClient.REPLY_IMAGE)
                )
                await message.delete()

                attachment_file_path.unlink()





            



            


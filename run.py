import os

from horny_police import client
from horny_police import logging


def main() -> None:
    logger = logging.get_logger()

    logger.info("bot starting up...")

    bot = client.HornyPoliceClient()

    bot.run(os.getenv("CLIENT_TOKEN"))

if __name__ == "__main__":
    main()
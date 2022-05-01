![Horny Police Image Banner](./reply_image.png)

# horny_police
NSFW content moderation bot for Discord.

## Usage
1. Clone down the repository.
2. Build the image with `docker build -t horny_police:latest .`
3. Run the image with `docker run horny_police -e TEMP_SAVE_DIRECTORY=<SOMEWHERE_TO_TEMP_DOWNLOAD_FILES_TO> -e CLIENT_TOKEN=<YOUR_CLIENT_TOKEN>`

## Credits
### @bedapudi6788
> The bot uses their NudeNet model for classifying NSFW content. 
>
> [Model can be found here](https://github.com/notAI-tech/NudeNet). 
>
> [Their blog can be found here](http://bpraneeth.com/).

## Notes
### ([Issue #1](https://github.com/backplateorbit/horny-police/issues/1)) INVALID_PROTOBUF error.
The `ADD` directives in the Docker file may fail with a 401 from Github. This is because you need to be logged in to access NSFW repositories on Github. To mitigate this, use the links in the Dockerfile to download the model files yourself, and tweak the Dockerfile to use the `COPY` directive to copy them in instead of `ADD` which copies them from a remote URL.

### ([Issue #9](https://github.com/backplateorbit/horny-police/issues/9)) Docker Image Size
The built docker image for the bot is huge. Sorry about that.
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
>[Model can be found here](https://github.com/notAI-tech/NudeNet). 
>
> [Their blog can be found here](http://bpraneeth.com/).
# disco-bot
music suggestion bot for discord.<br/>
d-hello: Greeting message,<br/>
d-h: Suggest happy songs,<br/>
d-l: Suggest sad songs,<br/>
d-charts: YT links of top10 chart hits<br />
dg-"genre": YT links of "genre" playlist<br />
da-"artist": YT links of top10 tracks of "artist"<br />
d-help: Info about the bot<br/><br/>

url for bot: https://discord.com/api/oauth2/authorize?client_id=800048826756890655&permissions=3214400&scope=bot

## Setting up the bot
### Configuring the bot
To begin configuring disco-bot, create a `config.py` file placed in the disco_bot folder alongside `__main__.py`.
This is where your bot token and LastFM API token will be loaded from.

It is recommended to import sample_config and extend the Config class, as this will ensure your config contains all defaults set in the sample_config, hence making it easier to upgrade.

An example `config.py` file could be:

```
from disco_bot.sample_config import Config

class Development(Config):
    BOT_TOKEN = "YOUR BOT TOKEN HERE"
    API_KEY = "YOUR LastFM API KEY HERE"
    USER_AGENT = "Aratrika Ray"
    BOT_COLOR = 0xB39DDB
```

### Installing Python dependencies
Install the necessary python dependencies by moving to the project directory and running:

`pip3 install -r requirements.txt`.

This will install all necessary python packages.

### Running the bot
After you've configured all the required variables and installed all the required libraries, it's time to run the bot!
To start the bot, simply run the following:
```
python3 -m disco_bot
```
And you're done!

The bot is now up and running ready to serve your favourite music artists, types, genres or anything else you need!


# disco-bot
music suggestion bot for discord.<br/>
d-hello: Greeting message,<br/>
d-h: Suggest happy songs,<br/>
d-l: Suggest sad songs,<br/>
d-charts: YT links of top10 chart hits<br />
dg-<genre>: YT links of <genre> playlist<br />
da-<artist>: YT links of top10 tracks of <artist><br />
d-help: Info about the bot<br/><br/>

url for bot: https://discord.com/api/oauth2/authorize?client_id=800048826756890655&permissions=3214400&scope=bot

## Setting up the bot
There are two possible ways of configuring your bot: an env file, or ENV variables.

The prefered version is to use an `env` file, as it makes it easier to see all your settings grouped together.
This file should be placed in the root of the project where the sample_env is.
This is where your bot token will be loaded from.

It is recommended to rename sample_env to env, as this will ensure your env contains all necessary values.

### Python dependencies

Install the necessary python dependencies by moving to the project directory and running:

`pip3 install -r requirements.txt`.

This will install all necessary python packages.

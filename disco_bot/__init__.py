import sys
# if version < 3.8, stop bot.
if sys.version_info[0] < 3 or sys.version_info[1] < 8:
	LOGGER.error("You MUST have a python version of at least 3.8! Multiple features depend on this. Bot quitting.")
	quit(1)

from disco_bot.config import Development as Config
api_key = Config.API_KEY
token = Config.BOT_TOKEN
user_agent = Config.USER_AGENT

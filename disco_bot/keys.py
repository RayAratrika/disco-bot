import os;
from dotenv import load_dotenv;

load_dotenv();
def bot_token():
	return os.getenv('BOT_TOKEN');
def lfm_api_key():
	return os.getenv('API_KEY');
def lfm_user_agent():
	return os.getenv('USER_AGENT');
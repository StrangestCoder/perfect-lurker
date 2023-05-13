import os
from dotenv import load_dotenv
load_dotenv()

client_id = os.environ['CLIENT_ID']
access_token= os.environ['ACCES_TOKEN']
users_oauth_token = os.environ['USER_OAUTH_TOKEN']
users_channel_id = int(os.environ['USER_CHANNEL_ID'])
initial_channel = os.environ['INITIAL_CHANNEL']
moderator_id = os.environ['MODERATOR_ID']

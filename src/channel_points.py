import twitchio
import asyncio
from twitchio.ext import pubsub
from src.configuration import access_token

class Client():

    def __init__(self):
        # Initialise our Bot with our access token, prefix and a list of channels to join on boot...
        # prefix can be a callable, which returns a list of strings or a string...
        # initial_channels can also be a callable which returns a list of strings...
        super().__init__(token=access_token, prefix='?', initial_channels=['simulakrum'])
    
    @client.event(self)
    async def handle_pubsub_event(event: pubsub.PubSubChannelPointsMessage):
        print(event)
        if event.message.type == 'reward-redeemed':
            reward_id = event.message.data['redemption']['reward']['id']
            if reward_id == 'perfect-lurker' and event.message.data['redemption']['user']['points_balance'] >= 10:
                print('bazinga')

    @client.event(self)
    async def event_pubsub_channel_points(event: pubsub.PubSubChannelPointsMessage):
        print(event)

    async def on_connect(self):
        await client.pubsub.subscribe('channel-points-rewards-redemption.' + client.nick + '.' + str(client.channel_id))

client = twitchio.Client(token=access_token)
client.pubsub = pubsub.PubSubPool(client)
client.run()

import twitchio
import asyncio
from twitchio.ext import pubsub
from src.basic_bot import Bot
from src.channel_points import Client
import src.configuration

async def main():
    mahclient= Client()
    mahclient.topics = [
        pubsub.channel_points(users_oauth_token)[users_channel_id],
        pubsub.bits(users_oauth_token)[users_channel_id]
    ]
    await mahclient.pubsub.subscribe_topics(topics)
    await mahclient.start()
    bot = Bot()
    bot.run()

    mahclient.loop.run_until_complete(main())

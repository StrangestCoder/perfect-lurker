from twitchio.ext import commands, eventsub
import twitchio
from src.configuration import access_token, client_id, initial_channel

esbot = commands.Bot.from_client_credentials(client_id=client_id, client_secret=access_token)
esclient = eventsub.EventSubClient(esbot, webhook_secret="...", callback_route="https://localhost:4000")

class Bot(commands.Bot):

    def __init__(self):
        # Initialise our Bot with our access token, prefix and a list of channels to join on boot...
        # prefix can be a callable, which returns a list of strings or a string...
        # initial_channels can also be a callable which returns a list of strings...
        super().__init__(token=access_token, prefix='?', initial_channels=['simulakrum'])

    async def __ainit__(self) -> None:
        self.loop.create_task(esclient.listen(port=4000))
        try:
            await esclient.subscribe_channel_follows_v2(broadcaster=5016229, moderator=5016229)
        except twitchio.HTTPException:
            pass

    async def event_ready(self):
        # Notify us when everything is ready!
        # We are logged in and ready to chat and use commands...
        print(f'Bot Logged in as | {self.nick}')
        print(f'Bot User id is | {self.user_id}')

    async def event_message(self, message):
        # Messages with echo set to True are messages sent by the bot...
        # For now we just want to ignore them...
        if message.echo:
            return

        # Print the contents of our message to console...
        print(message.content)

        # Since we have commands and are overriding the default `event_message`
        # We must let the bot know we want to handle and invoke our commands...
        await self.handle_commands(message)

    @commands.command()
    async def join(self, ctx: commands.Context):
        # Here we have a command join, we can invoke our command with our prefix and command name
        # e.g ?join
        # We can also give our commands aliases (different names) to invoke with.
        # Sending a reply back to the channel is easy... Below is an example.
        print(f'{ctx.author.name} squeezed in the clowncar. clowns. muhahaha')

bot = Bot()
bot.loop.run_until_complete(bot.__ainit__())

@esbot.event()
async def event_eventsub_notification_followV2(payload: eventsub.ChannelFollowData) -> None:
    print("Received event!")
    channel = bot.get_channel("channel")
    await channel.send(f"{payload.data.user.name} followed woohoo!")

bot.run()
# bot.run() is blocking and will stop execution of any below code here until stopped or closed.

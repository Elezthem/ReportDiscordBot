import discord

intents = discord.Intents.all()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Bot {client.user.name} is ready')
    print('------')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!report'):
        report_channel_id = 123456789012345678 # Replace with the ID of the channel where reports will be sent

        report_text = message.content[8:]  # Remove "!report " from the message

        report_channel = client.get_channel(report_channel_id)
        if report_channel is not None:
            await report_channel.send(f'Report from {message.author.name}#{message.author.discriminator}: {report_text}')
            await message.channel.send('Report sent successfully!')
        else:
            await message.channel.send('Cannot find a channel to send reports.')

# Replace 'YOUR_BOT_TOKEN' with your bot token
client.run('YOUR_BOT_TOKEN')

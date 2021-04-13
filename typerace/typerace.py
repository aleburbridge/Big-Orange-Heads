import discord 
import random
import datetime
from raceprompts import text
client = discord.Client()

TOKEN = 'YOUR TOKEN HERE'
channelID = 'YOUR ID HERE (int)'

@client.event
async def on_ready():
    general_channel = client.get_channel(channelID)
    print('Connected Successfully')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('race'):
        channel = message.channel
        textAnswer = text[random.randint(0,(len(text) -1))]

        def check(m):
            return m.content == textAnswer and m.channel == channel

        bot_msg = await channel.send(textAnswer)
        human_msg = await client.wait_for('message', check=check)
        
        time1 = bot_msg.created_at
        time2 = human_msg.created_at
        duration = time2 - time1
        minutes = duration.total_seconds()/60
        wpm = int((len(textAnswer)/5) / minutes)

        await channel.send(f'{human_msg.author.name} is the winner, with a typing speed of {wpm} WPM!')

client.run(TOKEN)
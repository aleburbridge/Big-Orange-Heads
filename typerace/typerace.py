import discord 
import random
import datetime
from raceprompts import text
client = discord.Client()

TOKEN = 

@client.event
async def on_ready():
    print('WPM game connected')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('race'):
        channel = message.channel
        textAnswer = text[random.randint(0,(len(text) -1))]
        def check(m):
            return textAnswer in m.content and m.channel == channel

        bot_msg = await channel.send(textAnswer)
        human_msg = await client.wait_for('message', check=check)
        
        duration = human_msg.created_at - bot_msg.created_at 
        minutes = duration.total_seconds()/60
        wpm = int((len(textAnswer)/5) / minutes)
        await channel.send(f'{human_msg.author.name} is the winner, with a typing speed of {wpm} WPM!')

client.run(TOKEN)
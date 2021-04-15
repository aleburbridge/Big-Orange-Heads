import discord 
client = discord.Client()

TOKEN = 

@client.event
async def on_ready():
    print('Bob has connected')

players = ['Tsukimoto','Hoshino','Kazama','Sukano']

@client.event
async def on_message(message):
    if message.content.startswith('$boh'):
        embed=discord.Embed(title=f"Genie: {players[-1]}", description="-------------------------------------", color=0xffa200)
        embed.set_thumbnail(url="https://pathfinderwiki.com/mediawiki/images/0/01/Zhyen.jpg")
        for i in range(len(players)):
            embed.add_field(name=f"{players[i]}\'s Gold\u200B", value="n", inline=True)
            embed.add_field(name=f"{players[i]}\'s Wishes\u200B", value="n", inline=True)
            embed.add_field(name=f"{players[i]}\'s Head", value="BIG AND ORANGE", inline=True)
        embed.add_field(name="Items", value="Trumpet\nFife\nTabour")  

        await message.channel.send(embed=embed)

client.run(TOKEN)
import discord
from discord.ext import commands
import youtube_dl

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def play(ctx, url : str):
    # Verbinden Sie den Bot mit dem Sprachkanal des Benutzers
    channel = ctx.author.voice.channel
    await channel.connect()

    # Verwenden Sie youtube_dl, um die Musik aus der URL abzuspielen
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    # Laden Sie die heruntergeladene Musikdatei und senden Sie sie an den Sprachkanal
    source = discord.FFmpegPCMAudio("song.mp3")
    ctx.voice_client.play(source)

bot.run("MTA2Mzk0ODEwNjYxNTQ5Njc3NQ.Gp1vwI.Ll4ORjV3eEDCwSy0e6Iic2dbq9tiCdPnKhTlH4")
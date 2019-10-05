import os
import time
import discord
import random



TOKEN = "Can't tell you that"

from discord.ext import commands

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print(
        f'{bot.user} is connected to discord!'
    )

@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f"Hi {member.name}, welcome to the server!"
    )

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return


    if "lasagna" in message.content.lower() or "lasagne" in message.content.lower():
        response = "did somebody say lasagna?"
        await message.channel.send(response)

    if message.content.lower() == "garfdaily":
        localtime = time.gmtime()
        if len(str(localtime.tm_mday)) == 1:
            day = "0" + str(localtime.tm_mday)
        else:
            day  = localtime.tm_mday

        garfFileName = "https://d1ejxu6vysztl5.cloudfront.net/comics/garfield/2019/"+str(localtime.tm_year)+"-"+str(localtime.tm_mon)+"-"+day+".gif"

        await message.channel.send(garfFileName)
        print ("A user requested this comic:", garfFileName)
    
    if message.content.lower() == "garfrandom":
        daycap = 31
        localtime = time.gmtime()
            
        randomYear = str(random.randint(1979, localtime.tm_year - 1))
        randomMonth = random.randint(1,12)
        if randomMonth == 2:
            daycap = 28
        elif randomMonth == 4 or randomMonth == 6 or randomMonth == 9 or randomMonth == 11:
            daycap = 30
        randomDay = str(random.randint(1,daycap))
        
        if len(randomDay) == 1:
            randomDay = "0" + randomDay
            
        randomMonth = str(randomMonth)

        if len(randomMonth) == 1:
            randomMonth = "0" + randomMonth
        
        garfFileName = "https://d1ejxu6vysztl5.cloudfront.net/comics/garfield/"+randomYear+"/"+randomYear+"-"+randomMonth+"-"+randomDay+".gif"
        await message.channel.send(garfFileName)
        
    if message.content.lower() == "garftrivia":
        trivias = ["Trivia fact #1: Garfield is an orange cat", "Trivia fact #2: Garfield was started on june 19th 1978", "Trivia fact #3: GarfieldEATS is the offical Garfield Resteraunt and food delivery service.", "Trivia fact #4: Jon Arbuckle's job is a cartoonist."]
        await message.channel.send(random.choice(trivias))

bot.run(TOKEN)

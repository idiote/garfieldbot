import os
import time
import discord
import random

character = ['Garfield', 'Jon', 'Odie', 'Liz', 'Lyman', 'A spider']
verb = ['kills', 'belittles', 'meets', 'eats', 'hurts', 'yells at', 'hugs', 'kisses', 'befriends', 'uses', 'talks to', 'jokes about', 'wants', 'reads', 'beats up', 'screams at', 'is scared of', 'watches', 'destroys']
noun = ['Odie', 'Jon', 'a spider', 'Garfield', 'Liz', 'you', 'lasagna', 'an accordion', 'Pooky', 'Lyman', 'a comic', 'a dog', 'money', 'the tv', 'a book', 'the window', 'a car', 'him/herself', 'food']



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
        trivias = ["Trivia fact #1: Garfield is an orange cat", 
                   "Trivia fact #2: Garfield was first published on June 19th 1978", 
                   "Trivia fact #3: GarfieldEATS is the offical Garfield Restauraunt and food delivery service.", 
                   "Trivia fact #4: Jon Arbuckle works as a cartoonist.", 
                   "Trivia fact 5#: Nermal is male.", 
                   "Trivia fact # 6: Odie was originally owned by Lyman, before being given to Jon.", 
                   "Trivia fact #7: Garfield has a teddy bear named Pooky.", 
                   "Trivia fact #8: Liz is a vet.", 
                   "Trivia fact #9: In 'Long Lost Lyman,' an episode of The Garfield Show, it’s revealed that Lyman became a wildlife photographer.",
                   "Trivia fact #10: Despite Garfield drinking his fair share of coffee, it is actually very dangerous for cats, dogs  most small pets to have caffeine.",
                   "Trivia fact #11: On the February 2nd, 2013 comic strip, Garfield built a scale model replica of the parthenon, only to eat it later as it was made of chocolate.",
                   "Trivia fact #12: According to the christmas eve 2018 comic, Santa is real in the Garfield universe.",
                   "Trivia fact #13: Jons Father, Mother and Brother all work on a farm together."
                  ]
        
        await message.channel.send(random.choice(trivias))

        
    if message.content.lower() == "garfhelp":
        helpcommands = ["garfdaily - sends the daily Garfield comic", 
                        "garfrandom - sends a random Garfield comic", 
                        "garftrivia - sends a random fact about Garfield", 
                        "odiekick - sends a gif of Garfield kicking Odie",
                        "garflinks - important garfield links",
                        "garfprompt - comes up with a random garfield based prompt"
                       ]

        helpmessage = "Garfield Bot 1.0 Commands\n```"

        for i in range(len(helpcommands)):
            helpmessage += helpcommands[i]
            helpmessage += "\n \n"

        helpmessage += "```"
        
        await message.channel.send(helpmessage)
        
    if message.content.lower() == "odiekick":
        response = "http://66.media.tumblr.com/tumblr_lq5hk354UG1qbqwr6o1_400.gif"
        await message.channel.send(response)
        
    if message.content.lower() == "garflinks":
        links = ["official website - https://garfield.com/", 
                 "official twitter - https://twitter.com/garfield", 
                 "offical youtube account - https://www.youtube.com/OfficialGarfield", 
                 "offical japanese twitter account - https://twitter.com/garfield_jp",
                 "official GarfieldEATS website - https://garfieldeats.com/", 
                 "GarfBot's GitHub source code - https://github.com/cookie-cuttr/garfieldbot"
                       ]

        send = "Important garfield links \n```"

        for i in range(len(links)):
            send += links[i]
            send += "\n \n"

        send += "```"
        await message.channel.send(send)
        
    if "monday" in message.content.lower():
        await message.channel.send("I **HATE** mondays!")
        
    if message.content.lower() == "garfprompt":
        verbused = verb[random.randint(0, len(verb)-1)]
        nounused = noun[random.randint(0, len(noun)-1)]
        charused = character[random.randint(0, len(character)-1)]
        response = charused + " " + verbused + " " + nounused
        await message.channel.send(response)



bot.run(TOKEN)

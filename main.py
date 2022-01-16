import os
from PIL import Image, ImageDraw, ImageFont
import asyncio
import time as t
import random
from replit import db

from webserver import keep_alive

import discord
from discord.ext import commands

client = discord.Client()
bot = commands.Bot(command_prefix='%', help_command=None)

def addTokens(userid, amount):
    if str(userid) + "_tokens" in db.keys():
        usertokens = db[str(userid) + "_tokens"]
        usertokens += amount

        db[str(userid) + "_tokens"] = usertokens
    else:
        db[str(userid) + "_tokens"] = 0
        usertokens = db[str(userid) + "_tokens"]
        usertokens += amount

        db[str(userid) + "_tokens"] = usertokens

def subtractTokens(userid, amount):
    if str(userid) + "_tokens" in db.keys():
        usertokens = db[str(userid) + "_tokens"]
        usertokens -= amount

        db[str(userid) + "_tokens"] = usertokens
    else:
        db[str(userid) + "_tokens"] = 0
        usertokens = db[str(userid) + "_tokens"]
        usertokens -= amount

        if usertokens <= 0:
            usertokens = 0

        db[str(userid) + "_tokens"] = usertokens

def getTokens(userid):
    if str(userid) + "_tokens" in db.keys():
        return db[str(userid) + "_tokens"]
    else:
        db[str(userid) + "_tokens"] = 0
        return db[str(userid) + "_tokens"]

def addLevels(userid, amount):
    if str(userid) + "_levels" in db.keys():
        userlevels = db[str(userid) + "_levels"]
        userlevels += amount

        db[str(userid) + "_levels"] = userlevels
    else:
        db[str(userid) + "_levels"] = 0
        userlevels = db[str(userid) + "_levels"]
        userlevels += amount

        db[str(userid) + "_levels"] = userlevels

def getLevels(userid):
    if str(userid) + "_levels" in db.keys():
        return db[str(userid) + "_levels"]
    else:
        db[str(userid) + "_levels"] = 0
        return db[str(userid) + "_levels"]

@bot.command()
async def help(ctx):
    await ctx.send("My prefix is %\n\nCommands:\nhelp\nmath\nobama\nslots\nsocials\ntoken")

@bot.command()
async def socials(ctx):
    await ctx.send("aftemathic actually made this bot, but real creator of the bot is TheCreator")
    embed=discord.Embed(title="Follow me on social media!", description="I post little to nothing, but seeing my follower count increase is incredibly satisfying.", color=discord.Color.red())

    embed.set_author(name="TheCreator", icon_url="https://images-ext-1.discordapp.net/external/DIG7D4gYmoqZUvs8GEi1TQn_UTLMbOh25APURa45pVc/https/lh3.googleusercontent.com/a-/AOh14GgyWf-iAzQRRgAVsacRifDpMN6_IOkV7w9Q1Lqu%3Ds600-k-no-rp-mo")

    embed.add_field(name="Youtube", value="https://www.youtube.com/channel/UC1U-tRxYC7sr1kd-Q92iyHA", inline=True)

    embed.add_field(name="Twitter", value="https://twitter.com/TheCreator1337_", inline=True)

    embed.add_field(name="Twitch", value="https://www.twitch.tv/thecreator133769", inline=True)

    embed.add_field(name="Reddit", value="https://www.reddit.com/user/TheCreator_1337", inline=False)

    await ctx.send(embed=embed)

@bot.command()
async def slots(ctx):
    def check(message: discord.Message):
            return message.channel == ctx.channel and message.author != ctx.me

    symbols = [":grapes:", ":cherries:", ":lemon:", ":green_apple:", ":kiwi:", ":peach:"]

    row1 = []
    row2 = []
    row3 = []

    await ctx.send('Enter your bet!')

    try:
        bet = await bot.wait_for('message', check=check, timeout=15.0)
    except asyncio.TimeoutError:
        await ctx.send('You took too long to enter your bet.')
    except:
        await ctx.send("Something went wrong.")
    else:
        try:
            int(bet.content)
        except ValueError:
            await ctx.send("Your bet wasn't a number...")
        except:
            await ctx.send("Something went wrong...")
        else:
            await ctx.send("Rolling...")

            for i in range(3):
                row1.append(random.choice(symbols))

            for i in range(3):
                row2.append(random.choice(symbols))

            for i in range(3):
                row3.append(random.choice(symbols))

            t.sleep(5)

            if row1[0] == row1[1] and row1[1] == row1[2] or row2[0] == row2[1] and row2[1] == row2[2] or row3[0] == row3[1] and row3[1] == row3[2]:
                await ctx.send(row1[0] + row1[1] + row1[2] + "\n" + row2[0] + row2[1] + row2[2] + '\n' + row3[0] + row3[1] + row3[2] + "\n\nYou won! Your reward would have been **" + str(int(bet.content) * 2) + "** if this wasn't just a simulation!")
                print("sideways win")

            elif row1[0] == row2[0] and row2[0] == row3[0] or row1[1] == row2[1] and row2[1] == row3[1] or row2[2] == row2[2] and row2[2] == row3[2]:
                await ctx.send(row1[0] + row1[1] + row1[2] + "\n" + row2[0] + row2[1] + row2[2] + '\n' + row3[0] + row3[1] + row3[2] + "\n\nYou won! Your reward would have been **" + str(int(bet.content) * 2) + "** if this wasn't just a simulation!")
                print("downward win")

            elif row1[0] == row2[1] and row2[1] == row3[2] or row1[2] == row2[1] and row2[1] == row3[0]:
                await ctx.send(row1[0] + row1[1] + row1[2] + "\n" + row2[0] + row2[1] + row2[2] + '\n' + row3[0] + row3[1] + row3[2] + "\n\nYou won! Your reward would have been **" + str(int(bet.content) * 2) + "** if this wasn't just a simulation!")
                print("crossed win")
            else:
                await ctx.send(row1[0] + row1[1] + row1[2] + "\n" + row2[0] + row2[1] + row2[2] + '\n' + row3[0] + row3[1] + row3[2] + "\n\nYou lost. Your reward would have been **" + str(int(bet.content) * 2) + "** if this wasn't just a simulation.")

@bot.command()
async def math(ctx):
    def check(message: discord.Message):
        return message.channel == ctx.channel and message.author != ctx.me

    def generateEquation(a, b, sign):
        if sign == 1:
            equation = str(a) + " + " + str(b)
        elif sign == 2:
            equation = str(a) + " - " + str(b)
        elif sign == 3:
            equation = str(a) + " x " + str(b)
        elif sign == 4:
            equation = str(a) + " ÷ " + str(b)
        elif sign == 5:
            equation = str(a) + " % " + str(b)

        return equation

    await ctx.send("What subject would you like? (Please choose with a number.)\n\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Modulus")

    try:
        option = await bot.wait_for('message', check=check, timeout=15.0)
    except asyncio.TimeoutError:
        await ctx.send('You took too long to enter your answer.')
    except:
        await ctx.send("Something went wrong.")
    else:
        try:
            int(option.content)
        except ValueError:
            await ctx.send("Your answer wasn't a number. We will choose your subject for you.")
            operation = random.randint(1, 5)
        except:
            await ctx.send("Something went wrong. We will choose your subject for you.")
            operation = random.randint(1, 5)
        else:
            operation = int(option.content)

    reward_amount = random.randint(5, 25)

    t.sleep(1)

    if operation == 1:
        a = random.randint(1, 100)
        b = random.randint(1, 100)

        sum = a + b

        equation = generateEquation(a, b, 1)

        await ctx.send("What is " + equation + "?")
        
        try:
            answer = await bot.wait_for('message', check=check, timeout=15.0)
        except asyncio.TimeoutError:
            await ctx.send('You took too long to enter your answer.')
        except:
            await ctx.send("Something went wrong.")
        else:
            try:
                int(answer.content)
            except ValueError:
                await ctx.send("Your answer isn't a number.")
            except:
                await ctx.send("Something went wrong.")
            else:
                if answer.content == str(sum):
                    addTokens(ctx.author.id, reward_amount)
                    await ctx.send("Good job! You got rewarded " + str(reward_amount) + " tokens!")
                else:
                    await ctx.send("Sorry, the sum was " + str(sum) + ".")
    if operation == 2:
        a = random.randint(1, 100)
        b = random.randint(1, 100)

        difference = a - b

        equation = generateEquation(a, b, 2)

        await ctx.send("What is " + equation + "?")
        
        try:
            answer = await bot.wait_for('message', check=check, timeout=15.0)
        except asyncio.TimeoutError:
            await ctx.send('You took too long to enter your answer.')
        except:
            await ctx.send("Something went wrong.")
        else:
            try:
                int(answer.content)
            except ValueError:
                await ctx.send("Your answer isn't a number.")
            except:
                await ctx.send("Something went wrong.")
            else:
                if answer.content == str(difference):
                    addTokens(ctx.author.id, reward_amount)
                    await ctx.send("Good job! You got rewarded " + str(reward_amount) + " tokens!")
                else:
                    await ctx.send("Sorry, the difference was " + str(difference) + ".")
    if operation == 3:
        a = random.randint(1, 100)
        b = random.randint(1, 100)

        product = a * b

        equation = generateEquation(a, b, 3)

        await ctx.send("What is " + equation + "?")
        
        try:
            answer = await bot.wait_for('message', check=check, timeout=15.0)
        except asyncio.TimeoutError:
            await ctx.send('You took too long to enter your answer.')
        except:
            await ctx.send("Something went wrong.")
        else:
            try:
                int(answer.content)
            except ValueError:
                await ctx.send("Your answer isn't a number.")
            except:
                await ctx.send("Something went wrong.")
            else:
                if answer.content == str(product):
                    addTokens(ctx.author.id, reward_amount)
                    await ctx.send("Good job! You got rewarded " + str(reward_amount) + " tokens!")
                else:
                    await ctx.send("Sorry, the product was " + str(product) + ".")
                    
    if operation == 4:
        a = random.randint(1, 100)
        b = random.randint(1, 100)

        while a % b != 0 and a != b:
            b = random.randint(1, 100)

        quotient = a / b

        equation = generateEquation(a, b, 4)

        await ctx.send("What is " + equation + "?")
        
        try:
            answer = await bot.wait_for('message', check=check, timeout=15.0)
        except asyncio.TimeoutError:
            await ctx.send('You took too long to enter your answer.')
        except:
            await ctx.send("Something went wrong.")
        else:
            try:
                int(answer.content)
            except ValueError:
                await ctx.send("Your answer isn't a number.")
            except:
                await ctx.send("Something went wrong.")
            else:
                if answer.content == str(int(quotient)):
                    addTokens(ctx.author.id, reward_amount)
                    await ctx.send("Good job! You got rewarded " + str(reward_amount) + " tokens!")
                else:
                    await ctx.send("Sorry, the quotient was " + str(quotient) + ".")
    if operation == 5:
        a = random.randint(1, 100)
        b = random.randint(1, 100)

        while a < b:
            a = random.randint(1, 100)

        quotient = a % b

        equation = generateEquation(a, b, 5)

        await ctx.send("What is " + equation + "?")
        
        try:
            answer = await bot.wait_for('message', check=check, timeout=15.0)
        except asyncio.TimeoutError:
            await ctx.send('You took too long to enter your answer.')
        except:
            await ctx.send("Something went wrong.")
        else:
            try:
                int(answer.content)
            except ValueError:
                await ctx.send("Your answer isn't a number.")
            except:
                await ctx.send("Something went wrong.")
            else:
                if answer.content == str(int(quotient)):
                    addTokens(ctx.author.id, reward_amount)
                    await ctx.send("Good job! You got rewarded " + str(reward_amount) + " tokens!")
                else:
                    await ctx.send("Sorry, the quotient was " + str(int(quotient)) + ".")

@bot.command()
async def obama(ctx):
    def check(message: discord.Message):
        return message.channel == ctx.channel and message.author != ctx.me

    await ctx.send("What text do you want?")

    try:
        text = await bot.wait_for('message', check=check, timeout=15.0)
    except asyncio.TimeoutError:
        await ctx.send('You took too long to enter your text.')
    except:
        await ctx.send("Something went wrong.")
    else:

        obamas = [
            "images/obama/obama1.png",
            "images/obama/obama2.png",
            "images/obama/obama3.png",
            "images/obama/obama4.png"
        ]

        base = Image.open(random.choice(obamas)).convert("RGBA")
        txt = Image.new("RGBA", base.size, (255,255,255,0))

        fnt = ImageFont.truetype("fonts/SEGOEUI.TTF", 84)

        d = ImageDraw.Draw(txt)

        d.text((base.size[0] // 2, base.size[1] // 2), str(text.content), font=fnt, fill=(255,255,255,255))

        out = Image.alpha_composite(base, txt)
        out.save("images/obama/obama_edited.png")

        await ctx.send(file=discord.File("images/obama/obama_edited.png"))

@bot.command()
async def token(ctx):
    def check(message: discord.Message):
            return message.channel == ctx.channel and message.author != ctx.me

    await ctx.send("Please enter a answer.\n\nOptions:\nmyTokens\nmyLevel\nlevelUpCost\nlevelUp")

    try:
        option = await bot.wait_for('message', check=check, timeout=15.0)
    except asyncio.TimeoutError:
        await ctx.send('You took too long to enter your option.')
    except:
        await ctx.send("Something went wrong.")
    else:
        if option.content == "myTokens":
            base = Image.open("images/tokenstemplate.png").convert("RGBA")
            txt = Image.new("RGBA", base.size, (255,255,255,0))

            fnt = ImageFont.truetype("fonts/SEGOEUI.TTF", 32)

            d = ImageDraw.Draw(txt)

            d.text((65,10), ctx.author.display_name, font=fnt, fill=(255,255,255,255))
            d.text((141,100), str(getTokens(ctx.author.id)), font=fnt, fill=(255,255,255,255))

            out = Image.alpha_composite(base, txt)
            out.save("images/tokenstemplate_edited.png")

            await ctx.send(file=discord.File("images/tokenstemplate_edited.png"))

        elif option.content == "myLevel":
            base = Image.open("images/levelstemplate.png").convert("RGBA")
            txt = Image.new("RGBA", base.size, (255,255,255,0))

            fnt = ImageFont.truetype("fonts/SEGOEUI.TTF", 32)

            d = ImageDraw.Draw(txt)

            d.text((65,10), ctx.author.display_name, font=fnt, fill=(255,255,255,255))
            d.text((141,100), str(getLevels(ctx.author.id)), font=fnt, fill=(255,255,255,255))

            out = Image.alpha_composite(base, txt)
            out.save("images/levelstemplate_edited.png")

            await ctx.send(file=discord.File("images/levelstemplate_edited.png"))

        elif option.content == "levelUp":
            cost = getLevels(ctx.author.id) * 125
            usertokens = getTokens(ctx.author.id)

            if usertokens >= cost:
                addLevels(ctx.author.id, 1)
                subtractTokens(ctx.author.id, cost)

                newlv = getLevels(ctx.author.id)

                await ctx.send("You have leveled up to level " + str(newlv) + "!")
            else:
                await ctx.send("You don't have enough money to level up. You need " + str(cost - usertokens) + " more tokens.")

        elif option.content == "levelUpCost":
            cost = getLevels(ctx.author.id) * 125
            await ctx.send("You need " + str(cost) + " tokens to level up.")

        else:
            await ctx.send("That was a invalid option.")    

keep_alive()
bot.run("your bot token")
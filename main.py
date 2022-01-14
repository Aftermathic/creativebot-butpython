import os
import asyncio
import time as t
import random
import discord
from discord.ext import commands

import config

token = config.token

client = discord.Client()
bot = commands.Bot(command_prefix='%')

@bot.command()
async def socials(ctx):
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
    
bot.run(token)

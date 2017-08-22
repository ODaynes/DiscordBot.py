import discord
import asyncio

# dice roll
import random

# app configuration
import config

client = discord.Client()

@client.event
async def on_ready():
    msg = "Name: " + client.user.name + " | ID: " + client.user.id 
    print("Logged in as: ")
    print(msg)
    print("-" * len(msg))

@client.event
async def on_message(message):
    if(message.content.lower().startswith("!shoutback")):
        msg = message.content[10:].upper()
        response = msg if msg != "" else "I can't shout nothing!"
        await client.send_message(message.channel, response)
    if(message.content.lower().startswith("!roll")):
        await client.send_message(message.channel, "You rolled a " + str( random.choice( range(1,7) ) ) + ".")
    if(message.content.lower().startswith("!hello")):
        await client.send_message(message.channel, "Hello, " + message.author.mention + "! :)")
    if(message.content.lower().startswith("!goodnight")):
        await client.send_message(message.channel, "Goodnight, " + message.author.mention + "! :)")

client.run(config.token)       
    

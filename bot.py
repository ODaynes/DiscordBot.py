import discord

# app configuration
import config

client = discord.Client()

scoreboard = {
    "g": 0,
    "h": 0,
    "r": 0,
    "s": 0
}

allocatable_points = [
    5, 10,
    20, 50
]

@client.event
async def on_ready():
    msg = "Name: %s | ID: %s" % (client.user.name, client.user.id)
    print(msg)
    print("-" * len(msg))


@client.event
async def on_message(message):

    if message.content.lower().startswith("!commands"):
        msg = "The following commands are available to the user:\n\n" + \
            "!vote [Gryffindor|Slytherin|Ravenclaw|Hufflepuff] [5|10|20|50] - " \
            "This allows you to allocate points to your selected house. " \
            "You can allocate points to your house once an hour.\n" \
            "!scoreboard - Displays to current house cup scoreboard."

        await client.send_message(message.channel, msg)

    # handle user voting

    if message.content.lower().startswith("!vote"):
        values = message.content.lower().split(" ")

        msg = ""

        if len(values) < 3:
            msg += "The !vote command is missing required parameters."
        else:
            house = values[1][0]
            points = values[2]
            if house not in scoreboard.keys():
                msg += "User must vote for Gryffindor, Slytherin, Ravenclaw or Hufflepuff."
            else:
                try:
                    points = int(points)
                    if points not in allocatable_points:
                        msg += "User must allocate either 5, 10, 20 or 50 points to a house."
                    else:
                        scoreboard[house] += points
                        msg = "%s has allocated %s points to house (%s)" % (message.author.mention, str(points), house.upper())
                except TypeError:
                    msg += "The points to allocate value is in an invalid format and must be a positive integer."

        await client.send_message(message.channel, msg)

    # display current scoreboard

    if message.content.lower().startswith("!scoreboard"):

        msg = ""

        for key, value in scoreboard.items():
            msg += "%s: %s".ljust(10) % (key.upper(), str(value))
            msg += "\n"

        await client.send_message(message.channel, msg)

client.run(config.token)
import discord

client = discord.Client()

@client.event
async def on_ready():
    print("We have logged in")

@client.event
async def on_message(message):
    if message.content == "!Hi":
        await message.channel.send("Hello")

client.run("Filler")
###################################################################################
print('Whos 7ft and an absolute monster')
input()
print('ShaqO Neil!')
print()
print('Why was the basketball court wet?')
input()
print('Because people were dribbling on it!')
print()
print('What does a Cleveland Cavaliers fan do when his team has won the NBA Finals?')
input()
print("He turns off the PlayStation 4")
input()
print('What is th difference between a bucket of shit and an Golden State Warriors fan?')
input()
print('The bucket.')
input()
print("What do NBA players and robbers have in common?")
input()
print("They both Steal, Run and shoot")
input()
print("I've got a great idea for a NBA themed Fast Food restaurant. I call it...")
input()
print("Shake-Shaq")


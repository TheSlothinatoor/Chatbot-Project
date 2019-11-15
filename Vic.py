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
input()
###############################################Updated###################################################################

##################INCOMPLETE#########################
print('Whos 7ft and an absolute monster')
reply = input()
if reply == "Shaq".lower():
    print("You stole my joke from me")
print('ShaqO Neil!')
print()
print('Why was the basketball court wet?')
input()
if reply == "Is it somehting to do with dribble.":
    print("make this fun")
print('Because people were dribbling on it!')
print()
print('What does a Cleveland Cavaliers fan do when his team has won the NBA Finals?')
input()
if reply =="ps4".upper():
    print(" Im gonna keep going i dont care")
print("He turns off the PlayStation 4")
input()
print('What is th difference between a bucket of shit and an Golden State Warriors fan?')
input()
if reply ==" Warriors are trash":
    print("Im geting bored of you")
print('The bucket.')
input()
print("What do NBA players and robbers have in common?")
input()
if reply =="what".upper():
    print("Watch how you speak to me but......")
print("They both Steal, Run and shoot")
input()
print("I've got a great idea for a NBA themed Fast Food restaurant. I call it...")
if reply =="what".upper():
    print("What did i say about how you speak to me but anyways...")
input()
print("Shake-Shaq")
input()
###########################################################
#################################################################################Minor Code (Attempted Split Attempted)#############
str1 = 'This string'
if 'is' in str1:
    print (str1)

    
str2 = 'This is a string'
if 'is' in str2:
    print (str2)

if 'is' in str1.split():
    print(str1)

if 'is' in str2.split():
    print(str2)

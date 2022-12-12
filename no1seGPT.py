import openai
import discord
from discord.ext import commands
from discord import Status

#no1se bot description


# Set up OpenAI API key
openai.api_key = "YOUR_OPENAI_TOKEN"

intents = discord.Intents.default()
intents.message_content = True

# Set up Discord bot
client = commands.Bot(command_prefix='!' ,intents=intents)

status = Status("online")

client.status = status;

@client.event
async def on_ready():
  await client.change_presence(activity=discord.Game(name=f" !no1seGPT (WRITE HERE)"))

# Listen for the no1seGPT command
@client.command()
async def no1seGPT(ctx, *, input):
    # Generate a response using OpenAI's GPT-3 model
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=input,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Send the response to Discord
    user_mention = ctx.message.author.mention
    response_text = f"{user_mention}, {response['choices'][0]['text']}"

    await ctx.send(response_text)

# Start the bot
client.run("REPLACE_THIS_WITH_YOUR_DISCORD_TOKEN")

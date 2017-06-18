import asyncio
import time
import discord.ext.commands
import markovify

time.sleep(1)

with open("/root/sample.txt", encoding="utf8")as f:
    text = f.read()

text_model=markovify.Text(text, state_size=2)

client = discord.Client() #connection stuff
async def background_loop(): # start of loop de loop
    await client.wait_until_ready()
    while not client.is_closed:
        channel = client.get_channel('CHANNEL_ID_HERE)
        try:
            messages = (text_model.make_sentence(tries=6, max_overlap_total=8, max_overlap_ratio=0.6, char_limit=140))
        except Exception:
            continue
        try:
            await client.send_message(channel, (messages))
        except Exception:
            continue
        await asyncio.sleep(20)

client.loop.create_task(background_loop())
client.run("TOKEN_HERE")


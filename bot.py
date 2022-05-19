from discord.ext import commands

def blockify(given_text : str):
    given_text = given_text.lower()
    #given_text = given_text.replace('_','') 
    text_to_block_dict = {
        letter : uni_emoji for (letter, uni_emoji) in zip(
            [chr(ltr) for ltr in range(ord("a"), ord("z") + 1)],
            [chr(uni_emo) for uni_emo in range(127462 , 127487 + 1)]
        )
    }
    
    return "".join([
        text_to_block_dict[f] for f in given_text
    ])


client = commands.Bot(command_prefix= "!")



@client.event
async def on_message(message):
    if message.content == "e":
        await message.add_reaction("🟥")
        await message.add_reaction("🔷")
        await message.add_reaction("🟨")
        try:
            for each_regional in blockify(message.author.name):
                await message.add_reaction(each_regional)
        except Exception as e:
            await message.channel.send(f"Error is `{e}`")
        await message.add_reaction("⬜")
        await message.add_reaction("🔶")
        await message.add_reaction("🟩")



client.run("TOKEN")        
import discord

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Brexit"))

@client.event
async def on_member_join(member):
    guild  = client.get_guild(906711064958337126)
    border = guild.get_channel(931591123103780935)
    rules = guild.get_channel(931258829138702366)
    roles = guild.get_channel(927622856408440873)
    gen = guild.get_channel(911402373988110357)
    embed=discord.Embed(title="Welcome!",description=f"Yooo {member.mention}, welcome to wafflers, to get verified please **STATE YOUR AGE AND GENDER**. Be chill and make sure to get {roles.mention} and follow the server {rules.mention}.", color=discord.Colour.blue())
  
    embed.set_image(url="https://media.discordapp.net/attachments/911402373988110357/940013767645876334/DO_THE_ROBOT.gif")
  
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/927621918830526465/929540613274210384/W_FFLERS_8.png")
  
    embed.set_footer(text="FAISAAL BOP")
    new_personRole = discord.utils.get(member.guild.roles, id=936017992267997245)
    await member.add_roles(new_personRole)
    await border.send("@here", embed=embed)
    await gen.send(f"everyone welcomee {member.mention}")
    
@client.event
async def on_member_remove(member):
    guild = client.get_guild(906711064958337126)
    channel = guild.get_channel(911402373988110357)
    await channel.send(f"**{member.display_name}** got deported")

client.run(<id here>)

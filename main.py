from discord.ext import commands,tasks
from embeds import *
import sqlite3
from xp_system import *
from server_info import *
from moderation import *
import asyncio

intents = discord.Intents.all()
client = commands.Bot(command_prefix="!")


@client.event
async def on_ready():
 print('Online')
 xps_create()
 svinfo_create()
 mod_create()


@client.event
async def on_guild_join(guild):
  '''
  Guild Entry Information 
  '''
  try:
   await guild.owner.send(embed=embed_announce)
  except:
    pass    
  svinfo_addServer(guild)

@client.event
async def on_member_join(member):
  '''
  Welcome New Members
  '''
  xps_addmember(member)
  mod_addServer(member)
  wel= svinfo_getWelcome(member)
  await member.send(wel)



@client.event
async def on_message(message):
  '''
  On Message Event to process member messages.
  '''
  if(message.content.startswith("!help")or (not message.guild==None) and message.guild.id==336642139381301249):
    return
  try:
    if(message.author.id!=client.user.id and not message.content.startswith("!")):
      s=xps_addxp(message.author)
      if(s):
        await message.channel.send(message.author.mention+" Level UP!!")
  except IndexError:
    xps_addmember(message.author)
    mod_addServer(message.author)
    if(message.author.id!=client.user.id and not message.content.startswith("!")):
      s=xps_addxp(message.author)
      if(s):
        await message.channel.send(message.author.mention+" Level UP!!")
  await client.process_commands(message)




@commands.max_concurrency(1)  
@client.command() 
async def count(ctx):
  '''
  Counter of Server and Member Number
  '''
  if (ctx.author.id==290537253850054658):
    await ctx.channel.send(f"Server Number: {len(client.guilds)}\nUser Number:{len(client.users)}")
  else:
    pass
    

@commands.max_concurrency(1)  
@client.command() 
async def info(ctx):
  '''
  Information about the bot!
  '''
  try:
    if(ctx.message.content.split(" ")[1]=="profile"):
      embed_helpprof.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
      await ctx.channel.send(embed=embed_helpprof)
    elif(ctx.message.content.split(" ")[1]=="mod"):
      embed_helpmain.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
      await ctx.channel.send(embed=embed_helpmod)
    elif(ctx.message.content.split(" ")[1]=="others"):
      embed_helpoth.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
      await ctx.channel.send(embed=embed_helpoth)
    elif(ctx.message.content.split(" ")[1]=="bot"):
      embed_helpbot.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
      await ctx.channel.send(embed=embed_helpbot)
    else:
      embed_helpmain.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
      await ctx.channel.send(embed=embed_helpmain)
  except:
    embed_helpmain.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
    await ctx.channel.send(embed=embed_helpmain)

@commands.max_concurrency(1)  
@client.command() 
async def profile(ctx,member:discord.Member):
  '''
  A full customizeable profile with your xp, information and changeable picture and color!
  '''
  print(type(member))
  try:
    level,xp,status,pp,colour=xps_profil(member)
    embed=discord.Embed(title=member.display_name + " Profile",description="Level: "+str(level)+"\nXP: "+str(xp)+"/"+str(level*30)+"\n*"+status+"*",colour=colour)
    try:
     embed.set_image(url=pp)
    except:
      embed.set_image(url=member.avatar_url)
    await ctx.channel.send(embed=embed)
  except IndexError:
    xps_addmember(member)
    mod_addServer(member)
    level,xp,status,pp,colour=xps_profil(member)
    embed=discord.Embed(title=member.display_name + " Profile",description="Level: "+str(level)+"\nXP: "+str(xp)+"/"+str(level*30)+"\n*"+status+"*",colour=colour)
    embed.set_image(url=pp)
    await ctx.channel.send(embed=embed)

@commands.max_concurrency(1)  
@client.command() 
async def status(ctx,*drm):
  '''
  Changes member's personal profile status!
  '''
  try:
   durum=" ".join(drm)
   xps_setstatus(ctx.author,durum)
  except IndexError:
    xps_addmember(ctx.author)
    mod_addServer(ctx.author)
    durum=" ".join(drm)
    xps_setstatus(ctx.author,durum)

@commands.max_concurrency(1)  
@client.command() 
async def colour(ctx,renk):
  '''
  Changes member's personal profile color!
  '''
  try:
   xps_setcolour(ctx.author,int(renk,16))
  except IndexError:
    xps_addmember(ctx.author)
    mod_addServer(ctx.author)
    xps_setcolour(ctx.author,int(renk,16))


@commands.max_concurrency(1)  
@client.command() 
async def pp(ctx,pp):
  '''
  Changes member's personal profile picture!
  '''
  try:
   xps_setpp(ctx.author,pp)
  except IndexError:
    xps_addmember(ctx.author)
    mod_addServer(ctx.member)
    xps_setpp(ctx.author,pp)


@commands.has_permissions(manage_guild=True)
@commands.max_concurrency(1)  
@client.command() 
async def setinvite(ctx,inv):
  '''
  Changes Server's Invite!
  '''
  try:
   svinfo_setInvite(ctx.guild,inv)
  except IndexError:
   svinfo_addServer(ctx.guild)
   svinfo_setInvite(ctx.guild,inv)

@commands.max_concurrency(1)  
@client.command() 
async def invite(ctx):
  try:
    inv= svinfo_sendInvite(ctx.guild)
    await ctx.channel.send(ctx.author.mention+" "+inv)
  except IndexError:
   svinfo_addServer(ctx.guild)
   inv= svinfo_sendInvite(ctx.guild)
   await ctx.channel.send(ctx.author.mention+" "+inv)
   

@commands.max_concurrency(1)  
@client.command() 
@commands.has_permissions(kick_members=True)
async def warn(ctx,member:discord.Member,*args):
  '''
  A moderation command to track member warnings!
  '''
  try:
   reason=" ".join(args)
   embed=mod_setWarn(member,reason)
   await member.send(embed=embed)
  except IndexError:
    xps_addmember(member)
    mod_addServer(member)
    reason=" ".join(args)
    embed=mod_setWarn(member,reason)
    await member.send(embed=embed)

@commands.has_permissions(kick_members=True)
@commands.max_concurrency(1)  
@client.command() 
async def kick(ctx,member:discord.Member,*args):
  '''
  A moderation command to kick the member from the guild!
  '''
  try:
   reason=" ".join(args)
   embed=mod_setKick(member,reason)
   await ctx.guild.kick(member)
   await member.send(embed=embed)
  except IndexError:
    xps_addmember(member)
    mod_addServer(member)
    reason=" ".join(args)
    embed=mod_setKick(member,reason)
    await ctx.guild.kick(member)
    await member.send(embed=embed)
 
@commands.has_permissions(ban_members=True)
@commands.max_concurrency(1)  
@client.command() 
async def ban(ctx,member:discord.Member,*args):
  '''
  A moderation command to ban them member from the guild!
  '''
  try:
   reason=" ".join(args)
   embed=mod_setBan(member,reason)
   await member.send(embed=embed)
   await ctx.guild.ban(member)
   
  except IndexError:
    xps_addmember(member)
    mod_addServer(member)
    reason=" ".join(args)
    embed=mod_setBan(member,reason)
    await member.send(embed=embed)
    await ctx.guild.ban(member)
    

@commands.has_permissions(kick_members=True)
@commands.max_concurrency(1)  
@client.command() 
async def aprofile(ctx,member:discord.Member):
  '''
  A moderation command to check member's profile with additional moderation stuff!
  '''
  try:
    embed=mod_aprofile(member)
    await ctx.channel.send(embed=embed)
  except IndexError:
    xps_addmember(member)
    mod_addServer(member)
    xps_setcolour(ctx.author,int(renk,16))
    embed=mod_aprofile(member)
    await ctx.channel.send(embed=embed)
 

@commands.has_permissions(manage_guild=True)
@commands.max_concurrency(1)  
@client.command() 
async def welcome(ctx,*args):
  '''
  A moderation command to set welcome information!
  '''
  try:
   wel=" ".join(args)
   svinfo_setWelcome(ctx.guild,wel)
  except IndexError:
   svinfo_addServer(ctx.guild)
   wel=" ".join(args)
   svinfo_setWelcome(ctx.guild,wel)
  
@commands.max_concurrency(1)  
@client.command() 
async def mydata(ctx):
  '''
  Sends Personal Data Information
  '''
  await ctx.channel.send(ctx.author.mention+"** Your Data Security is important for us!**\n1) Camarade Bot only store your and your server's id and member list.\n2)Anybody except Bot do not have any acces to these data\n3)When you leave server, your data will be removed completely\n4)If you have any problems or questions about security, contact bot's developpers: !contact")

@commands.max_concurrency(1)  
@client.command() 
async def contact(ctx):
  '''
  Sends owner's contact information
  '''
  await ctx.channel.send(embed=embed_contact)




@tasks.loop(reconnect=True)
async def presence():
  '''
  Task for dynamic bot status
  '''
  try:
   await client.change_presence(activity=discord.Game(f"{len(client.users)} users in {len(client.guilds)} servers!"), status=discord.Status.do_not_disturb)
   await asyncio.sleep(60)
  except:
    print("Deneniyor.")
    await asyncio.sleep(20)
   
    

presence.start()

client.run("NTA2MjAyNTk3NDczMTI0MzUy.W9Yb6A.Oy2cvZH2m0UcKNdjcpiaoNlkmXo",reconnect=True)

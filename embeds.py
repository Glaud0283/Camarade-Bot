import discord

##Announce 
embed_announce = discord.Embed(title="Camarade Bot at your service!", colour=discord.Colour(0xd300ff),description="Camarade Bot is a bot to make everything easy and funny for you!")
embed_announce.set_thumbnail(url="https://cdn.discordapp.com/attachments/399626867885211676/723941791316836352/bKUAAAAAElFTkSuQmCC.png")
embed_announce.set_author(name="Camarade Bot", url="https://discord.com/oauth2/authorize?client_id=506202597473124352&scope=bot&permissions=2146958847", icon_url="https://cdn.discordapp.com/attachments/399626867885211676/723941791316836352/bKUAAAAAElFTkSuQmCC.png")
embed_announce.set_footer(text="Glaud#0283 - Developper", icon_url="https://cdn.discordapp.com/attachments/399626867885211676/723944450748973136/Bundesarchiv_Bild_101I-299-1805-162C_Nordfrankreich2C_Panzer_VI_28Tiger_I29.png")
embed_announce.add_field(name="**Profiles!!**", value="Every member have their own customizeable profiles! Change it as you wish!",inline=True)
embed_announce.add_field(name="**Moderation Tools!**", value="You can moderate faster in your discord. Every member have a moderation log for admins.",inline=True)
embed_announce.add_field(name="**Levels and XPs**", value="Send more messages to reach higher levels!",inline=True)
embed_announce.add_field(name="Are you ready?",value="To start, use command: *!info*",inline=False)

##Help Main
embed_helpmain = discord.Embed(title="Camarade Bot Help", colour=discord.Colour(0xd300ff),description="All help commands:")
embed_helpmain.set_thumbnail(url="https://cdn.discordapp.com/attachments/399626867885211676/723941791316836352/bKUAAAAAElFTkSuQmCC.png")
embed_helpmain.set_author(name="Camarade Bot", url="https://discord.com/oauth2/authorize?client_id=506202597473124352&scope=bot&permissions=2146958847", icon_url="https://cdn.discordapp.com/attachments/399626867885211676/723941791316836352/bKUAAAAAElFTkSuQmCC.png")
embed_helpmain.add_field(name="!info profile",value="Shows the help page for profile and xp commands",inline=False)
embed_helpmain.add_field(name="!info mod",value="Shows the help page for moderation commands",inline=False)
embed_helpmain.add_field(name="!info others",value="Shows the help page for other commands",inline=False)
embed_helpmain.add_field(name="!info bot",value="Shows the help page for bot and security",inline=False)

##Helpprof
embed_helpprof = discord.Embed(title="Camarade Bot Help", colour=discord.Colour(0xd300ff),description="Profile Commands:")
embed_helpprof.set_thumbnail(url="https://cdn.discordapp.com/attachments/399626867885211676/723941791316836352/bKUAAAAAElFTkSuQmCC.png")
embed_helpprof.set_author(name="Camarade Bot", url="https://discord.com/oauth2/authorize?client_id=506202597473124352&scope=bot&permissions=2146958847", icon_url="https://cdn.discordapp.com/attachments/399626867885211676/723941791316836352/bKUAAAAAElFTkSuQmCC.png")
embed_helpprof.add_field(name="!profile [@user]",value="Shows the profile and level status of a member",inline=False)
embed_helpprof.add_field(name="!status [sentence]",value="Sets your profile status",inline=False)
embed_helpprof.add_field(name="!pp [link]",value="Sets your profile picture",inline=False)
embed_helpprof.add_field(name="!colour [hex code] ",value="Sets your profile colour",inline=False)

##Helpmod
embed_helpmod = discord.Embed(title="Camarade Bot Help", colour=discord.Colour(0xd300ff),description="Moderation Commands:")
embed_helpprof.set_thumbnail(url="https://cdn.discordapp.com/attachments/399626867885211676/723941791316836352/bKUAAAAAElFTkSuQmCC.png")
embed_helpmod.set_author(name="Camarade Bot", url="https://discord.com/oauth2/authorize?client_id=506202597473124352&scope=bot&permissions=2146958847", icon_url="https://cdn.discordapp.com/attachments/399626867885211676/723941791316836352/bKUAAAAAElFTkSuQmCC.png")
embed_helpprof.add_field(name="!aprofile [@user]",value="Shows the admin logs of a member",inline=False)
embed_helpmod.add_field(name="!warn [@user] [reason]",value="Sends a member warning message and logs it",inline=False)
embed_helpmod.add_field(name="!kick [@user] [reason]",value="Kick the member, sends an information to target message message and logs it",inline=False)
embed_helpmod.add_field(name="!ban [@user] [reason] ",value="Ban the member, sends an information to target message message and logs it",inline=False)

##Helpoth
embed_helpoth = discord.Embed(title="Camarade Bot Help", colour=discord.Colour(0xd300ff),description="Other Commands:")
embed_helpoth.set_thumbnail(url="https://cdn.discordapp.com/attachments/399626867885211676/723941791316836352/bKUAAAAAElFTkSuQmCC.png")
embed_helpoth.set_author(name="Camarade Bot", url="https://discord.com/oauth2/authorize?client_id=506202597473124352&scope=bot&permissions=2146958847", icon_url="https://cdn.discordapp.com/attachments/399626867885211676/723941791316836352/bKUAAAAAElFTkSuQmCC.png")
embed_helpoth.add_field(name="!welcome [text]",value="Sets server's welcome message!",inline=False)
embed_helpoth.add_field(name="!setinvite [invitelink]",value="Sets server's invite link for command !invite",inline=False)
embed_helpoth.add_field(name="!invite",value="Sends the invite link",inline=False)

##Helpbot
embed_helpbot = discord.Embed(title="Camarade Bot Help", colour=discord.Colour(0xd300ff),description="Bot Commands:")
embed_helpbot.set_thumbnail(url="https://cdn.discordapp.com/attachments/399626867885211676/723941791316836352/bKUAAAAAElFTkSuQmCC.png")
embed_helpbot.set_author(name="Camarade Bot", url="https://discord.com/oauth2/authorize?client_id=506202597473124352&scope=bot&permissions=2146958847", icon_url="https://cdn.discordapp.com/attachments/399626867885211676/723941791316836352/bKUAAAAAElFTkSuQmCC.png")
embed_helpbot.add_field(name="!mydata",value="See how we store and secure your data!",inline=False)
embed_helpbot.add_field(name="!contact",value="Contact Information of developper",inline=False)

##contact
embed_contact = discord.Embed(title="Contact:", colour=discord.Colour(0xd300ff))
embed_contact.set_thumbnail(url="https://cdn.discordapp.com/attachments/399626867885211676/723941791316836352/bKUAAAAAElFTkSuQmCC.png")
embed_contact.set_author(name="Camarade Bot", url="https://discord.com/oauth2/authorize?client_id=506202597473124352&scope=bot&permissions=2146958847", icon_url="https://cdn.discordapp.com/attachments/399626867885211676/723941791316836352/bKUAAAAAElFTkSuQmCC.png")
embed_contact.add_field(name="Discord:",value="Glaud#0283",inline=False)
embed_contact.add_field(name="Steam:",value="https://steamcommunity.com/id/Glaudd/",inline=False)


import sqlite3 
import discord
con = sqlite3.connect("mod.db")

cursor = con.cursor() 

def mod_create():
  cursor.execute("CREATE TABLE IF NOT EXISTS kitaplık (Member TEXT, Warn INT, Kick INT, Ban INT)") 
  con.commit()

def mod_addServer(member):
  cursor.execute("INSERT INTO kitaplık VALUES(?,?,?,?)",(member.mention,0,0,0))
  con.commit()

def mod_setWarn(member,reason):
    
  no = cursor.fetchall()[0][0]
  cursor.execute("Update kitaplık set Warn = ? where Member =  ?",(no + 1,member.mention))
  con.commit()
  embed=discord.Embed(title="You  have been Warned!",description="Reason: "+reason+"\nNext time, you might have a serious punishment. Be careful!" ,colour=0xffe603)
  return embed

def mod_setKick(member,reason):
  cursor.execute("Select Kick From kitaplık where Member = ?",(member.mention,)) 
  no = cursor.fetchall()[0][0]
  cursor.execute("Update kitaplık set Kick = ? where Member =  ?",(no + 1,member.mention))
  con.commit()
  embed=discord.Embed(title="You have been Kicked!",description="Reason: "+reason+"\nYou still can join to server but be careful!" ,colour=0xff0d0d)
  return embed


def mod_setBan(member,reason):
  cursor.execute("Select Ban From kitaplık where Member = ?",(member.mention,)) 
  no = cursor.fetchall()[0][0]
  cursor.execute("Update kitaplık set Ban = ? where Member =  ?",(no + 1,member.mention))
  con.commit()
  embed=discord.Embed(title="You have been Banned!",description="Reason: "+reason,colour=0x000000)
  return embed

def mod_aprofile(member):
  cursor.execute("Select Warn From kitaplık where Member = ?",(member.mention,)) 
  warn = cursor.fetchall()[0][0]
  cursor.execute("Select Kick From kitaplık where Member = ?",(member.mention,)) 
  kick = cursor.fetchall()[0][0]
  cursor.execute("Select Ban From kitaplık where Member = ?",(member.mention,)) 
  ban = cursor.fetchall()[0][0]
  embed=discord.Embed(title=member.display_name+"'s Profile",description="Warn: "+str(warn)+"\nKick: " +str(kick)+"\nBan: "+str(ban),colour=0x0014ff)
  return embed
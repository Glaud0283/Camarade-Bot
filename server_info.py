import sqlite3 
con = sqlite3.connect("svinfo.db")

cursor = con.cursor() 

def svinfo_create():
  cursor.execute("CREATE TABLE IF NOT EXISTS kitaplık (Server_id TEXT, link TEXT,Welcome TEXT)") 
  con.commit()

def svinfo_addServer(guild):
  cursor.execute("INSERT INTO kitaplık VALUES(?,?,?)",(guild.id,"This server did not set an invite link yet: !setinvite","Welcome!\n\nBe sure that you read Camarade Bot's **Data procces and handling system** by using command: !mydata"))
  con.commit()

def svinfo_setInvite(guild,invite):
  cursor.execute("Select link From kitaplık where Server_id = ?",(guild.id,)) 
  inv = cursor.fetchall()[0][0]
  cursor.execute("Update kitaplık set link = ? where Server_id =  ?",(invite,guild.id))
  con.commit()
  
def svinfo_sendInvite(guild):
  cursor.execute("Select link From kitaplık where Server_id = ?",(guild.id,)) 
  inv = cursor.fetchall()[0][0]
  return inv

def svinfo_setWelcome(guild,welcome):
  cursor.execute("Select link From kitaplık where Server_id = ?",(guild.id,)) 
  inv = cursor.fetchall()[0][0]
  cursor.execute("Update kitaplık set Welcome = ? where Server_id =  ?",(welcome+"\n\nBe sure that you read Camarade Bot's **Data procces and handling system** by using command: !mydata",guild.id))
  con.commit()

def svinfo_getWelcome(member):
  cursor.execute("Select Welcome From kitaplık where Server_id = ?",(member.guild.id,)) 
  wel = cursor.fetchall()[0][0]
  return wel

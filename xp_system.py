import sqlite3 

con = sqlite3.connect("xp_system.db")

cursor = con.cursor() 

def xps_create():
  cursor.execute("CREATE TABLE IF NOT EXISTS kitaplık (Member TEXT, Level INT, XP INT, Colour INT, Status INT, Pp TEXT)") 
  con.commit()

def xps_addmember(member):
  cursor.execute("INSERT INTO kitaplık VALUES(?,?,?,?,?,?)",(member.mention,1,0,0x44aa00,'Kim Kimi yendi çok mu önemli?',str(member.avatar_url)))
  con.commit()

def xps_takeall():
  cursor.execute("Select * From kitaplık") 
  data = cursor.fetchall()
  return data

def xps_addxp(member):
  cursor.execute("Select XP From kitaplık where Member = ?",(member.mention,)) 
  x = cursor.fetchall()[0][0]
  cursor.execute("Select Level From kitaplık where Member = ?",(member.mention,)) 
  l = cursor.fetchall()[0][0]
  x=x+1
  if(x==l*30):
    cursor.execute("Update kitaplık set XP = ? where Member =  ?",(0,member.mention))
    cursor.execute("Update kitaplık set Level = ? where Member =  ?",(l+1,member.mention))
    con.commit()
    return True
  else:
    cursor.execute("Update kitaplık set XP = ? where Member =  ?",(x,member.mention))
    con.commit()
    return False

def xps_profil(member):
  cursor.execute("Select Level From kitaplık where Member = ?",(member.mention,)) 
  level = cursor.fetchall()[0][0]
  cursor.execute("Select XP From kitaplık where Member = ?",(member.mention,)) 
  xp = cursor.fetchall()[0][0]
  cursor.execute("Select Status From kitaplık where Member = ?",(member.mention,)) 
  status = cursor.fetchall()[0][0]
  cursor.execute("Select Pp From kitaplık where Member = ?",(member.mention,)) 
  pp = cursor.fetchall()[0][0]
  cursor.execute("Select Colour From kitaplık where Member = ?",(member.mention,)) 
  colour = cursor.fetchall()[0][0]
  return level,xp,status,pp,colour

def xps_setstatus(member,durum):
  cursor.execute("Select Level From kitaplık where Member = ?",(member.mention,)) 
  level = cursor.fetchall()[0][0]
  cursor.execute("Update kitaplık set Status = ? where Member =  ?",(durum,member.mention))
  con.commit()

def xps_setcolour(member,clr):
  cursor.execute("Select Level From kitaplık where Member = ?",(member.mention,)) 
  level = cursor.fetchall()[0][0]
  cursor.execute("Update kitaplık set Colour = ? where Member =  ?",(clr,member.mention))
  con.commit()
  
def xps_setpp(member,pp):
  cursor.execute("Select Level From kitaplık where Member = ?",(member.mention,)) 
  level = cursor.fetchall()[0][0]
  cursor.execute("Update kitaplık set Pp = ? where Member =  ?",(pp,member.mention))
  con.commit()
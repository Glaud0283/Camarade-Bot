import binanceapi
import settings
import discord_alerts


class User:
    '''
    User object for automation. All actions are applied for all users automatically.
    '''
    instances = []
    def __init__(self,name,apiKey,secretKey):
        self.name = name
        self.apiKey = apiKey
        self.secretKey = secretKey
        self.instances.append(self)
    
    def new_order(self,apiKey,secretKey,symbol,side,coin_price):
        binanceapi.new_order(apiKey,secretKey,symbol,side,coin_price) # New order for a single target
    
    @classmethod
    def new_order_for_all(cls,symbol,side,coin_price): # General order for all users.
        for client in cls.instances:
            client.new_order(client.apiKey,client.secretKey,symbol,side,coin_price)
        
        discord_alerts.webhook_alert(symbol,side,coin_price,c)
        

    
def load_users():
    for u in settings.userList:
        User(u[0],u[1],u[2])



    

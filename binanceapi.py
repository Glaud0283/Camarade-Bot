from binance.client import Client

constant = 4 # Coefficent to divide wallet value

def new_order(apiKey,secretKey,symbol,side,coin_price): 
    '''
    Enters a new entry to binance by using given parameters.
    
    '''
    client = Client(apiKey,secretKey)
    for coin in client.futures_account_balance():
        if (coin["asset"]=="USDT"):
            rawSize=float(coin["balance"])
            break
    
    size=rawSize / constant
    quantity=round(size/coin_price)
    client.futures_create_order(symbol=symbol, side=side, type='MARKET', quantity=quantity)



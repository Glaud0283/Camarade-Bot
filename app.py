from flask import Flask
from flask import request
import users

app = Flask(__name__)
users.load_users()

@app.route("/")
def hello():
    '''
    This API is used to take post requests from TradingView to process and send requests to Binance.
    '''
    return "Ready!!"

@app.route('/api/NewOrder',methods=['POST'])
def newOrder():
    '''
    Take posts from Tradingview and creates a new entry.
    '''
    data = request.json
    users.User.new_order_for_all(data["symbol"],data["side"],data["coin_price"])
    return "Post Succesful!"

if __name__ == "__main__":
    app.run(port=5000)
    

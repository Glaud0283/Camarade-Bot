from discord_webhook import DiscordWebhook, DiscordEmbed
from datetime import datetime

def webhook_alert(symbol,side,coin_price,client_number):
    '''
    Webhook Conection with Discord for Notifications and logs.
    '''
    now = datetime.now()
    timestamp = datetime.timestamp(now)
    description = (
        f"Coin: {symbol}\n"
        f"Side: {side}\n"
        f"Price: {coin_price}\n"
        f"Client number: {client_number}"
    )
    if side.lower() == "buy":
        color = "00ff27"
    elif side.lower() == "sell":
        color = "ff0004"
    webhook = DiscordWebhook(url='--Webhook Url Here--')
    embed = DiscordEmbed(title='New Position Order', description=description, color=color)
    embed.set_timestamp()
    embed.set_footer(text='Glaud#0283', icon_url='https://glaud.should-be.legal/3kR3RAm.png')
    embed.set_thumbnail(url='https://glaud.should-be.legal/A1wFArM.png')
    webhook.add_embed(embed)
    webhook.execute()

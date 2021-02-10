from denariusrpc.authproxy import AuthServiceProxy, JSONRPCException

import urllib
import json
import requests

#DDNS to push API data to name
ddns_update_name = 'api:python_example'
ddns_update_expiration = 9999

#coingecko API for Denarius to BTC pricing, marketcap, 24 hour volume
coingecko_url = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=denarius&vs_currencies=btc&include_market_cap=true&include_24hr_vol=true')
coingecko_data = str(json.loads(coingecko_url.text))
print(coingecko_data)

# rpc_user and rpc_password are set in the denarius.conf file
rpc_connection = AuthServiceProxy("http://%s:%s@127.0.0.1:32369"%("rpcusername", "rpcpassword"))

#push coingecko json into the DDNS value
name_push = rpc_connection.name_update(ddns_update_name, coingecko_data, ddns_update_expiration)
print(name_push)

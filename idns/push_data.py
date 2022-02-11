from innovarpc.authproxy import AuthServiceProxy, JSONRPCException

import urllib
import json
import requests

#IDNS to push API data to name
idns_update_name = 'api:python_example'
idns_update_expiration = 9999

#coingecko API for Innova to BTC pricing, marketcap, 24 hour volume
coingecko_url = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=innova&vs_currencies=btc&include_market_cap=true&include_24hr_vol=true')
coingecko_data = str(json.loads(coingecko_url.text))
print(coingecko_data)

# rpc_user and rpc_password are set in the innova.conf file
rpc_connection = AuthServiceProxy("http://%s:%s@127.0.0.1:14531"%("rpcusername", "rpcpassword"))

#push coingecko json into the IDNS value
name_push = rpc_connection.name_update(idns_update_name, coingecko_data, idns_update_expiration)
print(name_push)

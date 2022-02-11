#requires https://github.com/innova-foundation/python-innovarpc and innova daemon/QT wallet
from innovarpc.authproxy import AuthServiceProxy, JSONRPCException

#IDNS to look up data
idns_lookup_data = 'api:pricefeedInnova'

# rpc_user and rpc_password are set in the innova.conf file
rpc_connection = AuthServiceProxy("http://%s:%s@127.0.0.1:14531"%("rpcusername", "rpcpassword"))

name_show_feed = rpc_connection.name_show(idns_lookup_data)
print(name_show_feed)

name_show_value = name_show_feed['value']
print(name_show_value)

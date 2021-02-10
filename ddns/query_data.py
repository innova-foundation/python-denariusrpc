#requires https://github.com/buzzkillb/python-denariusrpc and denarius daemon/QT wallet
from denariusrpc.authproxy import AuthServiceProxy, JSONRPCException

#DDNS to look up data
ddns_lookup_data = 'api:pricefeedDenarius'

# rpc_user and rpc_password are set in the denarius.conf file
rpc_connection = AuthServiceProxy("http://%s:%s@127.0.0.1:32369"%("rpcusername", "rpcpassword"))

name_show_feed = rpc_connection.name_show(ddns_lookup_data)
print(name_show_feed)

name_show_value = name_show_feed['value']
print(name_show_value)

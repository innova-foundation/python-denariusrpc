#create new Denarius DDNS name based on name, value and expiration
from denariusrpc.authproxy import AuthServiceProxy, JSONRPCException

#DDNS to create data
ddns_create_name = 'api:python_example'
ddns_create_value = 'example value'
ddns_create_expiration = 9999

# rpc_user and rpc_password are set in the denarius.conf file
rpc_connection = AuthServiceProxy("http://%s:%s@127.0.0.1:32369"%("rpcusername", "rpcpassword"))

name_create = rpc_connection.name_new(ddns_create_name, ddns_create_value, ddns_create_expiration)
print(name_create)

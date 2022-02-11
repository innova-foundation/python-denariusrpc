#create new Innova DDNS name based on name, value and expiration
from innovarpc.authproxy import AuthServiceProxy, JSONRPCException

#DDNS to create data
idns_create_name = 'api:python_example'
idns_create_value = 'example value'
idns_create_expiration = 9999

# rpc_user and rpc_password are set in the innova.conf file
rpc_connection = AuthServiceProxy("http://%s:%s@127.0.0.1:14531"%("rpcusername", "rpcpassword"))

name_create = rpc_connection.name_new(idns_create_name, idns_create_value, idns_create_expiration)
print(name_create)

from innovarpc.authproxy import AuthServiceProxy, JSONRPCException

#IDNS to update data
idns_update_name = 'api:python_example'
idns_update_value = 'example value update'
idns_update_expiration = 9999

# rpc_user and rpc_password are set in the innova.conf file
rpc_connection = AuthServiceProxy("http://%s:%s@127.0.0.1:14531"%("rpcusername", "rpcpassword"))

name_update = rpc_connection.name_update(idns_update_name, idns_update_value, idns_update_expiration)
print(name_update)

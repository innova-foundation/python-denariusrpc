from denariusrpc.authproxy import AuthServiceProxy, JSONRPCException

#DDNS to update data
ddns_update_name = 'api:python_example'
ddns_update_value = 'example value update'
ddns_update_expiration = 9999

# rpc_user and rpc_password are set in the denarius.conf file
rpc_connection = AuthServiceProxy("http://%s:%s@127.0.0.1:32369"%("rpcusername", "rpcpassword"))

name_update = rpc_connection.name_update(ddns_update_name, ddns_update_value, ddns_update_expiration)
print(name_update)

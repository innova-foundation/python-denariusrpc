from innovarpc.authproxy import AuthServiceProxy, JSONRPCException

# rpc_user and rpc_password are set in the innova.conf file
rpc_connection = AuthServiceProxy("http://%s:%s@127.0.0.1:14531"%("user", "password"))
get_block_count = rpc_connection.getblockcount()
print "Block Height:", (get_block_count)
get_staking_info = rpc_connection.getstakinginfo()
print "Wallet Staking Weight:", (get_staking_info[u'weight'])
print "Net Stake Weight:", (get_staking_info[u'netstakeweight'])

get_info = rpc_connection.getinfo()
print "Peers:", (get_info[u'connections'])
print "Daemon Version:", (get_info[u'version'])

get_blockchain_info = rpc_connection.getblockchaininfo()
print "Circulating:", (get_blockchain_info[u'moneysupply']), "INN"

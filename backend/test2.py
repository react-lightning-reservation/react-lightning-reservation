from lndgrpc import LNDClient

# from https://github.com/adrienemery/lnd-grpc-client

# pass in the ip-address with RPC port and network ('mainnet', 'testnet', 'simnet')
# the client defaults to 127.0.0.1:10009 and mainnet if no args provided
lnd = LNDClient("192.168.2.237:10009", network='mainnet', macaroon_filepath='../private/lnd/admin.macaroon', cert_filepath='../private/lnd/tls.cert')

lnd.get_info()


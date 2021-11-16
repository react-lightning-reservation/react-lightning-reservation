import lightning_pb2 as ln
import lightning_pb2_grpc as lnrpc
import grpc
import os
import codecs

# Due to updated ECDSA generated tls.cert we need to let gprc know that
# we need to use that cipher suite otherwise there will be a handhsake
# error when we communicate with the lnd rpc server.
os.environ["GRPC_SSL_CIPHER_SUITES"] = 'HIGH+ECDSA'
#os.environ["GRPC_SSL_CIPHER_SUITES"] = (
#    "ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-SHA256:ECDHE-RSA-AES256-SHA384:"
#    "ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES128-GCM-SHA256:"
#    "ECDHE-ECDSA-AES128-SHA256:ECDHE-ECDSA-AES256-SHA384:ECDHE-ECDSA-AES256-GCM-SHA384"
#)

# Lnd cert is at ~/.lnd/tls.cert on Linux and
# ~/Library/Application Support/Lnd/tls.cert on Mac
cert = open(os.path.expanduser('../private/lnd/tls.cert'), 'rb').read()
creds = grpc.ssl_channel_credentials(cert)
channel = grpc.secure_channel('192.168.2.237:10009', creds)
#channel = grpc.insecure_channel('192.168.2.237:10009')
stub = lnrpc.LightningStub(channel)

with open(os.path.expanduser('../private/lnd/admin.macaroon'), 'rb') as f:
    macaroon_bytes = f.read()
    macaroon = codecs.encode(macaroon_bytes, 'hex')

response = stub.WalletBalance(ln.WalletBalanceRequest(), metadata=[('macaroon', macaroon)])
print(response.total_balance)

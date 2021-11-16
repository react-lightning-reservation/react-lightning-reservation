#!/usr/bin/env python3
import json
import web
import lightning_pb2 as ln
import lightning_pb2_grpc as lnrpc
import grpc
import os
import codecs

f = open('slot_data.json')
data = json.load(f)
f.close()

urls = (
    '/slots', 'list_slots',
    '/slots/(.*)', 'get_slot',
    '/invoices', 'list_invoices',
    '/invoices/(.*)', 'get_invoice'
)

# Due to updated ECDSA generated tls.cert we need to let gprc know that
# we need to use that cipher suite otherwise there will be a handhsake
# error when we communicate with the lnd rpc server.
os.environ["GRPC_SSL_CIPHER_SUITES"] = 'HIGH+ECDSA'

cert = open(os.path.expanduser('../private/lnd/tls.cert'), 'rb').read()
creds = grpc.ssl_channel_credentials(cert)
channel = grpc.secure_channel('192.168.2.237:10009', creds)
stub = lnrpc.LightningStub(channel)
with open(os.path.expanduser('../private/lnd/admin.macaroon'), 'rb') as f:
    macaroon_bytes = f.read()
    macaroon = codecs.encode(macaroon_bytes, 'hex')

app = web.application(urls, globals())
class list_slots:        
    def GET(self):
        web.header('Access-Control-Allow-Origin', '*')
        web.header('Access-Control-Allow-Credentials', 'true')
        return json.dumps(data)

class get_slot:
    def GET(self, id):
        web.header('Access-Control-Allow-Origin', '*')
        web.header('Access-Control-Allow-Credentials', 'true')
        for s in data['slots']:
            if s['id'] == id:
                return json.dumps(s)
        web.notfound(self)
        return "not found"

class list_invoices:        
    def GET(self):
        web.header('Access-Control-Allow-Origin', '*')
        web.header('Access-Control-Allow-Credentials', 'true')
        response = stub.ListInvoices(ln.ListInvoiceRequest(), metadata=[('macaroon', macaroon)])
        return json.dumps(response)
        
class get_invoice:
    def GET(self, id):
        web.header('Access-Control-Allow-Origin', '*')
        web.header('Access-Control-Allow-Credentials', 'true')
        response = stub.ListInvoices(ln.ListInvoiceRequest(), metadata=[('macaroon', macaroon)])
        for s in response['invoices']:
            if s['payment_request'] == id:
                return json.dumps(s)
        web.notfound(self)
        return "not found"

if __name__ == "__main__":
    app.run()
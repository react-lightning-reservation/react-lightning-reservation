#!/bin/bash
python3 -m venv myvenv
source myvenv/bin/activate
pip3 install -r requirements.txt
git clone https://github.com/googleapis/googleapis.git
# not as instructed: curl -o rpc.proto -s https://raw.githubusercontent.com/lightningnetwork/lnd/master/lnrpc/rpc.proto
#curl -o lightning.proto -s https://raw.githubusercontent.com/lightningnetwork/lnd/master/lnrpc/lightning.proto
# curl -o lightning.proto -s https://raw.githubusercontent.com/lightningnetwork/lnd/c4e55bbe6b19d53d5c7af946ab7d31237de08179/lnrpc/lightning.proto
curl -o lightning.proto -s https://raw.githubusercontent.com/lightningnetwork/lnd/0-13-4-branch/lnrpc/rpc.proto
python3 -m grpc_tools.protoc --proto_path=googleapis:. --python_out=. --grpc_python_out=. lightning.proto
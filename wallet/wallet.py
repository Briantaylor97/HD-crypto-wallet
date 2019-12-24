from constants import *
import subprocess
import os
import json
import web3
from web3 import Web3
from dotenv import load_dotenv
from web3.middleware import geth_poa_middleware
from web3.gas_strategies.time_based import medium_gas_price_strategy
from eth_account import Account
from bit import Key, PrivateKey, PrivateKeyTestnet
from bit.network import NetworkAPI, satoshi_to_currency
from pathlib import Path
from getpass import getpass

load_dotenv()
mnemonic= os.getenv("MNEMONIC")
priv_key= os.getenv("PRIVATE_KEY")
conn = Web3.HTTPProvider("http://127.0.0.1:8545")
w3 = Web3(conn)
w3.middleware_onion.inject(geth_poa_middleware, layer=0)

print(mnemonic)
print(pkey)

#Functions for wallet

#def derive_wallet(mnemonic, coins):
 #   coin_store= {}
  #  for coin in coins:
   #     bash_command = f'php ./derive -g --format=json --coin={coin} --'









#def create_tx(account, recipient, amount):
    #gasEstimate = w3.eth.estimateGas(
       # {"from": account.address,
       # "to": recipient,
       # "value": amount}
    #)
    #return {
     #   "from": account.address,
     #   "to": recipient,
     #   "value": amount,
     #   "gasPrice": w3.eth.gasPrice,
     #   "gas": gasEstimate,
     #   "nonce": w3.eth.getTransactionCount(account.address),
    #}

#def send_tx(account, recipient, amount):
 #   tx = create_raw_tx(account, recipient, amount)
 #   signed_tx = account.sign_transaction(tx)
 #   result = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
 #   print(result.hex())
 #   return result.hex()
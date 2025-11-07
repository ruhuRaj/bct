import random
from web3 import Web3,HTTPProvider
from ca import *
import json
from time import sleep

def sensorydata():
    voltage=random.randint(1,10)
    current=random.randint(1,4)
    return voltage,current

def connect_Blockchain_iot(acc):
    blockchain_address="http://127.0.0.1:7545"
    web3=Web3(HTTPProvider(blockchain_address))
    if(acc==0):
        acc=web3.eth.accounts[0]
    web3.eth.defaultAccount=acc
    artifact_path='build/contracts/power.json'
    contract_address=powerContractAddress
    with open(artifact_path) as f:
        contract_json=json.load(f)
        contract_abi=contract_json['abi']

    contract=web3.eth.contract(address=contract_address,abi=contract_abi)
    print('connected with blockchain')
    return (contract,web3)

while True:
    v,c=sensorydata()
    contract,web3=connect_Blockchain_iot(0)
    tx_hash=contract.functions.addPower(v,c).transact()
    web3.eth.waitForTransactionReceipt(tx_hash)
    sleep(5)
    status=contract.functions.viewPower().call()
    print('Block Added and Cumulative Power is',status)


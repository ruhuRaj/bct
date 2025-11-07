import streamlit as st
from web3 import Web3, HTTPProvider
from ca import *
import json
import time

def connect_Blockchain_iot(acc):
    blockchain_address="http://127.0.0.1:7545"
    web3=Web3(HTTPProvider(blockchain_address))
    if(acc==0):
        acc=web3.eth.accounts[0]
    web3.eth.defaultAccount=acc
    artifact_path='c:/Users/BITG/Desktop/lower-electricity-bills-using-blockchain-main/build/contracts/power.json'
    contract_address=powerContractAddress
    with open(artifact_path) as f:
        contract_json=json.load(f)
        contract_abi=contract_json['abi']

    contract=web3.eth.contract(address=contract_address,abi=contract_abi)
    print('connected with blockchain')
    return (contract,web3)

st.title('Lower Electricity Bills using Blockchain')

contract,web3=connect_Blockchain_iot(0)
status=contract.functions.checkPower().call()
st.success(status)
if(status==1):
    st.image('c:/Users/BITG/Desktop/lower-electricity-bills-using-blockchain-main/src/solar_roof.jpg')
else:
    st.image('c:/Users/BITG/Desktop/lower-electricity-bills-using-blockchain-main/src/power_grid.jpg')

time.sleep(4)
st.rerun()
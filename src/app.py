import os
from pathlib import Path
import streamlit as st
from web3 import Web3, HTTPProvider
from ca import powerContractAddress
import json

# Directories
SRC_DIR = Path(__file__).resolve().parent
REPO_ROOT = SRC_DIR.parent

# Configurable via environment variables for deployment
RPC_URL = os.getenv("RPC_URL", "http://127.0.0.1:7545")
CONTRACT_ADDRESS = os.getenv("CONTRACT_ADDRESS", powerContractAddress)


def connect_Blockchain_iot(acc):
    web3 = Web3(HTTPProvider(RPC_URL))
    if not web3.isConnected():
        st.warning(f"Could not connect to blockchain node at {RPC_URL}")
        return (None, web3)

    if acc == 0:
        # web3.eth.accounts may be empty depending on provider
        acc = web3.eth.accounts[0] if web3.eth.accounts else None

    web3.eth.default_account = acc

    artifact_path = REPO_ROOT / 'build' / 'contracts' / 'power.json'
    if not artifact_path.exists():
        st.error(f"Contract artifact not found: {artifact_path}")
        return (None, web3)

    with open(artifact_path) as f:
        contract_json = json.load(f)
        contract_abi = contract_json.get('abi')

    contract = web3.eth.contract(address=CONTRACT_ADDRESS, abi=contract_abi)
    return (contract, web3)


st.title('Lower Electricity Bills using Blockchain')

contract, web3 = connect_Blockchain_iot(0)
if contract is None:
    # connect_Blockchain_iot already displayed an error/warning
    st.stop()

try:
    status = contract.functions.checkPower().call()
    st.success(f"Power status: {status}")

    # Images are stored in src/ — use a relative path so Streamlit Cloud can find them
    img_path = SRC_DIR / ('solar_roof.jpg' if status == 1 else 'power_grid.jpg')
    if img_path.exists():
        st.image(str(img_path))
    else:
        st.warning(f"Image not found: {img_path}")

except Exception as e:
    st.error("Error calling contract function. See details below.")
    st.exception(e)
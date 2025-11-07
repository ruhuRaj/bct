# Lower Electricity Bills using Blockchain

This repository contains a demo Streamlit app and a Solidity smart contract that illustrate how on-chain data could influence an application's UI.

Quick files
- `src/app.py` — Streamlit app (entrypoint)
- `src/ca.py` — contract address (now configurable via env var)
- `build/contracts/power.json` — compiled contract artifact (ABI)
- `contracts/power.sol` — smart contract source

Prerequisites
- Node.js + Truffle (for compiling & deploying contracts)
- Ganache (for local testing) or an RPC provider (Infura/Alchemy) for public testnets
- Python 3.8+ and a virtual environment

Python dependencies
- See `requirements.txt`. Streamlit Cloud will install these automatically when deploying.

Run locally (dev)
1. Start Ganache (if testing locally).
2. Deploy contracts to Ganache:
	```bash
	truffle migrate --reset
	```
3. Run the Streamlit app from the project root (use your venv):
	```powershell
	.\.venv\Scripts\streamlit.exe run src/app.py
	```

Deploy to Streamlit Community Cloud
1. Push this repository to GitHub (already done: `ruhuRaj/bct`).
2. On Streamlit Cloud create a new app with:
	- Repository: `ruhuRaj/bct`
	- Branch: `main`
	- Main file path: `src/app.py`
3. Set the following Environment Variables (Settings → Secrets):
	- `RPC_URL` — an HTTP RPC endpoint for the network you want to query (e.g. Infura/Alchemy URL for Goerli/Mainnet).
	- `CONTRACT_ADDRESS` — the deployed `power` contract address on the same network as `RPC_URL`.

Notes
- The app's default configuration connects to Ganache on `http://127.0.0.1:7545`. When deploying to Streamlit Cloud you must supply a public RPC in `RPC_URL` and a public `CONTRACT_ADDRESS` on that network.
- `src/ca.py` reads `CONTRACT_ADDRESS` from the environment if available — safer for deployments.

Optional help
- If you'd like, I can:
  - Add a deployment script for Truffle+Infura to deploy to a public testnet.
  - Make the app automatically read ABI from `build/contracts/power.json` and fall back gracefully if missing.

Contact
For questions, reach out on LinkedIn: https://linkedin.com/in/MadhuPIoT

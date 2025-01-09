from flask import Flask, render_template, request, session, jsonify, redirect, url_for
from web3 import Web3
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = '6cc539744a69a12bdf6fe9ebbb6f'

# Connect to Ethereum network (Infura URL)
infura_url = 'https://mainnet.infura.io/v3/6cc5397709d44a69afe9ebbb6f'  # Replace with your own Infura Project ID
web3 = Web3(Web3.HTTPProvider(infura_url))

if not web3.is_connected():
    raise ConnectionError("Failed to connect to Ethereum network.")

# Load ERC-20 ABI
try:
    with open('erc20_abi.json') as f:
        erc20_abi = json.load(f)
except FileNotFoundError:
    raise FileNotFoundError("The 'erc20_abi.json' file is missing.")

# Routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/create_wallet', methods=['GET', 'POST'])
def create_wallet():
    wallet_info = None
    error = None

    if request.method == 'POST':
        wallet_name = request.form.get('wallet_name')

        try:
            # Create a new wallet if no session exists
            account = web3.eth.account.create(wallet_name)
            wallet_info = {
                'address': account.address,
                'private_key': account.key.hex()
            }
            session['wallet_info'] = wallet_info  # Save the wallet info in session
            session['transactions'] = []  # Initialize an empty list for transactions
            return redirect(url_for('view_wallet'))  # Redirect to view the wallet
        except Exception as e:
            error = str(e)

    return render_template('create_wallet.html', wallet_info=wallet_info, error=error)

@app.route('/view_wallet')
def view_wallet():
    wallet_info = session.get('wallet_info')

    if not wallet_info:
        return redirect(url_for('create_wallet'))  # If no wallet found, redirect to create wallet

    # Get transaction history from session
    transactions = session.get('transactions', [])
    
    return render_template('view_wallet.html', wallet_info=wallet_info, transactions=transactions)

@app.route('/send_transaction', methods=['POST'])
def send_transaction():
    data = request.json
    wallet_info = session.get('wallet_info')
    if not wallet_info:
        return jsonify({'error': 'No wallet information found.'}), 400

    private_key = wallet_info['private_key']
    address = wallet_info['address']
    nonce = web3.eth.get_transaction_count(Web3.to_checksum_address(address))

    txn = {
        'to': data['to'],
        'value': web3.to_wei(data['amount'], 'ether'),
        'gas': 21000,
        'gasPrice': web3.to_wei('50', 'gwei'),
        'nonce': nonce
    }

    signed_txn = web3.eth.account.sign_transaction(txn, private_key)
    txn_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)

    # Store the transaction hash in session
    transactions = session.get('transactions', [])
    transactions.append(txn_hash.hex())
    session['transactions'] = transactions

    return jsonify({'transaction_hash': txn_hash.hex()})

@app.route('/transaction_details/<txn_hash>', methods=['GET'])
def transaction_details(txn_hash):
    try:
        # Fetch transaction receipt using txn_hash
        txn_receipt = web3.eth.get_transaction_receipt(txn_hash)
        if txn_receipt is None:
            return jsonify({'error': 'Transaction not found or pending.'}), 404

        # Get the full transaction details
        txn_details = web3.eth.get_transaction(txn_hash)
        return jsonify({
            'txn_hash': txn_hash,
            'from': txn_details['from'],
            'to': txn_details['to'],
            'value': web3.from_wei(txn_details['value'], 'ether'),
            'gas_used': txn_receipt['gasUsed'],
            'block_number': txn_receipt['blockNumber'],
            'status': txn_receipt['status']
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

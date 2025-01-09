# Crypto Wallet Flask Application

## **Project Overview**
This project is a simple Flask-based web application for managing Ethereum wallets. It allows users to create a new wallet, view wallet details, send transactions, and track transaction history. The app interacts with the Ethereum blockchain using the Web3.py library and provides a user-friendly interface for basic wallet operations.

---

## **Features**
1. **Wallet Creation**:
   - Generate a new Ethereum wallet with a unique address and private key.
   - Wallet information is securely stored in the session.

2. **View Wallet**:
   - Display wallet address and private key.
   - View transaction history associated with the wallet.

3. **Send Transactions**:
   - Transfer Ether to other Ethereum addresses.
   - Track transaction hashes for verification.

4. **Transaction Details**:
   - Fetch and display detailed information for specific transactions.

5. **Error Handling**:
   - Provides meaningful error messages for issues like insufficient balance or invalid inputs.

---

## **Technologies Used**
- **Python**:
  - Flask: For building the web application.
  - Web3.py: For interacting with the Ethereum blockchain.
  - JSON: For handling ABI and request/response data.
- **Frontend**:
  - HTML5, CSS3, Bootstrap: For responsive and user-friendly UI.
- **Blockchain**:
  - Ethereum network via Infura.

---

## **Setup Instructions**

### **Prerequisites**
- Python 3.7+
- An Infura Project ID for Ethereum network access
- A stable internet connection

### **Installation**
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/crypto-wallet-app.git
   cd crypto-wallet-app
   ```
2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Create a file named `erc20_abi.json` in the project root and paste the ABI of an ERC-20 token if required.

5. Replace the Infura URL in the code with your Infura Project ID:
   ```python
   infura_url = 'https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID'
   ```

---

## **How to Run**
1. Start the Flask application:
   ```bash
   python app.py
   ```
2. Open your browser and navigate to:
   ```
   http://127.0.0.1:5000/
   ```
3. Use the interface to create wallets, view wallet details, and send transactions.

---

## **Project Structure**
```
crypto-wallet-app/
|-- templates/
|   |-- index.html           # Landing page
|   |-- create_wallet.html   # Create wallet interface
|   |-- view_wallet.html     # Wallet and transaction details
|-- static/
|   |-- css/                 # Custom styles (optional)
|-- app.py                   # Main Flask application
|-- erc20_abi.json           # ABI for ERC-20 tokens (if needed)
|-- requirements.txt         # Python dependencies
```

---

## **API Endpoints**

### **1. Home**
- **URL**: `/`
- **Method**: GET
- **Description**: Landing page for the application.

### **2. Create Wallet**
- **URL**: `/create_wallet`
- **Method**: GET, POST
- **Description**: Create a new Ethereum wallet.
- **Input**: Wallet name (optional).
- **Output**: Wallet address and private key.

### **3. View Wallet**
- **URL**: `/view_wallet`
- **Method**: GET
- **Description**: View wallet details and transaction history.

### **4. Send Transaction**
- **URL**: `/send_transaction`
- **Method**: POST
- **Description**: Send Ether to another address.
- **Input**: JSON payload with `to` (recipient address) and `amount` (Ether).
- **Output**: Transaction hash.

### **5. Transaction Details**
- **URL**: `/transaction_details/<txn_hash>`
- **Method**: GET
- **Description**: Fetch detailed information about a transaction.
- **Input**: Transaction hash.
- **Output**: Transaction details including block number, gas used, status, etc.

---

## **Security Considerations**
1. **Private Key Management**:
   - The private key is displayed in the application for demonstration purposes but should never be exposed in production.
   - Use encrypted storage or environment variables for private keys.

2. **HTTPS**:
   - Deploy the application over HTTPS to secure data transmission.

3. **Rate Limiting**:
   - Implement rate limiting to prevent abuse of transaction APIs.

4. **Error Handling**:
   - Validate inputs to prevent invalid transactions.
   - Gracefully handle exceptions and provide meaningful error messages.

---

## **Future Enhancements**
1. **ERC-20 Token Support**:
   - Extend the app to send and receive ERC-20 tokens.

2. **User Authentication**:
   - Add user login and session management for multi-user support.

3. **Advanced Transactions**:
   - Support custom gas prices and limits.

4. **Deployment**:
   - Deploy the application to cloud platforms like AWS, Heroku, or Azure.

5. **Mobile-Friendly UI**:
   - Enhance the design for a seamless mobile experience.

---

## **License**
This project is licensed under the MIT License.

---

## **Contact**
For any queries or contributions, feel free to reach out:
- **Email**: your.email@example.com
- **GitHub**: [your-github-username](https://github.com/your-github-username)


from web3 import Web3

web3 = Web3(Web3.HTTPProvider('https://eth-sepolia.g.alchemy.com/v2/GUwpQv7dGLI2Ba4ecDTplOZmw2ubB2ue'))

# print(web3.is_connected())

balance = web3.eth.get_balance('0x967D5De076f1cba86eA1723453a475d29CE708E7')
balance_address1_in_wei = web3.from_wei(balance, 'ether')

print(balance_address1_in_wei)

from_account = '0x967D5De076f1cba86eA1723453a475d29CE708E7'
to_account = '0x49b4973d2f77fa21eC778faf3490e96cf91D20Ff'
private_key = 'f590645b0f9d23997fd68e54fb708223b7372118cf088f625ebf8cdcc45eb7da'

address1 = Web3.to_checksum_address(from_account)
address2 = Web3.to_checksum_address(to_account)

nonce = web3.eth.get_transaction_count(address1)

tx = {
    'nonce': nonce,
    'to': address2,
    'value': web3.to_wei(0.001, 'ether'),
    'gas': 21000,
    'gasPrice': web3.to_wei(40, 'gwei')
}

signed_tx = web3.eth.account.sign_transaction(tx, private_key)

tx_transaction = web3.eth.send_raw_transaction(signed_tx.rawTransaction)

balance_address2 = web3.eth.get_balance(to_account)

balance_address2_in_wei = web3.from_wei(balance_address2, 'ether')

print(balance_address2_in_wei)

import requests
import config as config


def get_pinned_files():
    pinata_api_url = 'https://api.pinata.cloud'
    endpoint = '/data/pinList?status=pinned'
    headers = {
        'Content-Type': 'application/json',
        'pinata_api_key': str(config.PINATA_API_Key),
        'pinata_secret_api_key': str(config.PINATA_API_Secret)
    }
    response = requests.get(
        f'{pinata_api_url}{endpoint}',
        headers=headers
    )
    data = response.json()
    print(data)
    files = []
    if response.status_code == 200:
        for item in data['rows']:
            file_info = {
                'name': item['metadata']['name'],
                'ipfs_hash': item['ipfs_pin_hash'],
                'date_pinned': item['date_pinned']
            }
            files.append(file_info)
    else:
        files.append({'error': 'Failed to get list of pinned files'})

    return files

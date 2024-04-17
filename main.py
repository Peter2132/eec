from web3 import Web3
from web3.middleware import geth_poa_middleware
from contract_info import abi, contract_address

W3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
W3.middleware_onion.inject(geth_poa_middleware, layer=0)

contract = W3.eth.contract(address=contract_address, abi=abi)
print(contract.address)


balance1 = W3.eth.get_balance('0x1993C25c66Cfe4c602eAc4Cf126A463ca4E8eC96')
balance2 = W3.eth.get_balance('0xa59F109f7e98C8Cf59461187699243468E43bfcb')
balance3 = W3.eth.get_balance('0x1ACDA6bd40d28092Aa92813C545f00DF7b301C56')
balance4 = W3.eth.get_balance('0xA521b902AD580222C10a15943f243C179BdFbABc')
balance5 = W3.eth.get_balance('0x78194966F2dD91b7798Fef46DaA7e907b6A77B12')


print(balance1,balance2, balance3, balance4, balance5)


def auth():
    public_key = input('Enter public key: ')
    password = input('Enter password: ')
    try:
        W3.genth.personal.unlock_account(public_key, password)
        return public_key
    except Exception as e:
        print(f"error {e}")
        return None

def register():
    password = input('Enter password: ')
    address = W3.geth.personal.new_account(password)
    print(f"Your address: {address}")


def sendEth(account):
    pass

def getBalance(account):
    pass

def withDraw(account):
    pass

def main():
    account = ""
    is_auth = False
    while True:
        if not is_auth:
            choise = input("выберите:\n1. Avtor\n2. Regis")
            match choise:
                case "1":
                    account = auth()
                    if account != None and account != "":
                        is_auth = True
                case "2":
                    register()
                case _:
                    print("Error")
        elif is_auth:
            choise = input("Enter:\n1. Send efir\n2. Chek balance\n3. Balance\n4/. Show balance\n5. Exit")
            match choise:
                case "1":
                    sendEth(account)
                case "2":
                    getBalance(account)
                case "3":
                    withDraw(account)
                case "4":
                    pass
                case "5":
                    is_auth = False
                case _:
                    print("Not correct")

if __name__ == "__main__":
    main()




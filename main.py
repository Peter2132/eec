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

from enum import Enum

class AdStatus(Enum):
    OPEN = 0
    CLOSED = 1


import re

def validate_password(password):
    if len(password) < 8:
        return False, "Пароль должен содержать минимум 8 символов."
    if not re.search("[0-9]", password):
        return False, "Пароль должен содержать хотя бы одну цифру."
    if not re.search("[A-Z]", password):
        return False, "Пароль должен содержать хотя бы одну заглавную букву."
    if not re.search("[a-z]", password):
        return False, "Пароль должен содержать хотя бы одну строчную букву."
    if not re.search("[!@#$%^&*(),.?\":{}|<>]", password):
        return False, "Пароль должен содержать хотя бы один специальный символ."
    return True, "Пароль валиден."

# Используйте эту функцию в вашем методе регистрации
def register():
    password = input('Введите пароль: ')
    valid, message = validate_password(password)
    if not valid:
        print(message)
        return
    address = W3.geth.personal.new_account(password)
    print(f"Ваш адрес: {address}")

def auth():
    public_key = input('Enter public key: ')
    password = input('Enter password: ')
    try:
        W3.geth.personal.unlock_account(public_key, password)
        return public_key
    except Exception as e:
        print(f"error {e}")
        return None




def sendEth(account):
    try:
        value = int(input("Enter summu for transfer: "))
        tx_hash = contract.functions.sendEth().transact({
            'from': account,
            'value': value,
        })
        print(f"Transact send: {tx_hash.hex()}")

    except Exception as e:
        print(f"Error: {e}")


def getBalance(account):
    try:
        balance = contract.functions.getBalance().call({
            'from': account,
        })
        print(f"Balance on the SmartContract: {balance} wei")
    except Exception as e:
        print(f"Error: {e}")

def withDraw(account):
    try:
        to = input("Enter addres account: ")
        amount = int(input("Enter summu for transfer on smart-contract: "))
        tx_hash = contract.functions.withdrawll(to, amount).transact({
            'from': account,
        })
        print(f"Balance on the SmartContract: {tx_hash.hex()} ")
    except Exception as e:
        print(f"Error: {e}")
def create_estate(square, rooms, es_type, account):
    try:
        tx_hash = contract.functions.createEstate(square, rooms, es_type).transact({
            'from': account
        })
        print(f"Estate created: {tx_hash.hex()}")
    except Exception as e:
        print(f"Error: {e}")

def update_estate_status(estate_id, new_status, account):
    try:
        tx_hash = contract.functions.updateEstateStatus(estate_id, new_status).transact({
            'from': account
        })
        print(f"Estate status updated: {tx_hash.hex()}")
    except Exception as e:
        print(f"Error: {e}")

def create_ad(estate_id, price, account):
    try:
        tx_hash = contract.functions.createAd(estate_id, price).transact({
            'from': account
        })
        print(f"Ad created: {tx_hash.hex()}")
    except Exception as e:
        print(f"Error: {e}")

def update_ad_status(ad_id, new_status, account):
    try:
        tx_hash = contract.functions.updateAdStatus(ad_id, new_status).transact({
            'from': account
        })
        print(f"Ad status updated: {tx_hash.hex()}")
    except Exception as e:
        print(f"Error: {e}")

def buy_estate(ad_id, value, account):
    try:
        tx_hash = contract.functions.buyEstate(ad_id).transact({
            'from': account,
            'value': value
        })
        print(f"Estate purchased: {tx_hash.hex()}")
    except Exception as e:
        print(f"Error: {e}")


def get_balance(account):
    balance = contract.functions.getBalance().call({
        'from': account
    })
    print(f"Баланс: {balance} wei")
    return balance

def get_estates():
    estates = contract.functions.getEstates().call()
    for estate in estates:
        print(f"ID: {estate[0]}, Площадь: {estate[1]}, Комнаты: {estate[2]}, Тип: {estate[3]}")
    return estates

def get_ads():
    ads = contract.functions.getAds().call()
    for ad in ads:
        print(f"ID: {ad[0]}, ID недвижимости: {ad[1]}, Цена: {ad[2]}, Статус: {'Открыто' if ad[3] == 0 else 'Закрыто'}")
    return ads

def main():
    account = ""
    is_auth = False
    while True:
        if not is_auth:
            choice = input("Выберите:\n1. Авторизация\n2. Регистрация\n")
            match choice:
                case "1":
                    account = auth()
                    if account is not None and account != "":
                        is_auth = True
                case "2":
                    register()
                case _:
                    print("Ошибка ввода.")
        elif is_auth:
            choice = input("Введите:\n1. Отправить эфир\n2. Проверить баланс\n3. Снять средства\n4. Показать баланс аккаунта\n5. Создать недвижимость\n6. Создать объявление\n7. Обновить статус недвижимости\n8. Обновить статус объявления\n9. Купить недвижимость\n10. Получить информацию о недвижимостях\n11. Получить информацию о объявлениях\n12. Выход\n")
            match choice:
                case "1":
                    sendEth(account)
                case "2":
                    get_balance(account)
                case "3":
                    withDraw(account)
                case "4":
                    print(f"Баланс аккаунта: {W3.eth.get_balance(account)}")
                case "5":
                    square = int(input("Введите площадь: "))
                    rooms = int(input("Введите количество комнат: "))
                    es_type = int(input("Введите тип недвижимости (0, 1, 2...): "))
                    create_estate(square, rooms, es_type)
                case "6":
                    estate_id = int(input("Введите ID недвижимости: "))
                    price = int(input("Введите цену: "))
                    create_ad(estate_id, price)
                case "7":
                    estate_id = int(input("Введите ID недвижимости: "))
                    new_status = input("Введите новый статус (true/false): ").lower() == 'true'
                    update_estate_status(estate_id, new_status)
                case "8":
                    ad_id = int(input("Введите ID объявления: "))
                    new_status = input("Введите новый статус (0 - Открыто, 1 - Закрыто): ")
                    update_ad_status(ad_id, AdStatus(int(new_status)))
                case "9":
                    ad_id = int(input("Введите ID объявления: "))
                    value = int(input("Введите сумму для покупки: "))
                    buy_estate(ad_id, value)
                case "10":
                    get_estates()
                case "11":
                    get_ads()
                case "12":
                    is_auth = False
                case _:
                    print("Некорректный ввод.")

if __name__ == "__main__":
    main()





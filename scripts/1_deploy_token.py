from brownie import AgroToken
from scripts.helpful_scripts import get_account
from web3 import Web3

initial_supply = Web3.toWei(1000, 'ether')


def main():
    account = get_account()
    agro_token = AgroToken.deploy(initial_supply, {"from": account})
    print(agro_token.name())

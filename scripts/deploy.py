from eth_account import Account
from brownie import FundMe, network, config, MockV3Aggregator

# import get_account function
from scripts.helpful_scripts import (
    get_account,
    deploy_mocks,
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
)


def deploy_fund_me():
    account = get_account()
    # we can pass variable to constructor in deploy() setting

    # if we are on a persistent network like rinkeby, use the associated address
    # otherwise, deploy mocks AggregatorV3Interface
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    else:
        deploy_mocks()
        # use the latest deployed Mock
        price_feed_address = MockV3Aggregator[-1].address

    # "publish_source = True" use my own API key to verify, publish and flaten contract
    # "publish_source = config" means if it is in development network,
    #  no verify is needed.

    # we can pass variable to constructor in deploy() setting
    # price_feed_address will be passed to variable in constructor in FundMe.sol
    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()]["verify"],
    )
    print(f"Contract deployed to {fund_me.address}")
    # return fund_me so we have fundMe contract to work with during testing
    return fund_me


def main():
    deploy_fund_me()

from brownie import accounts, config, network, MockV3Aggregator
from web3 import Web3

DECIMAL = 8
STARTING_PRICE = 20000000000

# we add new network "ganache-local" under ethereum as persistent network
# but it is also a local network
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]

# we fork a mainnet for local use
FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork", "mainnet-fork-dev"]


def get_account():
    # if network is development, which means local blockchain
    # with self-created accounts, then we use those accounts
    # if network is not development, we use our own account from MetaMask
    if (
        network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS
        or network.show_active() in FORKED_LOCAL_ENVIRONMENTS
    ):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])
        # If we want to use our own account from MetaMask
        # use the following code and we just need to enter password
        # during execution
        # return accounts.load("Test_Account_Alpha")


def deploy_mocks():
    print(f"The active network is {network.show_active()}")
    print("Deploying Mocks...")
    # we can pass variable to constructor in deploy() setting
    # decimal - 18 and _initialAnswer - 20000000000
    # will be passed to variables in constructor in MockV3Aggregator.sol
    # since we need to deploy mock which is a contract, we need to
    # specify our account address

    # len(MockV3Aggregator) <= 0 meaning if Mock has not been deployed before
    # if it has been deployed before, then use the latest one.
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(DECIMAL, STARTING_PRICE, {"from": get_account()})
    print("Mocks Deployed")


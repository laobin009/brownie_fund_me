from scripts.helpful_scripts import get_account, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from scripts.deploy import deploy_fund_me
from brownie import network, accounts, exceptions
import pytest


def test_can_fund_and_withdraw():
    account = get_account()
    fund_me = deploy_fund_me()
    entrance_fee = fund_me.getEntranceFee() + 100
    tx = fund_me.fund({"from": account, "value": entrance_fee})
    tx.wait(1)
    assert fund_me.addressToAmountFunded(account.address) == entrance_fee
    tx2 = fund_me.withdraw({"from": account})
    tx2.wait(1)
    assert fund_me.addressToAmountFunded(account.address) == 0


# def test_only_owner_can_withdrawer():

#     # telling python that if we are using live network,
#     # then skip this test
#     if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
#         pytest.skip("only for local testing")

#     fund_me = deploy_fund_me()

#     # The Accounts.add method is used to randomly generate a new account:
#     bad_actor = accounts.add()

#     # this code tell pytest if there is this exception
#     # when running fund_me.withdraw({"from": bad_actor})
#     # then the test is pass.
#     with pytest.raises(exceptions.VirtualMachineError):
#         fund_me.withdraw({"from": bad_actor})


1. brownie cannot download npm package, so we set up to have packages
    downloaded from Github.
    We need to set it up on brownie-config.yaml "dependecies" and "compiler"
    Change to pragma solidity ^0.8.15;

2. after deploying FundMe.sol on Rinkeby, the contract need to be verified and
    flaten the contract, meaning the code of imported package need to be seen on 
    the contract instead of just using "import"
    1. we need to go to ethereum.io to create account and create API_key
    2. put API_key into .env
    3. patiently waiting for the process finished with 
        "Verification complete. Result: Pass - Verified"

3. dynamically getting eth-to-usd price from AggregatorV3Interface
    1. Add priceFeed in constructor in FundMe.sol
    2. modify getVersion() and getPrice() functions in FundMe.sol
    3. download Mock script for development network in contracts/test folder
    4. set up in deploy.py and helpful_scripts.py 

4. add new network in brownie, we want to have a persistent ganache-cli network
    that track all deployments and transactions.
    1. command "brownie networks add Ethereum ganache-local host=http://127.0.0.1:8545 chainid=1337"
    2. add LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]

5. create fund_and_withdraw.py script

6. testing
    1. using "brownie test -k" to test only one function,
        if we test two functions together, somehow the pytest.raises does not work

7. fork and customize a mainnet 
    1. using command "brownie_fund_me>brownie networks add development 
    mainnet-fork-dev cmd=ganache-cli host=http://127.0.0.1 
    fork=https://eth-mainnet.g.alchemy.com/v2/jDXw-zJNhf5XGvWJIuD9yGlnFes04QgU 
    accounts=10 mnemonic=brownie port=8545"
    2. the fork url is from alchemy "Fund Me Demo" view key detail
    3. because it is a development network, so it will terminate each run command
        and no saving of previous run.
        so we cannot run fund_and_withdraw.py after deploy.py
        since contract deployed in deploy.py is gone and clean out
        when we run fund_and_withdraw.py

8. Upload code to Github
    1. command - [git init -b main]
    2. command - [git config user.name "laobin009"]
        command - [git confi user.email"weibin.ye.leaf@gmail.com"]
    3. add ".env" to ".gitignore"
    4. command - [git commit -m "first commit"] we need to use double quotations here
    5. command - [git remote add origin https://github.com/laobin009/brownie_fund_me.git]
    6. command - [git push -u origin main]
    7. enter password

    Push to github after updating files in local
    1. command - [git status] - check what has been changed
    2. command - [git diff] - check changes details
    3. command - [git add ReadMe.txt]
    4. command - [git commit -m "Files update"]
    5. command - [git push -u origin main]

9. Run tests
    1. Brownie Ganache Chain with Mocks: Always
    2. Testnet: Always (but only for integration testing)
    3. Brownie mainnet-fork: Optional
    4. Custom mainnet-fork: Optional
    5. Self/Local Ganache: Notnecessary, but good for tinkering.
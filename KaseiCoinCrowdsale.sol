pragma solidity ^0.5.0;

import "./KaseiCoin.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/crowdsale/Crowdsale.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/crowdsale/emission/MintedCrowdsale.sol";

// Have the KaseiCoinCrowdsale contract inherit the following OpenZeppelin:
// * Crowdsale
// * MintedCrowdsale
contract KaseiCoinCrowdsale is Crowdsale, MintedCrowdsale {
    // Provide parameters for all of the features of your crowdsale, such as the `rate`, `wallet` for fundraising, and `token`.
    constructor(
        uint256 rate,
        address payable,
        KaseiCoin token // the KaseiCoin itself that the KaseiCoinCrowdsale will work with
    ) public Crowdsale(rate, wallet, token) {
        // constructor can stay empty
    }
}

contract KaseiCoinCrowdsaleDeployer {
    // Create an `address public` variable called `kasei_token_address`.
    // YOUR CODE HERE!
    address public kasei_token_address;
    // Create an `address public` variable called `kasei_crowdsale_address`.
    // YOUR CODE HERE!
    address public kasei_crowdsale_address;

    // Add the constructor.
    constructor(
        // YOUR CODE HERE!
        string memory name,
        string memory symbol,
        address payable wallet // this address will receive all Ether raised by the sale
    ) public {
        // Create a new instance of the KaseiCoin contract.
        // YOUR CODE HERE!
        KaseiCoin token = new KaseiCoin(name, symbol, 18);
        // Assign the token contract’s address to the `kasei_token_address` variable.
        // YOUR CODE HERE!
        kasei_token_address = address(token);
        // Create a new instance of the `KaseiCoinCrowdsale` contract
        // YOUR CODE HERE!
        KaseiCoinCrowdsale kasei_crowdsale = new KaseiCoinCrowdsale(
            1,
            wallet,
            token
        );
        // Aassign the `KaseiCoinCrowdsale` contract’s address to the `kasei_crowdsale_address` variable.
        // YOUR CODE HERE!
        kasei_crowdsale_address = address(kasei_crowdsale);
        // Set the `KaseiCoinCrowdsale` contract as a minter
        // YOUR CODE HERE!
        token.addMinter(kasei_crowdsale_address);
        // Have the `KaseiCoinCrowdsaleDeployer` renounce its minter role.
        // YOUR CODE HERE!
        token.renounceMinter();
    }
}
//My Wallet
// 0xF634ceAf7A72C10480bE7c4e3772aC14e11A1713

//Cowdsale Address
//0xe87181505BF3691c3fE28463CC87df48cbD5fCf5

//Token Address
//0x69329CAD0fae0468388F6Bb83Fb4cdAFAEC577bA

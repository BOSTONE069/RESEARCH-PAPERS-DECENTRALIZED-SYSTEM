// SPDX-License-Identifier: MIT

pragma solidity ^0.8.13;

contract ResearchPapers {

    // Struct to store details of each paper
    struct Paper {
        string title;
        string author;
        string ipfsHash;
        uint timestamp;
    }

    // Mapping to store papers by hash
    mapping (bytes32 => Paper) public papers;

    // Mapping to store ISP token balances by address
    mapping (address => uint256) public balances;

    // Total supply of ISP tokens
    uint256 public totalSupply = 1000000;

    // Conversion rate from wei to ISP tokens
    uint256 public conversionRate = 1 ether;

    // Token details
    string public constant name = "ISP Token";
    string public constant symbol = "ISP";
    uint8 public constant decimals = 18;

    // Event emitted on token transfer
    event Transfer(address indexed from, address indexed to, uint256 value);

    // Constructor to set initial ISP token balance for contract owner
    constructor() {
        //balances[msg.sender] = totalSupply * conversionRate;
    }

    // Function to publish a research paper
    function publishPaper(string memory _title, string memory _author, string memory _ipfsHash) public returns (bool) {
        bytes32 paperHash = keccak256(abi.encodePacked(_title, _author, _ipfsHash));
        // Make sure paper has not already been published
        require(papers[paperHash].timestamp == 0, "This paper has already been published.");

        // Store paper details
        papers[paperHash] = Paper({
            title: _title,
            author: _author,
            ipfsHash: _ipfsHash,
            timestamp: block.timestamp
        });

        return true;
    }

    // Function to get the IPFS hash of a published paper
    function getPaper(string memory _title, string memory _author, string memory _ipfsHash) public view returns (string memory) {
        bytes32 paperHash = keccak256(abi.encodePacked(_title, _author, _ipfsHash));
        // Make sure paper has been published
        require(papers[paperHash].timestamp != 0, "This paper has not been published yet.");

        return papers[paperHash].ipfsHash;
    }

    // Function to purchase ISP tokens
    function buyISP() public payable returns (bool) {
        uint256 amount = msg.value / conversionRate;
        // Make sure payment amount is greater than zero
        require(amount > 0, "Insufficient funds.");
        // Make sure enough tokens are available for purchase
        require(amount <= balances[address(this)], "Not enough tokens available for purchase.");

        // Update token balances
        balances[msg.sender] += amount;
        balances[address(this)] -= amount;

        // Emit transfer event
        emit Transfer(address(this), msg.sender, amount);

        return true;
    }

    // Function to view a published paper
    function viewPaper(string memory _title, string memory _author, string memory _ipfsHash) public returns (bool) {
        bytes32 paperHash = keccak256(abi.encodePacked(_title, _author, _ipfsHash));
        // Make sure paper has been published
        require(papers[paperHash].timestamp != 0, "This paper has not been published yet.");
        // Make sure user has enough ISP tokens to view paper
        require(balances[msg.sender] > 0, "You need to purchase ISP tokens to view this paper.");

        balances[msg.sender]--;

        return true;
    }

    // Function to withdraw funds from contract balance
    function withdraw() public returns (bool) {
        uint256 amount = address(this).balance;
        // Make sure balance is greater than zero
        require(amount > 0, "Insufficient funds.");

        // Transfer balance to sender address
        payable(msg.sender).transfer(amount);

        return true;
    }

}

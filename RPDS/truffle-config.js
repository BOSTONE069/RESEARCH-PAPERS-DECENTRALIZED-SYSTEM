const HDWalletProvider = require("@truffle/hdwallet-provider");
require("dotenv").config();

const { PROJECT_ID, MNEMONIC } = process.env;
module.exports = {
  contracts_build_directory: "./contracts",
  networks: {
    development: {
      host: "localhost",
      port: 7545,
      network_id: "*", // Match any network id
      gas: 5000000,
    },

    //sepolia network
    sepolia: {
      networkCheckTimeout: 10000,
      provider: () =>
        new HDWalletProvider(
          MNEMONIC,
          `https://eth-sepolia.g.alchemy.com/v2/${PROJECT_ID}`
        ),
      network_id: 11155111, // Sepolia id
      confirmations: 2,
      timeoutBlocks: 200,
    },

    mainnet: {
      provider: () =>
        new HDWalletProvider(
          MNEMONIC,
          `https://eth-mainnet.g.alchemy.com/v2/${PRODUCT_ID_MAINNET}`
        ),
      network_id: 1,
      confimation: 2,
      timeoutBlocks: 200,
      skipDryRun: true,
    },
  },

  compilers: {
    solc: {
      version: "^0.8.13",
      settings: {
        optimizer: {
          enabled: true, // Default: false
          runs: 200, // Default: 200
        },
      },
    },
  },
};
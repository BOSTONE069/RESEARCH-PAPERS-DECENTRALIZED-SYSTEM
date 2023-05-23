const researchPaper = artifacts.require("ResearchPapers");

module.exports = function (deployer) {
  deployer.deploy(researchPaper);
};

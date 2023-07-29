const paymentAmount = document.getElementById("paymentAmount");

async function makePayment() {
  const amount = paymentAmount.value;

  if (!amount || isNaN(amount) || amount <= 0) {
    alert("Please enter a valid payment amount.");
    return;
  }

  const paymentAddressValue = paymentAddress.value.trim();

  if (!paymentAddressValue) {
    alert("Please enter a valid payment address.");
    return;
  }

  const transactionParameters = {
    from: window.userWalletAddress,
    to: paymentAddressValue,
    value: window.ethereum.utils.toHex(window.ethereum.utils.toWei(amount)),
  };

  try {
    const txHash = await window.ethereum.request({
      method: "eth_sendTransaction",
      params: [transactionParameters],
    });

    console.log("Transaction hash:", txHash);

    // Optional: You can show a success message or perform any additional actions after the payment is made.
    alert("Payment successful!");
  } catch (error) {
    console.error("Payment error:", error);
    alert("Payment failed. Please try again.");
  }
}

pay.addEventListener("click", makePayment);

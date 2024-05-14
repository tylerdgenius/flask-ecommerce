function validateForm(formData) {
  const creditCardValue = formData.credit_card.replace(/[-\s]/g, "");
  if (!/^\d{16}$/.test(creditCardValue)) {
    alert("Please enter a valid 16-digit credit card number.");
    return false;
  }

  if (formData.name.trim() === "") {
    alert("Please enter your name.");
    return false;
  }
  if (formData.expiration.trim() === "") {
    alert("Please enter the expiration date.");
    return false;
  }
  if (formData.cvv.trim() === "" || !/^\d{3,4}$/.test(formData.cvv)) {
    alert("Please enter the CVV.");
    return false;
  }

  return true;
}

function submitForm() {
  const formData = {
    credit_card: document.getElementById("credit-card").value,
    name: document.getElementById("name").value,
    expiration: document.getElementById("expiration").value,
    cvv: document.getElementById("cvv").value,
  };

  if (!validateForm(formData)) {
    return;
  }

  fetch("/cart/process_payment", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(formData),
  })
    .then((response) => {
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      return response.json();
    })
    .then((data) => {
      console.log(data);
      alert("Checkout successful!");
    })
    .catch((error) => {
      console.error("Error:", error);
      alert("Checkout failed. Please try again.");
    });
}

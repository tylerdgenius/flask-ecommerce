function removeFromCart(productId) {
  $.ajax({
    url: `/cart/remove/${productId}`,
    method: "POST",
    success: function (response) {
      console.log("Item removed from cart:", response);
      alert(`Product with id ${productId} removed from cart`);
      window.location.reload();
    },
    error: function (err) {
      console.error("Error removing item from cart:", err);
      alert(`Error removing item from cart: ${err}`);
    },
  });
}

function clearItems() {
  $.ajax({
    url: `/cart/clear`,
    method: "POST",
    success: function (response) {
      alert(`Cleared products from cart`);
      window.location.reload();
    },
    error: function (err) {
      console.error("Error clearing cart:", err);
      alert(`Error clearing cart: ${err}`);
    },
  });
}

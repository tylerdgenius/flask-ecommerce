$(document).ready(function () {
  function getCartContents() {
    $.ajax({
      url: "/cart/contents",
      method: "GET",
      success: function (response) {
        console.log("Cart contents:", response);
        $("#cart-contents").empty();

        response.forEach(function (product) {
          var itemHtml = `
              <div class="col-md-3 col-sm-6 col-xs-12 single-card" data-product-id="${product.id}">
                <a href="products/single/${product.id}">
                  <img class='image' src="${product.picture_url}" alt="${product.name}" />
                </a>
                <p class="lead lead-text text-center">${product.name} - $${product.price}</p>
                <p class="text-center">Environmental Impact: ${product.environmental_impact}</p>
                <div class="btn-container">
                  <button type="button" class="btn-primary btn button" onclick="removeFromCart(${product.id})">Remove from Cart</button>
                </div>
              </div>
          `;

          $("#cart-contents").append(itemHtml);
        });
      },
      error: function (err) {
        console.error("Error retrieving cart contents:", err);
      },
    });
  }

  getCartContents();
});

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

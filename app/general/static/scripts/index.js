$(document).ready(function () {
  $(".single-card").hover(
    function () {
      var $card = $(this); // Capture the reference to the card element

      var productId = $card.data("product-id");
      $.ajax({
        url: "/products/get_product_details/" + productId,
        method: "GET",
        success: function (response) {
          var description = `${response.description.slice(0, 300)}...`;

          $card.append(
            `<div class="product-description hover-card">${description}</div>`
          );
        },
        error: function (err) {
          console.error("Error fetching product details:", err);
        },
      });
    },
    function () {
      // Remove the description when mouse leaves the card
      $(this).find(".product-description").remove();
    }
  );

  function loadItems(sortBy) {
    $.ajax({
      url: `/products/sort_items/${sortBy}`,
      method: "GET",
      success: function (response) {
        $("#items-container").empty();

        response.forEach(function (product) {
          var itemHtml = `
              <div class="col-md-3 col-sm-6 col-xs-12 single-card" data-product-id="${product.id}">
                <a href="products/single/${product.id}">
                  <img class='image' src="${product.picture_url}" alt="${product.name}" />
                </a>
                <p class="lead lead-text text-center">${product.name} - $${product.price}</p>
                <p class="text-center">Environmental Impact: ${product.environmental_impact}</p>
                <div class="btn-container">
                  <button type="button" class="btn-primary btn button" onclick="addToCart(${product.id})">Add to Cart</button>
                </div>
              </div>
          `;

          $("#items-container").append(itemHtml);
        });
      },
      error: function (err) {
        console.error("Error loading sorted items:", err);
      },
    });
  }

  $("#sort-by").change(function () {
    var sortBy = $(this).val();
    loadItems(sortBy);
  });

  loadItems("name");
});

function addToCart(productId) {
  $.ajax({
    url: `/cart/add/${productId}`,
    method: "POST",
    success: function (response) {
      console.log("Item added to cart:", response);
      alert(`Product with id ${productId} added to cart`);
    },
    error: function (err) {
      if (err.responseJSON.message) {
        return alert(`Error: ${err.responseJSON.message}`);
      }

      return alert(`Error adding item to cart: ${err}`);
    },
  });
}

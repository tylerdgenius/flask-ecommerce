$(document).ready(function () {
  function loadItems(sortBy) {
    console.log({ sortBy });
    let url = "/";

    if (sortBy) {
      url = `/?sort_by=${sortBy}`;
    }

    window.location.href = url;
  }

  $("#sort-by").change(function () {
    var sortBy = $(this).val();
    loadItems(sortBy);
  });

  $(".single-card").hover(
    function () {
      var $card = $(this);
      console.log({ $card });
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
      $(this).find(".product-description").remove();
    }
  );
});

function addToCart(productId) {
  $.ajax({
    url: `/cart/add/${productId}`,
    method: "POST",
    success: function (response) {
      console.log("Item added to cart:", response);
      alert(`Product with id ${productId} added to cart`);
      window.location.reload();
    },
    error: function (err) {
      if (err.responseJSON.message) {
        return alert(`Error: ${err.responseJSON.message}`);
      }

      return alert(`Error adding item to cart: ${err}`);
    },
  });
}

$(".single-card").hover(
  function () {
    var $card = $(this);
    console.log({ $card });
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
    $(this).find(".product-description").remove();
  }
);

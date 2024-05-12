function addToCart(itemId) {
  console.log({ itemId });
  //   fetch("/add_to_cart", {
  //     method: "POST",
  //     headers: { "Content-Type": "application/json" },
  //     body: JSON.stringify({ item_id: itemId }),
  //   }).then((response) => {
  //     if (response.ok) {
  //       alert("Item added to cart!");
  //     } else {
  //       alert("Failed to add item to cart.");
  //     }
  //   });
  console.log("Javascript");
}

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
});

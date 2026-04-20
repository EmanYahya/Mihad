$(document).ready(function() {
    document.querySelectorAll('.wishlist-btn').forEach(function(button) {
        button.addEventListener('click', function() {
            var productId = button.getAttribute('data-product-id');
            var action = button.getAttribute('data-action');
            if (action == 'add') {
                // Add product to wishlist
                $.ajax({
                    url: '/add-to-wishlist/' + productId + '/',
                    type: 'get',
                    dataType: 'json',
                    success: function(response) {
                        button.setAttribute('data-action', 'remove');
                        button.classList.add('added');
                        button.innerHTML = '<i class="fa fa-heart"></i><span>Added to Wishlist</span>';
                    },
                    error: function(response) {
                        console.log(response);
                    }
                });
            } else {
                // Remove product from wishlist
                $.ajax({
                    url: '/remove-from-wishlist/' + productId + '/',
                    type: 'get',
                    dataType: 'json',
                    success: function(response) {
                        button.setAttribute('data-action', 'add');
                        button.classList.remove('added');
                        button.innerHTML = '<i class="fa fa-heart-o"></i><span>Add to Wishlist</span>';
                    },
                    error: function(response) {
                        console.log(response);
                    }
                });
            }
        });
    });
});

$(document).ready(function() {
    document.querySelectorAll('.cart-btn').forEach(function(button) {
        button.addEventListener('click', function() {
            var productId = button.getAttribute('data-product-id');
            var action = button.getAttribute('data-action');
            if (action == 'add') {
                // Add product to wishlist
                $.ajax({
                    url: '/add-to-cart/' + productId + '/',
                    type: 'post',
                    dataType: 'json',
                    success: function(response) {
                        button.setAttribute('data-action', 'remove');
                        button.classList.add('added');
                        button.innerHTML = '<i class="fa fa-shopping-cart"></i><span>Added to Wishlist</span>';
                    },
                    error: function(response) {
                        console.log(response);
                    }
                });
            } else {
                // Remove product from wishlist
                $.ajax({
                    url: '/remove-from-cart/' + productId + '/',
                    type: 'post',
                    dataType: 'json',
                    success: function(response) {
                        button.setAttribute('data-action', 'add');
                        button.classList.remove('added');
                        button.innerHTML = '<i class="fa far-shopping-cart-o"></i><span>Add to Wishlist</span>';
                    },
                    error: function(response) {
                        console.log(response);
                    }
                });
            }
        });
    });

});

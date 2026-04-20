$(document).ready(function() {
    document.querySelectorAll('.wishlist-btn').forEach(function(button) {
        button.addEventListener('click', function() {
            var productId = button.getAttribute('data-product-id');
            var action = button.getAttribute('data-action');
            if (action == 'add') {
                // Add product to wishlist
                $.ajax({
                    url: '/app/add-to-wishlist/' + productId + '/',
                    type: 'get',
                    dataType: 'json',
                    success: function(response) {
                        button.setAttribute('data-action', 'remove');
                        button.classList.add('added');
                        button.innerHTML = '<i class="fa fa-heart"></i>';
                    },
                    error: function(response) {
                        console.log(response);
                    }
                });
            } else {
                // Remove product from wishlist
                $.ajax({
                    url: '/app/remove-from-wishlist/' + productId + '/',
                    type: 'get',
                    dataType: 'json',
                    success: function(response) {
                        button.setAttribute('data-action', 'add');
                        button.classList.remove('added');
                        button.innerHTML = '<i class="fa fa-heart-o"></i>';
                    },
                    error: function(response) {
                        console.log(response);
                    }
                });
            }
        });
    });

    document.querySelectorAll('.cart-btn').forEach(function(button) {
        button.addEventListener('click', function() {
            var productId = button.getAttribute('data-product-id');
            var action = button.getAttribute('data-action');
            if (action == 'add') {
                // Add product to wishlist
                $.ajax({
                    url: '/app/add-to-cart/' + productId + '/',
                    type: 'get',
                    dataType: 'json',
                    success: function(response) {
                        button.setAttribute('data-action', 'remove');
                        button.classList.add('added');
                        button.innerHTML = '<i class="fa fa-shopping-cart">';
                    },
                    error: function(response) {
                        console.log(response);
                    }
                });
            } else {
                // Remove product from wishlist
                $.ajax({
                    url: '/app/remove-from-cart/' + productId + '/',
                    type: 'get',
                    dataType: 'json',
                    success: function(response) {
                        button.setAttribute('data-action', 'add');
                        button.classList.remove('added');
                        button.innerHTML = '<i class="far fa-shopping-cart-o"></i>';
                    },
                    error: function(response) {
                        console.log(response);
                    }
                });
            }
        });
    });

});


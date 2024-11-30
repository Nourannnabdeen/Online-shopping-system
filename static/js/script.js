// Helper Functions
function validateEmail(email) {
    const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return regex.test(email);
}

function showAlert(message, type = 'info') {
    alert(message); // Can be replaced with a modal or custom alert
}

// Login Form Validation
document.addEventListener('DOMContentLoaded', () => {
    const loginForm = document.getElementById('loginForm');
    
    if (loginForm) {
        loginForm.addEventListener('submit', function (event) {
            event.preventDefault(); // Prevent form submission
            
            const email = document.getElementById('loginEmail').value.trim();
            const password = document.getElementById('loginPassword').value.trim();

            if (!email || !password) {
                showAlert('Please fill in both email and password.', 'error');
            } else if (!validateEmail(email)) {
                showAlert('Please enter a valid email address.', 'error');
            } else {
                showAlert('Login successful!', 'success');
                // Perform login action or redirect
            }
        });
    }
});

// Register Form Validation
document.addEventListener('DOMContentLoaded', () => {
    const registerForm = document.getElementById('registrationForm');
    
    if (registerForm) {
        registerForm.addEventListener('submit', function (event) {
            event.preventDefault(); // Prevent form submission
            
            const username = document.getElementById('username').value.trim();
            const email = document.getElementById('email').value.trim();
            const password = document.getElementById('password').value.trim();
            const confirmPassword = document.getElementById('confirmPassword').value.trim();

            if (!username || !email || !password || !confirmPassword) {
                showAlert('All fields are required.', 'error');
            } else if (!validateEmail(email)) {
                showAlert('Please enter a valid email address.', 'error');
            } else if (password !== confirmPassword) {
                showAlert('Passwords do not match.', 'error');
            } else {
                showAlert('Registration successful!', 'success');
                // Perform registration action or redirect
            }
        });
    }
});

// Shopping Cart Management
document.addEventListener('DOMContentLoaded', () => {
    const cartItems = document.querySelectorAll('.cart-item');
    const totalItemsEl = document.getElementById('total-items');
    const totalCostEl = document.getElementById('total-cost');

    function updateCartTotals() {
        let totalItems = 0;
        let totalCost = 0;

        cartItems.forEach((item) => {
            const quantity = parseInt(item.querySelector('input[type="number"]').value, 10) || 0;
            const price = parseFloat(item.querySelector('.item-price').textContent.replace('$', '')) || 0;
            totalItems += quantity;
            totalCost += quantity * price;
        });

        totalItemsEl.textContent = totalItems;
        totalCostEl.textContent = totalCost.toFixed(2);
    }

    if (cartItems.length > 0) {
        cartItems.forEach((item) => {
            const quantityInput = item.querySelector('input[type="number"]');
            const removeButton = item.querySelector('.remove-item');

            if (quantityInput) {
                quantityInput.addEventListener('change', updateCartTotals);
            }

            if (removeButton) {
                removeButton.addEventListener('click', () => {
                    item.remove();
                    updateCartTotals();
                });
            }
        });
    }

    updateCartTotals();
});

// Redirect to Cart Page on Add to Cart Button Click
document.addEventListener('DOMContentLoaded', () => {
    const addToCartButtons = document.querySelectorAll('.add-to-cart-btn');

    addToCartButtons.forEach(button => {
        button.addEventListener('click', () => {
            // Redirect to shopping cart page
            window.location.href = 'shopping-cart.html';
        });
    });
});

// Checkout Form Validation
document.addEventListener('DOMContentLoaded', () => {
    const checkoutForm = document.getElementById('checkout-form');

    if (checkoutForm) {
        checkoutForm.addEventListener('submit', function (event) {
            event.preventDefault(); // Prevent form submission

            const fullName = document.getElementById('full-name').value.trim();
            const address = document.getElementById('address').value.trim();
            const paymentMethod = document.querySelector('input[name="payment-method"]:checked');

            if (!fullName || !address || !paymentMethod) {
                showAlert('Please fill in all required fields and select a payment method.', 'error');
            } else {
                showAlert('Order placed successfully!', 'success');
                // Perform order placement action or redirect
            }
        });
    }
});
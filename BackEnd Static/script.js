document.addEventListener('DOMContentLoaded', () => {
    document.body.addEventListener('click', (event) => {
        if (event.target.classList.contains('add-to-cart-btn')) {
            const productId = event.target.getAttribute('data-id');
            // Send product ID to the back-end API
            fetch('http://127.0.0.1:8080/api/cart/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ product_id: productId }),
            })
                .then(response => response.json())
                .then(data => {
                    alert('Product added to cart!');
                })
                .catch(error => console.error('Error adding to cart:', error));
        }
    });
});
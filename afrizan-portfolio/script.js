function scrollToSection("home") {
    const section = document.getElementById(sectionId);
    section.scrollIntoView({ behavior: 'smooth' });
}

fetch('http://127.0.0.1:5000/submit', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify({ username: 'example', password: '12345' }),
})
    .then(response => { 
        if (!response.ok) {
            throw new Error('Credentials not found');
        }
        return response.json();
    })
    .then(data => {
        console.log('Success:', data); // Handle the response data
        let customer_id = data.id;
        let payment_url = 'http://127.0.0.1:5000/payment';
        let payment_data = {
            customer_id: customer_id,
            amount: 100 // Example amount, replace with actual amount
        };
        fetch(payment_url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(payment_data)
        })
            .then(paymentResponse => {
                if (!paymentResponse.ok) {
                    throw new Error('Payment failed');
                }
                return paymentResponse.json();
            })
            .then(paymentData => {
                console.log('Payment Success:', paymentData); // Handle payment success
                scrollToSection("services"); // Replace 'home' with the actual ID of the section you want to scroll to
            })
            .catch(paymentError => {
                console.error('Payment Error:', paymentError);
            });
    })
    .catch(error => {
        console.error('Error:', error);
    });

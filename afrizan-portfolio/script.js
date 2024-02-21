fetch('http://localhost:5000/api/data')
    .then(response => {
        if (!response.ok) {
            throw new Error('Failed to fetch data');
        }
        return response.json();
    })
    .then(data => {
        console.log('Data:', data);
        let customer_id = data.id;
        let payment_url = 'http://localhost:5000/payment';
        let payment_data = {
            customer_id: customer_id,
            amount: 100  // Replace with actual amount
        };
        fetch(payment_url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
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
            console.log('Payment Success:', paymentData);
            scrollToSection("services"); // Replace with actual section ID
        })
        .catch(paymentError => {
            console.error('Payment Error:', paymentError);
        });
    })
    .catch(error => {
        console.error('Error:', error);
    });

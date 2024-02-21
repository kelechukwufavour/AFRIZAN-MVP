// Sign Up Form Submission
document.getElementById('signupForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent default form submission

    // Get form data
    const formData = {
        firstName: document.getElementById('firstName').value,
        lastName: document.getElementById('lastName').value,
        phone: document.getElementById('phone').value,
        email: document.getElementById('email').value,
        password: document.getElementById('password').value,
        confirmPassword: document.getElementById('confirmPassword').value
    };

    // Send form data to backend API
    fetch('http://localhost:5000/api/signup', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData)
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Sign up failed');
        }
        return response.json();
    })
    .then(data => {
        console.log('Sign up successful:', data);
        // Redirect user to the login page upon successful sign-up
        window.location.href = 'http://localhost:8000/login.html';
    })
    .catch(error => {
        console.error('Sign up error:', error);
        // Display error message if details have already been captured
        document.getElementById('errorMessage').style.display = 'block';
    });
});

// Fetch Data
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

// Login Form Submission
document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the default form submission

    // Get the form data
    const formData = new FormData(event.target);

    // Convert form data to JSON object
    const jsonData = {};
    formData.forEach((value, key) => {
        jsonData[key] = value;
    });

    // Send a POST request to the backend for authentication
    fetch('http://localhost:5000/api/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(jsonData)
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Invalid credentials');
        }
        return response.json();
    })
    .then(data => {
        console.log('Login successful:', data);
        // Redirect to the home page upon successful login
        window.location.href = 'http://localhost:8000/home.html'; // Update the URL as needed
    })
    .catch(error => {
        console.error('Login error:', error);
        // Display error message to the user
        alert('Login failed. Please check your credentials and try again.');
    });
});


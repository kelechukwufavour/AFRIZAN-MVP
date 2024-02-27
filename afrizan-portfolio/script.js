$(document).ready(function() {
    var lastScrollTop = 0;
    var isScrollingUp = false;

    $(".menu-icon").on("click", function() {
        $("nav ul").toggleClass("showing");
    });

    // Scrolling Effect
    $(window).on("scroll", function() {
        var st = $(this).scrollTop();

        if (st > lastScrollTop) {
            // scrolling down
            isScrollingUp = false;
        } else {
            // scrolling up
            isScrollingUp = true;
        }

        lastScrollTop = st;

        if (isScrollingUp) {
            $('nav').removeClass('black');
        } else {
            $('nav').addClass('black');
        }
    });
});

// Script for API Integration //

document.addEventListener('DOMContentLoaded', function() {
    // Selecting form, and preventing its default behavior when submitted
    let form = document.querySelector('form');
    form.addEventListener('submit', function(event) {
      event.preventDefault();
    let message = document.querySelector('#for-message');


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
    fetch('http://127.0.0.1:5000/api/signup', { // Update URL to match backend endpoint
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
fetch('http://127.0.0.1:5000/api/data') // Update URL to match backend endpoint
    .then(response => {
        if (!response.ok) {
            throw new Error('Failed to fetch data');
        }
        return response.json();
    })
    .then(data => {
        console.log('Data:', data);
        let user_id = data.id;
        let payment_url = 'http://127.0.0.1:5000/payment'; // Update URL to match backend endpoint
        let payment_data = {
            user_id: customer_id,
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
    fetch('http://127.0.0.1:5000/api/login', { // Update URL to match backend endpoint
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

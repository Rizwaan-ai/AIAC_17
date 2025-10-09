// ...existing code...

// Wait for the DOM to load before accessing elements
document.addEventListener('DOMContentLoaded', function() {
    // Get the button by its ID
    const alertButton = document.getElementById('alertButton');
    if (alertButton) {
        // Add a click event listener to the button
        alertButton.addEventListener('click', function() {
            // Show an alert message when the button is clicked
            alert('Button clicked!');
        });
    }
});

// ...existing code...
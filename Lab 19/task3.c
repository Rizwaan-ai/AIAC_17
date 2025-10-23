#include <iostream>
// C++ function to calculate factorial recursively
// It is recommended to use 'long long' for the return type in a real-world scenario
// to prevent overflow for numbers larger than 12! (which exceeds a standard 32-bit 'int')
int factorial(int n) {
    // Input validation for negative numbers (returns 0 or could throw an exception)
    if (n < 0) {
        std::cerr << "Error: Factorial not defined for negative numbers." << std::endl;
        return 0; 
    }
    // Base case: Factorial of 0 is 1
    if (n == 0) {
        return 1;
    } 
    // Recursive step: n * factorial(n - 1)
    else {
        return n * factorial(n - 1);
    }
}
int main() {
    // --- C++ Output ---
    std::cout << "--- C++ Output ---" << std::endl;

    // Test 1: Given Input 5
    std::cout << "Input: 5 -> Factorial = " << factorial(5) << std::endl;

    // Test 2: Given Input 0
    std::cout << "Input: 0 -> Factorial = " << factorial(0) << std::endl;

    // Dynamic Input Example
    int dynamic_num;
    std::cout << "\nEnter an integer for factorial: ";
    
    // Check if the input operation was successful
    if (std::cin >> dynamic_num) {
        int result = factorial(dynamic_num);
        // Only print result if the function didn't return an error (0) due to negative input
        if (dynamic_num >= 0) {
            std::cout << "Input: " << dynamic_num << " -> Factorial = " << result << std::endl;
        }
    } else {
        std::cout << "Invalid input. Please enter a valid integer." << std::endl;
    }

    return 0;
}
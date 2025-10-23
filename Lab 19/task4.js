// JavaScript function to iterate over an array (list) and print elements
function printStudents(students) {
    console.log("--- JavaScript Output ---");
    console.log("Student List:");
    
    // Using a for...of loop for clean iteration over array elements
    for (const name of students) {
        console.log(name);
    }
}

// Test with sample student names
const studentArray = ["Alice", "Bob", "Charlie", "Diana"];
printStudents(studentArray);
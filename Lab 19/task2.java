class ConditionalStatements {
    public static String checkNumber(int num) {
        if (num > 0) {
            return "The number is positive";
        } else if (num < 0) {
            return "The number is negative";
        } else {
            return "The number is zero";
        }
    }

    public static void main(String[] args) {
        // Test calls and output
        System.out.println("Java Output:");
        System.out.println("Input: -5 -> Output: " + checkNumber(-5));
        System.out.println("Input: 0 -> Output: " + checkNumber(0));
        System.out.println("Input: 7 -> Output: " + checkNumber(7));
    }
}
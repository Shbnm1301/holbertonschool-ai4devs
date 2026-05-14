public class Bug2 {

    public static void main(String[] args) {
        String price = "100";
        int tax = 20;

        // BUG: String + int concatenation instead of numeric operation
        int total = price + tax;

        System.out.println("Total price: " + total);
    }
}

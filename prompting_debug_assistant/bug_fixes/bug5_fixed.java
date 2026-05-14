public class Bug2 {

    public static void main(String[] args) {
        String price = "100";
        int tax = 20;

        int total = Integer.parseInt(price) + tax;

        System.out.println("Total price: " + total);
    }
}

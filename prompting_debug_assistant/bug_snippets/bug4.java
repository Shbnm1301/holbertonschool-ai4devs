public class Bug1 {

    public static void main(String[] args) {
        int[] numbers = {1, 2, 3, 4, 5};

        int sum = 0;

        // BUG: loop condition causes ArrayIndexOutOfBounds
        for (int i = 0; i <= numbers.length; i++) {
            sum += numbers[i];
        }

        System.out.println("Sum: " + sum);
    }
}

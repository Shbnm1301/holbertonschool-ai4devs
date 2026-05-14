## Bug 1 – bug1.py
**Intended Behavior**: Print all numbers in a list.  
**Issue Type**: Off-by-one error.  
**Notes**: The loop reads one extra element from the list.

## Bug 2 – bug2.py
**Intended Behavior**: Divide two numbers and print the result.  
**Issue Type**: Runtime error (ZeroDivisionError).  
**Notes**: The program crashes when division by zero occurs.

## Bug 3 – bug3.js
**Intended Behavior**: Calculate the sum of values in an array.  
**Issue Type**: Logical error (off-by-one).  
**Notes**: The loop iterates one element too many, causing incorrect output.


## Bug 4 – bug4.java
**Intended Behavior**: Calculate and print the sum of all numbers in the array. 
**Issue Off-by-one error (ArrayIndexOutOfBoundsException)
**Notes**: The loop condition i <= numbers.length allows the index i to reach numbers.length, but valid array indexes in Java only go from 0 to numbers.length - 1. This causes an attempt to access an element outside the array, leading to a runtime crash.


## Bug 5 – bug5.java
**Intended Behavior**:  Calculate the total price by adding tax to a numeric price and print the result.
**Issue Type**: Type error / logical error (invalid arithmetic operation with String)
**Notes**: The variable price is a String, but the code tries to add it to an int (tax). In Java, this results in string concatenation behavior or a compile-time error depending on context. Instead of performing numeric addition, it incorrectly mixes types, so the value is not treated as a number.


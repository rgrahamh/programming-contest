# P00_Simple Calculator
###### By: Ryan Houck
## Problem Description
The objective of this problem is to create a Reverse Polish Notation calculator that parses input (a combination of symbols and positive integer values), does calculation, and produces the answer as a float with 4 trailing decimal places (or `Invalid Input` if the input has mismatching signage and numbers).

### What's Reverse Polish Notation?
Reverse Polish Notation (RPN) is a postfix notation standard (operator after the operands) for performing mathematical operations. Whenever you parse a number, it goes on the stack (basically a list where you push top or pop from the top), and then when you come across an operator, you do that operation on the top two numbers of the stack and then store the result back on the stack. If your operands and operations are properly balanced, you should have exactly one more operand than operator.

So, if you want to do:
```
6 + 7 + (5 - 3)
```
You would enter:
```
6 7 + 5 3 - +
```
This would add 6 and 7, subtract 5 and 3, and then add those two results. The answer would then be:
```
15.0000
```

## Input Specifications
All input will be a combination of positive integer values and any of the following operands: `+`, `-`, `*`, and `/`. The input should be read until it hits a newline or an EOF. This input will be delimited by single spaces, and the number of operations should be one less than the number of operands if it's valid input. If there are any characters aside from `0`-`9` and the aforementioned operators, it should be considered invalid input. There is no defined maximum for the possible number of operations, so your code should be prepared to handle an arbitrarily-sized stack.

## Output Specifications
If the input is valid (is not defying the rules of math, has properly matched operators/operands, and is formatted correctly), the output should be a single number: the answer as floating point number (with the precision of four decimal places). If there's just one integer as the input, it should output as that integer in its floating-point representation. In all cases where the input is invalid, print `Invalid Input` and exit the program.

## Examples
Examples are included in the `examples_cases` directory. For ease of viewing, though, they are also listed below:
#### Example 1:
***Input:***
```
3 5 *
```
***Output:***
```
15.0000
```
#### Example 2:
***Input:***
```
3 8 + 7 /
```
***Output:***
```
1.5714
```
#### Example 3:
***Input:***
```
165 98 78 + 68 - -
```
***Output:***
```
57.0000
```

## Test generation
I also wrote a little script to help generate some extra tests called `test_gen.py`; all you have to do it input the number of numbers you want it to generate (between 1 and the max integer value), and then it will generate a valid test for you. It's currently included in the `misc` directory.

"""
Task: Arithmetic Operators

Description:
    Read two integers from standard input and print:
    1. The sum of the two numbers
    2. The difference of the two numbers (first - second)
    3. The product of the two numbers

Input Format:
    The first line contains the first integer.
    The second line contains the second integer.

Output Format:
    Print three lines:
        - Sum of the two integers
        - Difference of the two integers
        - Product of the two integers

Sample Input:
    3
    2

Sample Output:
    5
    1
    6
"""

# Solution


def main() -> None:
    a = int(input().strip())
    b = int(input().strip())
    print(a+b)
    print(a-b)
    print(a*b)
    
if __name__ == '__main__':
    main()

    

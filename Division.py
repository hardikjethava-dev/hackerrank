"""
Task: Division

Description:
    Read two integers from standard input and print:
    1. The result of integer division (a // b)
    2. The result of float division (a / b)

    No rounding or formatting is required.

Input Format:
    The first line contains the first integer.
    The second line contains the second integer.

Output Format:
    Print two lines:
        - Integer division result
        - Float division result

Sample Input:
    4
    3

Sample Output:
    1
    1.33333333333
"""


# Solution

def main() -> None:
    a = int(input())
    b = int(input())
    
    print(a//b)
    print(a/b)

if __name__ == '__main__':
    main()
"""
Task: Loops

Description:
    Read an integer n from standard input. For each non-negative integer i
    where 0 <= i < n, print the square of i on a new line.

Input Format:
    The first and only line contains the integer n.

Output Format:
    Print n lines, each containing the square of the corresponding integer.

Sample Input:
    5

Sample Output:
    0
    1
    4
    9
    16
"""

# Solution
def main() -> None:
    a = int(input().strip())

    for i in range(a):
        print(i*i)

if __name__ == '__main__':
    main()
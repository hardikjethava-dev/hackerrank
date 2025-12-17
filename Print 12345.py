"""
Reads an integer n from standard input and prints the sequence of integers
from 1 through n as a single concatenated string without spaces.

The solution must not use any string manipulation methods. The integers
should be combined using numeric operations and printed directly.

Input Format:
- A single integer n (n >= 1) read from STDIN.

Output Format:
- A single line containing the numbers from 1 to n concatenated together
  with no spaces.

Example:
Input:
3

Output:
123
"""

# Solution 1

def main() -> None:
    n = int(input())
    for i in range(1, n+1):
        print(i, end="")

if __name__ == '__main__':
    main()


# Solution 2
def main() -> None:
    n = int(input())
    l = [i for i in range(1,n+1)]
    print(*l,sep="")

if __name__ == '__main__':
    main()



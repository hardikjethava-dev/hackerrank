"""
Task: Write a function to determine whether a given year is a leap year.

Description:
    An extra day (February 29) is added to the calendar nearly every four years
    to correct for the Earth's orbital period. In the Gregorian calendar, a year
    is a leap year if it satisfies the following conditions:

    - The year is evenly divisible by 4, AND
    - If the year is evenly divisible by 100, it must also be divisible by 400

    As a result:
        - Years divisible by 400 are leap years
        - Years divisible by 100 but not by 400 are NOT leap years
        - Years divisible by 4 but not by 100 are leap years

Input Format:
    An integer representing the year to test.

Output Format:
    Return True if the year is a leap year, otherwise return False.

Sample Input:
    1990

Sample Output:
    False
"""

# Solution
def is_leap(year):

    leap = False
    if (year % 400 == 0) or (year % 4 ==0 and year % 100 != 0):
        leap = True    
    return leap

year = int(input())
print(is_leap(year))
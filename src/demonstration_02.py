"""
Challenge #2:

Write a function that takes an integer `minutes` and converts it to seconds.

Examples:
- convert(5) ➞ 300
- convert(3) ➞ 180
- convert(2) ➞ 120
"""
def convert(minutes):
    secondsInAMinute = 60
    return minutes * secondsInAMinute

print(convert(5))
print(convert(3))
print(convert(2))
import sys 

def test(number: int):
    if number < 2:
        raise ValueError("number cannot be lower than 2")

try:
    test(1)
except ValueError as e:
    print("error:", e)
    exit(1)

print("tests a été effectué")
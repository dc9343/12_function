def fizz_buzz_convert(x: int) -> str:
    if x % 15 == 0:
        return "FizzBuzz"
    elif x % 3 == 0:
        return "Fizz"
    elif x % 5 == 0:
        return "Buzz"
    else:
        return str(x)


y1 = fizz_buzz_convert(x=1)
print(y1)

y2 = fizz_buzz_convert(x=3)
print(y2)

y3 = fizz_buzz_convert(x=15)
print(y3)

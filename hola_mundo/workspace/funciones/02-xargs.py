def suma(*numbers):

    result = 0

    for number in numbers:
        result += number

    print(result)


suma(3, 2)
suma(1, 5, 9, 7)

def distance_from_zero(number):
    if type(number) == int or type(number) == float:
        return abs(number)
    else:
        return "nope"

print(distance_from_zero(-5))

print(distance_from_zero(6))

print(distance_from_zero("what?"))

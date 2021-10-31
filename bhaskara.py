import math

valueOfA = int(input('Please, enter the value of A: '))
valueOfB = int(input('Please, enter the value of B: '))
ValueOfC = int(input('Please, enter the value of C: '))

# First let's calculate the delta value
delta = valueOfB ** 2 - 4 * valueOfA * ValueOfC
print("delta: ", delta)


if delta > 0:
    squareRootOfDelta = math.sqrt(delta)
    print(squareRootOfDelta)
    valueOfX = (-valueOfB + squareRootOfDelta) / (2 * valueOfA)
    valueOfY = (-valueOfB - squareRootOfDelta) / (2 * valueOfA)
    print("x = ", valueOfX, "x' = ", valueOfY)

elif delta == 0:
    squareRootOfDelta = math.sqrt(delta)
    x = (-valueOfB) / (2 * valueOfA)
    print(x)

else:
    print('There is no square root')

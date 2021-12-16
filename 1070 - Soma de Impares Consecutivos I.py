num1 = int(input())
num2 = int(input())
somador = 0

if num1 < num2:
    for i in range(num1, num2):
        if i % 2 != 0:
            somador += i
    print(somador)
elif num2 < num1:
    for i in range(num2, num1):
        if i % 2 != 0:
            somador += i
    print(somador)
elif num1 == num2:
    print(0)

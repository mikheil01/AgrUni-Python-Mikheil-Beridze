n = int(input("Enter number: "))

if 1 <= n <= 100:
    fib = []
    for i in range(n):
        if i == 0:
            fib.append(0)
        elif i == 1:
            fib.append(1)
        else:
            fib.append(fib[-1] + fib[-2])
    print(fib)
else:
    print("შეიყვანეთ ნატურალური რიცხვი 1-დან 100-მდე.")
n = int(input("Enter number: "))

if 1 <= n <= 1000:
    for i in range(1, n + 1):
        if n % i == 0:
            print(i, end=" ")
else:
    print("შეიყვანეთ ნატურალური რიცხვი 1-დან 1000-მდე.")
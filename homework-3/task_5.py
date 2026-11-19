s1 = input("შეიყვანეთ პირველი სტრიქონი: ").lower()
s2 = input("შეიყვანეთ მეორე სტრიქონი: ").lower()

chars1 = sorted(i for i in s1 if not i.isspace())
chars2 = sorted(i for i in s2 if not i.isspace())

if chars1 == chars2:
    print("YES")
else:
    print("NO")
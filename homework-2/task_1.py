import math

a = float(input("შეიყვანეთ პირველი გვერდი: "))
b = float(input("შეიყვანეთ მეორე გვერდი: "))
c = float(input("შეიყვანეთ მესამე გვერდი: "))

if a > 0 and b > 0 and c > 0 and (a + b > c) and (a + c > b) and (b + c > a):
    perimeter = a + b + c
    s = perimeter / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print(f"პერიმეტრი: {perimeter}")
    print(f"ფართობი: {area}")
else:
    print("მოცემული გვერდებით სამკუთხედი არ არსებობს.")
number = input("შეიყვანეთ რიცხვი:")

if number.strip() == "":
  number = 0
else:
  number = float(number)

square = number**2

print(f"თქვენ მიერ შეყვანილი რიცხვის ({number}) კვადრატი არის: {square}")
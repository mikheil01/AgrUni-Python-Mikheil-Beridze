text = input("შეიყვანეთ სტრიქონი ან წინადადება: ").lower()

cleaned = "".join(i for i in text if "a" <= i <= "z")

if cleaned == cleaned[::-1]:
    print("სიტყვა/წინადადება არის პალინდრომა")
else:
    print("სიტყვა/წინადადება არ არის პალინდრომა")
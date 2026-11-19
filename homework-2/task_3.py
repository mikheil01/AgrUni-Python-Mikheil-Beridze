while True:
    user_input = input("შეიყვანეთ წელიწადი: ").strip()
    if user_input.isdigit() and int(user_input) > 0:
        year = int(user_input)
        break
    print("არასწორი მონაცემი. გთხოვთ, შეიყვანოთ ნატურალური რიცხვი.")

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(f"{year} ნაკიანი წელია.")
else:
    print(f"{year} არ არის ნაკიანი წელი.")
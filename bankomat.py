
import csv
FILE_NAME = "account.txt"

def Find_user(pin):
    with open(FILE_NAME, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["pin"] == pin:
                return row
    return None


def Update_balance(pin, New_balance):
    rows= []
    with open(FILE_NAME, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["pin"]==pin:
                row["balance"] =str(New_balance)
            rows.append(row)
    with open(FILE_NAME, "w" , encoding="utf-8") as file:
        fieldnames = ["pin", "name", "balance"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)          

def ATM():
    attempts=0
    max_attempts=3
    while attempts<max_attempts:
     pin = input("შეიყვანეთ PIN კოდი")   
     user =Find_user(pin)  
     if user:
        print(f"\n გამარჯობა, {user['name']}!") 
        break      
     else:
         attempts +=1
         remaining=max_attempts-attempts
         if remaining>0 :
             print(f"PIN არასწორია. დარჩენილი მცდელობები: {remaining}")
         else:
             print("სამჯერ არასწორი PIN შეყვანის გამო მომხმარებელი დაბლოკილია") 
             return 
    name=user["name"]
    balance = float(user["balance"])    
    while True:
        print("\n აირჩიეთ ოპერაცია")  
        print("1. ბალანსის შემოწმება")  
        print("2. თანხის შეტანა")
        print("3. თანხის გატანა")
        print("4. გამოსვლა")

        choice = input ("აირჩიეთ მოქმედება: ")
        if choice == "1":
             print(f"მიმდინარე ბალანსი: {balance:.2f} ₾")
        elif choice == "2":
            try:
                amount = float(input("შეიყვანეთ შესატანი თანხა"))
                if amount <= 0 :
                    print("შეიყვანეთ დადებითი თანხა!") 
                else:
                    balance += amount
                    Update_balance(pin, balance)
                    print(f"თანხა წარმატებით დაემატა! ახალი ბალანსი: {balance:.2f} ₾")
            except ValueError:
                    print("შეიყვანეთ სწორი რიცხვი!")
        elif choice == "3":
            try:
                amount = float(input("შეიყვანეთ გამოსატანი თანხა: ")) 
                if amount<=0 :
                   print("შეიყვანეთ დადებითი თანხა!") 
                   continue
                fee = amount * 0.001
                total = amount + fee
                if total > balance:
                   print("არასაკმარისი ბალანსი!") 
                   continue
                else:
                    balance -= total
                    Update_balance(pin, balance)
                    print(f"თანხა წარმატებით განაღდა! საკომისიო: {fee:.2f} ₾")
                    print(f"ახალი ბალანსი: {balance:.2f} ₾")
            except ValueError:
                    print("შეიყვანეთ სწორი რიცხვი!")    


        elif choice == "4":
            print("\nგმადლობთ, რომ გამოიყენეთ ბანკომატი!")
            break

        else:
            print("არასწორი არჩევანი!")
        cont = input("გსურთ გააგრძელოთ ოპერაციები? (კი/არა): ").strip().lower()
        if cont != "კი":
            print("\nგმადლობთ, რომ გამოიყენეთ ბანკომატი!")
            break
ATM()


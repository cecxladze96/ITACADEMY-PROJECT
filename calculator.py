
  
def calculator():
 try:
    num1 = float(input("შეიყვანეთ პირველი რიცხვი : "))
    num2 = float(input("შეიყვანეთ მეორე რიცხვი : "))
 except ValueError:
    print("შეცდომა: შესაძლებელია მხოლოდ რიცხვების შეყვანა") 
    return

 print ("აირჩიეთ არითმეტიკული მოქმედება")     
 print ("+ (დამატება)")   
 print ("- (გამოკლება)")   
 print ("* (გამრავლება)")   
 print ("/ (გაყოფა)")   

 operation = input("შეიყვანეთ სასურველი მოქმედება:")

 if operation == "+":
   result = num1 +num2
   
 elif operation == "-":
   result = num1 - num2
   
 elif operation == "*":
   result = num1 * num2
   
 elif operation == "/":
   if num2 == 0:
    print("შეცდომა: ნულზე გაყოფა შეუძლებელია.")
    return
   result = num1/num2        
 else:
   print("არასწორი ოპერაციის არჩევანი.")
   return    

 result = round(result, 2)  
 print(f"შედეგი: {result}")
calculator()        


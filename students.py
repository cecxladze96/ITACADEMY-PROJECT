import re
class Student:
    next_roll_number = 1
    def __init__(self, name: str, score):
     if not isinstance(name, str):
      raise TypeError("სახელი უნდა იყოს სტრინგი")
     if not re.fullmatch(r"[ა-ჰ ]+", name):
      raise ValueError("სახელი უნდა შედგებოდეს მხოლოდ ქართული ასოებით")
     self._name=name
     self._roll_number = Student.next_roll_number
     Student.next_roll_number +=1
     self.score=score
    
    @property
    def name(self):
        return self._name
    @property
    def roll_number(self):
        return self._roll_number
    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self,value:float):
        if not isinstance(value, (int, float)):
            raise TypeError("ქულა უნდა იყოს რიცხვი")
        if not (0 <= value <= 100):
            raise ValueError("ქულა უნდა იყოს 0-დან 100-მდე")
        self._score = value
        if value >= 90:
            self._grade = "A"
        elif value >= 80:
            self._grade = "B"
        elif value >= 70:
            self._grade = "C"
        elif value >= 60:
            self._grade = "D"
        else:
            self._grade = "F"

    @property
    def grade(self) -> str:
        return self._grade
    


   
class StudentManager:
    def __init__(self):
        self._students = []
    def print_table_header(self):
        print(f"{'სია №':10} {'სახელი':<10} {'შეფასება':<10}")
        print("-" * 40)    
        
    def add_student(self):
        name = input("შეიყვანეთ სტუდენტის სახელი: ")
        try:
            score =float(input("შეიყვანეთ სტუდენტის შეფასება: "))
            student = Student(name, score)
            self._students.append(student)
            print("სტუდენტი დაემატა წარმატებით!\n")
            self.display_all_students()
        except ValueError as e:
            print("შეცდომა: ქულა უნდა იყოს 0-დან 100-მდე.\n")
        except TypeError as e:
           print("შეცდომა: ქულა უნდა იყოს რიცხვი.\n")   

    def display_all_students(self):
      if not self._students:
        print("სია ცარიელია \n")
        return
      self.print_table_header()
      for student in self._students:
        print(f"{student.roll_number:<10} {student.name:<20} {student.grade:<10}")
        print("-" * 40)

    def find_student(self):
     try: 
       roll_number = int(input("სტუდენტის მოსაძებნათ შეიყვანეთ სიის ნომერი ")) 
       if roll_number <= 0:
        raise ValueError("სიის ნომერი უნდა იყოს დადებითი მთელი რიცხვი.")
     except ValueError as e:
        print("შეცდომა: გთხოვთ შეიყვანოთ მთელი რიცხვი")
        return
     found = False
     for student in self._students:
        if student.roll_number == roll_number:
            self.print_table_header()
            print(f"{student.roll_number:<10} {student.name:<20} {student.grade:<10}")
            found = True
            break
     if not found:
        print(f"სტუდენტი სიის ნომრით {roll_number} ვერ მოიძებნა.\n")  


    def update_student(self):
       try:
        roll_number = int(input("შეიყვანეთ სტუდენტის სიის ნომერი შეფასების განახლებისთვის: ").strip())
       except ValueError:
        print("შეცდომა: სიის ნომერი უნდა იყოს მთელი რიცხვი.\n")
        return
       found = False
       for student in self._students:
          if student.roll_number==roll_number:
           found = True
           try:
             new_score = float(input("შეიყვანეთ ახალი ქულა (0-100): "))
             student.score = new_score
             print("სტუდენტზე ინფორმაცია განახლდა წარმატებით!\n")
             self.print_table_header()
             print(f"{student.roll_number:<10} {student.name:<20} {student.grade:<10}")

           except ValueError as e:
                print(f"შეცდომა: ქულა უნდა იყოს 0-დან 100-მდე.\n")
           except TypeError as e:
                print(f"შეცდომა: ქულა უნდა იყოს რიცხვი.\n")       
           return
       if not found:
          print("სტუდენტი ვერ მოიძებნა.\n")




def main():
    manager=StudentManager()
    while True:
        print("სტუდენტთა მართვის სისტემა")
        print(" სტუდენტის დამატება, ღილაკი: 1")
        print(" სტუდენტის სიის გამოძახება, ღილაკი: 2")
        print(" სტუდენთის ძიება სიის ნომრით, ღილაკი 3")
        print(" სტუდენტზე ინფორმაციის განახლება, ღილაკი: 4")
        print("გასვლა, ღილაკი: 5")
        choice = input("ჩაწერეთ სასურველი მოქმედება: \n")

        if choice == '1':
            manager.add_student()
        elif choice == '2':
            manager.display_all_students()
        elif choice == '3':
            manager.find_student()
        elif choice == '4':
            manager.update_student()
        elif choice == '5':
            print("გამოსვლა...")
            break
        else:
            print("არასწორი არჩევანი. სცადეთ კიდევ ერთხელ.\n")


main()


class Student:
    next_roll_number = 1
    def __init__(self, name, grade):
     self._name: str=name
     self._roll_number = Student.next_roll_number
     Student.next_roll_number +=1
     if len(grade) != 1:
         raise ValueError("შეფასება უნდა იყოს ერთ ასოიანი")
     self._grade: str=grade 

    def get_name(self):
        return self._name

    def get_roll_number(self):
        return self._roll_number

    def get_grade(self):
        return self._grade

    def set_grade(self, grade):
        if len(grade) != 1:
            raise ValueError("შეფასება უნდა იყოს ერთ ასოიანი")
        self._grade = grade

    def display_info(self):
        print(f"Name: {self.get_name()}")
        print(f"Roll Number: {self.get_roll_number()}")
        print(f"Grade: {self.get_grade()}")

   
class StudentManager:
    def __init__(self):
        self._students = []
        
    def add_student(self):
        name = input("შეიყვანეთ სტუდენტის სახელი: ")
        grade = input("შეიყვანეთ სტუდენტის შეფასება: ")
        try:
            student = Student(name, grade)
            self._students.append(student)
            print("სტუდენტი დაემატა წარმატებით!\n")
        except ValueError as e:
            print(f"შეცდომა: {e}\n")

    def display_all_students(self):
      if not self._students:
        print("სტუდენტი ვერ მოიძებნა. \n")
      for student in self._students:
        student.display_info()
        print("_"*20)    

    def find_student(self):
     roll_number = int(input("სტუდენტის მოსაძებნათ შეიყვანეთ სიის ნომერი ")) 
     for student in self._students:
        if student.get_roll_number()==roll_number:
            student.display_info()
            return
     print (f"სტუდენტი სიის ნომრით{roll_number} ვერ მოიძებნა. \n")  


    def update_student(self):
     roll_number = int(input("შეიყვანეთ სტუდენტის სიის ნომერი რომელზეც გსურთ შეფასების განახლება "))
     for student in self._students:
        if student.get_roll_number()==roll_number:
            grade=input("შეიყვანეთ ახალი ქულა(ერთნიშნიანი ): ")
            try:
                if len(grade) != 1:
                    raise ValueError("Grade must be a single character")
                student.set_grade(grade)
                print("სტუდენტზე ინფორმაცია განახლდა წარმატებით!\n")
            except ValueError as e:
                print(f"Error: {e}\n")
            return
    print("სტუდენტი ვერ მოიძებნა.\n")




def main():
    manager=StudentManager()
    while True:
        print("სტუდენტთა მართვის სისტემა")
        print(" სტუდენტის დასამატება, ღილაკი: 1")
        print(" სტუდენტის სიის გამოძახება, ღილაკი: 2")
        print(" სტუდენთის ძიება სიის ნომრით, ღილაკი 3")
        print(" სტუდენტზე ინფორმაციის განახლება, ღილაკი: 4")
        print("გასვლა, ღილაკი: 5")
        choice = input("ჩაწერეთ სასურველი მოქმედება: ")

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

   

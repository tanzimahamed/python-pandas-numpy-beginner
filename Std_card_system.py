class Student:
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks  # list of 3 subject marks

    def calculate_average(self):
        return sum(self.marks) / len(self.marks)

    def get_result(self):
        avg = self.calculate_average()
        if avg >= 40:
            return "Pass"
        else:
            return "Fail"

    def display_report(self):
        print("\n----- Student Report Card -----")
        print("Name       :", self.name)
        print("Roll No.   :", self.roll)
        print("Marks      :", self.marks)
        print("Average    :", self.calculate_average())
        print("Result     :", self.get_result())
        print("-------------------------------")

# --- Main Program ---
name = input("Enter student name: ")
roll = input("Enter student roll no: ")
marks = []

for i in range(1, 4):
    m = int(input(f"Enter marks for Subject {i}: "))
    marks.append(m)

student1 = Student(name, roll, marks)
student1.display_report()

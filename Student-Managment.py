# Commit: Initialize student details and marks list
name = input("Please enter your name : ")
marks = []
total = 0
percentage = []

#  Input marks for 5 subjects
for i in range(5):
    mark = int(input(f"Enter marks of {i+1} Subject out of 50 : "))
    marks.append(mark)
print(f"{name}'s marks are : {marks}")

# Function to calculate total marks
def total_marks(marks):
    global total
    for ch in marks:
        total += ch
    print("Total marks are: ", total)

total_marks(marks)

#  Function to calculate percentage
def per(marks):
    global percentage
    percentage = (total / 250) * 100
    print(f"Your Percentage is : {percentage} %")

per(marks)

# Determine grade based on percentage
grade = percentage
if grade >= 80:
    print("A Grade")
elif grade >= 70:
    print("B Grade")
elif grade >= 60:
    print("C Grade")
else:
    print("Fail...!")

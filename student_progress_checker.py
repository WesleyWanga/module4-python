print("Student Progress Checker ") #program title
print("------------------------------")
student_name= input("Enter the student name:")
lab_score=float(input("Enter lab score: "))  # Float used when expecting values that are decimals
project_score=float(input("Enter project score: "))
attendance=float(input("Enter attendance percentage: "))
completed_labs=int(input("Enter number of completed labs: ")) # int used when expecting values that are whole numbers
active_input=input("Is the student active?Type yes or no:")

average_score= (lab_score+project_score)/2

if average_score>=50 and attendance>=90 and completed_labs>=8 and active_input=="yes":
 print("Status: Pass")
else:
 print("Status: fail")
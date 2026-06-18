#string datatype

student_name= "John"
course="Software Development"
email="john@gmail.com"

#integer datatype -  whole number
age= 21
completed_labs=5
score=80
number_of_students=32

#Float datatypes - used for numbers that are not whole numbers.
height=1.65
average_score=72.8
price= 1500.75

#boolean data types- has two possible value that are true or false
is_active= True
has_submitted= False
is_logged_in= True
has_passed= False 

# checking datatypes 
#In javascript we will have typeof()
# in python we will have type()

print(type(height)) 
print(type (has_submitted))

#arithmetic operators: perform mathematical operations (+,-,/,*,%,//,**)
num1= 10
num2= 5

total= num1+num2
print(total)

total_marks=100
marks_lost= 15

final_marks= total_marks-marks_lost
print(final_marks)

price= 2000
quantity= 3

total_price= price*quantity
print(total_price)

total_score= 8
number_of_subject= 4
average_score= total_score/number_of_subject
print (average_score)

 # floor division- divide values and remove the decimal part
result= 17//5
print(result)

# modulus- gives the remainder after division
remainder= 17%5
print(remainder)

#exponentiation- used to raise a number to a power

output=4**4
print(output)

# Assignment operators- used to assign values to variables (=)
score= 90
print(90) 
#update the variable score (=,+=,-=,*=,/=)
score= 100
print(score)

# +=
completed_labs+=1 #comppleted_labs=completed_labs+1
print(completed_labs)

# -=
remaining_labs= 10
remaining_labs-=2
print(remaining_labs)

# *=
points= 10
points*=3
print(points)

# /=
score/=2
print(score)

#comparison opeartors- used to compare 2 values. The result is a boolean value (==, !=,>,<,>=,<=)
score= 120
print(score==150)

print(score!=90)
print(score>40)
print(score>200)
print(score<100)

attendance= 90
print(attendance>=90)
print(attendance<=85)

#Logical Operators (and, or, not)
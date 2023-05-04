#1) Update the Student Class to include these attributes - first_name, last_name, age, country
 #    - Add these methods to the Student class
 #            - show_full_name
 #           - year_of_birth
 #           - show_initial
class Student:
    first_name="Mary" 
    last_name="Wambui"
    age=20
    country="kenya"
def __init__(self,show_full_name,year_of_birth,show_initial):
    self.show_full_name=show_full_name
    self.year_of_birth=year_of_birth
    self.show_initial=show_initial
student=Student()  
print(f"{student.first_name}{student.last_name}") 
print(f"{student.age}")
print(f"{student.first_name[0]}{student.last_name[0]}") 


#create 3 files in the classes directory car.py, fruit.py, and bank.py. Define the following classes in each module respectively. 
#Car
#Fruit
#Account
#Each class should have one class attribute and three instance variables.
  




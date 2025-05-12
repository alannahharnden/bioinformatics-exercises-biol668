class Person:

    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last

    ##Add operator overload for print that prints
    ##First Name: firstname
    ##Last  Name: lastname
        

#Make derived class "Employee" that inherits the base class Person
#In the constructor, grab all the Person methods using the super() method
#(1) Add a new variable to hold date of birth called "dob" to the __init__
#   Overload __str__ with super and add "\nDOB: " + str(self.dob)
#(2) Also add a new variable "ssn" to the __init__ to hold the social security number
#    Add a new method called get_ssn that returns the ssn


if __name__=="__main__":

    ##Test situation
    """
    boss = Person("Hamed", "Haq")
    empl = Employee("Ted", "McMaster", "03151970", 999999999)

    print(boss)
    print(empl)
    print(empl.get_ssn())
    """





class Employe:
    count=0

    def __init__(self, name, designation, salary):

        self.name = name
        self.designation = designation
        self.salary = []
        Employe.count=Employe.count+1

    def getdata(self):
        
        self.name = input()
        self.designation = input()
        self.salary=list(input().split) 
        print('The name of Employe is : ', self.name)
        print('You work here as : ', self.designation)
        print('And your Salary is : ', self.salary)
        
    def avg(self):
        m=self.salary
        for i in range(Employe.count):
            m = int(input('enter the salary: {} of employee {}:').format(self.name,i+1))
            self.salary.append(m)
        self.total=m[0]+m[1]
        self.avg=self.total/2
        print(self.avg)
    
    def displaycount(self):
        print("number of employes in the organization are",Employe.count)



employe1=Employe('name', 'designation','salary')

employe2=Employe('name', 'designation','salary')
employe1.getdata()
employe2.getdata()
employe1.displaycount()
Employe().avg()





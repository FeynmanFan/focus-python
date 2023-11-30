import pandas as pd
import classes.employee as empl
    
filePath = "employees.xlsx"

df = pd.read_excel(filePath)

employees = df[['firstName', 'lastName', 'salary']]

for index, row in employees.iterrows():
    emp = empl.employee()
    emp.firstName = row['firstName']
    emp.lastName = row['lastName'] 
    emp.salary = row['salary']
    
    print(emp.firstName + " " + emp.lastName + " makes ")
    print(emp.salaryOpinion())
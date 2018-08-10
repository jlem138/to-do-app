import sqlite3
from employee import Employee

conn = sqlite3.connect(':memory:')

c = conn.cursor()

c.execute("""CREATE TABLE employees (
                first text,
                last text,
                pay integer
                )""")

emp_1 = Employee('John', 'Doe', 80000)
emp_2 = Employee('Mark', 'Johnson', 10000)
emp_3 = Employee('Sarah', 'Franklin', 80000)
emp_4 = Employee('Mark', 'Franklin', 70000)

def insert_emp(emp):
    with conn:
        c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {'first': emp.first, 'last': emp.last, 'pay': emp.pay})

def get_emps_by_name(lastname):
    c.execute("SELECT * FROM employees WHERE last =:last", {'last': lastname})
    return c.fetchall()

def update_pay(emp, pay):
    with conn:
        c.execute("""UPDATE employees SET pay = :pay WHERE first = :first AND last =:last""",
        {'first': emp.first, 'last': emp.last, 'pay': pay})

def remove_emp(emp):
    with conn:
        c.execute("DELETE from employees WHERE first = :first AND last =:last", {'first': emp.first, 'last':emp.last})

insert_emp(emp_1)
insert_emp(emp_2)
insert_emp(emp_3)
insert_emp(emp_4)

emps = get_emps_by_name('Franklin')
print(emps)

update_pay(emp_2, 95)
remove_emp(emp_1)
print(emps)



conn.close()

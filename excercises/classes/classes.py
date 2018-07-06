class Company(object):
    """This represents a company in which people work"""

    def __init__(self, company_name, date_founded):
        self.company_name = company_name
        self.date_founded = date_founded
        self.employees = set()

    def get_company_name(self):
        """Returns the name of the company"""

        return self.company_name
# Add the remaining methods to fill the requirements above

class Employee(object):
    # this represents and employee
    def __init__(self, first_name, last_name, job_title, start_date):
        self.first_name = first_name
        self.last_name = last_name
        self.job_title = job_title
        self.start_date = start_date
        

    def get_employee_name(self):
        # returns an employee
        return self.first_name + self.last_name

# if __name__ == '__main__':
    # create company
NashvilleSoftwareSchool = Company("Nashville Software School", "2014")

# create employees
steve = Employee("Steve", "Brownlee", "Instructor", "2015")
ryan = Employee("Ryan", "Tanay", "Instructor", "2015")
charisse = Employee("Charisse", "Lambert", "Instructor", "2015")

NashvilleSoftwareSchool.employees.add(steve)
NashvilleSoftwareSchool.employees.add(ryan)
NashvilleSoftwareSchool.employees.add(charisse)
print(NashvilleSoftwareSchool.employees)

# class Customer:
#     def __init__(self, fn, ln, acct):
#         self.accountNumber = acct
#         self.firstName = fn
#         self.lastName = ln


# class Bank:
#     def __init__(self):
#         self.name = ""
#         self.address = ""
#         self.lastName = ""

#         self.customers = set()

# if __name__ == '__main__':
#     # Create the bank
#     FirstTennessee = Bank()

#     # Create some customers
#     steve = Customer("Steve", "Brownlee", "000000000")
#     ryan = Customer("Ryan", "Tanay", "000000000")
#     charisse = Customer("Charisse", "Lambert", "000000000")

#     # Add the customers into the aggregate instance variable of the bank
#     FirstTennessee.customers.add(steve)
#     FirstTennessee.customers.add(ryan)
#     FirstTennessee.customers.add(charisse)
#     print(FirstTennessee)
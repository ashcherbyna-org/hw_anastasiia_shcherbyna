class Company:
    def __init__(self, company_name, set_up_date):
        self.company_name = company_name
        self.set_up_date = set_up_date


company1 = Company("Epam", 1993)
company2 = Company("Global Logic", 2000)
company3 = Company("Ciklum", 2002)
print(company1.company_name, company1.set_up_date)
print(company2.company_name, company2.set_up_date)
print(company3.company_name, company3.set_up_date)


class Employee:
    def __init__(self, name, age, project):
        self.name = name
        self.age = age
        self.project = project


employee1 = Employee("Mark England", 1987, "Vava cars")
employee2 = Employee("Valentin Rossoha", 1989, "Vava cars")
employee3 = Employee("Andrii Vovk", 1987, "No project")
print(employee1.age, employee1.name, employee1.project)
print(employee2.age, employee2.name, employee2.project)
print(employee3.age, employee3.name, employee3.project)

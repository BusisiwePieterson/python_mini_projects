class Employee:
    def __init__(self, basic_salary=500):
        self.basic_salary = basic_salary

class Chef(Employee):
    def __init__(self, hourly_wage, hours, days):
        super().__init__(550)
        self.hourly_wage = hourly_wage
        self.hours = hours
        self.days = days
    
    def chef_monthly_income(self):
        return self.hourly_wage * self.hours * self.days + self.basic_salary 
    
class Waiter(Employee):
    def __init__(self, monthly_salary, tips):
        super().__init__(600)
        self.monthly_salary = monthly_salary
        self.tips = tips

    def waiter_monthly_income(self):
        return self.monthly_salary + self.tips * 0.5 + self.basic_salary

class Cleaner(Employee):
    def __init__(self, monthly_salary, extra_hours, extra_hour_wage):
        super().__init__()
        self.monthly_salary = monthly_salary
        self.extra_hours = extra_hours
        self.extra_hour_wage = extra_hour_wage

    def cleaner_monthly_income(self):
        return self.monthly_salary + self.extra_hours * self.extra_hour_wage + self.basic_salary


busi = Chef(20, 8, 26)
print(busi.chef_monthly_income())

lali = Waiter(3000, 200)
print(lali.waiter_monthly_income())

candy = Cleaner(3500, 15, 20)
print(candy.cleaner_monthly_income())



        
        
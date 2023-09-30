"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, salary, hours=0, commission_amnt=0, commission_num=0):
        self.name = name
        self.salary = salary
        self.hours = hours
        self.commission_amnt = commission_amnt
        self.commission_num = commission_num


    def get_pay(self):
        total = self.salary
        if self.hours:  # Hourly wage
            total *= self.hours

        if self.commission_num:    # Contract commission
            total += (self.commission_amnt * self.commission_num)
        else:   # Bonus commission
            total += self.commission_amnt
        return total

    def __str__(self):
        text = f"{self.name} works on a "
        if self.hours:
            text += f"contract of {self.hours} hours at {self.salary}/hour"
        else:
            text += f"monthly salary of {self.salary}"

        if self.commission_num:
            text += f" and receives a commission for {self.commission_num} contract(s) at {self.commission_amnt}/contract"
        elif self.commission_amnt:
            text += f" and receives a bonus commission of {self.commission_amnt}"

        text += f". Their total pay is {self.get_pay()}."
        return text


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', 4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', 25, 100)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', 3000, 0, 200, 4)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', 25, 150, 220, 3)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', 2000, 0, 1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', 30, 120, 600)



class LoggedAccess:
    def __set_name__(self, owner, name):
        self.public_name = name
        self.private_name = "_" + name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        value = getattr(instance, self.private_name)
        print(f"Accessing {self.public_name} giving {value}")
        return value

    def __set__(self, instance, value):
        print(f"Updating {self.public_name} to {value}")
        setattr(instance, self.private_name, value)


class Employee:
    name = LoggedAccess()
    position = LoggedAccess()
    salary = LoggedAccess()

    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary


john = Employee("John", "Software Engineer", 100000)
print(john.name)
print(john.position)
print(john.salary)
john.salary = 150000
print(john.salary)

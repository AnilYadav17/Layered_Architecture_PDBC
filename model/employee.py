class Employee:
    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary

    def __repr__(self):
        return f"Employee(id={self.id}, name='{self.name}', salary={self.salary})"
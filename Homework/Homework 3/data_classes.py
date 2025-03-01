import json

class Person:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def to_dict(self):
        return {"name": self.name, "age": self.age, "email": self.email}

class Student(Person):
    def __init__(self, name, age, email, student_id):
        super().__init__(name, age, email)
        self.student_id = student_id

    def to_dict(self):
        data = super().to_dict()
        data["student_id"] = self.student_id
        return data

def save_to_json(filename, people):
    with open(filename, "w") as file:
        json.dump([person.to_dict() for person in people], file, indent=4)

def display_json(filename):
    try:
        with open(filename, "r") as file:
            data = json.load(file)
            print(json.dumps(data, indent=4))
    except FileNotFoundError:
        print("File not found.")

# Example Usage
if __name__ == "__main__":
    person1 = Person("Alice", 30, "alice@example.com")
    student1 = Student("Bob", 20, "bob@example.com", "S12345")
    
    save_to_json("people.json", [person1, student1])
    display_json("people.json")

# def function_name():
# def this_is_a_person():

class ThisIsAPerson:

    def __init__(self, name, sex, height, ethnicity, age):
        self.name = name
        self.sex = sex
        self.height = height
        self.ethnicity = ethnicity
        self.age = age

    def write_to_file(self):
        sentence = f"Hi, my name is {self.name}. I am a {self.sex}, and {self.age} years old. I am {self.height}, and my ethnicity is {self.ethnicity}."

        with open("people.txt", "w") as file:
            file.write(sentence)


person1 = ThisIsAPerson("Caius", "male", "5'8", "white", "23")
person1.write_to_file()

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print('Имя: {}. Возраст: {}'.format(self.name, self.age))



bob = Person("Bob", 92)
sellu = Person("Sellu", 29)

bob.introduce()
sellu.introduce()
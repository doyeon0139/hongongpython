class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def greeting(self):
        print('저는 {}살 {}에 사는 {}입니다'.format(self.age, self.address, self.name))

# p1 = Person('철수', 28, '서울')
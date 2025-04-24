class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

if __name__=='__main__':
    p1=Person('John','Doe')
    print(p1.first_name)
    print(p1.last_name)

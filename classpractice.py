class Person(object):
    class_type = 'I am a People'
    people_counter = 0

    def __init__(self, nm):
        self.name = nm
        Person.people_counter += 1

    def returnname(self):
        print self.name
        print self.name + ', you are person number ' + str(Person.people_counter)
Jon = Person("Jon")
Jon.returnname()

Nick = Person("Nick")
Nick.returnname()
print Nick.class_type

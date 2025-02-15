from random import randrange

from human import Human


class Native(Human):
    def _init_(self, name, date_of_birth,gender,height,phone):
        super()._init_(name,date_of_birth,gender,height)
        self.phone = phone
        self._id = self.generate_id()

    @staticmethod
    def generate_id():
        return "scv" + str(randrange(1000,999999))


    def _str_(self):
        return f'''
        {super()._str_()}
        Phone :{self.phone}
        ID :{self._id}'''


person = Native("Edwin","22-03-1995","Male","6.2","09096041561")
print(person)
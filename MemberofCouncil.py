class MemberofCouncil(object):
    def __init__(self, fullname, birthdate, group, age):
        self._fullname = fullname
        self._birthdate = birthdate 
        self._group = group 
        self._age = age

    def changeinfo(self):
        print("Choose what info you want to change\n 1. Name \n 2. Group")
        ch = input()
        if ch == "1":
            self._fullname = input()
        else:
            self._group = input()

    def getinfo(self):
        return self._fullname, self._birthdate, self._group
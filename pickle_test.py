import pickle

class Person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def intro(self):
        print(self.name+" "+str(self.age)+" "+self.gender)

def main():
    """
    deal with some type of data
    :return:
    """
    str2ser = "this is a fucking donkey"
    dict2ser = {'age':13,'name':'jack'}
    byte_byte = pickle.dumps(dict2ser)
    obj = pickle.loads(byte_byte)
    print(obj)

    scr = Person("suncerui",22,"female")
    byte_scr = pickle.dumps(scr)
    newscr = pickle.loads(byte_scr)
    newscr.intro()


if __name__ == '__main__':
    main()
class cookie():
    chocolate = False
    def __init__(self):
        print("A cookie is made")
    def add_chocolate (self):
        self.chocolate = True
    def chocolate_question (self):
        if (self.chocolate):
            print("A chocolate cookie")
        else:
            print("no chocolate")
g=cookie()

g.chocolate_question()
g.add_chocolate()
g.chocolate_question()

class cookie():
    chocolate = False
    def __init__(self,flavor=None):
        self.flavor=flavor
        print("A cookie is made with",flavor)
    def add_chocolate (self):
        self.chocolate = True
    def chocolate_question (self):
        if (self.chocolate):
            print("A chocolate cookie")
        else:
            print("no chocolate")
g=cookie()
g=cookie("bananas")


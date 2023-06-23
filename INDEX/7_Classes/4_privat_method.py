class example:
    __hidden_atribute = "Hidden atribute"

    def __privat_method(self):
        print("privat_method")

    def public_method(self):
        return self.__privat_method()
e = example()
e.public_method()
e.__privat_method()
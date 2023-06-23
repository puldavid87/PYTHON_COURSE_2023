class movie:
    def __init__(self,title, duration, date):
        self.title = title
        self.duration = duration
        self.date = date
        print("New movie has been crated")

    #string method
    def __str__(self):
        return "{} takes {} minutes and created in {} ".format(self.title,self.duration,self.date)
    
    def __len__ (self):
        return self.duration
    
movie1 = movie("Shrek", 200, 1996)
print(str(movie1))
print(len(movie1))


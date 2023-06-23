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
    
class catalogue:
    movies = []
    def __init__(self, movies=[]):
        self.movies = movies
    
    def add_movies(self,mov):
        self.movies.append(mov)
    
    def show_movies (self):
        for m in self.movies:
            print(m)

movie2 = movie("The grandfather",175,1972)
c = catalogue([movie2])
c.add_movies(movie("Sherk",120,1996))
print(c.show_movies) 


        

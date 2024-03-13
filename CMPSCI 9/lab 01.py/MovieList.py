from Movie import Movie
class MovieList:
    def __init__(self):
        self.movieList = {}

    def addMovie(self, movie):
        if movie.genre in self.movieList:
            self.movieList[movie.genre].append(movie)
        else:
            self.movieList[movie.genre] = [movie]

    def removeMovie(self, movie):
        if movie.genre in self.movieList:
            for i in self.movieList[movie.genre]:
                if i.title == movie.title and i.genre == movie.genre and i.year == movie.year:
                    self.movieList[movie.genre].remove(i) 

    def removeGenre(self, genre):
        genre = genre.upper()
        if genre in self.movieList:
            del self.movieList[genre]

    def getMoviesByGenre(self, genre):
        genre = genre.upper()
        if genre in self.movieList:
            a_str = [a.toString() for a in self.movieList[genre]]
            return "\n".join(a_str)
        else:
            return ""


    def doesMovieExist(self, movie):
        if movie.genre in self.movieList:
            for i in self.movieList[movie.genre]:
                if i.title == movie.title and i.genre == movie.genre and i.year == movie.year:
                    return True
        return False
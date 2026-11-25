from abc import ABC,abstractmethod

class iterator(ABC):

    @abstractmethod
    def has_next(self)-> bool:
        pass
    
    @abstractmethod
    def next(self):
        pass



class playlist_iterator(iterator):
    
    def __init__(self,song_list):
        self.__song_list=song_list
        self.__current=0

    def has_next(self):
        if self.__current < len(self.__song_list):
            return True
        else :
            return False

    def next(self):
        while self.has_next():
            current_song=self.__song_list[self.__current]
            self.__current+=1
            return current_song
        
        return None

class playlist:
    def __init__(self):
        self.__playlist=[]

    def add_song(self,song_obj):
        self.__playlist.append(song_obj)
    
    def show_songs(self):
        return playlist_iterator(self.__playlist)


class song:
    def __init__(self,title):
        self.__title=title
    
    def get_title(self):
        return self.__title


playlist=playlist()
playlist.add_song(song("Dirty Deeds Done Dirt Cheap"))
playlist.add_song(song("Numb"))
playlist.add_song(song("Rolling in the Deep"))

iterator=playlist.show_songs()


while iterator.has_next():
    print(iterator.next().get_title())
    
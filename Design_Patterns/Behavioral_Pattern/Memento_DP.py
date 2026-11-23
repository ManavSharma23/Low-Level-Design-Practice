# Memento Design Pattern

# Saves an object's previous state so it can be restored later.
# Allows undo functionality without exposing the object's internal details.
# Commonly used in text editors, games, and applications with undo/redo features.
# Example: Restoring a document to its previous version.



class TextMemento:
    
    def __init__(self,text):
        self.__savedText=text

    def get_saved_text(self):
        return self.__savedText

class TextEditor:

    def __init__(self):
        self.__text=""

    def write(self,message):
        self.__text+=message
    
    def get_text(self):
        return self.__text
    
    def save(self):
        return TextMemento(self.__text)

    def restore(self,memento):
        self.__text=memento.get_saved_text()

class History:

    def __init__(self):
        self.__history=[]

    def update(self,memento):
        self.__history.append(memento)

    def show_history(self):
        for i in range(len(self.__history)):
            print(f"{i} = {self.__history[i].get_saved_text()}")


    def undo(self):
        if len(self.__history)>0:
            self.__history.pop()
            if len(self.__history)==0:
                return TextMemento("")
            else:
                return self.__history[-1]
        else:
            return TextMemento("")


    
t1 = TextEditor()
h = History()

# write the first version
t1.write("Hello ")
t1.write("World")

print("Current Text:", t1.get_text())

# save the first snapshot
h.update(t1.save())

# modify the text
t1.write(" Good ")
t1.write("Morning")

print("\nUpdated Text:", t1.get_text())

# save the second snapshot
h.update(t1.save())

# display saved history
print("\nBefore Undo:")
h.show_history()

# undo and restoring the previous state
t1.restore(h.undo())

# display text after undo
print("\nAfter Undo:")
print("Current Text:", t1.get_text())

# display remaining history
h.show_history()

        
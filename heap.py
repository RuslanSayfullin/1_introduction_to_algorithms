#создание структуры данных куча
class Heap():
    def __init__(self):
        self.values = []
        self.size = 0

    def insert(self, х):
        self.values.append(x)
        self.size +=1

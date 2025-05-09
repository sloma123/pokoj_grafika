import bge

class SetObjectColor(bge.types.KX_PythonComponent):
    args = {}

    def start(self, args):
        # Ustawienie koloru RGBA
        #maksymalna wartość =1 (100%)
        self.object.color = (0.88, 0.59, 1.0, 0.08)   

    def update(self): # metoda wywoływana automatycznie co klatkę 
    # pusta instrukcja w Pythonie — oznacza "nic nie rób".
        pass

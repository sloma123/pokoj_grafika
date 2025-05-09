import bge

class SetObjectColor(bge.types.KX_PythonComponent):
    args = {}

    def start(self, args):
        self.object.color = (1.0, 0.3, 0.7, 1.0)  # Ustawienie koloru RGBA

    def update(self):
        pass

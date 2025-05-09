import bge
from collections import OrderedDict

class ThirdPerson(bge.types.KX_PythonComponent):
    """Basic third character controller

    W: move forward
    S: move backward
    A: move left
    D: move right
    """

    args = OrderedDict([
        ("Move Speed", 0.05),
    ])

    def start(self, args):
        self.move_speed = args['Move Speed']

    def update(self):
        keyboard = bge.logic.keyboard
        inputs = keyboard.inputs

        move_x = 0  # lewo/prawo
        move_y = 0  # przód/tył

        if inputs[bge.events.WKEY].values[-1]:
            move_y -= self.move_speed
        if inputs[bge.events.SKEY].values[-1]:
            move_y += self.move_speed
        if inputs[bge.events.AKEY].values[-1]:
            move_x -= self.move_speed
        if inputs[bge.events.DKEY].values[-1]:
            move_x += self.move_speed

        # Zastosuj ruch w lokalnym układzie współrzędnych (True)
        self.object.applyMovement((move_x, 0, move_y ), True)
#test
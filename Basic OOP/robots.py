class Robot:

    def __init__(self, model: str, weigth: int, height: int):
        self.model = model
        self.weight = weigth
        self.height = height

    def move(self):
        print(f'Robot {self.model} moving forward...')

    def move_back(self):
        print(f'Robot {self.model} moving back...')

    def move_left(self):
        print(f'Robot {self.model} moving left...')

    def move_right(self):
        print(f'Robot {self.model} moving right...')


class Spot(Robot):

    NAME = 'Spot'

    def __init__(self, model, weigth, height: int):
        super().__init__(model, weigth, height)
        self.model = self.NAME + ' - ' + self.model

    def jump(self):
        print(f'Robot {self.model} jumping...')


class Atlas(Spot):

    NAME = 'Atlas'

    def dancing(self):
        print(f'Robot {self.model} dancing...')



r = Robot('base', 120, 150)
r.move()

s = Spot('Ani', 120, 150)
s.move()

a = Atlas('dasd', 122, 111)
a.dancing()
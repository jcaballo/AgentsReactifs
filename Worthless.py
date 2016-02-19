from Rock import Rock

class Worthless(Rock):
    def __init__(self, x, y, fenetre):
        super(Worthless, self).__init__(x, y, fenetre)
        self.label.config(bg="black")
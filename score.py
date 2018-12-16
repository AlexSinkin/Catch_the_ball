class Score:
    def __init__(self, canvas, x, y):
        self.hits = 0
        self.canvas = canvas
        self.text = canvas.create_text(x, y, text="Результат: 0", font='Arial 20')
        return

    def inc_hits(self):
        self.hits += 1
        self.update()
        return

    def update(self):
        self.canvas.itemconfig(self.text, text="Результат: {}".format(self.hits))
        return

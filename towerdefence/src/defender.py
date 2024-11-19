class Defender:
    cost = 10

    def __init__(self, image, damage = 10, attack_speed = 2, x = 0, y = 0):
        self.image = image
        self.damage = damage
        self.attack_speed = 2
        self.x = x
        self.y = y

    def get_img(self):
        return self.image
    
    def get_pos(self):
        return (self.x, self.y)
    
    def set_pos(self, x, y):
        self.x = x
        self.y = y

    def shoot(self):
        pass
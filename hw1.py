class Hero:
    def __init__(self, name, nickname, hp, damage):
        self.name = name
        self.nickname = nickname
        self.hp = hp
        self.damage = damage

    def heal(self):
        self.hp += 100

    def two_damage(self):
        self.damage *= 2

    def greetings(self):
        print(f'my name is {self.name}')

    def brand_phrase(self):
        print('good will win')


hero1 = Hero(name='Alexsey', nickname='Alex', hp=100, damage=50)
hero2 = Hero(name='Jonnar', nickname='Joni', hp=100, damage=30)
hero3 = Hero(name='Lukas', nickname='Luk', hp=100, damage=40)
hero4 = Hero(name='Bobi', nickname='Bob', hp=100, damage=60)

hero1.heal()
print(hero1.hp)
hero2.two_damage()
print(hero2.damage)
hero3.greetings()
hero4.brand_phrase()
class Character:
	def __init__(self, h, m):
		self.health = h
		self.mana = m
		print("Character Created!")

	def take_damage(self, power, speed):
		self.damage = power * speed

warrior = Character(100, 50)
mage = Character(50, 100)
rogue = Character(75, 75)
paladin = Character(80, 70)

print(warrior.take_damage)
warrior.take_damage(5, 8)
print(warrior.take_damage)
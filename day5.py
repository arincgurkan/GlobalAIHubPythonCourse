class Animal:
	def make_sound(self, sound):
		print(sound)

	def move(self, type_of_move):
		print(f"I'm moving with my {type_of_move}")

	is_animal_cool = False


class Cat(Animal):
	pass

class Dog(Animal):
	is_animal_cool = True

cat = Cat()
cat.make_sound("Meow")
cat.move("Foots")
print(f'Is this animal cool? {"Yeah!" if cat.is_animal_cool else "Nope, sorry."}\n\n')

dog = Dog()
dog.make_sound("How How")
dog.move("Foots")
print(f'Is this animal cool? {"Yeah!" if dog.is_animal_cool else "Nope, sorry."}')
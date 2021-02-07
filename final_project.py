#Define manager class
class Manager:
	def __init__(self, name, age, languages):
		self.name = name
		self.age = age
		self.languages = languages

	def print_infos(self):
		return f'I am {self.name} and {self.age} years old. The languages that I can speak are {", ".join(str(language) for language in self.languages)}.'


#Define employees clas with super method. Because they have same form
class Employees(Manager):
	emps = []
	def __init__(self, name, age, languages):
		self.emps.append(self)
		super().__init__(name, age, languages)

#Defining test employees.
emp1 = Employees("arinc", 15, ['Eng', 'Tur'])
emp2 = Employees("ali", 17, ['Eng', 'Ger'])

#Test the print_infos method
print(emp1.print_infos())

#print the languages that any of the employees can speak.
lang_list = []
for emps in Employees.emps:
	for lang in emps.languages:
		 if lang not in lang_list:
		 	lang_list.append(lang)

print(lang_list)
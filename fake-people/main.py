from faker import Faker
import file_operations
from random import randint, sample

fake = Faker('ru_RU')

min_ability = 8
max_ability = 14

number_of_sheets = 10

rune_abc = {
    'а': 'а͠', 'б': 'б̋', 'в': 'в͒͠',
    'г': 'г͒͠', 'д': 'д̋', 'е': 'е͠',
    'ё': 'ё͒͠', 'ж': 'ж͒', 'з': 'з̋̋͠',
    'и': 'и', 'й': 'й͒͠', 'к': 'к̋̋',
    'л': 'л̋͠', 'м': 'м͒͠', 'н': 'н͒',
    'о': 'о̋', 'п': 'п̋͠', 'р': 'р̋͠',
    'с': 'с͒', 'т': 'т͒', 'у': 'у͒͠',
    'ф': 'ф̋̋͠', 'х': 'х͒͠', 'ц': 'ц̋',
    'ч': 'ч̋͠', 'ш': 'ш͒͠', 'щ': 'щ̋',
    'ъ': 'ъ̋͠', 'ы': 'ы̋͠', 'ь': 'ь̋',
    'э': 'э͒͠͠', 'ю': 'ю̋͠', 'я': 'я̋',
    'А': 'А͠', 'Б': 'Б̋', 'В': 'В͒͠',
    'Г': 'Г͒͠', 'Д': 'Д̋', 'Е': 'Е',
    'Ё': 'Ё͒͠', 'Ж': 'Ж͒', 'З': 'З̋̋͠',
    'И': 'И', 'Й': 'Й͒͠', 'К': 'К̋̋',
    'Л': 'Л̋͠', 'М': 'М͒͠', 'Н': 'Н͒',
    'О': 'О̋', 'П': 'П̋͠', 'Р': 'Р̋͠',
    'С': 'С͒', 'Т': 'Т͒', 'У': 'У͒͠',
    'Ф': 'Ф̋̋͠', 'Х': 'Х͒͠', 'Ц': 'Ц̋',
    'Ч': 'Ч̋͠', 'Ш': 'Ш͒͠', 'Щ': 'Щ̋',
    'Ъ': 'Ъ̋͠', 'Ы': 'Ы̋͠', 'Ь': 'Ь̋',
    'Э': 'Э͒͠͠', 'Ю': 'Ю̋͠', 'Я': 'Я̋',
    ' ': ' '
}

skills = [
'Стремительный прыжок',
'Электрический выстрел',
'Ледяной удар',
'Стремительный удар',
'Кислотный взгляд',
'Тайный побег',
'Ледяной выстрел',
'Огненный заряд']

runic_skills = []
for skill in skills:
  for orig, repl in rune_abc.items():
    skill = skill.replace(orig, repl)
  runic_skills.append(skill)

for sheet in range(0,number_of_sheets):
  skill_list = sample(runic_skills,3)
  context = {
    'first_name': fake.first_name_male(),
    'last_name': fake.last_name_male(),
    'job': fake.job(),
    'town': fake.city(),
    'strength': randint(min_ability, max_ability),
    'agility': randint(min_ability, max_ability),
    'endurance': randint(min_ability, max_ability),
    'intelligence': randint(min_ability, max_ability),
    'luck': randint(min_ability, max_ability),
    'skill_1': skill_list[0],
    'skill_2': skill_list[1],
    'skill_3': skill_list[2]
  }

  file_operations.render_template('charsheet.svg', 'charsheets/charsheet-{}.svg'.format(sheet), context)
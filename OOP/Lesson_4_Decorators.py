# 1. Створити клас Candidate
# 2. В init передавати ﬁrst name, last name, email, tech stack, main skill, main skill grade
# 3. Створити @property метод який повертає ﬁrst name + ‘ ‘ + last name
# 4. Створити @classmethod generate candidates, який приймає в якості аргументу шлях до
# файлу
# 5. Метод generate candidates має повертати список об’єктів класу Candidate
# Файл тут (тиць)
# 6. ** Розширити метод generate candidates, щоб він міг отримувати в якості аргументу URL
# на файл та генерувати кандидатів з нього
# 7. Можно використовувати цей URL:
# https://bitbucket.org/ivnukov/lesson2/raw/4f59074e6fbb552398f87636b5bf089a1618da0a/candidates.csv

import csv
import requests


class Candidate:
    def __init__(self, first_name, last_name, email, tech_stack, main_skill, main_skill_grade):
        self.fist_name = first_name
        self.last_name = last_name
        self.email = email
        self.tech_stack = tech_stack
        self.main_skill = main_skill
        self.main_skill_grade = main_skill_grade

    @property
    def full_name(self):
        return f'{self.fist_name} {self.last_name}'

    @classmethod
    def generate_candidates(cls, path_to_file):
        res = []
        if path_to_file[0:4] == 'http':
            response = requests.get(path_to_file)
            if response.status_code != 200:
                print('Failed to get data:', response.status_code)
            else:
                reader = csv.DictReader(response.text.strip().split('\n'))
                for row in reader:
                    data = dict(first_name=row['Full Name'].split()[0],
                                last_name=row['Full Name'].split()[-1],
                                email=row['Email'],
                                tech_stack=row['Technologies'].split('|'),
                                main_skill=row['Main Skill'],
                                main_skill_grade=row['Main Skill Grade'])
                    res.append(cls(**data))

        else:
            with open(path_to_file) as fp:
                reader = csv.DictReader(fp)
                for row in reader:
                    data = dict(first_name=row['Full Name'].split()[0],
                                last_name=row['Full Name'].split()[-1],
                                email=row['Email'],
                                tech_stack=row['Technologies'].split('|'),
                                main_skill=row['Main Skill'],
                                main_skill_grade=row['Main Skill Grade'])
                    res.append(cls(**data))
        return res


if __name__ == '__main__':
    petro = Candidate('Petro', 'Ivanov', 'saas@df.dd', 'java', 'python', 'C#')
    # print(petro)
    print(petro.full_name)
    re = Candidate.generate_candidates('candidates.csv')
    print(re)
    re = Candidate.generate_candidates('https://bitbucket.org/ivnukov/lesson2/raw/4f59074e6fbb552398f87636b5bf089a16'
                                       '18da0a/candidates.csv')
    print(re)

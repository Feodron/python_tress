import time
import json
import pathlib


class Auto:
    def __init__(self, brand: str, age: int, color=None, mark=None, weight=None):
        self.brand = brand
        self.age = age
        self.color = color
        self.mark = mark
        self.weight = weight

    def move(self):
        print('move')

    def stop(self):
        print('stop')

    def birthday(self):
        self.age += 1
        print(f'{self.age}')


class Truck(Auto):
    def __init__(self, brand: str, age: int, color: str, mark: str, weight: int):
        super().__init__(brand, age, color, mark, weight)

    def move(self):
        print('attention')
        super().move()

    def load(self):
        time.sleep(1)
        print("load")
        time.sleep(1)


class Car(Auto):
    def __init__(self, brand: str, age: int, color: str, mark: str, weight: int, max_speed: int):
        super().__init__(brand, age, color, mark, weight)
        self.max_speed = max_speed

    def move(self):
        print(f'max speed is {self.max_speed}')


# auto = Auto("Toyta", 5, "black", "Corolla", 1750)
# print(auto.brand, auto.age, auto.color, auto.mark, auto.weight)
# auto.move()
# auto.stop()
# auto.birthday()
# truck = Truck("ITM", 4, 'red', '1500-4WD', 2600)
# print(truck.brand, truck.age, truck.color, truck.mark, truck.weight)
# truck.move()
# truck.load()
# truck.birthday()
bmw = Car("BMW", 5, 'white', 'M5', 2000, 60)
print(bmw.brand, bmw.age, bmw.color, bmw.mark, bmw.weight, bmw.max_speed)
bmw.move()
bmw.stop()
bmw.birthday()
truck = Truck('Kamaz', 50, 'orange', '6561', 4500)
print( truck.age, truck.color, truck.mark, truck.weight)
truck.move()
truck.load()
truck.birthday()
#######################################################################################################
"""
Написать программу телефонная книга используя классы.
Написать класс телефонной книги, который хранит список контактов.
Он должен иметь возможность искать контакты по имени и по телефону
(два разных метода), добавлять новые контакты и удалять контакты по имени или телефону.
Контакты реализовать в виде объектов класса Контакт. Данные телефонной книги хранить в json файле.
"""


class Contact:
    def __init__(self, name: str, phone: str):
        self.name = name
        self.phone = phone

    def __str__(self):
        return f"{self.name}: {self.phone}"


class PhoneBook:
    p = pathlib.Path('phone_book.json')

    def __init__(self):
        if not self.p.exists():
            self.p.touch()
            self.data = []
        else:
            with self.p.open('r') as file:
                try:
                    json_data = json.load(file)
                    self.data = [
                        Contact(
                            contact.get('name'),
                            contact.get('phone')
                        )
                        for contact
                        in json_data
                    ]
                except Exception:
                    self.data = []
        self.output_data = list(map(str, self.data))

    def add_contact(self, name: str, phone: str) -> None:
        for contact in self.data:
            if contact.name == name and contact.phone == phone:
                return print('Contact exists')
        self.data.append(Contact(name, phone))
        with self.p.open('w') as file:
            contacts = [
                {
                    'name': contact.name,
                    'phone': contact.phone
                }
                for contact
                in self.data
            ]
            file.write(json.dumps(contacts))
        self.output_data = list(map(str, self.data))

    def delete_contact(self, name: str, phone: str) -> None:
        for contact in self.data:
            if contact.name == name and contact.phone == phone:
                self.data.remove(contact)
        with self.p.open('w') as file:
            contacts = [
                {
                    'name': contact.name,
                    'phone': contact.phone
                }
                for contact
                in self.data
            ]
            file.write(json.dumps(contacts))
        self.output_data = list(map(str, self.data))

    def search_by_name(self, name: str):
        contacts = [str(contact) for contact in self.data
                    if contact.name == name]
        print(contacts)

    def search_by_phone(self, phone: str):
        contacts = [
            str(contact) for contact in self.data
            if contact.phone == phone]
        print(contacts)


if __name__ == '__main__':
    book = PhoneBook()
    # book.add_contact('Vlad', '+375447193574')
    # print(book.output_data)
    # book.add_contact('Ivan', '+375251234445')
    # print(book.output_data)
    # book.delete_contact('Ivan', '+375251234445')
    # print(book.output_data)
    # book.add_contact('Ivan', '+375251234445')
    print(book.output_data)
    book.search_by_name('Vlad')
    book.search_by_name('Ivan')
    book.delete_contact('Ivan', '+375251234445')
    print(book.output_data)
    book.add_contact('Ivan', '+375251234445')
    print(book.output_data)
    book.search_by_phone('+375251234445')
pip install pydantic
python payment_system.py

from typing import Type
from pydantic import BaseModel, EmailStr, Field
from datetime import date

# Модель User
class User(BaseModel):
    name: str
    mail: EmailStr
    address: str

# Модель Bank
class Banks(BaseModel):
    name: str
    rating: float = Field(..., ge=0, le=5)  # Рейтинг от 0 до 5
    opened: date  # Дата открытия банка

# Модель Card
class Cards(BaseModel):
    cardholder: User  # Ссылаемся на User модель
    which_bank: Banks  # Ссылаемся на Bank модель
    opened: date  # Дата открытия карты

# Модель Balance
class Balance(BaseModel):
    card: Cards  # Ссылаемся на модель Card
    amount: float  # Сумма на балансе
    currency: str  # Валюта баланса (например, "USD", "EUR")

# Пример использования
if __name__ == "__main__":
    user = User(name="John Doe", mail="johndoe@example.com", address="1234 Elm St.")
    bank = Banks(name="BigBank", rating=4.5, opened=date(2000, 1, 1))
    card = Cards(cardholder=user, which_bank=bank, opened=date(2024, 1, 1))
    balance = Balance(card=card, amount=1000.50, currency="USD")
    
    print(user)
    print(bank)
    print(card)
    print(balance)






____________________________________________
#если хочешь красиво можно использовать следующий метод
from typing import Type
from pydantic import BaseModel, EmailStr, Field
from datetime import date
from tabulate import tabulate

# Модель User
class User(BaseModel):
    name: str
    mail: EmailStr
    address: str

# Модель Bank
class Banks(BaseModel):
    name: str
    rating: float = Field(..., ge=0, le=5)  # Рейтинг от 0 до 5
    opened: date  # Дата открытия банка

# Модель Card
class Cards(BaseModel):
    cardholder: User  # Ссылаемся на User модель
    which_bank: Banks  # Ссылаемся на Bank модель
    opened: date  # Дата открытия карты

# Модель Balance
class Balance(BaseModel):
    card: Cards  # Ссылаемся на модель Card
    amount: float  # Сумма на балансе
    currency: str  # Валюта баланса (например, "USD", "EUR")

# Пример использования
if __name__ == "__main__":
    user = User(name="John Doe", mail="johndoe@example.com", address="1234 Elm St.")
    bank = Banks(name="BigBank", rating=4.5, opened=date(2000, 1, 1))
    card = Cards(cardholder=user, which_bank=bank, opened=date(2024, 1, 1))
    balance = Balance(card=card, amount=1000.50, currency="USD")

    # Подготовка данных для вывода в таблицу
    user_data = [
        ["Name", user.name],
        ["Email", user.mail],
        ["Address", user.address]
    ]
    
    bank_data = [
        ["Bank Name", bank.name],
        ["Rating", bank.rating],
        ["Opened", bank.opened]
    ]
    
    card_data = [
        ["Cardholder", f"{card.cardholder.name} ({card.cardholder.mail})"],
        ["Bank", card.which_bank.name],
        ["Opened", card.opened]
    ]
    
    balance_data = [
        ["Balance", balance.amount],
        ["Currency", balance.currency]
    ]
    
    # Выводим данные в таблицах
    print("User Information:")
    print(tabulate(user_data, headers=["Field", "Value"], tablefmt="grid"))
    print("\nBank Information:")
    print(tabulate(bank_data, headers=["Field", "Value"], tablefmt="grid"))
    print("\nCard Information:")
    print(tabulate(card_data, headers=["Field", "Value"], tablefmt="grid"))
    print("\nBalance Information:")
    print(tabulate(balance_data, headers=["Field", "Value"], tablefmt="grid"))













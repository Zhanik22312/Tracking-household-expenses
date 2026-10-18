import json
import os

FILENAME = "expenses.json"

def load_expenses():
    if os.path.exists(FILENAME):
        try:
            with open(FILENAME, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []
    return []

def save_expenses(expenses):
    with open(FILENAME, "w", encoding="utf-8") as f:
        json.dump(expenses, f, ensure_ascii=False, indent=4)

def main():
    expenses = load_expenses()

    print("=== Учёт домашних расходов ===")
    
    while True:
        print("\nМеню:")
        print("1. Добавить расход")
        print("2. Показать все расходы")
        print("3. Посчитать общую сумму")
        print("4. Выйти")
        
        choice = input("Выберите действие (1-4): ").strip()

        if choice == '1':
            name = input("Введите название покупки: ").strip()
            try:
                amount = float(input("Введите сумму: "))
                expenses.append({"name": name, "amount": amount})
                save_expenses(expenses)
                print(f"Расход '{name}' на сумму {amount} успешно добавлен и сохранен!")
            except ValueError:
                print("Ошибка: введите корректное число для суммы.")

        elif choice == '2':
            if not expenses:
                print("Список расходов пока пуст.")
            else:
                print("\nСписок ваших расходов:")
                for i, item in enumerate(expenses, 1):
                    print(f"{i}. {item['name']} — {item['amount']} ₸")

        elif choice == '3':
            total = sum(item['amount'] for item in expenses)
            print(f"\nОбщая сумма всех расходов: {total} ₸")

        elif choice == '4':
            print("Выход из программы. Хорошего дня!")
            break
        else:
            print("Неверный ввод, попробуйте снова.")

if __name__ == "__main__":
    main()
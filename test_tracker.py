def calculate_total(expenses):
    return sum(item['amount'] for item in expenses)

def test_calculate_total():
    mock_expenses = [
        {"name": "Кофе", "amount": 500},
        {"name": "Обед", "amount": 1500}
    ]
    total = calculate_total(mock_expenses)
    assert total == 2000, f"Ожидалось 2000, получено {total}"
    print("Тест подсчета суммы успешно пройден!")

if __name__ == "__main__":
    test_calculate_total()
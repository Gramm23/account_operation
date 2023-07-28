class Operations:
    def __init__(self, state, date, description, transfer_from, transfer_to, amount, currency):
        self.state = state
        self.date = date
        self.description = description
        self.transfer_from = transfer_from
        self.transfer_to = transfer_to
        self.amount = amount
        self.currency = currency

#     def __repr__(self):
#         return f"""Статус операции: {self.state}
# Дата операции: {self.date}
# Описание операции: {self.description}
# Счет отправителя: {self.transfer_from}
# Счет получателя: {self.transfer_to}
# Сумма платежа: {self.amount}
# Наименование валюты: {self.currency}"""

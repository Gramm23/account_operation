import json

from main.modul import Operations


def get_operations_list():
    with open('main/operations.json', encoding='utf-8') as data_operations:
        operations_list = json.load(data_operations)
        formatted_list = [item for item in operations_list if item]
        sorted_list = sorted(formatted_list, key=lambda item: item['date'], reverse=True)
        operations = []
        for item in sorted_list:
            state = item['state']
            date = item['date']
            description = item['description']
            transfer_to = item['to']
            amount = item['operationAmount']['amount']
            currency = item['operationAmount']['currency']['name']

            if 'from' in item:
                transfer_from = item['from']
            else:
                transfer_from = None

            operation = Operations(state, date, description, transfer_from, transfer_to, amount, currency)
            operations.append(operation)

        return operations



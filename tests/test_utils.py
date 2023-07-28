import main.utils
from main.utils import Operations
from main.utils import get_operations_list
import json
import pytest


@pytest.fixture()
def operations_list():
    with open("tests/filetest.json", encoding='utf-8') as data_testfile:
        operation_list = json.load(data_testfile)
        formatted_list = [item for item in operation_list if item]
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

            assert operation_list == main.utils.operations_list

        return operations


def test_open_operations_list(operations_list):
    assert len(operations_list) > 0
    assert isinstance(operations_list[0], Operations)

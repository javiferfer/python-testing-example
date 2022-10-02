from src.mocking_function.main import calculator


def test_calculator(mocker):
    mocker.patch(
        # sum_operation is from functions.py but imported to main.py
        'src.mocking_function.main.sum_operation',
        return_value=7
    )

    first_no, second_no = 5, 3
    result = calculator(first_no, second_no)
    assert result == 7

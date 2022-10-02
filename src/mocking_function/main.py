from src.mocking_function.functions import sum_operation


def calculator(first_no, second_no):
    result = sum_operation(first_no, second_no)
    return result


if __name__ == "__main__":
    calculator(3, 4)
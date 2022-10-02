from src.mocking_constant.constants import CONSTANT_A


def double():
    return CONSTANT_A * 2


if __name__ == "__main__":
    result = double()
    print(result)

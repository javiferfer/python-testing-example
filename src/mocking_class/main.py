from src.mocking_class.dataset import Dataset


def slow_dataset():
    dataset = Dataset()
    return dataset.load_data()

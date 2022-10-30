from unittest import TestCase, mock

from src.mocking_class.main import slow_dataset


class MockingClassTest(TestCase):

    @mock.patch('src.mocking_class.main.Dataset.load_data')
    def test_mocking_class_method(self, mocker):
        expected = 'xyz'

        def mock_load():
            return 'xyz'

        mocker.return_value = mock_load()
        actual = slow_dataset()
        assert expected == actual

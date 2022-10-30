from unittest import TestCase, mock

from src.mocking_function.main import calculator


class MockingFunctionTest(TestCase):

    @mock.patch('src.mocking_function.main.sum_operation')    
    def test_calculator_(self, mock_response):
        mock_response.return_value = 7
        first_no, second_no = 5, 3
        result = calculator(first_no, second_no)
        assert result == 7
    
        mock_response.return_value = 10
        first_no, second_no = 5, 3
        result = calculator(first_no, second_no)
        assert result == 10

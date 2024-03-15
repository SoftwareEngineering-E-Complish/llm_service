# test_query_generator.py

from unittest.mock import MagicMock
import unittest
from app.model.llm_adapters.i_llm_adapter import ILlmAdapter
from app.model.query_generator import QueryGenerator

class TestQueryGenerator(unittest.TestCase):

    def setUp(self):
        llm = MagicMock()
        llm.query_llm.return_value = 'llm'
        self.query_generator = QueryGenerator(llm)
        
    def test_query_llm(self):
        response = self.query_generator.generate_api_payload('test',{'test':4})
        self.assertEqual(response,'llm')
        
    def test_generate_api_payload_raises_value_error_for_non_string_inputs(self):
        with self.assertRaises(ValueError):
            self.query_generator.generate_api_payload(123, 'test')
        with self.assertRaises(ValueError):
            self.query_generator.generate_api_payload('test', [])

    def test_generate_api_payload_does_not_raise_value_error_for_string_inputs(self):
        try:
            self.query_generator.generate_api_payload('test', {'test':4})
        except ValueError:
            self.fail("generate_api_payload() raised ValueError unexpectedly.")

if __name__ == "__main__":
    unittest.main()
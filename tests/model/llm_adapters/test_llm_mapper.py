import unittest

from app.model.llm_adapters.llm_mapper import LlmMapper
from app.model.llm_adapters.openai_inference_api import OpenAiInference
from app.model.llm_adapters.i_llm_adapter import ILlmAdapter


class TestLlmMapper(unittest.TestCase):

    def test_map_with_valid_model_identifier(self):
        expected_adapter = OpenAiInference()
        adapter = LlmMapper.map('openai')
        self.assertIsInstance(adapter, ILlmAdapter)
        self.assertEqual(type(adapter), type(expected_adapter))

    def test_map_with_invalid_model_identifier_raises_not_implemented_error(self):
        with self.assertRaises(NotImplementedError):
            LlmMapper.map('invalid_model')

if __name__ == "__main__":
    unittest.main()
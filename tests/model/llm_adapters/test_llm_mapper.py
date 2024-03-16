import unittest
from unittest.mock import patch
from app.model.llm_adapters.llm_mapper import LlmMapper
from app.model.llm_adapters.openai_inference_api import OpenAiInference
from app.model.llm_adapters.i_llm_adapter import ILlmAdapter


class TestLlmMapper(unittest.TestCase):

    @patch('app.model.llm_adapters.llm_mapper.OpenAiInference', spec=OpenAiInference)
    def test_map_with_valid_model_identifier(self, _):
        adapter = LlmMapper.map('openai')
        self.assertIsInstance(adapter, ILlmAdapter)

    @patch('app.model.llm_adapters.llm_mapper.OpenAiInference', spec=OpenAiInference)
    def test_map_with_invalid_model_identifier_raises_not_implemented_error(self, _):
        with self.assertRaises(NotImplementedError):
            LlmMapper.map('invalid_model')

if __name__ == "__main__":
    unittest.main()
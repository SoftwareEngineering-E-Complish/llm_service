import unittest
from unittest.mock import MagicMock
from app.model.llm_adapters.openai_inference_api import OpenAiInference

class TestOpenAiInference(unittest.TestCase):

    def setUp(self):
        self.openai_inference = OpenAiInference()
        self.mock_chat_compilation_wrong = MagicMock()
        self.mock_chat_compilation_wrong.chat.completions.create.return_value = 'hiho'
        self.mock_chat_compilation_wrong_arguments = MagicMock()
        self.mock_chat_compilation_wrong_arguments.chat.completions.create.return_value.dict.return_value = {
            'choices': [{'message': {'tool_calls': [{'function': { 'arguments': 'blub' }} ]}}] }
        self.mock_chat_compilation_correct = MagicMock()
        self.mock_chat_compilation_correct.chat.completions.create.return_value.dict.return_value = {
            'choices': [{'message': {'tool_calls': [{'function': { 'arguments': {2:2} }} ]}}] }

    def test_query_llm_invalid_api_documentation_raises(self):
        with self.assertRaises(TypeError):
            self.openai_inference.query_llm('234','234')


    def test_query_llm_invalid_response_raises(self):
        self.openai_inference._OpenAiInference__client = self.mock_chat_compilation_wrong
        with self.assertRaises(RuntimeError):
            self.openai_inference.query_llm('234',{2:3})


    def test_query_llm_invalid_response_not_dict_raises(self):
        self.openai_inference._OpenAiInference__client = self.mock_chat_compilation_wrong_arguments
        with self.assertRaises(TypeError):
            self.openai_inference.query_llm('234',{2:3})


    def test_query_llm_valid(self):
        self.openai_inference._OpenAiInference__client = self.mock_chat_compilation_correct
        result = self.openai_inference.query_llm('234',{2:3})
        self.assertEqual(result,{2:2})
 



if __name__ == "__main__":
    unittest.main()

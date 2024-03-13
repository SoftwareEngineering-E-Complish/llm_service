

from app.model.llm_adapters.llm_mapper import LlmMapper
from app.model.query_generator import QueryGenerator
from app.utils.llm_response_dto import LlmResponseDto
from app.utils.open_api_parser import Parser
from app.config import llm_inference_model

class LlmService:
    def __init__(self):
        self.__llm_adapter = LlmMapper.map(llm_inference_model)
        self.__open_api_parser = Parser()

    def create_query(self, prompt, api_documentation) -> LlmResponseDto:
        query_generator = QueryGenerator(llm_adapter=self.__llm_adapter)
        openai_schema = self.__open_api_parser.get_openai_schema(api_documentation)
        llm_response = query_generator.generate_api_payload(prompt,openai_schema)
        return LlmResponseDto(llm_response)
                                                    




from app.model.llm_adapters.i_llm_adapter import ILlmAdapter
from app.model.llm_adapters.openai_inference_api import OpenAiInference


class LlmMapper:
 
    @staticmethod
    def map(model_identifier: str=None) -> ILlmAdapter: 
        models  = {'openai': OpenAiInference()}
        if not model_identifier in models:
            raise NotImplementedError(f'{model_identifier} not implemented yet')
        return models[model_identifier]
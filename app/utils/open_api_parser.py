import json
from typing import Dict
from app.utils.open_api_field import OpenApiField

class Parser:
    REQUIRED_KEY = "required"
    PARAMETERS_KEY = "parameters"
    REFERENCE_KEY = "$defs"
    PROPERTIES_KEY = "properties"

    def get_openai_schema(self, openapi_shema:dict) -> str:
        properties, required = self.__transform_format(openapi_shema.copy())
        return json.loads("""{
            "type": "function",
            "function": {
                "name": "get_property_filter",
                "description": "Get a filter for real estates or appartments in form of a JSON given the listed attributes parsed from the query",
              "parameters": {
             "type": "object",
            "properties":  """ + json.dumps(properties) + """, "required" : """+ json.dumps(required) + """}}}""")
    
    def __transform_format(self, content: Dict) -> Dict:
        properties: Dict[str,Dict] = content.pop(self.PROPERTIES_KEY)
        references = content.pop(self.REFERENCE_KEY, None)
        required = []
        for property_key, property_value in properties.items():
            field = OpenApiField(property_key, property_value)
            field.replace_anyOf()
            if field.is_required:
                required.append(field.name)
            if field.reference:
                field.replace_reference(references.get(field.reference))
            field.clean()
        return properties, required



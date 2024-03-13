import json
from typing import Dict, Union

class Field:
    ANYOF_KEY = 'anyOf'
    TYPE_KEY = 'type'
    REFERENCE_KEY = '$ref'
    ENUM_KEY = "enum"
    NOT_NEEDED_KEYS = ["default",'title']

    def __init__(self, name: str, schema:dict):
        self.__schema = schema
        self.__name = name
        self.__is_required = False
        self.__reference = None

    @property
    def name(self):
        return self.__name
    
    @property 
    def is_required(self) -> bool:
        return self.__is_required
    
    @property 
    def reference(self) -> Union[str, None]:
        return self.__reference

    def replace_anyOf(self) -> None:
        if self.__hasAnyOf():
            field_type_description: dict = self.__schema.pop(self.ANYOF_KEY)[0]
            has_reference = self.REFERENCE_KEY in field_type_description
            if has_reference:
                self.__schema[self.TYPE_KEY] = field_type_description[self.REFERENCE_KEY].split("/")[-1]
            else:
                self.__schema[self.TYPE_KEY] = field_type_description[self.TYPE_KEY]
        else:
            has_reference = self.REFERENCE_KEY in self.__schema
            self.__is_required = True
        if has_reference:
            self.__reference = self.__schema[self.TYPE_KEY]

    def replace_reference(self, reference: dict):
        self.__schema[self.TYPE_KEY] = reference[self.TYPE_KEY]
        if self.ENUM_KEY in reference:
            self.__schema[self.ENUM_KEY] = reference[self.ENUM_KEY]

    def clean(self) -> None:
        for key in self.NOT_NEEDED_KEYS:
            print(self.__schema)
            self.__schema.pop(key, None)
            print(self.__schema)

    def __hasAnyOf(self) -> bool:
        return self.ANYOF_KEY in self.__schema


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
        references = content.pop(self.REFERENCE_KEY)
        required = []
        for property_key, property_value in properties.items():
            field = Field(property_key, property_value)
            field.replace_anyOf()
            if field.reference:
                required.append(field.name)
                field.replace_reference(references.get(field.reference))
            field.clean()
        return properties, required



from typing import Union

class OpenApiField:
    ANYOF_KEY = 'anyOf'
    TYPE_KEY = 'type'
    REFERENCE_KEY = '$ref'
    ENUM_KEY = "enum"
    NOT_NEEDED_KEYS = ["default",'title','$ref']

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
            if has_reference:
                self.__schema[self.TYPE_KEY] = self.__schema[self.REFERENCE_KEY].split("/")[-1]
            self.__is_required = True
        if has_reference:
            self.__reference = self.__schema[self.TYPE_KEY]

    def replace_reference(self, reference: dict):
        self.__schema[self.TYPE_KEY] = reference[self.TYPE_KEY]
        if self.ENUM_KEY in reference:
            self.__schema[self.ENUM_KEY] = reference[self.ENUM_KEY]

    def clean(self) -> None:
        for key in self.NOT_NEEDED_KEYS:
            self.__schema.pop(key, None)

    def __hasAnyOf(self) -> bool:
        return self.ANYOF_KEY in self.__schema

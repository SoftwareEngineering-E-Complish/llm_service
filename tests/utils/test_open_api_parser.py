import unittest

from app.utils.open_api_parser import Parser

class TestParser(unittest.TestCase):
    def setUp(self):
        self.parser = Parser()

    def test_get_openai_schema(self):
        schema = {
            "properties": {
                "field1": {"type": "string"},
                "field2": {"anyOf": [{"type": "integer"}]}
            }
        }
        result = self.parser.get_openai_schema(schema)
        self.assertEqual(result["function"]["parameters"]["properties"]["field1"]["type"], "string")
        self.assertEqual(result["function"]["parameters"]["properties"]["field2"]["type"], "integer")
        self.assertEqual(result["function"]["parameters"]["required"], ["field1"])

    def test_get_openai_schema_with_ref(self):
        schema = {"$defs":{"PropertyType2":{"enum":["Apartment","House"],"title":"PropertyType2","type":"string"}},"properties":{"property_type2":{"$ref":"#/$defs/PropertyType2","description":"Type of the property","type":"string"}}}
        result = self.parser.get_openai_schema(schema)
        self.assertEqual(result,{'type': 'function', 'function': {'name': 'get_property_filter', 'description': 'Get a filter for real estates or appartments in form of a JSON given the listed attributes parsed from the query', 'parameters': {'type': 'object', 'properties': {'property_type2': {'description': 'Type of the property', 'type': 'string', 'enum': ['Apartment', 'House']}}, 'required': ['property_type2']}}} )

    def test_get_openai_schema_with_2ref(self):
        schema = {"$defs":{"PropertyType":{"enum":["Apartment","House"],"title":"PropertyType","type":"string"},"PropertyType2":{"enum":["Apartment","House"],"title":"PropertyType2","type":"string"}},"properties":{"property_type":{"anyOf":[{"$ref":"#/$defs/PropertyType"},{"type":"integer"}],"description":"Type of the property","type":"string"},"property_type2":{"$ref":"#/$defs/PropertyType2","description":"Type of the property","type":"string"}}}
        result = self.parser.get_openai_schema(schema)
        self.assertEqual(result,{'type': 'function', 'function': {'name': 'get_property_filter', 'description': 'Get a filter for real estates or appartments in form of a JSON given the listed attributes parsed from the query', 'parameters': {'type': 'object', 'properties': {'property_type': {'description': 'Type of the property', 'type': 'string', 'enum': ['Apartment', 'House']}, 'property_type2': {'description': 'Type of the property', 'type': 'string', 'enum': ['Apartment', 'House']}}, 'required': ['property_type2']}}})



if __name__ == '__main__':
    unittest.main()

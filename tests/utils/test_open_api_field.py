import unittest
from app.utils.open_api_field import OpenApiField


class TestOpenApiField(unittest.TestCase):
    def setUp(self):
        self.field = OpenApiField('test_field', {'type': 'string'})

    def test_name(self):
        self.assertEqual(self.field.name, 'test_field')

    def test_is_required_false(self):
        self.assertEqual(self.field.is_required, False)

    def test_reference(self):
        self.assertEqual(self.field.reference, None)

    def test_replace_anyOf_without_anyOf(self):
        self.field.replace_anyOf()
        self.assertEqual(self.field.is_required, True)

    def test_replace_anyOf_with_anyOf(self):
        self.field = OpenApiField('test_field', {'anyOf': [{'type': 'string'}]})
        self.field.replace_anyOf()
        self.assertEqual(self.field.is_required, False)

    def test_replace_reference(self):
        self.field.replace_reference({'type': 'integer'})
        self.assertEqual(self.field._OpenApiField__schema['type'], 'integer')

    def test_clean(self):
        self.field = OpenApiField('test_field', {'type': 'string', 'default': 'value', 'title': 'Title'})
        self.field.clean()
        self.assertNotIn('default', self.field._OpenApiField__schema)
        self.assertNotIn('title', self.field._OpenApiField__schema)

if __name__ == '__main__':
    unittest.main()

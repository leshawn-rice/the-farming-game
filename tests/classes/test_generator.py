from unittest import TestCase
from classes.generator import Generator


class GeneratorTestCase(TestCase):
    def test_generate_id(self):
        '''
        works: generate an id of size 12
        '''
        id = Generator.generateId(12, [])
        self.assertIsInstance(id, str)
        self.assertEqual(len(id), 12)

    def test_generate_id_invalid_length(self):
        id = Generator.generateId(None, [])
        self.assertIsNone(id)

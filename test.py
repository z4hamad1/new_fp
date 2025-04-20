import unittest
from unittest.mock import patch, MagicMock
from cat_fact_processor import CatFactProcessor


class TestCatFactProcessor(unittest.TestCase):

    @patch('requests.get')
    def test_get_fact_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = {"fact": "Cats are awesome!"}
        mock_get.return_value = mock_response
        
        processor = CatFactProcessor()
        fact = processor.get_fact()
        
        self.assertEqual(fact, "Cats are awesome!")
        self.assertIn(fact, processor.facts)


    def test_get_fact_length_empty(self):
        processor = CatFactProcessor()
        length = processor.get_fact_length()
        stats = processor.get_stats()

        self.assertEqual(length, 0)
        self.assertEqual(stats, {"average": 0, "min": 0, "max": 0})


    @patch('requests.get')
    def test_get_fact_length_with_facts(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = {"fact": "Cats are awesome!"}
        mock_get.return_value = mock_response
        
        processor = CatFactProcessor()
        processor.get_fact()
        length = processor.get_fact_length()

        self.assertEqual(length, len("Cats are awesome!"))


    @patch('requests.get')
    def test_get_stats_with_facts(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = {"fact": "Cats are awesome!"}
        mock_get.return_value = mock_response
        
        processor = CatFactProcessor(num_facts=3)
        processor.get_fact()  
        processor.get_fact() 
        
        stats = processor.get_stats()
        lengths = [len("Cats are awesome!")] * 2  
        self.assertEqual(stats["average"], sum(lengths) / len(lengths))
        self.assertEqual(stats["min"], min(lengths))
        self.assertEqual(stats["max"], max(lengths))


@patch('requests.get')        
def test_get_fact_length_with_facts(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = {"fact": "Cats are awesome!"}
        mock_get.return_value = mock_response
        
        processor = CatFactProcessor()
        processor.get_fact() 
        length = processor.get_fact_length()
        self.assertEqual(length, len("Cats are awesome!"))


if __name__ == '__main__':
    unittest.main()
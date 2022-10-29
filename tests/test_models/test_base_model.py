import unittest
from models import base_model

"""Base Model Unittest Module."""

class TestBaseModel(unittest.TestCase):
    """Represent the test model for Base Model."""

    def setUp(self):
        self.b1 = base_model.BaseModel()
        self.b2 = base_model.BaseModel()
        self.objs_dict = self.b1.to_dict()
        self.created_at = self.objs_dict['created_at']
        self.updated_at = self.objs_dict['updated_at']

    def test_id(self):
        """Test if id is unique."""
        self.assertNotEqual(self.b1.id, self.b2.id)

    def test_dict_created_at(self):
        """Test if created_at is a str."""
        self.assertIsInstance(self.created_at, str)
    
    def test_dict_updated_at(self):
        """Test if updated_at is a str."""
        self.assertIsInstance(self.updated_at, str)

    def test_to_dict(self):
        """Test if to_dict return a dict."""
        self.assertIsInstance(self.objs_dict, dict)

    def test_class_name(self):
        """Test if __class__ is in dict return by to_dict."""
        self.assertIn("__class__", self.objs_dict.keys())

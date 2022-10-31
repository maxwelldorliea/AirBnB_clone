#!/usr/bin/python3

"""This is the Amenity Module."""
from models import BaseModel
from models.amenity import Amenity
import unittest



class TestAmenity(unittest.TestCase):
    """Implement unittest for Amenity."""

    def setUp(self) -> None:
        """Set up Amenity unittest."""
        self.a1 = Amenity()

    def test_name(self):
        """Test if  Amenity has attribute name."""
        self.assertTrue(hasattr(self.a1, 'name'))

    def test_name_empty(self):
        """Test attribute name is empty."""
        self.assertEqual(self.a1.name, '')

    def test_issubclass_base_model(self):
        """Test if Amenity is subclass of BaseModel."""
        self.assertIsInstance(self.a1, BaseModel)

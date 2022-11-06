#!/usr/bin/python3

"""This is the File Storage Unittest Module."""


from models import FileStorage
from models import BaseModel
import unittest


class TestFileStorage(unittest.TestCase):
    """Implement unittest for FileStorage model."""

    def setUp(self) -> None:
        """Set up FileStorage unittest."""
        self.storage = FileStorage()
        self.base = BaseModel()
        self.storage.new(self.base)

    def test_all(self):
        """Test if the all method return dict."""
        self.assertIsInstance(self.storage.all(), dict)

    def test_new(self):
        """Test if the new method adds new object to __objects."""
        self.assertIsNotNone(self.storage.all())01~

"""Tests for pwnmothership."""

import unittest
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TestPwnmothership(unittest.TestCase):
    """Test cases for pwnmothership."""

    def test_main_go_exists(self):
        """Test that main.go exists."""
        main_go = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "main.go")
        self.assertTrue(os.path.exists(main_go), "main.go should exist")

    def test_go_mod_exists(self):
        """Test that go.mod exists."""
        go_mod = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "go.mod")
        self.assertTrue(os.path.exists(go_mod), "go.mod should exist")

    def test_python_file_exists(self):
        """Test that pwnmothership.py exists."""
        py_file = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "pwnmothership.py")
        self.assertTrue(os.path.exists(py_file), "pwnmothership.py should exist")

    def test_public_dir_exists(self):
        """Test that public directory exists."""
        public_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "public")
        self.assertTrue(os.path.isdir(public_dir), "public/ directory should exist")

    def test_requirements_exists(self):
        """Test that requirements.txt exists."""
        req = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "requirements.txt")
        self.assertTrue(os.path.exists(req), "requirements.txt should exist")


if __name__ == "__main__":
    unittest.main()

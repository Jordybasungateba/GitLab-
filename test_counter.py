from unittest import TestCase
import status
from counter import app


class CounterTest(TestCase):
    """Test the Counter class."""

    def setUp(self):
        self.client = app.test_client()

    def test_create_a_counter(self):
        """Test that a counter can be created."""
        result = self.client.post("counter/foo")
        self.assertEqual(result.status_code, status.HTTP_201_CREATED)

    # def test_duplicate_counter(self):
    #     """Test duplicate counter creation returns 409."""
    #     result = self.client.post("counter/bar")
    #     self.assertEqual(result.status_code, status.HTTP_201_CREATED)
    #     result = self.client.post("counter/bar")
    #     self.assertEqual(result.status_code, status.HTTP_409_CONFLICT)

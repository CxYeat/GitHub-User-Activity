# tests/test_github_api.py
import unittest
from unittest.mock import patch, MagicMock
from github_activity.github_api import GitHubActivity

class TestGitHubActivity(unittest.TestCase):

    def setUp(self):
        self.client = GitHubActivity("cxyeat")

    @patch("http.client.HTTPSConnection")
    def test_get_user_events_success(self, mock_https):
        mock_response = MagicMock()
        mock_response.status = 200
        mock_response.read.return_value = b'[{"type": "PushEvent", "repo": {"name": "repo"}, "payload": {"size": 1}, "created_at": "2025-07-13T10:00:00Z"}]'
        mock_https.return_value.getresponse.return_value = mock_response

        events = self.client.get_user_events()
        self.assertEqual(len(events), 1)
        self.assertEqual(events[0]["type"], "PushEvent")

    def test_format_date_valid(self):
        formatted = self.client.format_date("2025-07-13T10:00:00Z")
        self.assertEqual(formatted, "13.07.2025 10:00")

    def test_format_date_invalid(self):
        # invalid string should fallback and return original
        formatted = self.client.format_date("invalid-date")
        self.assertEqual(formatted, "invalid-date")

if __name__ == '__main__':
    unittest.main()

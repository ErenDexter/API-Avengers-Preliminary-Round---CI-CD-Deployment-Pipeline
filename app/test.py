import unittest

try:
	from app.main import index, health
except ModuleNotFoundError:
	from main import index, health


class TestAppHandlers(unittest.TestCase):
	def test_index_returns_plain_text_hello(self):
		resp = index()
		self.assertEqual(resp.status_code, 200)
		self.assertEqual(resp.media_type, "text/plain")
		self.assertEqual(resp.body, b"Hello, World!")

	def test_health_returns_ok_json_type(self):
		resp = health()
		self.assertEqual(resp.status_code, 200)
		self.assertEqual(resp.media_type, "application/json")
		self.assertEqual(resp.body, b"Ok")


if __name__ == "__main__":
	unittest.main()


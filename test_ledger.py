import unittest
from ledger import reconcile
class T(unittest.TestCase):
    def test_simple(self):
        r = reconcile([{"id": 1, "amount": 5, "memo": "a"}, {"id": 2, "amount": -5, "memo": "b"}])
        self.assertTrue(r["ok"])
if __name__ == "__main__":
    unittest.main()

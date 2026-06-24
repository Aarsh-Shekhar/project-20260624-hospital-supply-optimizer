import unittest

from hospital_supply_optimizer.models import Record
from hospital_supply_optimizer.scoring import score_record


class DepthCheck29(unittest.TestCase):
    def test_029_reporting_view(self):
        record = Record(id="item-029", exposure=86472, signal=0.449, urgency=1)
        self.assertGreaterEqual(score_record(record), 0)
        self.assertLessEqual(score_record(record), 1)


if __name__ == "__main__":
    unittest.main()

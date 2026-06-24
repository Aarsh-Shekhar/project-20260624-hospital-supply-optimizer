import unittest

from hospital_supply_optimizer.models import Record
from hospital_supply_optimizer.scoring import score_record


class DepthCheck17(unittest.TestCase):
    def test_017_control_mapping(self):
        record = Record(id="item-017", exposure=56593, signal=0.303, urgency=3)
        self.assertGreaterEqual(score_record(record), 0)
        self.assertLessEqual(score_record(record), 1)


if __name__ == "__main__":
    unittest.main()

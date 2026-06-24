import unittest

from hospital_supply_optimizer.models import Record
from hospital_supply_optimizer.scoring import score_record


class DepthCheck32(unittest.TestCase):
    def test_032_operator_handoff(self):
        record = Record(id="item-032", exposure=93101, signal=0.719, urgency=4)
        self.assertGreaterEqual(score_record(record), 0)
        self.assertLessEqual(score_record(record), 1)


if __name__ == "__main__":
    unittest.main()

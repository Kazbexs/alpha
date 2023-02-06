import unittest
import reader
import alpha
import pm4py
from tests.sample_log import log


class TestReader(unittest.TestCase):

    def test_read_data(self):
        test_log = pm4py.read_xes('/Users/kazbexs/Documents/Project/kazbexs/flask-server/tests/L1.xes')
        self.assertEquals(reader.read_data(log), test_log)
        
    def test_find_Tl(self):
        test_log = pm4py.read_xes('/Users/kazbexs/Documents/Project/kazbexs/flask-server/tests/L1.xes')
        activities = set(pm4py.get_attribute_values(test_log))
        self.assertCountEqual(alpha.find_Tl(log), activities)
        
    def test_find_Ti(self):
        test_log = pm4py.read_xes('/Users/kazbexs/Documents/Project/kazbexs/flask-server/tests/L1.xes')
        start_activities = set(pm4py.get_start_activities(test_log))
        self.assertCountEqual(alpha.find_Ti(log), start_activities)
        
    def test_find_To(self):
        test_log = pm4py.read_xes('/Users/kazbexs/Documents/Project/kazbexs/flask-server/tests/L1.xes')
        end_activities = set(pm4py.get_end_activities(test_log))
        self.assertCountEqual(alpha.find_To(log), end_activities)
        
    if __name__ == '__main__':
        unittest.main()




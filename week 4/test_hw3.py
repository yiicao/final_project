import unittest
from hw3 import PurpleDiversitySeekers, GoldDiversitySeekers, PurpleAgents, GoldAgents
from unittest.mock import patch
import random

class Test_AgentBehaviors(unittest.TestCase):
    #mock_show.return_value = None
    def test_PurpleDS(self):
        print("running test")
        random.seed(72)
        testPDSlist = [PurpleDiversitySeekers(random.randint(0,11), random.randint(0,11)) for x in range(6)] + [GoldDiversitySeekers(random.randint(0,1), random.randint(0,1)) for x in range(6)]
        for agent in testPDSlist:
            agent.check_neighbors(testPDSlist)
        self.assertTrue(testPDSlist[0].status=="happy")
    def test_PurpleDS2(self):
        print("running test")
        random.seed(72)
        testPDSlist = [PurpleDiversitySeekers(random.randint(0,11), random.randint(0,11)) for x in range(6)] + [GoldDiversitySeekers(random.randint(0,1), random.randint(0,1)) for x in range(6)]
        for agent in testPDSlist:
            agent.check_neighbors(testPDSlist)
        self.assertTrue(testPDSlist[11].status=="unhappy")
        
    def test_PurpleDS3(self):
        print("running test")
        random.seed(72)
        testPDSlist = [PurpleDiversitySeekers(random.randint(0,11), random.randint(0,11)) for x in range(6)] + [GoldDiversitySeekers(random.randint(0,1), random.randint(0,1)) for x in range(6)]
        for agent in testPDSlist:
            agent.check_neighbors(testPDSlist)
        for agent in testPDSlist:
            agent.move_if_unhappy()
        for agent in testPDSlist:
            agent.check_neighbors(testPDSlist)
        self.assertTrue(testPDSlist[0].status=="unhappy")

    def test_PurpleDS4(self):
        print("running test")
        random.seed(72)
        testPDSlist = [PurpleDiversitySeekers(random.randint(0,11), random.randint(0,11)) for x in range(6)] + [GoldDiversitySeekers(random.randint(0,1), random.randint(0,1)) for x in range(6)]
        for agent in testPDSlist:
            agent.check_neighbors(testPDSlist)
        for agent in testPDSlist:
            agent.move_if_unhappy()
        for agent in testPDSlist:
            agent.check_neighbors(testPDSlist)
        self.assertTrue(testPDSlist[11].x==38)
    
    def test_PurpleDS5(self):
        print("running test")
        random.seed(72)
        testPDSlist = [PurpleAgents(random.randint(0,11), random.randint(0,11)) for x in range(6)] + [GoldAgents(random.randint(0,1), random.randint(0,1)) for x in range(6)]
        for agent in testPDSlist:
            agent.check_neighbors(testPDSlist)
        self.assertTrue(testPDSlist[11].status=="happy")

    def test_PurpleDS6(self):
        print("running test")
        random.seed(72)
        testPDSlist = [PurpleAgents(random.randint(0,11), random.randint(0,11)) for x in range(6)] + [GoldAgents(random.randint(0,1), random.randint(0,1)) for x in range(6)]
        for agent in testPDSlist:
            agent.check_neighbors(testPDSlist)
        self.assertTrue(testPDSlist[0].status=="unhappy")
    
    def test_PurpleDS6_1(self):
        print("running test")
        random.seed(72)
        testPDSlist = [PurpleAgents(random.randint(0,11), random.randint(0,11)) for x in range(6)] + [GoldAgents(random.randint(0,1), random.randint(0,1)) for x in range(6)]
        for agent in testPDSlist:
            agent.check_neighbors(testPDSlist)
        self.assertTrue(testPDSlist[11].status=="happy")

    def test_PurpleDS7(self):
        print("running test")
        random.seed(72)
        testPDSlist = [PurpleAgents(random.randint(0,11), random.randint(0,11)) for x in range(6)] + [GoldAgents(random.randint(0,1), random.randint(0,1)) for x in range(6)]
        for agent in testPDSlist:
            agent.check_neighbors(testPDSlist)
        for agent in testPDSlist:
            agent.move_if_unhappy()
        for agent in testPDSlist:
            agent.check_neighbors(testPDSlist)
        self.assertTrue(testPDSlist[0].status=="happy")

if __name__ == '__main__':
    unittest.main()


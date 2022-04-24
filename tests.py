import unittest
from datetime import datetime
from capital_gains import Trade, Security

class TestTrade(unittest.TestCase):
    def setUp(self):
        self.today = datetime.now().strftime("%Y-%m-%d")
        self.security = 'NAME'
        self.quant = 10
        self.price = 150.99
        self.fee = 10.99
        self.trade = Trade(self.today, self.security, self.quant, self.price, self.fee)

    # test Trade object instantiation
    def test_trade_create(self):
        self.assertIsNotNone(self.trade)

    # test date assignment
    def test_date_assign(self):
        today_date = datetime.strptime(self.today, "%Y-%m-%d").date()
        self.assertEqual(today_date, self.trade.date)

    # test security assignment
    def test_name_assign(self):
        self.assertEqual(self.trade.security, self.security)

    # test quantity assignment
    def test_quantity_assign(self):
        self.assertEqual(self.quant, self.trade.quantity)
    
    #test price assignment
    def test_price_assign(self):
        self.assertEqual(self.price, self.trade.price)

    #test price assignment
    def test_price_assign(self):
        self.assertEqual(self.fee, self.trade.fee)

class TestSecurity(unittest.TestCase):
    def setUp(self):
        self.today = datetime.now().strftime("%Y-%m-%d")
        self.trade1 = Trade(self.today, 'AAPL', 10, 150.99, 10.99)
        self.trade2 = Trade(self.today, 'AAPL', -10, 120.25, 10.99)
        self.security = Security('AAPL')

    def test_security_create(self):
        self.assertIsNotNone(self.security)
        self.assertEqual(self.security.id, 'AAPL')

    def test_add_trades(self):
        self.security.add_trade(self.trade1)
        self.assertEqual(len(self.security.trades), 1)
        self.assertEqual(self.security.acb, self.trade1.price+self.trade1.fee) 
        self.assertEqual(self.security.balance, self.trade1.quantity)
        self.assertEqual(self.security.acb_per_share, self.security.acb/self.security.balance)

        self.security.add_trade(self.trade2)
        self.assertEqual(len(self.security.trades), 2)
        self.assertEqual(self.security.acb, 0)
        self.assertEqual(self.security.balance, 0)
        self.assertEqual(self.security.acb_per_share, 0)

    def test_ordering(self):
        security2 = Security("AMD")
        self.assertLess(self.security, security2)
        self.assertNotEqual(security2, self.security)

if __name__ == '__main__':
    unittest.main()
    
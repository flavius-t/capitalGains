import unittest
from datetime import datetime
from capital_gains import Trade

class TestTrade(unittest.TestCase):
    def setUp(self):
        self.today = datetime.now().strftime("%Y-%m-%d")
        self.security = 'NAME'
        self.quant = 10
        self.price = 150.99
        self.trade = Trade(self.today, self.security, self.quant, self.price)

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

if __name__ == '__main__':
    unittest.main()
    
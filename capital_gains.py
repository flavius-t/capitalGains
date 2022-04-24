from functools import total_ordering
from nltk.tokenize import word_tokenize
from datetime import datetime

class Trade:
    def __init__(self, date, security, quantity, price, fee):
        # date must be in ISO 8601 format: YYYY-mm-dd
        self.date = datetime.strptime(date, "%Y-%m-%d").date()
        self.security = security
        self.quantity = quantity
        self.price = price
        self.fee = fee

    def __str__(self):
        return f'{self.date} {self.security} {self.quantity} ${self.price}'
    
    def get_date(self):
        return self.date
    
    def get_security(self):
        return self.security
    
    def get_quantity(self):
        return self.quantity

    def get_price(self):
        return self.price

@total_ordering
class Security:
    def __init__(self, id):
        self.id = id
        self.trades = []
        self.acb = 0
        self.balance = 0
        self.acb_per_share = 0

    def __str__(self):
        return f'''{self.id}\n Number Trades: {len(self.trades)} Remaining Balance: {self.balance}
        ACB: {self.acb}'''

    def __eq__(self, other):
        return self.id == other.id
    
    def __lt__(self, other):
        return self.id < other.id

    def update_acb(self, trade):
        assert(trade.quantity != 0)
        # opening transaction
        if trade.quantity > 0:
            self.acb += trade.price + trade.fee
            self.balance += trade.quantity
            self.acb_per_share = self.acb / self.balance
        # closing transaction
        else:
            self.acb -= self.acb_per_share * trade.quantity
            self.balance += trade.quantity
            if self.balance == 0:
                self.acb = 0
                self.acb_per_share = 0
        
    def add_trade(self, trade):
        self.trades.append(trade)
        self.update_acb(trade)

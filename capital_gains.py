from nltk.tokenize import word_tokenize
from datetime import datetime

class Trade:
    def __init__(self, date, security, quantity, price):
        # date must be in ISO 8601 format: YYYY-mm-dd
        self.date = datetime.strptime(date, "%Y-%m-%d").date()
        self.security = security
        self.quantity = quantity
        self.price = price

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

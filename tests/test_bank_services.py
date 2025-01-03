import pytest
from unittest.mock import patch, MagicMock

from tests.mysqltrail import DBConnection
from pratice import email_check

db= DBConnection()
# def test_withdraw():
def test_email():
    assert email_check("name@yash.com")
    assert not email_check("@yash.com")
    assert not email_check("ww@")
    assert not email_check("ww@gg")

class TestBanking:

    def setup_method(self, method):
        self.db= DBConnection()

    # withdraw test cases
    def test_withdraw(self):
        assert db.withdraw(1005, 10)
        assert not db.withdraw(10, 100), "Invalid account_no"
        assert not db.withdraw(1004, 10000), "Exceeds Transaction Limit"
        assert not db.withdraw(1004, 2000), "Amount greater than balance"

    #deposit test cases
    def test_deposit(self):
        assert db.deposit(1005, 100)
        assert not db.deposit(10, 100)

    # trasfer test case
    @patch('builtins.input', side_effect=['1001','200'])
    def test_transfer(self, mock_input):
        result = self.db.transfer_money('1000')
        assert result


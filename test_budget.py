from budget import Budget

def test_budget():
    testObject = Budget(500)
    assert testObject.balance == 500

def test_deposit():
    testObject = Budget(500)
    testObject.deposit(100)
    assert testObject.balance == 600





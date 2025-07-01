# Aim: Create a Python class named Transaction with attributes for sender, receiver, and amount. Implement a method within the class to transfer money from the sender's account to the receiver's account. 
# Simulate user accounts with balances 
accounts = { 
    "Alice": 500, 
    "Bob": 300, 
    "Charlie": 200 
} 
 
# Transaction class definition 
class Transaction: 
    def __init__(self, sender, receiver, amount): 
        self.sender = sender 
        self.receiver = receiver 
        self.amount = amount 
 
    def transfer(self): 
        # Check if users exist 
        if self.sender not in accounts or self.receiver not in accounts: 
            print("  Either sender or receiver account doesn't exist.") 
            return 
 
        # Check for sufficient funds 
        if accounts[self.sender] < self.amount: 
            print(f"  Insufficient funds in {self.sender}'s account.") 
            return 
 
        # Perform transfer 
        accounts[self.sender] -= self.amount 
        accounts[self.receiver] += self.amount 
        print(f"   {self.amount} transferred from {self.sender} to {self.receiver}.") 
 
# Example usage 
print("   Initial account balances:", accounts)
 
# Create transactions 
t1 = Transaction("Alice", "Bob", 100) 
t1.transfer() 
 
t2 = Transaction("Bob", "Charlie", 50) 
t2.transfer() 
 
t3 = Transaction("Charlie", "Alice", 300)  # This should fail due to insufficient funds 
t3.transfer() 
 
print("\n     Final account balances:", accounts) 

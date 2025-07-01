# Aim: Allow users to create multiple transactions and display them in an organised format. 
import pandas as pd 
 
transactions = [] 
 
def create_transaction(sender, receiver, amount, description=""): 
    transaction = { 
        "Sender": sender, 
        "Receiver": receiver, 
        "Amount": amount, 
        "Description": description 
    } 
    transactions.append(transaction) 
    print("   Transaction recorded successfully!") 
 
 
def display_transactions(): 
    if transactions: 
        df = pd.DataFrame(transactions) 
        print("\n     All Transactions:") 
        print(df) 
    else: 
        print("    No transactions found.") 
 
# Example usage 
create_transaction("Alice", "Bob", 150, "Payment for services") 
create_transaction("Bob", "Charlie", 75, "Dinner split") 
create_transaction("Charlie", "Alice", 25, "Coffee refund") 
 
# Display all transactions 
display_transactions() 

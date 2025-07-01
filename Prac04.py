#Aim: Implement a function to add new blocks to the miner and dump the blockchain. 
 
import hashlib 
import time 
import json 
 
# Block class 
class Block: 
    def __init__(self, index, previous_hash, timestamp, data, nonce=0): 
        self.index = index 
        self.previous_hash = previous_hash 
        self.timestamp = timestamp 
        self.data = data 
        self.nonce = nonce 
        self.hash = self.calculate_hash() 
 
    def calculate_hash(self): 
        block_string = 
f"{self.index}{self.previous_hash}{self.timestamp}{json.dumps(self.data)}{self.nonce}" 
        return hashlib.sha256(block_string.encode()).hexdigest() 
 
# Blockchain class 
class Blockchain: 
    def __init__(self): 
        self.chain = [self.create_genesis_block()] 
        self.difficulty = 4  # Number of leading zeros in the hash 
 
    def create_genesis_block(self): 
        return Block(0, "0", time.time(), "Genesis Block") 
 
    def get_latest_block(self): 
        return self.chain[-1] 
 
    def mine_block(self, data): 
        previous_block = self.get_latest_block() 
        index = previous_block.index + 1 
        timestamp = time.time() 
        nonce = 0 
 
        print(f"    Mining block #{index}...")
       new_block = Block(index, previous_block.hash, timestamp, data, nonce) 
        while not new_block.hash.startswith('0' * self.difficulty): 
            new_block.nonce += 1 
            new_block.hash = new_block.calculate_hash() 
 
        self.chain.append(new_block) 
        print(f"   Block #{index} mined: {new_block.hash}") 
 
    def dump_chain(self): 
        print("\n       Blockchain Dump:") 
        for block in self.chain: 
            print({ 
                'Index': block.index, 
                'Previous Hash': block.previous_hash, 
                'Timestamp': time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(block.timestamp)), 
                'Data': block.data, 
                'Nonce': block.nonce, 
                'Hash': block.hash 
            }) 
 
# Create the blockchain 
my_blockchain = Blockchain() 
 
# Add (mine) blocks 
my_blockchain.mine_block({"sender": "Alice", "receiver": "Bob", "amount": 50}) 
my_blockchain.mine_block({"sender": "Bob", "receiver": "Charlie", "amount": 25}) 
my_blockchain.mine_block({"sender": "Charlie", "receiver": "Alice", "amount": 10}) 
 
# Dump the entire blockchain 
my_blockchain.dump_chain()

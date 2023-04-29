import hashlib
import json
import time

class Block:
    def __init__(self, data, previous_hash):
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.compute_hash()

    def compute_hash(self):
        data_string = json.dumps(self.data, sort_keys=True)
        hash_string = str(self.timestamp) + data_string + self.previous_hash
        return hashlib.sha256(hash_string.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [Block({}, "0")]

    def add_block(self, data):
        previous_hash = self.chain[-1].hash
        block = Block(data, previous_hash)
        self.chain.append(block)

    def validate(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]

            if current_block.previous_hash != previous_block.hash:
                return False

            if current_block.hash != current_block.compute_hash():
                return False

        return True

if __name__ == '__main__':
    blockchain = Blockchain()

    data1 = {
        "name": "Olaoluwasubomi Joshua Aduloju",
        "age": 20,
        "dob": "13/08/2004",
        "ssn": "123-45-6789"
    }
    blockchain.add_block(data1)

    data2 = {
        "name": "Jane Smith",
        "age": 28,
        "dob": "02/14/1994",
        "ssn": "987-65-4321"
    }
    blockchain.add_block(data2)

    print("Blockchain is valid:", blockchain.validate())
    print("Blockchain:", json.dumps([block.__dict__ for block in blockchain.chain], indent=4))

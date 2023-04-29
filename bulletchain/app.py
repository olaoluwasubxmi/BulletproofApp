from flask import Flask, render_template, request, jsonify
import hashlib
import json

app = Flask(__name__)

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block = json.dumps(self.__dict__, sort_keys=True).encode()
        return hashlib.sha256(block).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, "01/01/2021", "Genesis Block", "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

    def block_exists(self, block_hash):
        for block in self.chain:
            if block.hash == block_hash:
                return True
        return False

    def get_block_data(self, block_hash):
        for block in self.chain:
            if block.hash == block_hash:
                return {
                    "index": block.index,
                    "timestamp": block.timestamp,
                    "data": block.data
                }
        return None

app = Flask(__name__)
blockchain = Blockchain()

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    first_name = request.form['first_name']
    middle_initial = request.form['middle_initial']
    last_name = request.form['last_name']
    phone_number = request.form['phone_number']
    address = request.form['address']
    zip_code = request.form['zip_code']
    email = request.form['email']

    # Combine all information into a single string
    info_str = f"{first_name}{middle_initial}{last_name}{phone_number}{address}{zip_code}{email}"

    # Generate hash key using SHA256 algorithm
    hash_key = hashlib.sha256(info_str.encode()).hexdigest()[:28]

    # Save hash to file
    with open('hashes.txt', 'a') as f:
        f.write(f"{hash_key}\n")

    return f"Your information has been hashed with the following key: {hash_key}"


if __name__ == '__main__':
    app.run(debug=True)

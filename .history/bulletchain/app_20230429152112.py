from flask import Flask, render_template, request
import hashlib
import binascii

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/submit', methods=['POST'])
def submit():
    first_name = request.form['first_name']
    middle_initial = request.form['middle_initial']
    last_name = request.form['last_name']
    phone_number = request.form['phone_number']
    address = request.form['address']
    zip_code = request.form['zip_code']
    email = request.form['email']

    info_str = f"{first_name}{middle_initial}{last_name}{phone_number}{address}{zip_code}{email}"
    salt = b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f'
    hash_key = hashlib.scrypt(info_str.encode(), salt=salt, n=16384, r=8, p=1, dklen=64)
    hex_hash_key = binascii.hexlify(hash_key).decode()

    with open('hashes.txt', 'a') as f:
        f.write(f"{hex_hash_key},{info_str}\n")

    return f"Your information has been hashed with the following key: {hex_hash_key}"

@app.route('/search_hash', methods=['POST'])
def search_hash():
    hash_key = request.form['hash_key']

    with open('hashes.txt', 'r') as f:
        for line in f.readlines():
            saved_hash_key, saved_info = line.strip().split(',', 1)
            if saved_hash_key == hash_key:
                return f"The information for the provided hash key ({hash_key}) is: {saved_info}"

    return f"No information was found for the provided hash key: {hash_key}"

if __name__ == '__main__':
    app.run(debug=True)

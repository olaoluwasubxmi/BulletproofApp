from flask import Flask, render_template, request
import hashlib
import binascii

app = Flask(__name__)

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

    # Generate hash key using the scrypt hashing algorithm
    salt = b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f'
    hash_key = hashlib.scrypt(info_str.encode(), salt=salt, n=16384, r=8, p=1, dklen=64)
    hex_hash_key = binascii.hexlify(hash_key).decode()

    return f"Your information has been hashed with the following key: {hex_hash_key}"

if __name__ == '__main__':
    app.run(debug=True)

import hashlib

def get_input_data(hash_key):
    # Read the hashes from the file
    with open('hashes.txt', 'r') as f:
        hashes = f.read().splitlines()

    # Check if the hash exists in the file
    if hash_key in hashes:
        # Find the line that matches the hash
        with open('hashes.txt', 'r') as f:
            for line in f:
                if hash_key in line:
                    # Extract the input data from the line
                    input_str = line.rstrip('\n').replace(hash_key, '')
                    # Split the input data into its components
                    first_name = input_str[:10].strip()
                    middle_initial = input_str[10:11].strip()
                    last_name = input_str[11:21].strip()
                    phone_number = input_str[21:31].strip()
                    address = input_str[31:61].strip()
                    zip_code = input_str[61:66].strip()
                    email = input_str[66:].strip()
                    # Return a dictionary of the input data
                    return {
                        "first_name": first_name,
                        "middle_initial": middle_initial,
                        "last_name": last_name,
                        "phone_number": phone_number,
                        "address": address,
                        "zip_code": zip_code,
                        "email": email
                    }

    # If the hash is not found, return None
    return None

# Example usage
hash_key = '8b714dab1b053ecaaee672beaa68'
input_data = get_input_data(hash_key)
if input_data:
    print(f"The following information matches the hash {hash_key}:")
    for key, value in input_data.items():
        print(f"{key}: {value}")
else:
    print(f"No matching information found for hash {hash_key}")

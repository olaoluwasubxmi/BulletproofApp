import hashlib
import time

max_nonce = 2 ** 32  # maximum value for nonce (4 billion)

def proof_of_work(block, difficulty):
    """Perform proof of work on a given block with a given difficulty"""
    target = 2 ** (256 - difficulty)  # target value for the hash
    for nonce in range(max_nonce):
        data = block + str(nonce)
        hash_value = hashlib.sha256(data.encode()).hexdigest()
        if int(hash_value, 16) < target:
            return nonce, hash_value  # return the nonce and hash value
    return None, None  # proof of work not found

# Example usage:
block = "Olaoluwasubomi Aduloju"
difficulty = 20
start_time = time.time()
nonce, hash_value = proof_of_work(block, difficulty)
end_time = time.time()

if nonce is not None:
    print("Proof of work found!")
    print(f"Nonce: {nonce}")
    print(f"Hash value: {hash_value}")
    print(f"Time taken: {end_time - start_time:.3f} seconds")
else:
    print("Proof of work not found.")

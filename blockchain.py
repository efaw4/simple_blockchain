from hashlib import sha256
from datetime import datetime

chain = []

source_adress = "a"


def _hash(data):
    
    return sha256(data.encode()).hexdigest() # SHA256 hash raw block and return result in hexidecimal


def get_time():

    return datetime.today().strftime('%Y-%m-%d %H:%M:%S')


def genesis_block():


    data = f"0 {get_time()}"

    h = _hash(data)

    chain.append(h)


def create_block(transaction):

    current_block_n = len(chain) + 1 # Get current block number

    data = f"{last_block()} {get_time()} {transaction}" # Combine informations for new block

    h = _hash(data)

    chain.append(h)

    return current_block_n


def last_block():

    return chain[-1]








genesis_block()

print(f"block number : 1")

print(f"Genesis block hash : {chain[0]}")


while True:

    _input = input("> ")

    payload = _input.split(" ")

    payload.insert(0, source_adress) # Append source adress at first element

    block_n = create_block(payload)

    print(f"block number : {block_n}")

    print(f"source, data, destination : {payload}")

    print(chain)

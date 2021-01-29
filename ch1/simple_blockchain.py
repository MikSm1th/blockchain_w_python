import hashlib
import json

class Block:
    id = None
    history = None
    parent_id = None
    parent_hash = None

block_A = Block()
block_A.id = 1
block_A.history = 'Nelson likes cat'

block_B = Block()
block_B.id = 2
block_B.history = 'Marie likes dog'
block_B.parent_id = block_A.id
block_B.parent_hash = hashlib.sha256(json.dumps(block_A.__dict__).encode('utf-8')).hexdigest()

block_C = Block()
block_C.id = 3
block_C.history = 'Marie likes dog'
block_C.parent_id = block_B.id
block_C.parent_hash = hashlib.sha256(json.dumps(block_B.__dict__).encode('utf-8')).hexdigest()

block_D = Block()
block_D.id = 4
block_D.history = 'Sky loves turtle'
block_D.parent_id = block_C.id



if __name__ == '__main__':
    block_serialized = json.dumps(block_D.__dict__).encode('utf-8')
    print(block_serialized)
    payload = b'{"history": "Sky loves turtle", "parent_id": 3, "id": 4}'
    for i in range(1000000):
        nonce = str(i).encode('utf-8')
        result = hashlib.sha256(payload + nonce).hexdigest()
        if result[0:5] == '00000':
            print(i)
            print(result)
            break

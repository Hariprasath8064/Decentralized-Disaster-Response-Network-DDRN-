import hashlib

class Block:
    def __init__(self, index, previous_hash, data):
        self.index = index
        self.previous_hash = previous_hash
        self.data = data
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        return hashlib.sha256(f'{self.index}{self.previous_hash}{self.data}'.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, "0", "Genesis Block")

    def add_block(self, data):
        previous_block = self.chain[-1]
        new_block = Block(len(self.chain), previous_block.hash, data)
        self.chain.append(new_block)

    def display_chain(self):
        for block in self.chain:
            print(f"Index: {block.index}, Data: {block.data}, Hash: {block.hash}, Previous Hash: {block.previous_hash}")

if __name__ == "__main__":
    blockchain = Blockchain()
    blockchain.add_block("Data 1")
    blockchain.add_block("Data 2")
    blockchain.display_chain()

import hashlib
import random
import time


class Block:
    def __init__(self, data: str, previous_hash: bytes) -> None:
        self.data = data
        self.previous_hash = previous_hash
        self.hash = 0
        self.next_block_challenge = random.getrandbits(160)
        self.challenge_result = 0
        self.hash = 0

    def __str__(self) -> str:
        return f'{self.data} - {self.previous_hash} - {self.next_block_challenge} - {self.challenge_result}'

    def is_valid(Self):
        return hashlib.sha1(str(Self)) == Self.hash

    def update_hash(Self):
        Self.hash = hashlib.sha1(str(Self))


class BlockChain:
    def __init__(self) -> None:
        self.chain = list()

    def get_block(self, i=0):
        return self.chain[i]

    def add_new_block(self, data: str):
        last_block = self.chain[-1]

        if len(self.chain) == 0:
            Block(data, 0)

        new_block = Block(data, last_block.hash)
        new_block.challenge_result = solve_challenge(
            last_block.next_block_challenge)
        new_block.update_hash()

        self.chain.append(new_block)


def solve_challenge(block_hash, challenge):
    # encontrar valor X que acrescido ao block_hash seja < challenge
    # calculo
    return 0


begin = time.time()

blockchain = BlockChain("genesis")
for _ in range(1000000):
    blockchain.add_new_block("ola")

print(time.time() - begin)

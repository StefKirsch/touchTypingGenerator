import random

class SequenceGenerator:
    def __init__(self):
        self.history = set()

    def generate_sequence(self, chars, rows=None, word_len_range=(5, 8), words_count=100):
        """
        Generate a typing sequence.

        chars: list of characters to include in sequence.
        rows: list of rows to which characters belong. If given, should be same length as chars.
        word_len_range: range of lengths for words. Default is 5 to 7 characters.
        words_count: number of words in the sequence. Default is 50.
        """
        # If rows are given, filter chars by rows
        if rows:
            if len(chars) != len(rows):
                raise ValueError('chars and rows must be of the same length')
            chars = [c for c, r in zip(chars, rows) if r in rows]

        sequence = ''
        while len(sequence.split(' ')) < words_count:
            # Generate a word
            word_len = random.randint(*word_len_range)
            word = ''.join(random.choice(chars) for _ in range(word_len))
            sequence += word + ' '

        sequence = sequence.strip()  # remove trailing space

        # Check if sequence is unique
        if sequence in self.history:
            return self.generate_sequence(chars, rows, word_len_range, words_count)
        else:
            self.history.add(sequence)
            return sequence


# Usage
generator = SequenceGenerator()
chars = {
    "index_fingers": list("rtfgvbyuhjnm6578%^&*RTFGVB*YUHJNM"),
    "middle_fingers": list("4edc9ik,$EDC(IK<"),
    "ring_fingers": list("3wsx0ol.#WSX)OL>"),
    "pinkies": list("`12qaz~!@QAZ-=p[];\'\\/)_+P{}:\"|?")
}

print(generator.generate_sequence(chars["pinkies"]))

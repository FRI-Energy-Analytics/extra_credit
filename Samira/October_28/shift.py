from typing import List
class Solution:
    def shiftingLetters(self, S: str, shifts: List[int]) -> str:

        shifts = [sum(shifts[x:]) for x in range(len(shifts))]
        print(shifts)
        tmp = ''.join(map(lambda x: self.shift(S[x], shifts[x]) if x < len(shifts) else S[x], range(len(shifts))))
        return tmp

    def shift(self, ch: chr, times:int) -> chr:
        low = ord('a')
        max = 26
        val = ((ord(ch) - low) + times) % max + low
        return chr(val)
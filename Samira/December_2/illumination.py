from typing import List


class Solution:

    def gridIllumination(self, N: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        rows = {}
        cols = {}
        forwardDiag = {}
        backwardsDiag = {}
        lampHash = {}

        for lamp in lamps:
            r = lamp[0]
            c = lamp[1]

            if r * N + c not in lampHash:
                lampHash[r*N+c] = True
            self.increment_dict(rows, r)
            self.increment_dict(cols, c)
            self.increment_dict(forwardDiag, r+c)
            self.increment_dict(backwardsDiag, r-c)

        results = []
        for query in queries:
            r = query[0]
            c = query[1]
            results.append(1 if (self.check_dict(rows, r) or self.check_dict(cols, c) or
                           self.check_dict(forwardDiag, c+r) or self.check_dict(backwardsDiag, r-c)) else 0)

            for dr in range(-1, 2):
                for dc in range(-1, 2):
                    if N > r + dr >= 0 and N > c+dc >= 0 and (r+dr)*N+c+dc in lampHash and lampHash[(r+dr)*N+c+dc]:
                        self.decrement_dict(rows, r+dr)
                        self.decrement_dict(cols, c+dc)
                        self.decrement_dict(forwardDiag, c + dc + r + dr)
                        self.decrement_dict(backwardsDiag, r + dr - c - dc)
                        del lampHash[(r+dr)*N+c+dc]
        return results

    def increment_dict(self, dict, key):
        if key not in dict:
            dict[key] = 0
        dict[key] += 1

    def check_dict(self, dict, key):
        if key not in dict:
            return False
        return dict[key] > 0

    def decrement_dict(self, dict, key):
        if key in dict:
            dict[key]-=1


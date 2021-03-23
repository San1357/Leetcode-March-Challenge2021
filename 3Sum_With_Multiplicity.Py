'''Problem : 3Sum With Multiplicity '''

#CODE :

MOD = 10 ** 9 + 7

class Solution:
    def threeSumMulti(self, A: List[int], target: int) -> int:
        """
        Adapted from 3 sum
        3 pointers O(N + K^2)
        j, k scan each element once
        """
        counter = defaultdict(int)
        for a in A:
            counter[a] += 1

        keys = list(counter.keys())
        keys.sort()
        n = len(keys)
        ret = 0
        for i in range(n):
            j = i  # not i + 1
            k = n - 1
            while j <= k:  # not <
                a, b, c = keys[i], keys[j], keys[k]
                if b + c < target - a:
                    j += 1
                elif b + c > target - a:
                    k -= 1
                else:  # equal
                    if a < b < c:
                        ret += counter[a] * counter[b] * counter[c]
                    elif a == b < c:
                        # nC2
                        ret += counter[a] * (counter[a] - 1) // 2 * counter[c]
                    elif a < b == c:
                        ret += counter[a] * counter[b]  * (counter[b] - 1) // 2
                    elif a== b == c:
                        # nC3
                        ret += counter[a] * (counter[a] - 1) * (counter[a] - 2) // (3 * 2)
                    else:
                        raise

                    ret %= MOD
                    j += 1
                    k -= 1

        return ret

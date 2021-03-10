'''Problem : Integer To Roman '''

#CODE :


class Solution:
    def intToRoman(self, num: int) -> str:
        symbol = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        Value = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        i = 0
        res = ""
        while num > 0:
            while num >= Value[i]:
                num -= Value[i]
                res += symbol[i]
            i += 1
        return res
    

if __name__ == "__main__":
    s = Solution()
    print(s.intToRoman(2434))

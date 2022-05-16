class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:

        s = list(s)

        news = self.remover(s[:], k)
        print(s)

        while(s != news):
            s = news
            news = self.remover(s[:], k)
            print("news", news)
        return "".join(s)

    def remover(self, s, k):
        k = k-1

        i = 0
        while i < len(s):

            flag = 0
            for p in range(1, k+1):
                if i+p < len(s) and s[i] != s[i+p]:
                    flag = 1
                    break
            if flag != 1 and i+p+1 < len(s):
                val = s[i]
                while s[i] == val:
                    del s[i]

                break

            i = i+1
            # print("after ", s)
        return s


p = Solution()
print(p.removeDuplicates(
    "deeedbbcccbdaa", 3))

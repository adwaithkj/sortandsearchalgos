class Solution:
    def change(self, amount, coins) -> int:

        self.paths = []

        def recursetree(cur, path=[]):
            if cur == amount:
                self.paths.append(path)
                return
            elif cur > amount:
                return

            for i in coins:
                newpath = path[:]
                recursetree(cur+i, newpath+[i])

        recursetree(0, [])

        for i in self.paths:
            i.sort()

        for i in range(len(self.paths)):
            self.paths[i] = str(self.paths[i])
            self.paths[i] = "".join(self.paths[i])

        self.paths = set(self.paths)
        return len(self.paths)

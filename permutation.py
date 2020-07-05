class Solution:
    permutations = []
    def brute_forece(self, str: str, ans: str):
        if len(str) == 0:
            Solution.permutations.append(ans)
        for i in range(0, len(str)):
            self.brute_forece(str[0:i] + str[i + 1:len(str)], ans + str[i])

    def permutation1(self, str1: str, str2: str):
        if len(str1) != len(str2):
            return False
        self.brute_forece(str1, "")
        return str2 in Solution.permutations

    def quickSort(self, seq):
        if len(seq) < 1:
            return seq
        pivot = seq[0]
        left = []
        right = []
        for x in range(1, len(seq)):
            if seq[x] <= pivot:
                left.append(seq[x])
            else:
                right.append(seq[x])
        left = self.quickSort(left)
        right = self.quickSort(right)
        foo = [pivot]
        return left + foo + right

    def permutation2(self, str1: str, str2: str):
        if len(str1) != len(str2): return False
        return self.quickSort(str1) == self.quickSort(str2)

    def permutation3(self, str1: str, str2: str):
        if len(str1) != len(str2):
            return False
        strings = [0] * 128
        for i in range(0, len(str1)):
            strings[ord(str1[i])] = strings[ord(str1[i])] + 1

        for i in range(0, len(str2)):
            strings[ord(str2[i])] = strings[ord(str2[i])] - 1
            if(strings[ord(str2[i])] < 0):
                return False
        return True

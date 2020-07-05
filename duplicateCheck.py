class Solution:
    def duplicationCheck1(self, str: str):
        string = {}
        for i in range(1, len(str)):
            if str[i] in string:
                return False
            else:
                string[str[i]] = True
        return True

    def duplicationCheck2(self, str: str):
        array = [None] * 128
        for i in range(1, len(str)):
            code = ord(str[i])
            if(array[code]):
                return False
            array[code] = True
        return True

    def duplicationCheck3(self, str: str):
        sortedArray = self.quickSort(str)
        for x in range(1, len(sortedArray) - 1):
            if sortedArray[x] == sortedArray[x + 1]:
                return False
        return True

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
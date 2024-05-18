class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        int_digits = int("".join(map(str, digits)))
        int_digits = int_digits + 1

        int_dig = []
        for i in str(int_digits):
            int_dig.append(int(i))
        return int_dig

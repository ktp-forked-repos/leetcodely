"""Created by sgoswami on 7/28/17."""

"""Design and implement a TwoSum class. It should support the following operations: add and find.

add - Add the number to an internal data structure.
find - Find if there exists any pair of numbers which sum is equal to the value."""


class TwoSum(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.store = []
        self.map = {}

    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: void
        """
        if number in self.map:
            self.map[number] += 1
        else:
            self.map[number] = 1
            self.store.append(number)

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        for i in self.store:
            diff = value - i
            trigger = False
            if diff == i and diff in self.map:
                trigger = self.map[diff] > 1
            elif diff != i and diff in self.map:
                return True
        return trigger


if __name__ == '__main__':
    twoSum = TwoSum()
    twoSum.add(0)
    twoSum.add(-1)
    twoSum.add(1)

    print(twoSum.find(0))

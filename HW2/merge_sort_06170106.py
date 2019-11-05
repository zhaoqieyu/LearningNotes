#!/usr/bin/env python
# coding: utf-8

class Solution(object):

    def merge_sorted_array(self, left_array, right_array):
        #print('left_array')
        #print(left_array)
        #print('right_array')
        #print(right_array)
        if len(left_array) == 0:
            return left_array
        elif len(right_array) == 0:
            return right_array
        else:
            new_array = []
            x = 0
            y = 0
            i = 0

            if left_array[x] < right_array[y]:
                new_array.append(left_array[x])
                del left_array[x]
                x += x
                i += i
            else:
                new_array.append(right_array[y])
                del right_array[y]
                y += y
                i += i

            if len(left_array) == 0:
                new_array += right_array
            elif len(right_array) == 0:
                new_array += left_array
            else:
                new_array.extend(self.merge_sorted_array(left_array, right_array))
        #print('return')
        #print(new_array)
        return new_array

    def merge_sort(self, example):
        #print(example)
        middle = len(example)//2

        if len(example) > 1:
            return self.merge_sorted_array(self.merge_sort(example[:middle]), self.merge_sort(example[middle:]))
        else:
            return example


example = [9, 6, 21, 19, 23, 8]

output = Solution().merge_sort(example)
print(output)


class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        
        list_num = len(A)
        num_list_items = len(A[0])
        new_master_list = []

        for x in range(num_list_items):
            new_child_list = []
            for list in A:
                new_child_list.append(list[x])
            new_master_list.append(new_child_list)
        return new_master_list

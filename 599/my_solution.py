class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        common_rest = {}
        
        for i, rest in enumerate(list1):
            if rest in list2:
                common_rest[rest] = i + list2.index(rest)
        
        min_index = min(common_rest.itervalues())
        
        names = []
        
        for k,v in common_rest.iteritems():
            if v == min_index:
                names.append(k)
                
        return names

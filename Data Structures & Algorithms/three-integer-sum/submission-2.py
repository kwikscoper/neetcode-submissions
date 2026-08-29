class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        pos, neg, zeros = [], [], []
        res = set()
        for val in nums:
            if val > 0:
                pos.append(val)
            elif val < 0:
                neg.append(val)
            else:
                zeros.append(val)

        negset, posset = set(neg), set(pos)
        
        if len(zeros) >= 3:
            res.add((0, 0, 0))
        
        if zeros:
            for val in negset:
                if (-1 * val) in posset:
                    res.add((val, 0, -1 * val))
        
        for i in range(len(pos)):
            for j in range(i + 1, len(pos)):
                target = -1 * (pos[i] + pos[j])
                if target in negset:
                    res.add(tuple(sorted([pos[i], pos[j], target])))

        for i in range(len(neg)):
            for j in range(i + 1, len(neg)):
                target = -1 * (neg[i] + neg[j])
                if target in posset:
                    res.add(tuple(sorted([neg[i], neg[j], target])))

        return list(res)
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        return [i[0] for i in sorted(list(zip(names, heights)), key=lambda j: j[-1], reverse=True)]
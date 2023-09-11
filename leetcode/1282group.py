class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups={}

        for i,j in enumerate(groupSizes):
            if j not in groups:
                groups[j]=[i]
            else:
                groups[j].append(i)

        print(groups)

        res=[]

        for i in groups:
            count=i
            temp=[]

            while groups[i]!=[]:
                temp=groups[i][:count]
                groups[i]=groups[i][count:]
                res.append(temp)

        return res
                
                

        
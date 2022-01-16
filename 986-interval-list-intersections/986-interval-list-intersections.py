class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i,j=0,0
        res=[]
        while i<len(firstList) and j<len(secondList):
            lower_bound=max(firstList[i][0],secondList[j][0])
            higher_bound=min(firstList[i][1],secondList[j][1])
            
            if higher_bound<lower_bound:
                if higher_bound==firstList[i][1]:
                    i+=1
                else:
                    j+=1
            elif higher_bound==lower_bound:
                res.append([higher_bound,higher_bound])
                if firstList[i][1]>secondList[j][1]:
                    firstList[i][0]=higher_bound+1
                    j+=1
                elif firstList[i][1]==secondList[j][1]:
                    i+=1
                    j+=1
                else:
                    secondList[j][0]=higher_bound+1
                    i+=1
            else:
                res.append([lower_bound,higher_bound])
                if higher_bound==firstList[i][1]:
                    secondList[j][0]=lower_bound+1
                    i+=1
                else:
                    firstList[i][0]=lower_bound+1
                    j+=1
        return res
        
                
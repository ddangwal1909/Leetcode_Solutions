class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        
        user_dict={}
        
        for i in logs:
            if i[0] not in user_dict.keys():
                user_dict[i[0]]=[]
                user_dict[i[0]].append(i[1])
            else:
                if i[1] not in user_dict[i[0]]:
                    user_dict[i[0]].append(i[1])
        
        res_dict={}
        res_lst=[]
        for j in user_dict.keys():
            if len(user_dict[j]) not in res_dict.keys():
                res_dict[len(user_dict[j])]=1
                res_lst.append(len(user_dict[j]))
            else:
                res_dict[len(user_dict[j])]+=1
        
        
        res=[0 for i in range(k)]
        for i in range(len(res_lst)):
            res[res_lst[i]-1]=res_dict[res_lst[i]]
        
        return res
        
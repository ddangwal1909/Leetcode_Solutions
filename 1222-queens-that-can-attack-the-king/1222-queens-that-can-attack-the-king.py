class Solution:
    
    
    
    
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        
        res=[]
        
        
        def checkanyotherqueen(q_curr_idx,king,queens,type_cross):
            ## check upper left
            i1,j1=q_curr_idx
            i2,j2=king
            
            if type_cross=='UL':                            
                i1-=1
                j1-=1
                while i1!=i2 and j1!=j2:
                    if [i1,j1] in queens:
                        return True
                    i1-=1
                    j1-=1
                return False
            
            elif type_cross=='UR':                            
                i1-=1
                j1+=1
                while i1!=i2 and j1!=j2:
                    if [i1,j1] in queens:
                        return True
                    i1-=1
                    j1+=1
                return False
            
            elif type_cross=='LR':                            
                i1+=1
                j1+=1
                while i1!=i2 and j1!=j2:
                    if [i1,j1] in queens:
                        return True
                    i1+=1
                    j1+=1
                return False
            
            else:
                i1+=1
                j1-=1
                while i1!=i2 and j1!=j2:
                    if [i1,j1] in queens:
                        return True
                    i1+=1
                    j1-=1
                return False
            
            
        
        def checksamerow(q_idx,k_idx):
            if k_idx[0]==q_idx[0]:
                return True
            else:
                return False
        
        def checksamecol(q_idx,k_idx):
            if k_idx[1]==q_idx[1]:
                return True
            else:
                return False
        
        
        def checksamecross(q_idx,k_idx):
            
            ## check upper left
            i1,j1=q_idx
            while i1>=0 and j1>=0 and j1<8 and i1<8:
                if [i1,j1]==k_idx:
                    return (True,'UL')
                i1-=1
                j1-=1
            
            ## check upper right
            i1,j1=q_idx
            while i1>=0 and j1>=0 and j1<8 and i1<8:
                if [i1,j1]==k_idx:
                    return (True,'UR')
                i1-=1
                j1+=1
            
            
            ## check lower right
            i1,j1=q_idx
            while i1>=0 and j1>=0 and j1<8 and i1<8:
                if [i1,j1]==k_idx:
                    return (True,'LR')
                i1+=1
                j1+=1
                
            
            ## check lower left
            i1,j1=q_idx
            while i1>=0 and j1>=0 and j1<8 and i1<8:
                if [i1,j1]==k_idx:
                    return (True,'LL')
                i1+=1
                j1-=1
            
            return (False,'None')
        
        
        def helper(curr_idx,queens,king):
            flag1,flag2,flag3=False,False,False
            if checksamerow(queens[curr_idx],king):
                flag1=True
                for i in range(min(king[1],queens[curr_idx][1])+1,max(king[1],queens[curr_idx][1])):
                    if [queens[curr_idx][0],i] in queens:
                        flag1=False
                        break
            
            if checksamecol(queens[curr_idx],king):
                flag2=True
                for i in range(min(king[0],queens[curr_idx][0])+1,max(king[0],queens[curr_idx][0])):
                    if [i,queens[curr_idx][1]] in queens:
                        flag2=False
                        break
            
            samecross,type_cross=checksamecross(queens[curr_idx],king)
            
            if samecross:
                flag3=True
                if checkanyotherqueen(queens[curr_idx],king,queens,type_cross)==True:
                    flag3=False
            
            
            if flag1 or flag2 or flag3:
                return True
            
            return False
                    
                
        
        for i in range(len(queens)):
            if helper(i,queens,king)==True:
                res.append(queens[i])
        return res
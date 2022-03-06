# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        
        hashmap={}
        
        child=set()
        
        for i in descriptions:
            
            #print(i,hashmap)
            child.add(i[1])
            if i[0] in hashmap.keys() and i[1] in hashmap.keys():                
                if i[2]==1:
                    hashmap[i[0]].left=hashmap[i[1]]
                else:
                    hashmap[i[0]].right=hashmap[i[1]]
                    
            if i[0] not in hashmap.keys():
                tmp = TreeNode(i[0])
                hashmap[i[0]]=tmp
                if i[1] in hashmap.keys():
                    if i[2]==1:
                        hashmap[i[0]].left=hashmap[i[1]]
                    else:
                        hashmap[i[0]].right=hashmap[i[1]]
                
                
                
            if i[1] not in hashmap.keys():
                tmp = TreeNode(i[1])
                hashmap[i[1]]=tmp
                if i[2]==1:
                    hashmap[i[0]].left=hashmap[i[1]]
                else:
                    hashmap[i[0]].right=hashmap[i[1]]
        #print(hashmap)
        root = hashmap[(set(hashmap.keys())-child).pop()]
        return root
        
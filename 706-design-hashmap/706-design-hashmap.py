class MyHashMap:

    def __init__(self):
        self.hash_array=[]
        

    def put(self, key: int, value: int) -> None:
        flag=False
        idx=-1
        for i in range(len(self.hash_array)):
            if self.hash_array[i][0]==key:
                flag=True
                idx=i
                break
        if flag:
            self.hash_array[idx][1]=value
        else:
            self.hash_array.append([key,value])
        
            

    def get(self, key: int) -> int:
        res=-1
        for i in self.hash_array:
            if i[0]==key:
                res=i[1]
                break
        return res
        

    def remove(self, key: int) -> None:
        flag=False
        idx=-1
        for i in range(len(self.hash_array)):
            if self.hash_array[i][0]==key:
                idx=i
                flag=True
                break
        if flag:
            self.hash_array.pop(idx)
                


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
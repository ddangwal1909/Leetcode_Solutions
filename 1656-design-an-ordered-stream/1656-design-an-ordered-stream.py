class OrderedStream:

    def __init__(self, n: int):
        self.chunk= [None for i in range(n)]
        self.current=0
        print(self.chunk)
    
    def insert(self, idKey: int, value: str) -> List[str]:
        self.chunk[idKey-1]=value
        res=[]
        if self.current<len(self.chunk):
            while self.chunk[self.current]!=None:
                res.append(self.chunk[self.current])
                self.current+=1
                if self.current>=len(self.chunk):
                    break
        return res

# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)
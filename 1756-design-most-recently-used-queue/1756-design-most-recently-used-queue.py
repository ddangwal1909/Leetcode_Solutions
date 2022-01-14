class MRUQueue:

    def __init__(self, n: int):
        self.arr = [i for i in range(1,n+1)]

    def fetch(self, k: int) -> int:
        res=self.arr[k-1]
        if k==1:
            self.arr=self.arr[1:]
            self.arr.append(res)
        else:
            tmp_1 = self.arr[0:k-1]
            try:
                tmp_2 = self.arr[k:]
            except:
                tmp_2 = []
            
            #print(tmp_1)
            #print(tmp_2)
            #print(tmp_1.extend(tmp_2))
            if len(tmp_1)==0 and len(tmp_2)==0:
                self.arr=[res]
            elif len(tmp_1)==0:
                self.arr = tmp_2
            elif len(tmp_2)==0:
                self.arr = tmp_1
            else:
                tmp_1.extend(tmp_2)
                self.arr = tmp_1
            self.arr.append(res)
        return res

# Your MRUQueue object will be instantiated and called as such:
# obj = MRUQueue(n)
# param_1 = obj.fetch(k)
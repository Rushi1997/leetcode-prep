class TimeMap:

    def __init__(self):
        self.time ={}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.time:
            self.time[key].append([timestamp,value])
        else:
            self.time[key] = [[timestamp, value]]


    def get(self, key: str, timestamp: int) -> str:
        if key in self.time:
            list=self.time.get(key)
            i,j=0,len(list)-1
            result=""
            while i<=j:
                mid=(i+j)//2
                if list[mid][0]<=timestamp:
                    result= list[mid][1]
                    i=mid+1
                else:
                    j=mid-1
            return result
        else:
            return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

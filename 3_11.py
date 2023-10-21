class ArrayList:
    def __init__(self,capacity=100):
        self.capacity = capacity
        self.array = [None]*capacity
        self.size = 0
        
    def isEmpty(self): #공백
        return self.size == 0
    
    def isFull(self):  #포화
        return self.size == self.capacity
    
    def getEntry(self,pos):
        if 0 <= pos < self.size :
            return self.array[pos]
        else : return None

    def insert (self, pos, e):
        if not self.isFull() and 0<= pos <= self.size :
            for i in range(self.size, pos, -1):
                self.array[i] = self.array[i-1]
            self.array[pos] = e
            self.size += 1
        else : pass
    
    def delete(self, pos):
        if not self.isEmpty() and 0<= pos < self.size :
            e = self.array[pos]
            for i in range(pos,self.size-1) :
                self.array[i] = self.array[i+1]
            self.size -= 1
            return e
        else : pass

    def __str__( self ):
        return str(self.array[0:self.size])
    
    def findMax(self) : #최댓값 찾기
        if(self.isEmpty()):     #공백 검사 
            return -1
        
        max = 0                 

        for i in range(0,self.size) :   #0부터 배열의 요소에는 size -1 이니까 self.size 그대로 range의 끝에 넣어도 이상없음
            if(self.array[i]>max):      
                max = self.array[i]     
        
        return max        

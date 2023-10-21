class ArraySet:
    def __init__(self,capacity=100):
        self.capacity = capacity
        self.array = [None]*capacity
        self.size = 0

    def isEmpty(self) :
        return self.size == 0
    
    def isFull(self) :
        return self.size == self.capacity
    
    def contains(self, e) :
        for i in range(self.size) :
            if self.array[i] == e :
                return True
        return False
    
    def insert(self, e) :
        if not self.contains(e) and not self.isFull() :
            self.array[self.size] = e #배열의 맨 뒤에 추가
            self.size += 1

    def delete(self, e) :
        for i in range(self.size) :
            if self.array[i] == e :
                self.array[i] = self.array[self.size-1]
                self.size -= 1
                return
            
    def union (self, setB) : #합집환 반환 메소드
        setC = ArraySet()
        for i in range(self.size) :
            setC.insert(self.array[i])
        for i in range(setB.size) :
            if not setC.contains(setB.array[i]) :
                setC.insert(setB.array[i])
        return setC
    
    def intersect(self, setB) : #교집합 반환 메소드
        setC = ArraySet()
        for i in range(self.size) :
            if setB.contains(self.array[i]) :
                setC.insert(self.array[i])
        return setC
    
    def difference(self, setB) : #차집합 반환 메소드
        setC = ArraySet()
        for i in range(self.size) :
            if not setB.contains(self.array[i]) :
                setC.insert(self.array[i])
        return setC




    def __str__( self ) :
        return str(self.array[0:self.size])
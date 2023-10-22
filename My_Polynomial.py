class Polynomial:
    def __init__(self):
        self.coef=[]

    def degree(self):
        return len(self.coef)-1
    
    def add(self, polyB):    
        p = Polynomial()
        if self.degree() > polyB.degree(): #자신의 차수가 비교대상보다 더 크면
            for deg in range(polyB.degree()+1): #0부터 비교대상의 차수 갯수만큼 반복
                p.coef.append(self.coef[deg] + polyB.coef[deg]) #새로 만든 다항식에 차수에 맞는 계수 덧셈
            for deg in range(polyB.degree()+1,self.degree()+1): #비교대상 +1 차수부터 자신의 차수 끝까지 더하기(자신이 더 차수가 크니까)
                p.coef.append(self.coef[deg]) # 더하기 2단계 분리(0~비교대상 차수 , 비교대상 차수 +1 ~자신의 차수 끝)
        else:
            for deg in range(self.degree()+1):  #반대과정
                p.coef.append(self.coef[deg] + polyB.coef[deg])
            for deg in range(self.degree()+1,polyB.degree()+1):
                p.coef.append(polyB.coef[deg])
        return p 
    
    def substract(self,PolyB):
        t = ()
        if(self.degree()>PolyB.degree()):
            for deg in range(0,PolyB.degree()+1):
                t.coef[deg] = self.coef[deg] - PolyB.coef[deg]
            for deg in range(PolyB.degree()+1,self.degree()+1):
                t.coef[deg] = self.coef[deg] - PolyB.coef[deg]
        else:
            for deg in range(0,self.degree()+1):
                t.coef[deg] = self.coef[deg] - PolyB.coef[deg]
            for deg in range(0,PolyB.degree()):
                t.coef[deg] = self.coef[deg] - PolyB.coef[deg]

        return t
    
    def multiply(self, PolyB):
        t = Polynomial()
        t.coef = (self.degree() * PolyB.degree()) * [0]
        for degA in range(self.degree(),-1,-1):
            for degB in range(PolyB.degree(),-1,-1):
                temp = degA + degB
                t.coef[temp] += self.coef[degA] * PolyB.coef[degB]
        
        return t

    def evaluate(self,num):
        sum=0
        for i in range(self.degree(),-1,-1):
          sum=sum+self.coef[i] * (num**i)

        return sum
    
    def display(self,msg):
        print(msg, end='')
        for deg in range(self.degree(),0,-1):
            print(self.coef[deg], "x^",deg,"+",end='')
        print(self.coef[0])
        





def read_poly():#계수 읽어오기
    p = Polynomial()
    deg = int(input("다항식의 최고 차수를 입력하시오: "))
    p.coef = (deg+1)*[0]
    for i in range(deg, -1, -1):
        p.coef[i] = int(input(f"x^{i}의 계수 : "))
    return p



a = read_poly()
b = read_poly()
c=a.add(b)
a.display("A(x) = ")
b.display("B(x) = ")
c.display("C(x) = ")
print(" C(2) = ", c.evaluate(2))



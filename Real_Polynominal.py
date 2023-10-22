class Polynomial:

    def __init__(self):
        self.coef = []
    
    def degree(self):   #차수는 계수가 들어있는 리스트의 갯수 -1 
        return len(self.coef) - 1 
    
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
    
    def subtract(self, polyB):    
        p = Polynomial()
        if self.degree() > polyB.degree():
            for deg in range(polyB.degree()+1):
                p.coef.append(self.coef[deg] - polyB.coef[deg])
            for deg in range(polyB.degree()+1,self.degree()+1):
                p.coef.append(self.coef[deg])
        else:
            for deg in range(self.degree()+1):
                p.coef.append(self.coef[deg] - polyB.coef[deg])
            for deg in range(self.degree()+1,polyB.degree()+1):
                p.coef.append(polyB.coef[deg])
        return p
    
    def mult(self, polyB):
        p = Polynomial()
        p.coef = [0] * (self.degree() + polyB.degree() + 1)
        
        for degA in range(self.degree(), -1, -1):           
            for degB in range(polyB.degree(), -1, -1):               
                targetDeg = (degA + degB)
                p.coef[targetDeg] += self.coef[degA]*polyB.coef[degB]
        return p
    
    def display(self, msg):
        print(msg, end='')
        for deg in range(self.degree(), 0, -1):            
            print(self.coef[deg], "x^", deg, "+", end='')
        print(self.coef[0])
        
    def evaluate(self, x): # O(n)
        output = 0
        for deg in range(self.degree(), -1, -1):   
            output = output + self.coef[deg] * (x ** deg)
        return output
    
def read_poly():    #차수값 읽어오기
    p = Polynomial()
    deg = int(input("다항식의 최고 차수를 입력하세요: "))
    for n in range(deg, -1, -1): #두번째 -1은 0까지 출력함을 의미
        coef = int(input(f"x^{n}항의 계수 : "))
        p.coef.append(coef)
    p.coef.reverse()    
    return p
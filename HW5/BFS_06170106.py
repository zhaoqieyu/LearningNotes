from collections import defaultdict 
class Graph:
    def __init__(self): 
        self.graph = defaultdict(list)#產生graph，結構由defaultdict(list)的型蓋組成(self.graph是list型態)

    def addEdge(self,u,v): 
        self.graph[u].append(v) #因為self.graph是list型態，所以可以用append加進去U(key)，建立value(list) 

    def BFS(self, s): #s為出發點
        result = [] #把走過的順序存在此處方便之後印出來
        state1 = [] #先建立一個待完成清單
        state1.append(s) #把起點s加入待完成清單
        state2 = set() #把有走過的點加入state2中
        state2.add(s) #s已走完，因此可先將s加入
        while(len(state1)>0): #當待完成清單中還有值
            node = state1.pop(0) #從下面取出值
            neighbor = self.graph[node] #並看此值有無鄰居[]
            #以下是為了要依序把鄰居放入待完成清單
            for i in neighbor:#先看此鄰居有沒有走訪過
                if i not in state2: #若沒有
                    state1.append(i) #沒走過放待完成清單中
                    state2.add(i) #走過放state2
            result.append(node)#把取出來的值依序加入result
        return result#並傳回

    def DFS(self, s): #s為出發點
        result = [] #把走過的順序存在此處方便之後印出來
        stack = [] #先建立一個待完成清單
        stack.append(s) #把起點s加入待完成清單
        seen = set() #把有走過的點加入seen中
        seen.add(s) #s已走完，因此可先將s加入
        while(len(stack)>0): #當待完成清單中還有值
            node = stack.pop() #從上面取出值
            neighbor = self.graph[node] #並看此值有無鄰居[]
            #以下是為了要依序把鄰居放入待完成清單
            for i in neighbor:#先看此鄰居有沒有走訪過
                if i not in seen: #若沒有
                    stack.append(i) #沒走過放待完成清單中
                    seen.add(i) #走過放seen
            result.append(node)#把取出來的值依序加入result
        return result#並傳回

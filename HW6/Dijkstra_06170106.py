import sys 
from collections import defaultdict 


class Graph(): 

    def __init__(self, vertices):         
        self.V = vertices 
        self.graph = [] 
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 
        self.result = {} # to store result for dijkstra
        
        
    def addEdge(self,u,v,w): 
        self.graph.append([u,v,w])
        
    check = lambda self, parent , i : i if parent[i] == -1 else self.check(parent,parent[i]) 
    
    
    def Dijkstra(self, s): 
        start , shortest_path = [sys.maxsize] * self.V , [False] * self.V # to initial start and shortest_path
        start[s] = 0 #起始點的距離為0
        
        for index in range(self.V): #每個點都要納入考量
            u = start.index(sorted([start[i] for i in range(len(start)) if shortest_path[i] == False])[0])  # 找出距離最小，且尚未被加入的過的點           
            shortest_path[u] = True  #找到的點u為True，則代表已被加入  
            
            for v in range(self.V): # 更新start[] 
                if self.graph_matrix[u][v] > 0 and shortest_path[v] == False and start[v] > start[u] + self.graph_matrix[u][v]:# 若該點之前未被加入過，在加入該點後，透過該點，距離是否更近 
                    start[v] = start[u] + self.graph_matrix[u][v] #更新 V 點的距離
        
        for node in range(self.V): # to output start to result{}
            self.result[str(node)] = start[node]
        return  self.result
    
    
    def Kruskal(self):
        result_dic = {} # to store MST result
        index, output = 0, 0 # index:處理的邊/output:已輸出(找到)的邊 
        self.graph = sorted(self.graph,key=lambda item: item[2]) # 依照權重找出最小的邊(排序)
        parent = [-1]*self.V # 先假設parent為-1
        
        while output < self.V -1 : #若已找到的邊的數量小於已找到的邊的數量          
            u,v,w = self.graph[index] #先讀出list中的3個元素
            index += 1 #已處理第一個邊，繼續往下找
            
            if self.check(parent, u) !=  self.check(parent ,v) : #判斷是否有cicle(看u,v的parent是否相同)，若不同，代表沒有cicle 
                output += 1 #則把該點加入output
                result_dic[str(u)+"-"+str(v)]=w #u,v確認找到，加入dictionary
                parent[self.check(parent, self.check(parent, u))] = self.check(parent, self.check(parent, v)) #更改parent的值 
        return result_dic

from Crypto.Hash import MD5
class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class MyHashSet:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.data = [None] * capacity
        
    def MD5_hash(self,data):
        a = MD5.new()
        a.update(data.encode("utf-8"))
        x = a.hexdigest()
        index = int(x,16)%self.capacity
        return index
           
    def add(self, key):
        index = self.MD5_hash(key)
        if self.data[index] == None: #若原本該buckets中沒有值時
            self.data[index] = ListNode(key) #則把key直接加入該index中
            return
        else: #若原本該buckets中已經有值時
            node = self.data[index] #找到要把key放在哪個buckets，並存放在node中
            while node.next != None : #看該node的下一個(往該bucket後面看)是否為空，若不是空的
                node = node.next #先把目前的node指向下一個node
            node.next = ListNode(key) #再把key直接加入下一個node中
        
    def remove(self, key):
        index = self.MD5_hash(key)
        if self.data[index] != None and self.data[index].data == key: #若原本該buckets(index)非為空，且該bucket(index)中的值即為刪除值
            if self.data[index].next == None: #若此刪除值是Linked List中的最後一個(下一個值為空)
                self.data[index] = None #直接把最後一個刪除(改成空)
            else: #若此刪除值不是Linked List中最後一個
                self.data[index] = self.data[index].next #將要刪除的值的前一個index直接指向要刪除的值的下一個index
            return True
        elif ( self.data[index] != None and self.data[index].next != None ): #若原本該buckets(index)非為空，且該bucket(index)的下一個非為空
            next_node = self.data[index].next #把該bucket(index)的下一個存放為next_node
            while next_node != None : #當next_node不為0
                if  next_node.data == key: #且next_node等於搜尋值
                    if next_node.next == None :#若此刪除值是Linked List中的最後一個(下一個值為空)
                        next_node = None #直接把最後一個刪除(改成空)
                    else: #若此刪除值不是Linked List中最後一個
                        next_node =next_node.next #往下一個繼續
                    return True
                else: #且next_node不等於搜尋值
                    next_node = next_node.next #往下一個繼續
        return False
  
    def contains(self, key):
        index = self.MD5_hash(key)
        if self.data[index] != None and self.data[index].data == key: #若原本該buckets(index)非為空，且該bucket(index)中的值即為搜尋值
            return True #代表找到了，回傳True
        elif ( self.data[index] != None and self.data[index].next != None ): #若原本該buckets(index)非為空，且該bucket(index)的下一個非為空
            next_node = self.data[index].next #把該bucket(index)的下一個存放為next_node
            while next_node != None: #當next_node不為0
                if  next_node.data == key: #且next_node等於搜尋值
                    return True #代表找到了，回傳True
                else: #若next_node不等於搜尋值
                    next_node = next_node.next #再繼續往下找(next_node.next)
        return False

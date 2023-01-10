# 連結リスト
# 双方向連結リストの各ノード
class Node:
    def __init__(self,value=""):
        self.nex = None # 次のノード
        self.pre = None # 前のノード
        self.value = value  # ノードに付随している値

# 双方向連結リストの初期化
nil = Node()    # 何もないことを表すノードnil
nil.nex = nil   # 初期状態ではnilの次がnilを指すようにする
nil.pre = nil   # 初期状態ではnilの前がnilを指すようにする

# ノードpの直後にノードvを挿入する
def insert(v,p):
    v.nex = p.nex
    (p.nex).pre = v
    p.nex = v
    v.pre = p

# ノードvを削除する
def erase(v):
    (v.pre).nex = v.nex
    v.nex.pre = v.pre
    
# 連結リストの中身を順に出力する
def printList():
    values = []
    cur = nil.nex   # 先頭から出発
    while cur != nil:
        values.append(cur.value)
        cur = cur.nex
    print(values)
    
# 連結リストを作成する
sato = Node("sato")
suzuki = Node("suzuki")
takahashi = Node("takahashi")
ito = Node("ito")
watanabe = Node("watanabe")
yamamoto = Node("yamamoto")
nodes = [yamamoto,watanabe,ito,takahashi,suzuki,sato]
for node in nodes:
    insert(node,nil)
print("Before: ")
printList()

# watanabeノードを削除する
erase(watanabe)
print("After: ")
printList()
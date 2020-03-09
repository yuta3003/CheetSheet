# networkx

- [install](#install)
- [import](#import)
- [How To use](#how-to-use)
    - [Express between nodes with edges](#express-between-nodes-with-edges)

## install
```sh
pip install networkx
```

## import
```Python
import networkx as nx
```

## How To use

### Express between nodes with edges

```python
import networkx as nx

G = nx.Graph()  # 新規グラフを作成

G.add_node("A")                 # ノードを追加
print(nx.number_of_nodes(G))    #ノード数を出力
# 1

# リストも追加可能
G.add_nodes_from(["A", "B", "C", "D", "E"])    # A~Z の大文字を追加
print(nx.number_of_nodes(G))
# 5

G.add_edge("A", "B")            # エッジを追加
print(nx.number_of_edges(G))    # エッジ数を出力
# 1

#リストも追加可能
list_edge = [("C","D"), ("E", "F"), ("G", "H")]
G.add_edges_from(list_edge)
print(nx.number_of_edges(G))
# 4
```
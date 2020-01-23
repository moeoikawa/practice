▼pythonリスト削除について

・　すべての要素を削除: clear()¥n
・　指定した位置(index)の要素を削除し、値を取得: pop()
・　指定した値と同じ要素を検索し、最初の要素を削除: remove()
・　条件を満たす複数の要素を一括で削除: リスト内包表記
　 インデックス・スライスで位置・範囲を指定して削除: del

need_list = [aaa, bbb, ccc]
for i, row in enumerate(need_list):
    need_list.pop(i)　← そのindex番号が i の row をリストから削除
    
    
▼ブーリアン型（true, false）場合、if文は以下のように書くべき

if not show_to_broker:      ← if show_to_broker == false と同じこと

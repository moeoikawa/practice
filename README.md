▼pythonリスト削除について

・　すべての要素を削除: clear()
・　指定した位置(index)の要素を削除し、値を取得: pop()
・　指定した値と同じ要素を検索し、最初の要素を削除: remove()
・　条件を満たす複数の要素を一括で削除: リスト内包表記
　 インデックス・スライスで位置・範囲を指定して削除: del

need_list = [aaa, bbb, ccc]
for i, row in enumerate(need_list):
    need_list.pop(i)　← そのindex番号が i の row をリストから削除
    
    
▼ブーリアン型（true, false）場合、if文は以下のように書くべき
if not show_to_broker:      ← if show_to_broker == false と同じこと


▼python スライス

▼python ライブラリ

▼python （for enumerate）

▼Django (for ... empty)
for タグのオプションとして {% empty %} 節を使うことがでる。これはループさせようとした配列が空、または存在しなかった場合に表示する文字列を指定する

▼Docker

docker-compose stop
docker-compose build
docker-compose up (docker-compose up -d)

-d を付けるとログが省略される
エラーとかを見たい場合は -d を取るといい

▼python 三項演算子

▼Django (objects.filter, objects.get)
filter はカラムを取ってくるのではなく、指定した値を取ってくる

↓property_id から id を取得
aaa =  Negotiation.objects.filter(property_id = property_id)
negotiation_id = aaa.get().id

▼SQL
select * from aaa は、aaaテーブルの行を全て取ってくる
where は、列を指定できる



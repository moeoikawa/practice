# coding: utf-8

l = ['Alice', 'Bob', 'Charlie']

# インデックス番号, 要素の順に取得できる
# デフォルトだとenumerate()関数のインデックスは0から始まる
for i, name in enumerate(l):
    print(i, name)

#0以外の数値から開始したい場合は、enumerate()関数の第二引数に任意の開始数値を指定する
for i, name in enumerate(l, 1):
    print(i, name)

#charange1
print("<ch1.my favorite musician>")

musician = ["ポルカドットスティングレイ","king gnu","ずっと真夜中でいいのに"]
print(musician)

print(musician.pop())
musician.append("She is Summer")
print(musician)


#charange2
print("<ch2.my trip>")

obihiro = ("帯広", 11.1111, 22.2222)
asahikawa = ("旭川", 33.3333, 44.4444)
tokyo = ("東京", 55.5555, 66.6666)

trip = [obihiro, asahikawa, tokyo]
print(trip)

sapporo = ("札幌", 77.7777, 88.8888)

"""
trip[3] = sapporoではIndexError→追加はappendで。変更はインデックス指定
インデックスは0スタートなので注意。
"""

trip[1] = sapporo

print(trip)
print(trip[2])


#charange3
print("<ch3.about me>")

about_me = {"名前":"伊藤洋平",
            "身長":"171㎝",
            "体重":"73kg"}
print(about_me)

"""
about_me.append("血液型":"O")は×（appendはリスト追加用メソッド）
→辞書の要素追加は辞書名[キー] = バリュー
"""

"""既存キーのバリューを変更"""
about_me["体重"] = "72.5kg"

"""新要素を変更"""
about_me["血液型"] = "O型"
print(about_me)

print(about_me["名前"])


#charange4
print("<ch4.バリューの取り出し>")

key = input("キーを入力して下さい：")

if key in about_me:
    print(about_me[key])
else:
    print("登録がありません")


#charange5
print("<ch5.musician2>")

musician2 = {}
musician2["ポルカ"] = ["テレキャ", "ショート", "ヒミツ"]
musician2["King gnu"] = ["prayerX", "白日", "傘", "飛行艇"]
musician2["Summer"] = ["嬉しくなっちゃって", "大人になるね"]

print(musician2)


#charange6
# setコンテナは、有限集合を扱うコンテナ。リストからも作成可能
print("<ch6.set container>")

A = set([1,2,3,4])

list_b =[3,3,4,5,6,7]
B = set(list_b)

#重複要素はなくなる
print(A)
print(B)

#要素の追加
print("要素の追加")
B.add(8)
print(B)

#和集合
print("和集合：")
print(A | B)
print(A.union(B))
print(B.union(A))

#積集合
print("積集合：")
print(A & B)
print(A.intersection(B))
print(B.intersection(A))

#差集合
print("差集合：")
print(A - B)
print(A.difference(B))
print(B.difference(A))


#排他的論理和
print("排他的論理和：")
print(A ^ B)
print(A.symmetric_difference(B))
print(B.symmetric_difference(A))

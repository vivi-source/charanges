#charange1　ぶっちゃけ、このファイル自体も開けちゃうのね。
print("<ch1.何かファイル開く>")

with open("0999_charange.py","r", encoding="utf-8") as f:
    print(f.read())


#charange2
print("\n<ch2.キー入力をファイルに書き出し>")

list_q = ["名前", "身長", "体重", "血液型"]
with open("charange2.txt","w",encoding = "utf-8") as f:
    for i in list_q:
        f.write(i + ":" + input("{}は？：".format(i))+ "\n")


#charange3
print("\n<ch3.CSVファイルに書き出し>")
import csv

act = ["Top Gun", "Risky Business", "Minority Report"]
love = ["Titanic", "The Revanant", "Inception"]
human = ["Training Day", "Man of fire", "Flight"]
movies = [act, love, human]

with open("charange3.csv", "w", newline="") as f:
    w = csv.writer(f, delimiter=",")
    for i in movies:
        w.writerow(i)


#charange4
#　utf-8だと文字化ける。c932（シフトJIS）で指定
print("\n<ch4.CSVファイルに書き出し(日本語) >")

act = ["トップガン", "リスキービジネス", "マイノリティーリポート"]
love = ["タイタニック", "ザ・レヴァナント", "インセプション"]
human = ["鍛錬の日々", "燃える男", "フライト"]
movies = [act, love, human]

with open("charange4.csv", "w", newline="", encoding="cp932") as f:
    w = csv.writer(f, delimiter=",")
    for i in movies:
        w.writerow(i)


#charange1
print("<ch1.for loop>")

tv_drama = ["ウォーキング・デッド",
            "アントラージュ",
            "ザ・ソプラノズ",
            "ヴァンパイア・ダイアリーズ"]

for i in tv_drama:
    print(i)


#charange2
print("\n<ch2.for loop2>")

for i in range(25, 51):
    print(i)


#charange3
#　数字＋文字列の連結は可能だが、データ型を合わせる必要あり
print("\n<ch3.for loop3>")

for i,show in enumerate(tv_drama):
    print(str(i) + ":" + show)


#charange4
print("\n<ch4.type q for quit>")

while True:
    try:
        num = input("3の倍数を入力してください")
        if num == "q":
             break
        elif int(num) % 3 == 0:
            print("正解")
        else:
            print("不正解")
    except ValueError:
        print("数字を入力するか、qで終了します。")


#charange5
print("\n<ch5.掛け算>")

list1 = [8, 19, 148, 4]
list2 = [9, 1, 33, 83]
new_list = []

for i in list1:
    for j in list2:
        new_list.append(i * j)

print(new_list)

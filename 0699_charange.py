#charange1
print("<ch1.文字列取り出し>")

str_k = "カミュ"
print(str_k)
print(str_k[0])
print(str_k[1])
print(str_k[2])


#charange2　format
print("<ch2.{}で穴埋め format>")

str1 = input("type some letter:")
str2 = input("type a friend's name:")

print("私は昨日{}を書いて、{}に送った！".format(str1, str2))


#charange3　capitalize
print("<ch3.capitalize>")

str_ald = "aldous Huxley was born in 1894."

print(str_ald)
print(str_ald.capitalize())


#charange4　split
print("<ch4.split>")

str_w = "どこで？　誰が？　いつ？"
print(str_w)

list_w = " ".split(str_w)
print(list_w)


#charange5　join
#　メソッドを呼び出した文字列オブジェクトで、引数の文字列を連結する
print("<ch5.join>")

list_the_fox = ["The","fox","jmped","over","the","fence","."]
print(list_the_fox)

prd = list_the_fox.pop()
print(" ".join(list_the_fox) + prd)


#charange6　replace
print("<ch6.replace>")

str_sky = "A screaming comes across the sky."
print(str_sky)
print(str_sky.replace("s", "$"))


#charange7　index
print("<ch7.index>")

print("Hemingway".index("m"))


#charange8　エスケープ／クォートは種類違えばOK
print("<ch8.escape>")

print("吾輩は\"猫\"である。")
print("吾輩は'猫'である。")


#charange9　文字列結合　空白除去
print("<ch9.文字列結合>")

str_3 = "three "
print(str_3)
print((str_3 + str_3 + str_3).strip())
print((str_3 * 3).strip())


#charange10　スライス
print("<ch10.スライス>")

str_april = "四月の晴れた寒い日で、時計がどれも十三時を打っていた。"
print(str_april)
print(str_april[:str_april.index("、")])

# charange1
import statistics, random

list = []
for i in range(0,100):
    r = random.randint(0,100)
    print(r)
    list.append(r)

print("平均：{}".format(statistics.mean(list)))
print("調和平均：{}".format(statistics.harmonic_mean(list)))
print("中央値：{}".format(statistics.median(list)))
print("low median：{}".format(statistics.median_low(list)))
print("high median：{}".format(statistics.median_high(list)))
print("median grouped：{}".format(statistics.median_grouped(list)))
print("最頻値：{}".format(statistics.mode(list)))


# charange2
#　呼び出し元では、mathモジュールをインポートしなくてもOK
import cubed

#　無効データでやり直し。
#　数値が入力で終了　break
#　５回無効データ入れたら、終了　range(0,5)
for i in range(0,5):
    try:
        num = input("type a number")
        print("{}の３乗は{}".format(num, cubed.three(num)))
        break
    except ValueError:
        print("invalid")

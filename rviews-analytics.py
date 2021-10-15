data = []
count = 0
with open('ASA_Log.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1
        if count % 1000 == 0:
            print(len(data))
print('檔案讀取完了,總共有', len(data), '筆資料' )

sum_len = 0
for d in data:
    sum_len += len(d)
print('留言平均長度為： ', sum_len/len(data))

new = []
for d in data:
    if len(d) < 240:
        new.append(d)
print('總共有：', len(new) , '筆留言長度小於240')

name = []
account = input('請輸入您要查詢的帳號： ')
for d in data:
    if account in d:
        name.append(d)
if name == []:
    print('查不到資料')
else:
    print(name)

#進階快寫法
#name = [d for d in data if 'account' in d]
#if name == []:
#    print('查不到資料')
#else:
#    print(name)
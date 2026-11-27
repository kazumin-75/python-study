
########################################
## 問題4：ログイン試行（break・for else）
########################################

'''
attempts = ['abc', '1234', 'pass']
correct = 1234

attempts を入力されたパスワードの代わりに使います。先頭から最大3回まで順番に試してください。
• 正解したら「ログイン成功（2回目）」と表示して終了
• 3回とも間違えたら「アカウントロック」と表示
attempts = ["abc", "xyz", "pass"] でも試してください。
'''

attempts = ['abc', '1234', 'pass']
correct = "1234"

count = 0
for attempt in attempts:
    if correct == attempt:
        count += 1
        print('ログイン成功', count,'回目')
        break
    else:
        count += 1
else:
     print('アカウントロック')



count = 0
attempts = ["abc", "xyz", "pass"]

for attempt in attempts:
    if correct == attempt:
        count += 1
        print('ログイン成功', count,'回目')
        break
    else:
        count += 1
else:
    print('アカウントロック')



count = 0
attempts = ["abc", "xyz", "1234"]

for attempt in attempts:
    if correct == attempt:
        count += 1
        print('ログイン成功', count,'回目')
        break
    else:
        count += 1
else:
    print('アカウントロック')





############
## 改善点
##
## if の前に count += 1 を記載することで else をなくす
## または enumerate(attempts, 1) を使って、count をなくす
############


attempts = ['abc', '1234', 'pass']
correct = "1234"

count = 0
for attempt in attempts:
    count += 1
    if correct == attempt:
        print('ログイン成功', count,'回目')
        break
else:
    print('アカウントロック')



attempts = ['abc', '1234', 'pass']
correct = "1234"

for i, attempt in enumerate(attempts, 1):
    if correct == attempt:
        print('ログイン成功', i,'回目')
        break
else:
    print('アカウントロック')



attempts = ["abc", "xyz", "pass"]
correct = "1234"

count = 0
for attempt in attempts:
    count += 1
    if correct == attempt:
        print('ログイン成功', count,'回目')
        break
else:
    print('アカウントロック')



attempts = ["abc", "xyz", "1234"]
correct = "1234"

for i, attempt in enumerate(attempts, 1):
    if correct == attempt:
        print('ログイン成功', i,'回目')
        break
else:
    print('アカウントロック')


#密碼重試程式

#設定密碼 "a1234"
#使用者最多輸入3次
#不對的話，印出"密碼錯誤，還有__次機會"
#對的話，印出"登入成功"

password = '123'
i = 3
while i > 0 :
	pwd = input('請輸入密碼：')
	i = i - 1
	if pwd == password:
		print('登入成功！')
		break
	else:
		print("密碼錯誤。")
		if i > 0:
			print("還有", i, "次機會。")
		else:
			print('請洽客服')



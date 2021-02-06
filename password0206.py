#密碼重試程式

#設定密碼 "a1234"
#使用者最多輸入3次
#不對的話，印出"密碼錯誤，還有__次機會"
#對的話，印出"登入成功"

user_password = input('請輸入密碼：')

while True:
	
	if user_password == 'a1234':
		print('登入成功')
		break
	elif user_password != 'a1234':
		x = x - 1
		print('密碼錯誤，還有'+ str(x) +'次機會！')
	elif x == 0:
		print('密碼錯誤，請洽客服專員。')
	else:
		break



driving = input('你有沒有開過車？')
if driving != '有' and driving != '沒有':
	print('請輸入有或者沒有')
	raise SystemExit

age = input('你的年齡是多少？')
age = int(age)
if driving == '有':
	if age >= 18:
		print('你通過測驗了')
	else:
		print('奇怪 你怎麼會有開過車')
elif driving == '沒有':
	if age >= 18:
		print('你可以考駕照了')
	else:
		print('很好，再幾年就可以去考了')

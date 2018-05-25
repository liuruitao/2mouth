def is_year(year):
	if (year%400==0) or ((year%4==0) and (year&100!=0)):
		return 1
	else:
		return 0

def month_day(year,month,day):
	sum_day = 0
	da_month = [1,3,5,7,8,10,12]
	xiao_month = [4,6,9,11]
	for i in range(1,month):
		if i in da_month:
			sum_day +=31
		elif i in xiao_month:
			sum_day +=30
		elif is_year(year) and i==2:
			sum_day +=29
		elif i==2:
			sum_day +=28
	sum_day +=day
	print('%s是今年第%d天'%(year,sum_day))

def get_time(time):
	year = int(time[0:4])
	month = int(time[4:6])
	day = int(time[6:8])
	month_day(year,month,day)

get_time(str(20180525))

	

#-*- conding:utf-8 -*-
#!/user/bin/python

#设置万能验证码
from random import randint

#help('random')
#生成一个1000到9999之间的随机数

suijishu = randint(1000,9999)
print(u"生成的随机数:%d" %suijishu)

number = input('请输入随机数：')
print(number)
number = int(number)

if number == suijishu:
    print('登录成功！！')
elif number == 132741:
    print('登录成功！')
else:
    print('验证码输入有误！')


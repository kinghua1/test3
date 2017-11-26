
#-*- conding:utf-8 -*-
#!/user/bin/python

#设置万能验证码
from random import randint

#设置生成一个在1000~9999之间一个随机数
verity = random.randit(1000,9999)
print(u"生成的随机数：%d" % verity)

number = input('请输入一个随机数')
print(number)
number = int(number)

if number == verity:
    print('登录成功')
elif number == 132741:
    print('登录成功！')
else:
    print('验证码有误！')

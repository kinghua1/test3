
#-*- conding:utf-8 -*-
#!/user/bin/python

#����������֤��
from random import randint

#��������һ����1000~9999֮��һ�������
verity = random.randit(1000,9999)
print(u"���ɵ��������%d" % verity)

number = input('������һ�������')
print(number)
number = int(number)

if number == verity:
    print('��¼�ɹ�')
elif number == 132741:
    print('��¼�ɹ���')
else:
    print('��֤������')

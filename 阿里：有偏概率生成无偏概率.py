'''
有两个随机数产生器，R1以0.7的概率产生1，以0.3的概率产生0，而R2以0.3的概率产生1，0.7的概率产生0.问如何组合这两种产生器，使新得到的随机数产生器以0.5的概率产生1，0.5的概率产生0。随机数产生器可复用。
'''

R1生成1且R2生成1的概率等于R1生成0且R2生成0的概率。

设计程序:

while:
	if R1 == 1 and R2 == 1:
		return 1
		
	if R1 == 0 and R2 == 0:
		return 0
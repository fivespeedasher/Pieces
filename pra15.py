# 题目：利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。
score = int(input('Enter your score'))
def classify(score,):
    global grade
    # 将局部作用域转换为全局作用域
    if score<60:
        grade='C'
    elif score>=90:
        grade='A'
    else:
        grade='B'


classify(score)
print('%d is belong to %s level.'%(score,grade))
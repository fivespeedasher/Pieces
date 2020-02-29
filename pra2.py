'''
利润(I)低于或等于10万元时，奖金可提10%；
利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
20万到40万之间时，高于20万元的部分，可提成5%；
40万到60万之间时高于40万元的部分，可提成3%；
60万到100万之间时，高于60万元的部分，可提成1.5%;
高于100万元时，超过100万元的部分按1%提成.
从键盘输入当月利润I，求应发放奖金总数？
'''
i=int(input('Enter the profit\n'))
arr = [1000000, 600000, 400000, 200000, 100000, 0]  # 把阶梯数字组合成一个数组
rat = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]  # 把各个阶梯对应的提成比例组合成一个数组
r = 0  # 这里设置了r作为总奖金的基量，这个参数必不可少，它可以等于0，也可以不等于0。试想如果这是在算总工资，那么，r就可以赋上基本工资的值（但是计算总工资不推荐在这里赋上基本工资的值，因为到最后你还得减去5个基本工资）
for idx in range(0,6):  # 这里定义了一个新变量idx，以及它的range范围。range(0,6)的意思就是从第一位开始，到第6位结束.因为arr 和 rat 两个数组都是包含6个元素，所以range的最大范围应该设为6,。如果比6大，则会出现“list index out of range”错误，如果比6小，虽然不会报错，但奖金就会少发。这行代码开始了一个for循环。在这个for循环里，定义idx的值是没有用的，因为它是由range来赋值的，循环一轮，到下一轮就会再次变值。
    if i>arr[idx]:  # 这一行是一个计算前提，简意就是说你需要有盈利才能发奖金。需要注意的是arr[idx],在这个环境下，它代表range运行到某一位时arr数组里的那个数字，想通了这一点，你只能觉得它妙不可言。试想，他就像一个游标，或者说像体检时的台称，站上来不同的人，液晶会显示不同的数字。
        r+=(i - arr[idx]) * rat[idx]  # 著名的 r+=1 ！初次接触这种代码还是在试学Java时，当时只有一种感觉：r+=1怎么能是r=r+1的意思呢？更困惑的其实是：r怎么能等于r+1呢？r+1怎么说也比r多了1啊！这给初学者造成了不小的困扰，我不得不承认这点！现在细细想来，因为一切都是变量，你要更新这个变量，无论中间用了多少个新命名的变量来呈递不同阶段得到的值，最后还得来一句：r=×××。而这一行的作用，计算出每一阶梯的提成金额与上一个阶梯总额的和。它包含了加法、减法和乘法，rat[idx]和arr[idx]道理是相同的。所以这时我又回到for idx in range(0,6):这一行，感叹range函数确实太方便！
        print((i-arr[idx]) * rat[idx])  # 这里计算并打印出每一阶梯的提成金额与上一个阶梯总额的和。
        i=arr[idx]  # for 循环里不可缺少的赋值语句。这里突发奇想，如果把arr[idx]换成rat[idx]会怎样？测试的结果是：……*****不用想，工资肯定被扣得差不多了****！
print(r)  # 这里将每一轮的阶梯奖金相加，得到了总奖金数额。
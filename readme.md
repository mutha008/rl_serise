## 几种分类

1、理解环境 model-based RL

​	q-learning  deep q network  

2、不理解环境 model-free RL



1、基于概率   policy gradients

2、基于价值   q learning 、 sarsa



1、回合更新  policy gradients

2、单步更新 q learing/sarsa   效率高



1、在线学习   sarsa

2、离线学习  q learning 



## 基础知识

### 状态

（S，A，R，P，r）

S：状态

A：动作

R：奖励

P：策略

r：折现系数



### π 策略

π ： S -> A



### U：价值

![QQ图片20171210143327](.\QQ图片20171210143327.png)

### 

### Bellman equation 贝尔曼方程

![](.\QQ图片20171210143138.png)

### Delta rule

同梯度下降策略  当前状态:=当前状态 + a(理想-当前状态)



### Temporal difference 时序差分

delta rule应用到bellman condition 寻找最优路径

![QQ图片20171210144551](.\QQ图片20171210144551.png)

U值rule学习

![QQ图片20171210145505](.\QQ图片20171210145505.png)

其中不需要state transitions，称为model-free learning

### Q value

![QQ图片20171210145649](.\QQ图片20171210145649.png)



### Active learning

添加探索exploration ,   相对于exploitation

![QQ图片20171210150204](.\QQ图片20171210150204.png)

## Q learning算法描述



![u=771899190,3095662949&fm=173&app=25&f=JPEG](.\u=771899190,3095662949&fm=173&app=25&f=JPEG.jpg)


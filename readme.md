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

![QQ图片20171210143327](https://github.com/mutha008/rl_serise/blob/master/QQ图片20171210143327.png)

### 

### Bellman equation 贝尔曼方程

![](https://github.com/mutha008/rl_serise/blob/master/QQ图片20171210143138.png)

### Delta rule

同梯度下降策略  当前状态:=当前状态 + a(理想-当前状态)



### Temporal difference 时序差分

delta rule应用到bellman condition 寻找最优路径

![QQ图片20171210144551](https://github.com/mutha008/rl_serise/blob/master/QQ图片20171210144551.png)

U值rule学习

![QQ图片20171210145505](https://github.com/mutha008/rl_serise/blob/master/QQ图片20171210145505.png)

其中不需要state transitions，称为model-free learning

### Q value

![QQ图片20171210145649](https://github.com/mutha008/rl_serise/blob/master/QQ图片20171210145649.png)



### Active learning

添加探索exploration ,   相对于exploitation

![QQ图片20171210150204](https://github.com/mutha008/rl_serise/blob/master/QQ图片20171210150204.png)

## Q learning算法描述



![u=771899190,3095662949&fm=173&app=25&f=JPEG](https://github.com/mutha008/rl_serise/blob/master/u=771899190,3095662949&fm=173&app=25&f=JPEG.jpg)



## Sarsa

在线学习：每次更新q表不用max，直接用q(next_A, next_S) ， next_A来自策略P下的next_S

## Sarsa(λ)

每次更新q表λ步

## DQN

google  openai

![20170612221553966](https://github.com/mutha008/rl_serise/blob/master/20170612221553966.jpg)

## Double-DQN

解决过大估计Q值的问题

与DQN的区别在于q_target的更新方式  [PDF](http://www0.cs.ucl.ac.uk/staff/d.silver/web/Applications_files/doubledqn.pdf)

![ddqn](https://github.com/mutha008/rl_serise/blob/master/ddqn.PNG)

##  Dueling-DQN

[PDF](https://arxiv.org/abs/1511.06581)



## **Prioritized Experience Replay** 

TD-ERROR=Q现实-Q预测  ，绝对值越大的样本被抽取出来训练的概率越大，加快了最优策略的学习。



## Policy Gradients

基于行为的奖惩



## Actor Critic
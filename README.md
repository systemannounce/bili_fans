# b站粉丝增减查看仓库（仅限千粉以下）

> 如今我们终于得知那天取关我们粉丝的名字…………  
>    
> 参考仓库：https://github.com/SocialSisterYi/bilibili-API-collect

## 使用方法：

### 1. 先fork一份本仓库  

![image](https://github.com/systemannounce/bili_fans/assets/55303494/fed2de4c-752a-4b85-9cce-7c60ea725a57)

### 2. 这里直接点击右下角的CreateFork即可

![image](https://github.com/systemannounce/bili_fans/assets/55303494/62c9a1e1-dc63-4de7-8288-f0735d1a736a)

### 3. 然后我们回到你fork的仓库，特征是这里有一行蓝色的小字，而且仓库名前面是你的用户头像。

![image](https://github.com/systemannounce/bili_fans/assets/55303494/70596d7d-2168-41c7-838a-32072d5de932)

### 4. 添加环境变量

**首先，我们依次点击仓库里面的设置(Settings)->Secrets and variables->Actions**  

---

![image](https://github.com/systemannounce/bili_fans/assets/55303494/19fce90d-a029-4f11-bf1c-a5d4f7158085)  

---

**然后在打开的页面里面点击New Repository Secret**  

---

![image](https://github.com/systemannounce/bili_fans/assets/55303494/8b803a79-2113-497b-b8ad-d27f7c5eba52)  

---

**填写下面两个变量，变量内容下面有获取方法**  
|      Name     |                              Secret                            |
|      ----     |  -------------------------------------------------------------- |
|    bili_uid   | [b站UID](https://github.com/systemannounce/bili_fans/issues/2) |
| bili_sessdata | [获取方法](https://github.com/systemannounce/bili_fans/issues/1) |

**结束以后界面应该是下面这个样子**  

---

![image](https://github.com/systemannounce/bili_fans/assets/55303494/0ee6363e-aa6b-4e8b-a099-7e0cebd4904c)

### 5. 手动运行（自动运行为每一天的大概9点左右-北京时间）
> 本仓库带自动运行，每天运行一次，基本没有手动操作的必要，如果你实在想运行可以参照下面的步骤
![image](https://github.com/systemannounce/bili_fans/assets/55303494/771baaa5-e986-4721-bb4d-31e3d4ada811)

### 6. 查看粉丝变更
> 仓库每次自动提交都创建了一个tag，可以移步标签页进行比较和查看更改。
> [跳转](/tags)

### 7. 禁用仓库提醒
> 每天运行一次，如果没有粉丝数改变的话GitHub进行提交代码的时候会报错然后给你发个大大的ERROR电子邮件，如果不想被打扰到可以在你的仓库 `Unwatch` 这个位置禁用所有提醒。  
![image](https://github.com/systemannounce/bili_fans/assets/55303494/fad7bd8c-fe9c-4321-8876-e23c38b1328f)

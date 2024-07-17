# b站粉丝增减查看仓库（仅限千粉以下）

> 如今我们终于得知那天取关我们粉丝的名字…………

**基本相同，但是更易懂的文档链接：[bili_fans](https://www.systemannounce.com/2024/06/02/learning/Python/bili-fans/)**

---

## 注意：  
### 目前已知b站重名bug存在，请尽快更新到v1.4版本，如果是fork的用户请再你的仓库点击Update Branch

---

![image](https://github.com/user-attachments/assets/e4096da8-e69a-4d24-9554-3060a1fd3ebb)

---
## 提醒：
经过几天的测试，bilibili的SESSDATA就算不退出网页端一般三天左右刷新一次。  
如果遇到Actions报错退出代码 `160` ，提示信息 **-352** 或者是**账号未登录**的话，那就是SESSDATA失效了。

---

## 项目说明：

在我今天肝视频的时候，粉丝突然从600掉到599，我百思不得其解，然后想要找到掉的那个粉丝到底是因为早期关注我的还是最新关注我的，烦恼了好久  
于是我压根没心情做视频，导致了我肝出来了这个项目。
这个项目利用了GitHub的**修改追踪**机制，根据每次粉丝文件的修改可以很方便地看出每一次粉丝的变化，不管是**增加**还是**减少**。  
但是目前bilibili没有任何途径可以获得1000以后的粉丝列表，导致这个项目只能局限于某些小up，不过我正好就是小up。  

---

如果你不想泄露你的粉丝列表，你可以在右边 [Release](https://github.com/systemannounce/bili_fans/releases/latest) 处查看操作方法并且下载源码。

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

### 5. 启用Actions

>在Fork之后Actions处于未启用状态，请自行启动，否则将无法自动运行。
>
>具体操作步骤就是点击上面的Actions选项卡，然后点击中间的**I understand my workflows, go ahead and enable them**
>
>最后再在左边工作流界面启用fan名称的工作流即可

![image](https://github.com/systemannounce/bili_fans/assets/55303494/a27c2be6-3422-423f-959d-0c1a2d75b7ee)  
![image](https://github.com/systemannounce/bili_fans/assets/55303494/3b94f66a-efdd-4726-896a-54887797f077)



### 6. 手动运行（自动运行为每一天的大概9点左右-北京时间）
> 本仓库带自动运行，每天运行一次，基本没有手动操作的必要，如果你实在想运行可以参照下面的步骤
![image](https://github.com/systemannounce/bili_fans/assets/55303494/771baaa5-e986-4721-bb4d-31e3d4ada811)

### 7. 查看粉丝变更
> 仓库每次自动提交都创建了一个tag，可以移步标签页进行比较和查看更改。

### 8. 禁用仓库提醒
> 每天运行一次，如果没有粉丝数改变的话GitHub进行提交代码的时候会报错然后给你发个大大的ERROR电子邮件，如果不想被打扰到可以在你的仓库 `Unwatch` 这个位置禁用所有提醒。  
![image](https://github.com/systemannounce/bili_fans/assets/55303494/fad7bd8c-fe9c-4321-8876-e23c38b1328f)

### 9. 及时更新仓库
> 因为GitHub的规则，会对三个月没有动态的仓库自动禁止Actions的运行，请及时更新仓库，任何更改都可以。


> 感谢：https://github.com/SocialSisterYi/bilibili-API-collect

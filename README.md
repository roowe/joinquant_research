# joinquant_research

#### 环境初始化

我使用的是debian，相信其它Linux或OSX，应该也差不多。windows应该也差不多，使用py3的venv来隔离不同项目的包，避免版本冲突。

```shell
user@shell> mkdir joinquant_research
user@shell> cd joinquant_research
user@joinquant_research> python3 -m venv  py3
user@joinquant_research> source py3/bin/activate
user@joinquant_research> pip install wheel
user@joinquant_research> apt-get install python3-dev 
user@joinquant_research> pip install git+https://github.com/JoinQuant/jqdatasdk.git -i https://mirrors.aliyun.com/pypi/simple/
```



#### 本地运行

```
user@joinquant_research> source py3/bin/activate
user@joinquant_research> python xxx.py
```



#### 云端运行（聚宽后台->我的策略->投资研究运行）

删除or注释以下两行代码，复制到云端即可运行。

```
from jqdatasdk import *
auth(conf.user, conf.password)
```



#### 账户密码

```
user@joinquant_research> cp conf.py.tpl  conf.py ## 将其修改你的密码
```



#### Ref

- [聚宽JQData用户使用说明](https://www.joinquant.com/help/api/help?name=JQData)
- [JQData本地量化金融数据](https://www.joinquant.com/default/index/sdk)
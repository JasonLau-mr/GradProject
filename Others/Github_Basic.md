# git基本操作
>* git init - 初始化仓库
>* git status - 查看仓库状态
>* git add - 向暂存区中添加文件
>* git commit - 保存仓库的历史纪录    # git commit -m "First Commit"
>* git status - 查看仓库状态
>* git log - 查看提交日志  # git log --pretty=short 只显示提交信息的第一行
>* git diff - 查看更改前后的差别

# 分支的操作
>git branch - 显示分支一览表

# 创建，切换分支

### 切换到feature－A分支并进行提交

> **创建/切换feature-A**
>* git checkout -b feature-A
>* git branch feature-A
>* git checkout feature-A

>**提交**
>git commit -m "Add feature-A"

### 合并分支 (on master branch)

> git merge --no-ff feature-A

### 以图标形式查看分支

>git log --graph

# 回溯历史版本

> git reset --hard <hash value>

# 推送远程仓库

>* git remote add <name> <address>
>* git push -u <name> <branch>

# 从远程仓库获取

> git clone <address>

### 获取远程的feature-D 分支

>git checkout -b feature-D <name>/feature-D

### 获取最新的远程仓库分支

*将本地的分支更新到最新的状态*

>git pull <name> <branch>

# Pull Request

**在pull request前需要做的准备**

>1. Fork
>2. Clone
>3. Create branch(特性分支)

**特性分支(Topic Branch)**
*特性分支顾名思义，就是集中视线单一特性（主题）， 除此之外不进行任何作业的认知。在日常开发中，往往会创建数个特性分支，同时再次之外保留一个随时可以发布软件的稳定分支。稳定分支的角色通常由master分支担当*

>4. Git push to repository
>5. Create Pull Request

### 获取最新数据 

>git fetch <name>

# 采纳Pull Request

### 采纳Pull Request前的准备

>1. 代码审查
>2. 没有问题的话就Merge pull request

# Github 使用流程

>* Fork: 从原始仓库中fork一份到自己的仓库中
>* git clone: 将远程自己仓库中的代码保存到本地
>* git checkout -b <branch name>: 创建自己的分支，<branch name>通常以下阶段准备修改的方向命名
>* 在本地仓库中做相应的增添改
>* git add/ git diff/ git commit -m "statement"
>* git push <name> <branch-name>: 将本地的分支push到自己的仓库中
>* 在github主页 create pull request
>* 原始仓库接受到pull request，并调试处理


#### git是日常开发中常用的分布式版本控制工具,通过git,可以实现协同办公.

##### 四个概念:

> 工作区: 本地存放项目文件的地方,也就是项目文件夹
>
> 暂存区(index/stage): 使用git管理项目文件的时候,会在工作区文件夹下生成.git隐藏文件夹,这个文件夹称之为版本库, 它包含了两部分,一个是暂存区,暂存区是暂时存放文件的地方,通常使用add命令将工作区的文件添加到暂存区中区.
>
> 本地仓库: .git文件夹下还包括了git自动创建的master分支,HEAD指针指向master分支,commit命令可以将暂存区的文件添加到本地仓库中
>
> 远程仓库: 类似github的远程仓库, 使用git clone将远程仓库拷贝到本地仓库中,git push将本地仓库的文件推送到远程仓库.

---

##### 安装git

```
ubuntu:
$ sudo apt-get install git

windows:
官网下载git安装

创建ssh key, 邮箱为github的邮箱, 本地生成.ssh文件夹,需要使用id_rsa.pub 
$ ssh-keygen -t rsa -C "Youremail@email.com"

验证是否添加成功
$ ssh -T git@github.com

配置git, 是git识别用户的方式
$ git config --global user.name "Your name"
$ git config --global user.email "Youremail@email.com"

# 将文件夹变成版本库
$ git init

# 添加远程地址, 在不是克隆现有仓库时使用
$ git remote add origin git@github.com:yourname/yourrepo.git
```

---

##### git操作

```
# 本地文件添加到暂存区(Index)
$ git add <filename>
$ git add .  # 添加当前文件夹下所有文件

# 提交到本地仓库, -m后是本次提交说明
$ git commit -m "commit information"

# 提交到远程仓库
$ git push
$ git push origin master  # 推送到master分支
```

---

刚才git push时,我推送到的是master分支,默认情况下master是默认的分支.我们可以创建其他分支,在各个分支上进行开发,最后将它们合并到主分支上

##### 分支操作

```
# 创建分支, 并切换到该分支
$ git checkout -b branch_a

# 切换分支
$ git checkout master

# 删除分支
$ git branch -d brach_a
```

> 分支默认是只能自己看到,除非我们执行```git push origin branch_a```将本地分支推送到远程仓库.

---

##### 本地仓库与远程仓库同步操作

```
# 同步远程仓库,在当前目录下,先fetch,再merge远端的改动
$ git pull

# 合并其他分支到当前分支
$ git merge <branch>

# git diff
```

---

##### 标签:为软件分布创建标签

```
$ git tag 1.0.0 1b2e1d63ff
1b2e1d63ff 是你想要标记的提交 ID 的前 10 位字符。
可以使用下列命令获取提交 ID：
git log
你也可以使用少一点的提交 ID 前几位，只要它的指向具有唯一性。
```


# 使用git版本控制指南

### 一、PhiloVast版本控制流程：

#### 1. fork团队项目
 fork一份团队项目 [PhiloVast](https://github.com/octopustail/PhiloVast.git)到个人仓库中。

#### 2. 保持团队项目保持一致:
**step1. 将团队项目添加到remote中：**

1. 设置: ```git remote add upstream https://github.com/octopustail/PhiloVast.git```
2. 查看设置: ```git remote -v```

**step2. 与团队项目同步**
1. ```git fetch upstream``` 从"upstream"远端获取团队项目最新版本
2. ```git merge upstream/yourOwnBrach``` 将团队项目和自己的本地分支合并
> 这一步骤中如果出现冲突，则需要手动解决冲突。解决的冲突的具体操作就要根据情况来了
> 每次开发前要确认自己的版本和团队项目是一致的。


#### 3. push修改到自己的项目上
#### 4. 向团队项目提出pull request
#### 5. 团队项目负责人合并pull request

### commit规范

### 参考资料
[git版本控制流程](https://www.cnblogs.com/schaepher/p/4933873.html)
[团队中git的实践 - ourai.WS](https://ourai.ws/posts/working-with-git-in-team/)
[使用gitFlow的方式进行版本控制](https://zhuanlan.zhihu.com/p/23478654)
[git-workflows and tutorials-中文版本](https://github.com/xirong/my-git/blob/master/git-workflow-tutorial.md)


### pull、rebase、fetch
```pull```相当与```fetch```+```merge```。
```git pull --rebase```相当于将本地的修改移到同步了团队仓库的分支的顶部。 且别人对团队仓库的提交历史不会被合并

### 版本控制工作流
> 参考[《Git工作流指南 - 中文版本》](https://github.com/xirong/my-git/blob/master/git-workflow-tutorial.md)这篇文章非常👍

#### 集中式工作流
1⃣️ 、 建立中央仓库
2⃣️ 、 成员各自clone
3⃣ 、分别向中央仓库提交代码。如果发生冲突则解决冲突。（每次提交之前需要保持与当前中央仓库一致）

#### 功能分支工作流
1⃣️ 、建立中央仓库
2⃣️ 、成员各自clone
3⃣️ 、成员分别在中央仓库建立自己的分支，作为独立的功能分支
4⃣️ 、成员在各自的分支上进行开发，开发完毕后提出pr
5⃣️ 、merge提出的pr到```master```，这个过程要确定```master```是最新的。合并的过程：先在（完成merge这个人的）本地检出```master```分支是最新的额，然后```pull```或者```rebase```，将提出pr的那个分支合并到本地，然后再push到```origin```


#### gitflow工作流
主要思想：为功能开发，发布准备，bug修复配备独立分支。即为不同的分支定义好各自的角色，也可以加入pull request的机制来做code review

-----``` master```：包含已发布的版本
----- ```（bugfix）``` 临时的bug-fix
----- ```dev``` 包含所有历史记录
----- ```release```
-----``` feature1``` 功能开发分支
-----``` feature2 ``` 功能开发分支

1⃣️ 、 开发者在本地基于```dev```分支创建各自的功能分支。
2⃣️ 、 开发者在本地的功能分支上做开发
3⃣️ 、 开发者开发好一个功能后，提出合并到dev的pr
4⃣️ 、 准备正式发布，开启一个release分支，在这个分支清理发布、执行测试、更新文档。将这个分支merge到```dev```和```master```,然后删除这个分支。在这个步骤中可以发起code review的pr
5⃣️ 、 发现线上bug就从```master```拉出一个```bugfix```的分支，在这个分支中进行bug修改。修改完成后把```bugfix```分支合并到```dev```或者```master```。
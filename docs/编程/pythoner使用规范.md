# pythoner使用规范

1. 项目创建使用 cookiecutter 
使用以下命令创建项目
```
pip install cookiecutter 
cookiecutter https://github.com/AngusWG/cookiecutter-py-package.git
```
版本统一由 git + tag (versioneer) 管理   
在项目用setup.py 打包时  versioneer 会根据最近的tag标签 放入对应版本号

--- 

2. 养成format代码习惯

2.1 format code 快捷键 Ctrl + Alt + L  
2.2 format import 快捷键 Ctrl + Alt + O  

--- 

3.每个项目需要都有单元测  
单元测试的入口统一是Makefile中的 make check  方便运维建立统一的CICD

--- 

4. 项目需要打包到 pypi上

4.1 测试pypi pypi_dev 用于发测试版本包  
  
4.2 正式pypi pypi_st 用于发正式版本号 此pypi上的包  只能是纯数字版本号 不能有 + or dev 字样   正则为 /d+\./d+\./d+  


--- 

5. commit 时自动检查

* git hook 是指在对应git动作中触发的脚本
* pre-commit 指在提交`commit前`触发的动作

以下命令将设置一个默认 pre-commit    
在当前项目下有`Makeflie`的情况下 执行`make check`命令
```
python -c "from urllib.request import urlopen ;exec(urlopen('https://github.com/AngusWG/cookiecutter-py-package/raw/master/git_pre_commit_hook.py').read())"
```
* make 命令在windows上使用 需要安装 [cygwin](https://www.cygwin.com/)

--- 

### Cygwin 安装

安装时选择Make。
并将cygwin 的bin目录加到windows环境变量中，为了避免冲突，请尽量让Cygwin保持在环境变量第一条。
![image.png](https://upload-images.jianshu.io/upload_images/7485616-a7fd71a88a7f1ce0.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image.png](https://upload-images.jianshu.io/upload_images/7485616-1fb3bba591efaf3c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

--- 

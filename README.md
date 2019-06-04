# homework

## 马哥教育python实战22期

### 不要随意删除别人的代码！
### 
                   
```
默认目录不存在的，项目clone下来后，需要手动创建下:
创建01文件夹(目录)
在 01 文件夹里面新建文件夹(目录):
    P22044-hangzhou-yangfeng #这是个文件夹(目录)
    在 P22044-hangzhou-yangfeng 里面创建xxx.py 


说明:P22044-hangzhou-yangfeng(是你在群里面的学号和名字)
```

目录结构如下 
```
01：第一次作业提交的目录(不存在的话需要手动创建)         
    P22044-hangzhou-yangfemg 用自己的名字新建文件夹             
        xxxx.py 作业的代码文件            
    P22000-hangzhou-xiaozhi的目录          
        xxxx.py  作业代码文件    
           
02：第二次作业提交的目录(不存在的话需要手动创建)     
    P22044-hangzhou-yangfemg 用自己的名字新建文件夹             
         xxxx.py 作业的代码文件            
    P22000-hangzhou-xiaozhi的目录          
         xxxx.py 作业代码文件
              
03：第二次作业提交的目录(不存在的话需要手动创建)      
    P22044-hangzhou-yangfemg 用自己的名字新建文件夹             
         xxxx.py 作业的代码文件            
    P22000-hangzhou-xiaozhi的目录          
         xxxx.py 作业代码文件        
以此类推

```

### 1.命令行添加代码
```
第一次使用：         
centos：       
  yum install git       
  
  
Ubuntu：       
  apt-get install git

  
git clone git@github.com:magedu-python22/homework.git
# git@github.com:magedu-python22/homework.git 是我们这期专用的地址


更新本地代码(同步线上代码) git pull

查看代码状态 git status

每次提交作业前添加代码，只需要执行下面几行即可：
  git pull //拉取最新的代码文件
  git add .     
  git commit -m "first commit" //第一次提交  
  git pull //提交之前，先同步下最新版的代码，避免冲突
  git push -u origin master //同步到远程服务器      

用命令行操作，要添加ssh的公钥到github里，操作方法

创建SSH key的方法很简单，执行如下命令就可以： ssh-keygen 生成的SSH key文件保存在中～/.ssh/id_rsa.pub

然后用文本编辑工具打开该文件，我用的是cat,所以命令是： cat ~/.ssh/id_rsa.pub

接着拷贝出现在屏幕上的内容，将它粘帖到github帐号管理中的添加SSH key界面中。 打开github帐号管理中的添加SSH key界面的步骤如下：

登录github 点击右上方的Accounting，再点击settings图标 选择 SSH and GPGkeys， 点击 New SSH key 在出现的界面中填写SSH key的名称，填一个你自己喜欢的名称即可 然后将上面拷贝的cat ~/.ssh/id_rsa.pub 出现的内容，粘贴到key一栏，在点击“Add SSH key”按钮就可以了。 添加过程github会提示你输入一次你的github密码 添加完成后再次执行git clone就可以成功克隆github上的代码库了。
```
### 2. windows：
麻烦查看群共享文件

##### 获取镜像
可以使用`docker pull`命令从仓库获取所需要的镜像
```
eg: 从Docker hub仓库下载一个ubuntu12.04操作系统的镜像:
sudo docker pull ubuntu:12.04


```

`docker pull ubuntu:12.04`命令实际相当于`docker pull registry.hub.docker.com/ubuntu:12.04`命令,即从注册服务器 `istry.hub.docker.com`中的`ubuntu`仓库下载标记为12.04的镜像。

有时候官方仓库注册服务器下载较慢，可以从其他仓库下载。 从其它仓库下载时需要指定完整的仓库注册服务器地址。

完成后,即可随时使用该镜像了,例如创建一个容器,让其运行bash应用。
```
sudo docker run -t -i ubuntu:12.04 /bin/bash
root@720186dd05fb:/
```

#####列出本地镜像:
```
sudo docker images

[root@hhf ~]# sudo docker images
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
ubuntu              12.04               a11493a01736        12 days ago         103.6 MB
nginx               latest              4efb2fcdb1ab        2 weeks ago         183.4 MB
hello-world         latest              c54a2cc56cbb        9 weeks ago         1.848 kB
```
列出的字段信息:
* 来自哪个仓库 eg:ubuntu
* 镜像标记 eg: 12.04
* ID号(唯一) eg: a11493a01736
* 创建时间
* 镜像大小

>注:镜像的ID唯一标记了镜像，TAG信息用来标记同一仓库的不同镜像 ,例如`ubuntu`仓库有多个镜像，通过TAG信息来区分发行版本,例如12.04,14.04,16.04等。例如下面的命令指定使用镜像ubuntu: 12.04来启动一个容器

```
sudo docker run -t -i ubuntu:12.04 /bin/bash
```

####创建镜像:

* 从Docker Hub获取
* 利用本地文件系统创建

#####修改已有镜像

* 先使用下载的镜像启动容器
```
sudo docker run -t -i training/sinatra /bin/bash
root@17e25047c6f9:/#
```
注意：记住容器的 ID，稍后还会用到。
```
改源:
sed -i 's/archive.ubuntu.com/mirrors.aliyun.com/g' /etc/apt/sources.list
apt-get update -y
```
结束后,使用exit退出，现在容器已经被改变了,使用 `docker commit`命令来提交更新后的副本。
```
[root@hhf ~]# sudo docker commit -m "change apt repo" -a "Docker Newbee" 17e25047c6f9 hhf/ubuntu:v2 
sha256:c56ac0e16c79eb3059ca65909d138e502c4f705a952a6ddb8692204ae973a1de

-m: 提交的说明信息
-a: 更新的用户信息
17e25047c6f9: 用来创建镜像的容器的ID 
最后指定目标镜像的仓库名和 tag 信息.
```
使用`docker images`可以查看心创建的镜像:

```
hhf/ubuntu          v2                  c56ac0e16c79        About a minute ago   104.8 MB
```

之后，可以使用新的镜像来启动容器

```
docker run -i -t hhf/ubuntu:v2 /bin/bash
```

##### 利用Dockerfile创建镜像


使用`docker commit`来扩展一个镜像比较简单，但是不方便在团队中分享.我们可以使用`docker build`来创建一个新的镜像.为此,首先要创建一个Dockerfile，包含一下如何创建镜像的指令。

新建一个目录和一个 Dockerfile
```
mkdir hhf
cd hhf
touch Dockerfile
```
Dockerfile 中每一条指令都创建镜像的一层，例如：
```
# This is a comment
FROM ubuntu:12.04
MAINTAINER Docker Newbee <newbee@docker.com>
RUN sed -i 's/archive.ubuntu.com/mirrors.aliyun.com/g' /etc/apt/sources.list
RUN apt-get update -y
```
Docker file 的基本语法是:

* 使用#来注释
* `FROM` 指令告诉 Docker 使用哪个镜像作为基础
* 接着是维护者的信息
* `RUN` 开头的指令会在创建中执行，比如安装一个软件包,在这里使用 sed 将默认的apt源替换成了阿里云的

编写完 Dockerfile后可以使用`Docker build`来生成镜像

```
docker build -t="hhf/ubuntu:v3" .

Step 1 : FROM ubuntu:12.04
 ---> a11493a01736
Step 2 : MAINTAINER Docker Newbee <newbee@docker.com>
 ---> Running in 766d97773a41
 ---> 3472980dd191
Removing intermediate container 766d97773a41
Step 3 : RUN sed -i 's/archive.ubuntu.com/mirrors.aliyun.com/g' /etc/apt/sources.list
 ---> Running in 3ef28746fe30
 ---> 51c3d9df7cb4
Removing intermediate container 3ef28746fe30
Step 4 : RUN apt-get update -y
 ---> Running in dd332cbfc0ff
Get:1 http://mirrors.aliyun.com precise Release.gpg [198 B]
Get:2 http://mirrors.aliyun.com precise-updates Release.gpg [198 B]
。。。。。。
 ---> b81aab333e2c
Removing intermediate container dd332cbfc0ff
Successfully built b81aab333e2c

```

`-t`标记用来添加tag,指定新的镜像的用户信息， “.” 是 Dockerfile 所在的路径（当前目录），也可以替换为一个具体的 Dockerfile 的路径。

可以看到 build 进程在执行操作。它要做的第一件事情就是上传这个 Dockerfile 内容，因为所有的操作都要依据 Dockerfile 来进行。 然后，Dockfile 中的指令被一条一条的执行。每一步都创建了一个新的容器，在容器中执行指令并提交修改（就跟之前介绍过的 docker commit 一样）。当所有的指令都执行完毕之后，返回了最终的镜像 id。所有的中间步骤所产生的容器都被删除和清理了。

**注意一个镜像不能超过 127 层**

此外,还可以利用`ADD`命令复制本地文件到镜像,用`EXPOSE`命令向外开发端口，用`CMD`命令扫描容器启动后运行的程序等:例如
```
# put my local web site in myApp folder to /var/www
ADD myApp /var/www
# expose httpd port
EXPOSE 80
# the command to run
CMD ["/usr/sbin/apachectl", "-D", "FOREGROUND"]
```
现在可以利用新创建的镜像来启动一个容器。
```
docker run -i -t hhf/ubuntu:v3  /bin/bash
```

还可以用 `docker tag` 命令来修改镜像的标签。
```
docker tag fda80281b6a5 hhf/ubuntu:14.04
```

#####从本地文件系统导入
要从本地文件系统导入一个镜像，可以使用 openvz（容器虚拟化的先锋技术）的模板来创建： openvz 的模板下载地址为 [templates](http://openvz.org/Download/templates/precreated) 。

比如，先下载了一个 centos-6 的镜像，之后使用以下命令导入：
```
wget http://download.openvz.org/template/precreated/centos-6-x86_64-minimal.tar.gz
sudo cat centos-6-x86_64-minimal.tar.gz  |docker import - centos-6
```
然后查看新导入的镜像：
```
docker images
REPOSITORY          TAG                 IMAGE ID            CREATED             VIRTUAL SIZE
centos-6            latest              ed9e5fd8869a        17 seconds ago      343.8 MB
```
#####上传镜像
>用户可以通过 `docker push` 命令，把自己创建的镜像上传到仓库中来共享。例如，用户在 Docker Hub 上完成注册后，可以推送自己的镜像到仓库中。
```
docker login -u "lovehhf" -p "password"
docker push lovehhf/ubuntu:12.04
```

####存出和载入

#####存出镜像


如果要导出镜像到本地文件，可以使用 docker save 命令。

```
docker save -o centos_6_x86_x64.tar centos-6:latest
```

#####载入镜像

可以使用 `docker load` 从导出的本地文件中再导入到本地镜像库

```
sudo docker load --input centos_6_x86_x64.tar  
或
sudo docker load < centos_6_x86_x64.tar
```

这将导入镜像以及其相关的元数据信息（包括标签等）。


####移除镜像
#####移除本地镜像

如果要移除本地的镜像，可以使用 `docker rmi` 命令。注意 docker rm 命令是移除容器。

```
docker rmi hhf/ubuntu:v3
docker rmi ed9e5fd8869a
```
##### 清理所有未打过标签的本地镜像

`docker images` 可以列出本地所有的镜像，其中很可能会包含有很多中间状态的未打过标签的镜像，大量占据着磁盘空间。

使用下面的命令可以清理所有未打过标签的本地镜像

```
sudo docker rmi $(docker images -q -f "dangling=true")
相当于===>
sudo docker rmi $(docker images --quiet --filter "dangling=true")
```

#####镜像实现原理

Docker 镜像是怎么实现增量的修改和维护的？ 每个镜像都由很多层次构成，Docker 使用 Union FS 将这些不同的层结合到一个镜像中去。

通常 Union FS 有两个用途, 一方面可以实现不借助 LVM、RAID 将多个 disk 挂到同一个目录下,另一个更常用的就是将一个只读的分支和一个可写的分支联合在一起，Live CD 正是基于此方法可以允许在镜像不变的基础上允许用户在其上进行一些写操作。 Docker 在 AUFS 上构建的容器也是利用了类似的原理。
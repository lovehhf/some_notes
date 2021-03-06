
Android系统四大组件分别是 **活动（Activity**、**服务（Service）**、**广播接收器（BroadcastReceiver）**和 **内容提供器（ContentProvider** 。其中活动是所有 Android 应用程序的门面，凡是在应用中你看得到的东西，都是放在活动中的。而服务就比较低调了，你无法看到它，但它会一直在后台默默地运行，即使用户退出了应用，服务仍然是可以继续运行的。

广播接收器可以允许你的应用接收来自各处的广播消息，比如电话、短信等，当然你的应用同样也可以向外发出广播消息。内容提供器则为应用程序之间共享数据提供了可能，比如你想要读取系统电话簿中的联系人，就需要通过内容提供器来实现。



Android目录结构:


1. src

毫无疑问，src 目录是放置我们所有 Java 代码的地方，它在这里的含义和普通 Java项目下的 src 目录是完全一样的，展开之后你将看到我们刚才创建的HelloWorldActivity文件就在里面。

2. gen

这个目录里的内容都是自动生成的，主要有一个 R.java 文件，你在项目中添加的任何资源都会在其中生成一个相应的资源id。这个文件永远不要手动去修改它。

3. assets

这个目录用得不多，主要可以存放一些随程序打包的文件，在你的程序运行时可以动态读取到这些文件的内容。另外，如果你的程序中使用到了 WebView 加载本地网页的功能，所有网页相关的文件也都存放在这个目录下。

4. bin

这个目录你也不需要过多关注，它主要包含了一些在编译时自动产生的文件。其中会有一个你当前项目编译好的安装包，展开 bin 目录你会看到 HelloWorld.apk，把这个文件拷到手机上就可以直接安装了。

5. libs

如果你的项目中使用到了第三方 Jar包，就需要把这些 Jar 包都放在 libs 目录下，放在这个目录下的 Jar 包都会被自动添加到构建路径里去。你可以展开上图中Android 4.0、第一行代码 —— Android 18 Android Private Libraries、Android Dependencies 这些库，其中显示的Jar 包都是已经被添加到构建路径里的。

6. res

这个目录下的内容就有点多了，简单点说，就是你在项目中使用到的所有图片、布局、字符串等资源都要存放在这个目录下，前面提到的 R.java 中的内容也是根据这个目录下的文件自动生成的。当然这个目录下还有很多的子目录，图片放在 drawable 目录下，
布局放在 layout 目录下，字符串放在 values 目录下，所以你不用担心会把整个 res目录弄得乱糟糟的。

7. AndroidManifest.xml

这是你整个 Android 项目的配置文件，你在程序中定义的所有四大组件都需要在这个文件里注册。另外还可以在这个文件中给应用程序添加权限声明，也可以重新指定你创建项目时指定的程序最低兼容版本和目标版本。由于这个文件以后会经常用到，我们用到的时候再做详细说明。

8. project.properties

这个文件非常地简单，就是通过一行代码指定了编译程序时所使用的 SDK 版本。我们的 HelloWorld 项目使用的是 API 14，你也可以在这里改成其他版本试一试。这样整个项目的目录结构就都介绍完了，如果你还不能完全理解的话也很正常，毕竟里面有太多的东西你都还没接触过。不用担心，这并不会影响到你后面的学习。相反，等你学完整本书后再回来看这个目录结构图时，你会觉得特别地清晰和简单。
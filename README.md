# Python 算法与数据结构视频教程

## 课程简介
数据结构和算法是每个程序员需要掌握的基础知识之一，也是面试中跨不过的槛。目前关于 Python 算法和数据结构的系统中文资料比较欠缺，
笔者尝试录制视频教程帮助 Python 开发者掌握常用算法和数据结构，提升开发技能。
本教程是付费教程(文字内容和代码免费)，因为笔者录制的过程中除了购买软件、手写板等硬件之外，业余需要花费很多时间和精力来录制视频、查资料、编写课件和代码，养家糊口不容易，希望大家体谅。

## 链接
视频教程已经发布在网易云课堂和 csdn 学院，内容一致，推荐使用网易云课堂。

- [网易云课堂: Python数据结构与算法教程](http://study.163.com/course/introduction.htm?courseId=1005526003)
- [csdn 学院：Python数据结构与算法教程](https://edu.csdn.net/course/detail/8332)

电子书地址：

- [网上阅读《Python 算法与数据结构教程 》](http://pegasuswang.github.io/python_data_structures_and_algorithms/)
- [github 链接](https://github.com/PegasusWang/python_data_structures_and_algorithms)
- [readthedoc 电子书下载](http://python-data-structures-and-algorithms.readthedocs.io/zh/latest/)
- [《开源一个 Python 算法和数据结构中文教程[视频]》](https://zhuanlan.zhihu.com/p/36038003)  视频讲解示例

leetcode 实战图解教程(推荐)：

如果您有一定的基础，只是想快速针对面试刷题，也可以直接参考笔者针对《剑指offer》和 leetcode 经典题目的 Python 刷题图解实战。

- [图解Python数据结构与算法-实战篇- leetcode经典题目实战](https://study.163.com/course/courseMain.htm?courseId=1212203808&share=2&shareId=400000000496051)

笔者的其他课程：

- [玩转Vim 从放弃到爱不释手](https://www.imooc.com/learn/1129)
- [Python工程师面试宝典](https://coding.imooc.com/class/318.html)

## 痛点
- 讲 Python 数据结构和算法的资料很少，中文资料更少
- 很多自学 Python 的工程师对基础不够重视，面试也发现很多数据结构和算法不过关，很多人挂在了基础的数据结构和算法上
- 缺少工程应用场景下的讲解，很多讲算法的资料太『教科书化』。本书实现的代码工程上可用
- 网上很多视频教程不够循序渐进，不成系统

## 作者简介
曾就职于[知乎](https://www.zhihu.com/people/pegasus-wang/activities)，现腾讯视频后端工程师，多年 Python/Go 开发经验。

知乎专栏：

- [《Python 学习之路》](https://zhuanlan.zhihu.com/c_85234576)
- [《玩转vim(视频)》](https://zhuanlan.zhihu.com/vim-video)

电子书：[《Python web 入坑指南》](http://python-web-guide.readthedocs.io/zh/latest/)

## 课程内容
包括我们在业务开发和面试中常用的算法和数据结构，希望可以帮助 Python 开发者快速上手，很多老手写业务代码写多了很多基础知识忘记了，
也可以作为回顾。课程尽量用通俗的方式讲解，结合 python 语言和日常开发实践的经验。书中代码可以作为大家的面试笔试参考。
对于每个算法和用到的数据结构我们需要知道:

- 原理
- Python 实现方式
- 时间、空间复杂度
- 使用场景，什么时候用

## 目录结构
这里讲解的章节我参考了下边教材中列举的一些书籍，并且自己设计了大纲，争取做到循序渐进，简单实用。因为实现一些高级数据结构的时候会用到
很多底层数据结构，防止跳跃太大导致读者理解困难。

课程的目录结构如下，每一章都有配套的文字讲义(markdown)，示例代码，视频讲解，详细的讲解一般会放在视频里，使用手写板来
进行板书，包括文字、图示、手动模拟算法过程等。

- 课程介绍
- 课程简介之笨方法学算法
- 抽象数据类型 ADT，面向对象编程
- 数组和列表
- 链表，高级链表。双链表，循环双端链表
- 队列，双端队列，循环双端队列
- 栈，栈溢出
- 算法分析，时间复杂度 大O 表示法
- 哈希表，散列冲突
- 字典
- 集合
- 递归
- 查找：线性查找和二分查找
- 基本排序算法: 冒泡、选择、插入排序
- 高级排序算法: 归并排序、快排
- 树，二叉树
- 堆与堆排序
- 优先级队列
- 二叉查找树
- 图与图的遍历
- python 内置常用数据结构和算法的使用。list, dict, set, collections 模块，heapq 模块
- 面试笔试常考算法

## 编程语言
我们这里使用最近很火的Python。Python 入门简单而且是个多面手，在爬虫、web 后端、运维、数据分析、AI、量化投资等领域都有 Python 的身影，
无论是否是专业程序员， Python 都是一门学习性价比非常高的语言。
知乎、豆瓣、头条、饿了么、搜狐等公司都有广泛使用 Python。笔者日常工作使用也是 Python，有一定实践经验，
在知乎上维护了一个专栏[《Python 学习之路》](https://zhuanlan.zhihu.com/c_85234576)。

Python 抽象程度比较高， 我们能用更少的代码来实现功能，同时不用像 C/C++ 那样担心内存管理、指针操作等底层问题，
把主要心思放在算法逻辑本身而不是语言细节上，Python 也号称伪代码语言。所有代码示例使用 Python2/3 兼容代码，
不过只在 python3.5 下测试过，推荐用相同版本 Python 进行代码编写和测试。

## 受众
想要学习 Python 算法和数据结构的中级同学，包括自学的同学和本科低年级学生等。需要掌握 Python
的基本语法和面向对象编程的一些概念，有一定的 Python 使用经验。我们这里尽量只使用最基本的 Python 语法，不会再去介绍用到的 Python 语法糖。
数据结构和算法算是本科教育中偏难的课程，既需要你理解其原理，又需要具有有扎实的编程能力。

**请注意: 本教程不是零基础教程，着重于使用 Python 实现常用算法和数据结构，不适合从来没有学过算法和数据结构的新手同学，购买之前请慎重考虑，请确保你之前看过一本数据结构和算法的教材，最好有过其他语言实现算法的经验**

# 预备知识
（注意：有些同学看起来很吃力，为了不花冤枉钱，我建议你先整体浏览本电子书的内容和代码是否在自己的理解范围内，再决定是否购买视频。有些概念不是立马就能理解的，需要反复思考实践）

- 了解基本的数据结构和算法的概念，不适合**完全**没有了解过算法的新手，更不适合 Python 基础都没掌握的同学。购买之前请慎重考虑
- 无需太多数学基础，仅在算法时间复杂度分析的时候会用到一些简单数学知识。对于学习基础算法，逻辑思维可能更重要一些

## 参考教材和链接
这里我参考过三本书，均可以网购纸质版或者网络上搜索电子版，建议大家先大致阅读一本教材掌握基本原理，本教程重点在于 Pythonic 代码实现：

[《算法图解》](https://book.douban.com/subject/26979890/): 图解的形式很适合新手，示例使用的是 python。推荐基础较少的同学看这本书入门

[《Data Structures and Algorithms in Python》]( https://book.douban.com/subject/10607365/): 适合对 Python
和算法比较熟悉的同学，或者是有其他语言编程经验的同学。本书是英文版，缺点是书中错误真的很多，代码有些无法运行而且不够 Pythonic。该书 [勘误](http://bcs.wiley.com/he-bcs/Books?action=resource&bcsId=9003&itemId=0470618299&resourceId=35653)

[《算法导论》第三版]( https://book.douban.com/subject/20432061/): 喜欢数学证明和板砖书的同学可以参考，有很多高级主题。使用伪代码可以很快翻译成 Python

## 算法可视化

学习算法的过程中有时候会比较抽象，这里给大家推荐一些可视化的网站，方便更直观地理解各种算法和数据结构的执行步骤：

- https://github.com/algorithm-visualizer/algorithm-visualizer
- https://www.cs.usfca.edu/~galles/visualization/Algorithms.html
- https://runestone.academy/runestone/books/published/pythonds/index.html#

## 讲课形式

绘图演示+手写板+现场编码

我将使用绘图软件+手写板进行类似于纸笔形式的讲解，边讲边开个终端分成两个窗口，一个用 vim
编写代码，另一个窗口用来运行代码，所有代码我将会现场编写(还是很有挑战的)。
每个视频我会尽量控制时长，讲的内容尽量通俗易懂，摆脱学院派的授课方式。

你可以参考我在知乎发的专栏文章看下：

[那些年，我们一起跪过的算法题[视频]](https://zhuanlan.zhihu.com/p/35175401)

[抱歉，我是开发，你居然让我写单测[视频]](https://zhuanlan.zhihu.com/p/35352024)


## 课程特点

- 每个算法和数据结构都有讲义、视频(包含讲解、图示、手动模拟)、源代码。其中只有视频内容为付费内容
- 讲义循序渐进，结合自己的学习和使用经验讲解。github 上实时更新
- 视频演示更加直观易懂
- 演示代码实现思路，所有代码在视频里均现场编写
- 偏向工程应用和代码实现。代码直接可以用。每个文件都是自包含的，你可以直接运行和调试，这是目前大部分书籍做得不到位的地方
- 良好的工程实践：[编码之前碎碎念(工程实践)](http://python-web-guide.readthedocs.io/zh/latest/codingstyle/codingstyle.html)。
这是很多看了几本书没有太多业界实践经验就敢讲课的培训班老师教不了的。**知识廉价，经验无价**
- 每个实现都会有单测来验证，培养良好的编码和测试习惯，传授工程经验
- 结合 cpython 底层实现讲解（比如list 内存分配策略等），避免一些使用上的坑。并且会用 python 来模拟内置 dict 等的实现
- 每篇讲义后有思考题和延伸阅读链接，帮助大家加深思考和理解。大部分题目答案都可以网络上搜索到

## 资料

- 视频。包含所有讲解视频(网易公开课)
- 代码示例。所有代码我会放到 github 上。
- markdown 讲义，包含视频内容的提要等内容
- 延伸阅读。我会附上一些阅读资料方便想深入学习的同学

## 如何获取每章代码

注意每一章目录里都有 py 文件，在电子书里看不到。clone 下本代码仓库找到对应目录里的 python 文件即是每章涉及到的代码。
由于代码实现千差万别，本书代码实现具有一定的个人风格，不代表最佳实现，仅供参考，笔者尽量使用 python2/3 兼容代码。
目前已经新增《剑指offer》大部分经典题目的 Python 解法，每道题目附带leetcode 地址，大家可以自己尝试解决提交。
本项目遵守 MIT 协议，本项目下的所有代码您可以任意学习修改和使用， 但是直接引用代码请加上本项目 github 地址。


## 如何学习
笔者讲课录制视频的过程也是自己再整理和学习的过程，录制视频之前需要参考很多资料
希望对所讲到的内容，你能够

- 理解所讲的每个数据结构和算法的
    - 原理
    - Python 实现方式
    - 时间、空间复杂度
    - 使用场景，什么时候用
- 自己尝试实现，如果抛开视频自己写起来有困难可以反复多看几次视频，一定要自己手动实现。很多面试可能会让手写。一次不行就看完原理后多实践几次，直到能自己独立完成。
- 每章讲义后边都会有我设计的几个小问题，最好能够回答上来。同时还有代码练习题，你可以挑战下自己的掌握程度。
- 最好按照顺序循序渐进，每章都会有铺垫和联系，后边的章节可能会使用到前面提到的数据结构
- 根据自己的基础结合我列举的教材和视频学习，第一次理解不了的可以反复多看几次，多编写代码练习到熟练为止

## 课程目标
掌握基本的算法和数据结构原理，能独立使用 Python 语言实现，能在日常开发中灵活选用数据结构。
对于找工作的同学提升面试成功率。


## 开发和测试工具

推荐使用以下工具进行开发，如果使用编辑器最好装对 应 Python 插件，笔者视频演示中使用了 vim，读者可以自己挑选自己喜欢的开发工具：

- Pycharm
- Sublime
- Atom
- Vscode
- Vim/Emacs

注意视频中使用到了 pytest 测试框架和 when-changed 文件变动监控工具(方便我们修改完代码保存后自动执行测试)，你需要用 pip 安装

```py
pip install pytest
pip install when-changed
```

视频演示里我使用到了一个简单的 test.sh 脚本文件，内容如下:

```sh
#!/usr/bin/env bash

# pip install when-changed, 监控文件变动并且文件修改之后自动执行 pytest 单测，方便我们边修改边跑测试
 when-changed -v -r -1 -s ./    "py.test -s $1"
```
将以上内容放到 test.sh 文件后加上可执行权限, `chmod +x test.sh`，之后就可以用

```
'./test.sh somefile.py'
```
每次我们改动了代码，就会自动执行代码里的单元测试了。pytest 会自动发现以 test
开头的函数并执行测试代码。良好的工程需要我们用单测来保证，将来即使修改了内部实现逻辑也方便做回归验证。

或者你可以在的 ~/.bashrc  or  ~/.zshrc 里边加上这个映射（别忘记加上之后source下）:

```sh
# 监控当前文件夹文件变动自动执行命令
alias watchtest='when-changed -v -r -1 -s ./ '
```

然后在你的代码目录里头执行 `watchtest pytest -s somefile.py` 一样的效果


## 测试用例设计

笔者在刚学习编程的时候总是忘记处理一些特例(尤其是动态语言可以传各种值)，为了养成良好的编程和测试习惯，在编写单元测试用例的时候，
我们注意考虑下如下测试用例(等价类划分)：

- 正常值功能测试
- 边界值（比如最大最小，最左最右值）
- 异常值（比如 None，空值，非法值）

```
def binary_search(array, target):
    if not array:
        return -1
    beg, end = 0, len(array)
    while beg < end:
        mid = beg + (end - beg) // 2  # py3
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid
        else:
            beg = mid + 1
    return -1


def test():
    """
    如何设计测试用例：
    - 正常值功能测试
    - 边界值（比如最大最小，最左最右值）
    - 异常值（比如 None，空值，非法值）
    """
    # 正常值，包含有和无两种结果
    assert binary_search([0, 1, 2, 3, 4, 5], 1) == 1
    assert binary_search([0, 1, 2, 3, 4, 5], 6) == -1
    assert binary_search([0, 1, 2, 3, 4, 5], -1) == -1
    # 边界值
    assert binary_search([0, 1, 2, 3, 4, 5], 0) == 0
    assert binary_search([0, 1, 2, 3, 4, 5], 5) == 5
    assert binary_search([0], 0) == 0

    # 异常值
    assert binary_search([], 1) == -1
```

当然我们也不用做的非常细致，要不然写测试是一件非常繁琐累人的事情，甚至有时候为了测试而测试，只是为了让单测覆盖率好看点。
当然如果是web应用用户输入，我们要假设所有的参数都是不可信的。 但是很多内部调用的函数我们基于约定来编程，如果你瞎传参数，那就是调用者的责任了。


## 勘误

输出其实也是一种再学习的过程，中途需要查看大量资料、编写讲义、视频录制、代码编写等，难免有疏漏甚至错误之处。
有出版社找过笔者想让我出书，一来自己对出书兴趣不大，另外感觉书籍相对视频不够直观，有错误也不能及时修改，打算直接把所有文字内容讲义和代码等放到 github 上，供大家免费查阅。

如果你发现文字内容、代码内容、视频内容有错误或者有疑问，欢迎在 github 上提 issue 讨论(或者网易公开课评论区)，或者直接提 Merge Request，我会尽量及时修正相关内容，防止对读者产生误导。
同时非常感谢认真学习并及时发现书中错误的同学，非常欢迎针对知识本身的交流和讨论，任何建议和修正我都会认真求证。
对于提出修正意见或者提交代码的同学，由于人数比较多这里就不一一列举了，可以在以下列表查看，再次感谢你们。笔者信奉开源精神，『眼睛足够多，bug 无处藏』。
如果您发现视频中的代码有误，请及时使用 git pull 拉取本项目的代码更新，最好用目前最新的代码来学习和实践。

[issue](https://github.com/PegasusWang/python_data_structures_and_algorithms/issues?q=is%3Aissue+is%3Aclosed)

[contributors](https://github.com/PegasusWang/python_data_structures_and_algorithms/graphs/contributors)

## 如何更新代码(写给不熟悉 git 的同学)
如果你直接 clone 的本项目的代码仓库，可以直接使用 `git pull origin master` 拉取更新。
如果你先 fork 到了自己的仓库，然后 clone 到本地的是你自己的仓库，你可以编辑本地项目的 `.git/config`，
增加如下配置：

```sh
[remote "pegasuswang"]
	url = https://github.com/PegasusWang/python_data_structures_and_algorithms.git
	fetch = +refs/heads/*:refs/remotes/origin/*
```

然后使用 `git pull pegasuswang master` 拉取更新。

## 如何提问？
如果读者关于代码、视频、讲义有任何疑问，欢迎一起讨论
请注意以下几点：

- 描述尽量具体，视频或者代码哪一部分有问题(可以具体到文档或者代码行数)？请尽量把涉及章节和代码贴出来，方便定位问题。
- 如果涉及到代码，提问时请保持代码的格式
- 如果直接提了代码bug，最好有相关测试用例展示失败 test case，方便复现问题


## 本电子书制作和写作方式
使用 mkdocs 和 markdown 构建，使用  Python-Markdown-Math 完成数学公式。
markdown 语法参考：http://xianbai.me/learn-md/article/about/readme.html

安装依赖：
```sh
pip install mkdocs    # 制作电子书, http://markdown-docs-zh.readthedocs.io/zh_CN/latest/
# https://stackoverflow.com/questions/27882261/mkdocs-and-mathjax/31874157
pip install https://github.com/mitya57/python-markdown-math/archive/master.zip

# 或者直接
pip install -r requirements.txt

# 如果你 fork 了本项目，可以定期拉取主仓库的代码来获取更新，目前还在不断更新相关章节
```

你可以 clone 本项目后在本地编写和查看电子书：
```sh
mkdocs serve     # 修改自动更新，浏览器打开 http://localhost:8000 访问
# 数学公式参考 https://www.zybuluo.com/codeep/note/163962
mkdocs gh-deploy    # 部署到自己的 github pages
```

扫码加入课程：

![扫码加入课程](./163_course.png)

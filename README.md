# images_inquery_page

我现在需要写一个调查问卷的web，尽量简洁好看，善用组件
技术：jquery + bootstrap
内容：
分四轮问答，每一轮都有数个组问题，每组问题有5个问题
图片：
项目目录下有一个 index.html文件和一个tog目录，tog目录下有多个子文件夹，子文件夹命名："数字-组名"分别对应 id 与 name
每个子文件夹就是一组问题，有多少子文件夹就有多少组问题，四轮中不显示数字id，只显示序号(1开始)和组名，每轮都是这几组照片，而子目录下会有四个图片(文件名：origin, sketch, freecontrol, reno,renoop,ours

)和一个prompt.txt文件
每轮问答：
第一轮：
每组问题分两步
1. 画面只显示原图origin，限时5秒，超过五秒跳到第二步
2. 上方有一个图片(sketch)和prompt提示词，作参考；中间有两张A（freecontrol
）B（ours）图片；底下有五个问答，每轮每组的问题都是一样（四个问题都是单选A和B图片，第五个问题是一个滑动条(1-5分)表示答案可信度）
第二轮-第四轮：
只有一步，也就是第一轮的第二步，但是上方的图片有两个(原图origin, sketch)+prompt
下方有A(这三轮中分别是freecontrol, reno, renoOP)B(ours)图片，加上五个问题，跟第一轮的区别就是有没有将原图做成限时页面
最后页面：
感谢问答，一个按钮导出所有问答的json文件，文件中要能知道对应的id和name

# first-personal-work
由于已经学过《数据采集与预处理》，对于一些基本的网页格式还是可以分析并且进行处理，从而得到想要的数据。网页的爬取目前知道2中方式，一种是使用selenium模拟浏览器来获取网页，对于各种网页都可以用，唯一的缺点就是效率低，对于本题要获取全部的评论是不太实用的。另一种就是使用requests来获取网页源码，但是要对网页进行分析来拼凑每一次的url，效率比较高，当时在频繁的访问服务器的时候要注意反爬。本题为了被反爬，使用了time.sleep()来进行停顿。

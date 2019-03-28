'''爬虫简介

组成：控制节点，数据节点，爬虫节点（算法），资源库的构成

步骤：
    首先确定需要爬去的网页URL地址
    通过HTTP协议获取对应的HTML页面
    提取HTML页面里的有用数据
        如果是需要的数据就保存起来
        如果页面里面是其他URL，那么就继续执行第二步
Python写爬虫：语法优美、代码简介、开发效率高、三方模块多，调用其他接口也方便。有强大的爬虫Scrapy,以及成熟高效的scrapy-redis分布策略
爬虫框架Scrapy

需要的技能
    python基本语法
    如何抓取页面
        HTTP请求处理，urblib处理后的请求可以模拟浏览器发送请求，获取服务器响应的文件
    解析服务器响应的内容
        re\xpath(xml数据格式解析)\BeautifualSoup4\jsonpath(使用json格式获取网络请求格式)\pyquery
        目的是使用某种描述性语法提取匹配规则的数据
    如何采取动态HTML、y验证码的处理
        通过的动态页面采集  selenuim+PhantomJS(无界面浏览器），模拟真实浏览器加载js\ajax等非静态页面数据
        Tesseract 机器学习库，机器图像识别系统（识别图片中的文本）
    Scrapy框架
        中国常见的框架Scrapy\Pyspider
        高定制性能（异步网络框架twisted),所以数据下载速度非常快，提供了数据存储、数据下载、提取规则等组件
    分布式策略
        scrapy-redis
        在Scrapy的基础上添加了一套以Redis数据库为核心的一套组件，让scrapy框架支持分布式的功能，主要在Redis里做请求指纹去重，请求分配、数据临时存储
        
反爬虫技术：
    User-Agent
    代理
    验证码
    动态数据加载
    加密数据
    
爬虫类型：
    通用网络爬虫
        概念：搜索引擎用的网络爬虫
        用户群体：搜索引擎用的爬虫系统
        目标：尽可能把互联网上的所有网页下载下来，放到本地服务器形成备份。再对这些网页做相关处理（提取关键字、去掉广告等），最后提供一个用户检测接口
        抓取流程
            首先选取一部份已有的URL，把这些URL放到爬虫队列
            从队列里提取出这些URL，然后解析DNS得到主机IP，然后去把这个IP对应的服务器里下载HTML页面，保存到搜索引擎的本地服务器里，之后把爬过的URL放入已爬取的队列中
            分析这些网页内容，找出网页里的URL链接，继续执行第二步，直到爬去条件结束
        搜索引擎如何获取一个新的网站
            主动向百度站长提交域名
            在其他网站里设置网站的外链接
            搜索引擎会合DNS服务商合作，可以快速收录新的网站
        通用爬虫并不是万物皆可爬的，它需要遵守规则 Robots协议
            协议会指明通用爬虫可以爬取网页的权限
            Robota.txt只是一个建议，并不是所有爬虫都遵守，一般只有大型的搜索引擎爬虫才会遵守
        通用爬虫的工作流程
            爬去网页
            存储数据
            内容处理
            提供检索/排名服务
        搜索引擎排名
            PageRank值  点击量排名
            竞价排名   谁钱多谁排名靠前
        通用爬虫的缺点
            只能提供和文本的内容(HTML\WORD\PDF)等，但是不能提供多媒体（音乐、图片、视频）和二进制文件（程序、脚本）等
            提供结果千篇一律，不能针对不同人群提供不同的搜索结果
            不能理解人类语义上的检索
    聚焦网络爬虫
        概念 爬虫程序员写的针对某种内容的爬虫
        特点 面向主题爬虫，面向需求爬虫  会针对某种特定的内容取爬去信息，而且会保证信息和需求尽可能相关
    增量式网络爬虫
    深层网络爬虫
URL
    统一资源定位符，是互联网上的资源位置
    http://www.aspxfans.com:8080/news/index.as?boardID=5&ID=23232&page=1#name   参数#name锚指的是显示页面的位置
'''


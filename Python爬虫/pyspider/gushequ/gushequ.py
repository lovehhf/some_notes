#-*- coding:utf-8 -*-


"""
爬取股社区夜报并插入数据库
"""
import requests
import re
import MySQLdb

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6"}

url = "http://www.zixinke.cn/2016/11/page/1/"

class GuSheQu():
    def __init__(self):
        print("正在爬取文章：")

    def getHtml(self,url):   ##获取网站源代码并返回
        session = requests.session()
        html = session.get(url).content
        return html

    def getArticleUrl(self,html):   ##获取文章url
        articleUrl = re.findall('<a class="read-more" href="(.*?)">阅读全文',html,re.S)
        return articleUrl   ##是个列表

    def getArticleTitle(self,html):   ##获取文章标题
        articleTitle = re.findall('rel="bookmark">(.*?)</a>',html,re.S)
        return articleTitle

    def getArticleDate(self,articleTitle):
        date = re.findall(r'.*(201[1-6][0-9][0-9][0-9][0-9]).*',articleTitle)
        return date[0]

    def changePage(self,url,total_page): ##改变url并返回url列表
        now_page = int(re.search('page/(\d+)/', url, re.S).group(1))
        page_group = []
        for pageNum in range(now_page, total_page + 1):
            link = re.sub('page/(\d+)/', 'page/%s/' % pageNum, url, re.S)
            page_group.append(link)
        return page_group

    def insertInfo(self,date,title,url,content):
        try:
            conn = MySQLdb.connect(host='119.29.9.37', user='gushequ', passwd='gushequ123', charset='utf8',port=3306)
            cur = conn.cursor()
            # cur.select_db('mysql')
            conn.select_db('gushequ')
            # id,post_author,post_date,post_date_gmt,post_content,post_title,post_excerpt,post_status,comment_status,ping_status,post_password
            # post_name,to_ping,pinged,post_modified,post_modified_gmtpost_content_filtered,post_parent,guid,menu_order
            # post_type,post_mime_type,comment_count
            value = [date,title,url,content]
            cur.execute("insert into gushequ(post_date,post_title,url,post_content) values(%s,%s,%s,%s);", value)
            conn.commit()
            cur.close()
            conn.close()
        except MySQLdb.Error, e:
            print 'Mysql Error Msg:', e

    def getArticleDetail(self,url):
        html = self.getHtml(url)
        articleDetail = re.findall(r'<div class="entry-content">(.*?)<div class="open_social_box share_box">',html,re.S)
        return articleDetail[0]

    def getImages(self,url,html):
        imgUrl = re.findall('src="http://www.zixinke.cn/wp-content/uploads/2016/11/(.*?)" alt="', html, re.S)
        return imgUrl

if __name__ == '__main__':
    gushequ = GuSheQu()
    allPageUrl =  gushequ.changePage(url,4)
    for pageUrl in allPageUrl:
        print "\n" + pageUrl + ":"
        html = gushequ.getHtml(pageUrl)    ## 获取网站源代码

        allArticleUrl = gushequ.getArticleUrl(html)   ## 网站内的文章url
        # for articleUrl in allArticleUrl:
        #     print articleUrl
        #
        allArticleTitle = gushequ.getArticleTitle(html)
        # for ArticleTitle in allArticleTitle:
        #     print ArticleTitle

        for i in range(4):
            date = gushequ.getArticleDate(allArticleTitle[i])
            print date + " " + allArticleTitle[i] + " " + allArticleUrl[i]


        # for i in range(len(allArticleUrl)):
        #     try:
        #         date = gushequ.getArticleDate(allArticleTitle[i])  ##获取文章日期
        #     except IndexError as e :
        #         date = '20100000'
        #         print e
        #     title = allArticleTitle[i]
        #     url = allArticleUrl[i]
        #     content = gushequ.getArticleDetail(allArticleUrl[i])
        #     print "插入数据: %s" % title
        #     gushequ.insertInfo(date, title, url, content)

        # 保存图片文件到本地

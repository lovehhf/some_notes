#-*- coding:utf-8 -*-

import re

rep = {"base_resp":{"ret":0,"errmsg":"ok"},"enabled":1,"is_fans":1,"nick_name":"小飞同学～","logo_url":"http:\/\/wx.qlogo.cn\/mmhead\/ibhzWy4ibIEpA9VTHv0D7ia72mQHVGoGhBxRPEfoIzTwpTbFBC6AQBmvA\/132","my_comment":[],"elected_comment":[{"id":55,"my_id":10,"nick_name":"许数量","logo_url":"http:\/\/wx.qlogo.cn\/mmhead\/DNpG9Rich4OgZECBUjwrY6fxXAhjAWId3I1UCD9r49uE\/132","content":"社区君，你的刘备段子被各大公众号转载了！但是都不报你名字，为你抱不平。","create_time":1482331467,"content_id":"2075688867305881610","like_id":10002,"like_num":199,"like_status":0,"is_from_friend":0,"reply":{"reply_list":[{"content":"其实现在已经好很多了，几年前才惨，段子红人不红，整天跟个怨妇似得在微博上呼唤版权、正义。现在我已经有一定影响力，那些剽窃我内容的也怕被网友监督施压，有人抄袭的话评论席全是帮我说话的吃瓜群众，谢谢你们哩。","uin":2392015180,"create_time":1482331637,"reply_id":1,"to_uin":483283975,"reply_like_num":483}]},"is_from_me":0},{"id":229,"my_id":10,"nick_name":"Emma","logo_url":"http:\/\/wx.qlogo.cn\/mmhead\/LXqicVqwJiatoj5LRPKQkSD0fa4nY9dz4dlcf00QS0dbia6AjtntmrfKQ\/132","content":"我今天就光盯着上证看了，个股都没那么关心，有那么一个时段，我看到橘子在向我招手","create_time":1482331800,"content_id":"6304696658324094986","like_id":10007,"like_num":89,"like_status":0,"is_from_friend":0,"reply":{"reply_list":[{"content":"有一个网友和我说他花了30个亿想要把指数拉到自己预测的点位，结果最后时刻没控制好力度，偏差了一个点，问我能不能看在他的诚意份上，另外送一箱橘子。我听了以后深深的被触动，然后截图发给网警。","uin":2392015180,"create_time":1482332308,"reply_id":1,"to_uin":1467926581,"reply_like_num":317}]},"is_from_me":0},{"id":218,"my_id":166,"nick_name":"马少杰","logo_url":"http:\/\/wx.qlogo.cn\/mmhead\/5vucZpGJiczicUxmrYJMaSibJXFxZJ06WCMoHicyrVT9ocE\/132","content":"今天太忙了，忘了打新……快两年了，一次都没中过，就算是十几万的小散也够背了吧……","create_time":1482331777,"content_id":"294487202904146086","like_id":10008,"like_num":65,"like_status":0,"is_from_friend":0,"reply":{"reply_list":[{"content":"其实我家里人有一个账户，16万，4月份开始打新，打到现在也是一签都没中过，问我是不是券商问题，我说请坚持下去。今年还有最后10天，我真心希望没开过张的都能来一发。","uin":2392015180,"create_time":1482332433,"reply_id":1,"to_uin":68565645,"reply_like_num":276}]},"is_from_me":0},{"id":18,"my_id":30,"nick_name":"@林钊武","logo_url":"http:\/\/wx.qlogo.cn\/mmhead\/ajNVdqHZLLDkGtTL8Gq5mbG1fV0wqzEbrGlRnWEW9qxoOpVCjRr67Q\/132","content":"今晚的标题起得好，一看就想点进来看看究竟是哪几个王八蛋","create_time":1482331370,"content_id":"103620359508459550","like_id":10001,"like_num":216,"like_status":0,"is_from_friend":0,"reply":{"reply_list":[{"content":"陈大概是陈小鲁，李大概是李嘉诚，马有可能是马云，也有可能是马化腾，真相暴露了。\/微笑","uin":2392015180,"create_time":1482331490,"reply_id":1,"to_uin":24125995,"reply_like_num":258}]},"is_from_me":0},{"id":443,"my_id":3,"nick_name":"孔曹伟","logo_url":"http:\/\/wx.qlogo.cn\/mmhead\/Q3auHgzwzM4Kh0JhZNTVc4fuFaDbYUH6BgsCfSlTzSCjL5fPtLTFFQ\/132","content":"就想问之前做完床上运动看夜报的兄弟 生活好和谐吗","create_time":1482332480,"content_id":"11240750439580303363","like_id":10011,"like_num":52,"like_status":0,"is_from_friend":0,"reply":{"reply_list":[{"content":"那都是说说的，别当真，我夜报天天写，我就不信有人天天过夫妻生活，就算娶了林志玲也坚持不了。老有人问我性生活怎么样，I don't need sex，yebao fuck me every day\/微笑","uin":2392015180,"create_time":1482332955,"reply_id":1,"to_uin":2617191160,"reply_like_num":208}]},"is_from_me":0},{"id":243,"my_id":57,"nick_name":"Rachel","logo_url":"http:\/\/wx.qlogo.cn\/mmhead\/Q3auHgzwzM6zulc5Hia1PibVBd9tmOvxSLDBCTf3UTkyaECQiacMkhnqA\/132","content":"今年打新一只没中，终于中了一箱橘子。也算坚持总有回报吧。\/呲牙\/呲牙\/呲牙","create_time":1482331822,"content_id":"5223664552540897337","like_id":10006,"like_num":151,"like_status":0,"is_from_friend":0,"reply":{"reply_list":[{"content":"妹纸是1\/40？厉害啊，我算了算我这个中奖概率也不是很高，大概0.4%，比新股还难中，希望橘子能给你带来好运，早些中新股。","uin":2392015180,"create_time":1482332091,"reply_id":1,"to_uin":1216229180,"reply_like_num":130}]},"is_from_me":0},{"id":46,"my_id":7,"nick_name":"powerdavid","logo_url":"http:\/\/wx.qlogo.cn\/mmhead\/VVabiaQiaib5CQrpNYu2UBRyGHMsATLdaicHF6PZAC6DXia4\/132","content":"為啥有人估得那麼精準","create_time":1482331454,"content_id":"1765310586054246407","like_id":10003,"like_num":79,"like_status":0,"is_from_friend":0,"reply":{"reply_list":[{"content":"有一个名词叫做随机冠军，你让10000个小学生炒股，每年其中都会出几个赚五六倍的股神。","uin":2392015180,"create_time":1482331708,"reply_id":1,"to_uin":411018400,"reply_like_num":130}]},"is_from_me":0},{"id":23,"my_id":17,"nick_name":"anhei","logo_url":"http:\/\/wx.qlogo.cn\/mmhead\/PiajxSqBRaELZicyM8lSy8pumwALvrsZbFcVibOkAsicx12AEDKdATibQSg\/132","content":"竟然有人比我还准！以为自己橘子吃定了！3137.84都吃不到。","create_time":1482331395,"content_id":"2915041149003497489","like_id":10004,"like_num":74,"like_status":0,"is_from_friend":0,"reply":{"reply_list":[{"content":"最后报名参加的人超过9000人，基本上差距超过0.14点就入不了围了，你这个不冤，距离还挺远。明年如果发400箱的话大家中奖概率就高多了，你们记得要为我发功啊。","uin":2392015180,"create_time":1482331856,"reply_id":1,"to_uin":678710907,"reply_like_num":118}]},"is_from_me":0},{"id":209,"my_id":13,"nick_name":"许东","logo_url":"http:\/\/wx.qlogo.cn\/mmhead\/0xHguB4ToReAiaz8y4CRYMzdJQm2M7GtDPHzdLcvNvSM\/132","content":"最后那段，另外还有两个事给大家说下……，只说了一件啊","create_time":1482331770,"content_id":"2795901303128064013","like_id":10009,"like_num":60,"like_status":0,"is_from_friend":0,"reply":{"reply_list":[{"content":"啊......我忘记写另一个事了，是在集思录上看到有股民去世，密码家里人不知道，钱很难取出来。我想建议大家把自己资金密码什么的发一份邮件，给自己的配偶，但又觉得邮箱可能不安全，没想好怎么办，就忘记写了。但这事大家还真得好好想想，不可不防。","uin":2392015180,"create_time":1482332550,"reply_id":1,"to_uin":650971500,"reply_like_num":114}]},"is_from_me":0},{"id":404,"my_id":44,"nick_name":"张小妹","logo_url":"http:\/\/wx.qlogo.cn\/mmhead\/Q3auHgzwzM4Dw6GvKX0DSxkhbkscOeL5ZU0Pg3EsTXEPKibSgic90PRA\/132","content":"“明年如果发4000箱的话中奖概率就高了”哈哈哈哈哈哈，为毛我看到这句话笑得停不下来～","create_time":1482332306,"content_id":"10541169501934714924","like_id":10013,"like_num":48,"like_status":0,"is_from_friend":0,"reply":{"reply_list":[{"content":"妹纸，饭可以乱吃，话不能乱讲，你这条留言差点把我尿都吓出来，我特地掏出手机确认，我说的是400，不是4000，差一个零真的会死人的\/衰","uin":2392015180,"create_time":1482333336,"reply_id":1,"to_uin":2454307280,"reply_like_num":82}]},"is_from_me":0},{"id":244,"my_id":11,"nick_name":"J","logo_url":"http:\/\/wx.qlogo.cn\/mmhead\/j0L9PsEsTLgHwvG7ae0ibJnUcTBibe2h7Wia2rgbt85WVM\/132","content":"长城信息不是要13.04增发么？怎么股价一直在13以下","create_time":1482331824,"content_id":"1228145017822904331","like_id":10005,"like_num":45,"like_status":0,"is_from_friend":0,"reply":{"reply_list":[{"content":"爱情不是你想买，想买就能买，定增也一样，不要以为定增方案抛出来了就一定可以成功发行，每年有一个比例的发行失败，超过10%呢。而且有时候实在没办法还会调低发行价。","uin":2392015180,"create_time":1482332013,"reply_id":1,"to_uin":285949795,"reply_like_num":65}]},"is_from_me":0},{"id":448,"my_id":33,"nick_name":"Grace（CooperVision)","logo_url":"http:\/\/wx.qlogo.cn\/mmhead\/yYI4pIsF7XFJ7egAZ9xqDprHkfWLK8Thx5NURe1XCgAnrLok7OTldQ\/132","content":"橘子吃不到了，给我们介绍个买正宗橘子的卖家，就当是补偿我们吧","create_time":1482332499,"content_id":"12833798485916516385","like_id":10010,"like_num":53,"like_status":0,"is_from_friend":0,"reply":{"reply_list":[{"content":"我也不敢随便介绍，我这次的40箱是找我妈妈原先单位经常买的一个果农买的，100元一箱还是人情价，今年据说是小年，产量不多。很多果农自己的橘子卖光了，就在周边跟风种的果农那里收购一些，味道自然就会差一些。","uin":2392015180,"create_time":1482332791,"reply_id":1,"to_uin":2988101562,"reply_like_num":44}]},"is_from_me":0},{"id":415,"my_id":40,"nick_name":" Mic.Chen","logo_url":"http:\/\/wx.qlogo.cn\/mmhead\/Q3auHgzwzM4roibPib6bGDmnODbI9LN5mT8UxZVWOS6km9ska0E7PbXw\/132","content":"社区君怎么做的比特币啊？？求扫盲","create_time":1482332344,"content_id":"9504001557843148840","like_id":10012,"like_num":34,"like_status":0,"is_from_friend":0,"reply":{"reply_list":[{"content":"很多人都问过我在哪里交易比特币，是这样，比特币没有官方平台，只有民间平台。所有的民间平台都有一个问题，就是缺乏监管，理论上公司都有跑路的可能性。所以我自己也就小仓位玩，至于公开推荐是真不方便。他们也找过我，说开一个户给我100，我说我自己在你们那里炒没问题，广告不接。","uin":2392015180,"create_time":1482333191,"reply_id":1,"to_uin":2212822800,"reply_like_num":50}]},"is_from_me":0},{"id":395,"my_id":14,"nick_name":"简成","logo_url":"http:\/\/wx.qlogo.cn\/mmhead\/gQQO820rz5UxNNWCyv7AMRxpTK5KOzH8vziajauTC3XoBMun8agqlfg\/132","content":"最近在思考：1在股市里真的是大道至简所谓越简单的方法越有效么？2技术分析只是概率，唯有思想才能永恒？之所以想这两个问题就是因为股市里七亏两平一赚这个事实让我反思，股市里亏的这些人应该很多也是每天钻研技术分析、基本面分析甚至通宵达旦的，那么最终还是这个比例，多数人整体下来还是在亏，这是不是能说明我们多数人所掌握的所谓的技术和方法还无法战胜这个变幻莫测的市场呢，或者说是我们的思想出了问题比如对股市的预期收益率过高，或者说人本性的贪婪？社区君怎么看 求认真回答！ 求翻出来！！！","create_time":1482332267,"content_id":"9445834536580546574","like_id":10014,"like_num":36,"like_status":0,"is_from_friend":0,"reply":{"reply_list":[{"content":"首先，A股其实并没有7亏2平1赚那么残酷，那都是没根据的段子，A股长期看是正向市场，盈利的人肯定比10%要多。散户如果均匀入场的话，盈利比例比这个还要高，之所以亏的人多，是因为每次散户总是在股市最热的年份集体入场，比如2007、2015,。","uin":2392015180,"create_time":1482333476,"reply_id":1,"to_uin":2199279735,"reply_like_num":33}]},"is_from_me":0},{"id":630,"my_id":36,"nick_name":"NeverSayNever","logo_url":"http:\/\/wx.qlogo.cn\/mmhead\/s1tuxlxz2ibIENEwsR4hmNH9mzcg5uxB9gV2VicQIx0A8\/132","content":"看你邮箱就知道你叫刘超，对不对，哈哈","create_time":1482333706,"content_id":"54774684293529636","like_id":10015,"like_num":22,"like_status":0,"is_from_friend":0,"reply":{"reply_list":[{"content":"本人姓李，其实那三个操纵A股的恶庄里面的那个李，不一定是李嘉诚，呵呵，给你一个零下18度的微笑\/微笑 今晚到这，大家散伙睡觉\/月亮\/月亮","uin":2392015180,"create_time":1482333815,"reply_id":1,"to_uin":12753225,"reply_like_num":26}]},"is_from_me":0},{"id":581,"my_id":2,"nick_name":"Mountain","logo_url":"http:\/\/wx.qlogo.cn\/mmhead\/Q3auHgzwzM5YTwlGAdj1RI17DqeblEY5VVT9pIZwZEfGAYM6tHP6iaw\/132","content":"我有一点不明白的是，国海消失那两员工，干这事的动机是啥？即便是假章，代持的机构应该也是把款项汇给国海的公司帐，不会汇给他们个人。他们利益在哪啊？","create_time":1482333354,"content_id":"7245037395110789122","like_id":10016,"like_num":16,"like_status":0,"is_from_friend":0,"reply":{"reply_list":[{"content":"如果真的是他们两个人擅自做主的话，那就是希望把业绩给做上去，然后自己拿奖金拿提成？可能都觉得债券风险小，冒冒险也死不了。","uin":2392015180,"create_time":1482333721,"reply_id":1,"to_uin":1686866720,"reply_like_num":23}]},"is_from_me":0}],"friend_comment":[],"elected_comment_total_cnt":16}

commands = rep["elected_comment"]
count = 1

print ('<h2 style="color: #ff4c00;">精选留言:</h2>')
print ("<ul>")
for command in commands:
    try:
        reply_content = re.sub(r"\\","",command["reply"]["reply_list"][0]["content"])
    except IndexError as e:
        reply_content = ""
    command_content = re.sub(r"\\","",command["content"])
    print "<li>" + str(count) + ".\n<blockquote>" + command_content + "</blockquote>"
    print '<span style="color: #ff4c00;">回复：</span>'
    print reply_content +"</li>\n"
    count  += 1

print ("</ul>")


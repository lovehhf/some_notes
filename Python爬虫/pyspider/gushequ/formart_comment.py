#-*- coding:utf-8 -*-

import re

rep = {"base_resp":{"ret":0,"errmsg":"ok"},"enabled":1,"is_fans":1,"nick_name":"小飞同学～","logo_url":"http:\/\/wx.qlogo.cn\/mmhead\/ibhzWy4ibIEpA9VTHv0D7ia72mQHVGoGhBxRPEfoIzTwpTbFBC6AQBmvA\/132","my_comment":[],"elected_comment":[{"id":36,"my_id":126,"nick_name":"英语课代表","logo_url":"http:\/\/wx.qlogo.cn\/mmhead\/kSiaeFj92SMyJccX2tNXX6ElbpJBEB0wFnV6unsEqibia0A3CrCD0tFwg\/132","content":"假如有同行出资一个亿买你的公众号，卖不？你这号值千把万没问题吧？","create_time":1481467490,"content_id":"11964645891463184510","like_id":10003,"like_num":81,"like_status":0,"is_from_friend":0,"reply":{"reply_list":[{"content":"如果只是买我的号，那就卖给他了，我拿1000万给大家发红包，然后我再去写一个号，反正我本来就有一个备用号，还有微博，我大概1-2年就回来了。如果要把我这个人也买了，那我得想想。有风投找我询过价，两三千万估值，但我拒了，因我没想好自媒体融资能干什么，给我钱我也不能一晚写5篇出来。","uin":2392015180,"create_time":1481467887,"reply_id":2,"to_uin":2785736204,"reply_like_num":263}]},"is_from_me":0},{"id":14,"my_id":13,"nick_name":"李","logo_url":"http:\/\/wx.qlogo.cn\/mmhead\/Q3auHgzwzM62ibfLIECASUbrVwZ9sXzeCFIibLVLx9KhDvEoCk7L89Nw\/132","content":"伊利股份怎么看？谢谢！","create_time":1481467395,"content_id":"6205377433684672525","like_id":10001,"like_num":92,"like_status":0,"is_from_friend":0,"reply":{"reply_list":[{"content":"伊利和那几个险资股都不太一样，首先举牌的是阳光保险，还算比较老实规矩的。另外也承诺12个月不增持，大股东的定增也基本上能通过，我觉得和宝能、恒大概念股有区别，但现在风声紧，有可能被波及，但不会深跌的，比如17元以下，毕竟下面有定增方案撑着。","uin":2392015180,"create_time":1481467517,"reply_id":1,"to_uin":1444802022,"reply_like_num":81}]},"is_from_me":0},{"id":47,"my_id":8,"nick_name":"柔情似水","logo_url":"http:\/\/wx.qlogo.cn\/mmhead\/8dibXAaznPOFr29nD2Sp42PCBU5eaH7jFEkjxwIgkHCg\/132","content":"人家美股创新高，为啥A股这鸟样？是不是真的只是一张破纸？真的不如买房啊？","create_time":1481467518,"content_id":"1144703445463203848","like_id":10002,"like_num":84,"like_status":0,"is_from_friend":0,"reply":{"reply_list":[{"content":"别看美股创新高，估值还是我们高。美股那是因为人家慢牛，磨磨蹭蹭，但总能刷新高度，A股是半年透支10年涨幅，然后怂很多年。。。说到底还是我们太活跃，你知道么，创业板的年化换手率，大概是美股的9-10倍。","uin":2392015180,"create_time":1481467677,"reply_id":1,"to_uin":266522040,"reply_like_num":87}]},"is_from_me":0},{"id":194,"my_id":4,"nick_name":"心有戚戚焉","logo_url":"http:\/\/wx.qlogo.cn\/mmhead\/G9HRUGtypQv5unH1z7Gblv9z2703Sj06I7L3yTteIMk\/132","content":"其实宝能和恒大都是含赵量不够","create_time":1481467840,"content_id":"2628197862604804","like_id":10010,"like_num":87,"like_status":0,"is_from_friend":0,"reply":{"reply_list":[{"content":"我喜欢含赵量这个词，哈哈，恒大的保险牌照去年年底才买的，宝能就是泥腿子出身，这两活宝不懂保险和证券两边的潜规则，今年真是各种折腾，现在肯定是上面的赵家长老生气了，以后都很难再扑腾。","uin":2392015180,"create_time":1481468646,"reply_id":1,"to_uin":611925,"reply_like_num":63}]},"is_from_me":0},{"id":376,"my_id":23,"nick_name":"包包","logo_url":"http:\/\/wx.qlogo.cn\/mmhead\/ajNVdqHZLLABuVZtpwIaDndHUnN1f9GQ7fke3yq5RGD5IfwHOZyrvA\/132","content":"股大，如果现在开始定投计划，有没有好的标的投呀？较长期的定投计划～🙏","create_time":1481468687,"content_id":"228548459794268183","like_id":10011,"like_num":31,"like_status":0,"is_from_friend":0,"reply":{"reply_list":[{"content":"我过些天就给大家推荐可以长期定投的阿尔法公募基金，这个我以前答应过大家的，你们少等几天。","uin":2392015180,"create_time":1481468813,"reply_id":1,"to_uin":53213085,"reply_like_num":81}]},"is_from_me":0},{"id":406,"my_id":117,"nick_name":"我是屠三胖","logo_url":"http:\/\/wx.qlogo.cn\/mmhead\/Q3auHgzwzM7NaTaV3hV20bDGSf86ibmAElTiadlB3s9GxSregxTqib8dw\/132","content":"看你的夜报看出来当年明月的感觉了…………股社区，你喜欢读明朝的那些事儿吗？","create_time":1481468875,"content_id":"6426130330268205173","like_id":10013,"like_num":30,"like_status":0,"is_from_friend":0,"reply":{"reply_list":[{"content":"很喜欢那套书，我读过两遍。明朝那些事儿能大火，是因为它降低了历史的阅读门槛，这其实也是我一直在坚持做的，就是降低大家对证券金融的阅读门槛。我不在乎有人评价我的内容只适合小白阅读，我愿意服务小白，只要我自己不是小白就行。","uin":2392015180,"create_time":1481469117,"reply_id":1,"to_uin":1496200061,"reply_like_num":80}]},"is_from_me":0},{"id":28,"my_id":55,"nick_name":"Magus","logo_url":"http:\/\/wx.qlogo.cn\/mmhead\/LHdtlaBo22ejo60WHToWzYuk0sBkSDl7Q5qLSC2N8f93I99IBvBdibA\/132","content":"安邦真是证监会都不敢提吗？","create_time":1481467461,"content_id":"12741448829262364727","like_id":10004,"like_num":75,"like_status":0,"is_from_friend":0,"reply":{"reply_list":[{"content":"一个是安邦的背景硬，二个是安邦做事也比较四平八稳，安邦真正出手抢控股权的，只有民生银行，当时史玉柱急的上蹿下跳，但史玉柱那点能量安邦根本不在乎。至于这次中国建筑就是财务投资，而且投资计划都公开透明，给了证监会足够面子。","uin":2392015180,"create_time":1481467992,"reply_id":1,"to_uin":2966599732,"reply_like_num":74}]},"is_from_me":0},{"id":232,"my_id":65,"nick_name":"安儿","logo_url":"http:\/\/wx.qlogo.cn\/mmhead\/aXUpZVUYfjxFMQibEcgzibytdYWYowQTiaoOfz3SY3KxAVTaFibXUxav5w\/132","content":"你一直说缺口这玩意没意思，但为啥个个股评的都说要补缺口，不是说股市就是心里博弈么？为啥缺口一定要补，谁来补，散户们都是东蹦西窜的，买卖又不是同一阵线！如果你今天心情好，麻烦指点一下，谢谢！","create_time":1481467961,"content_id":"10652345164183371841","like_id":10006,"like_num":44,"like_status":0,"is_from_friend":0,"reply":{"reply_list":[{"content":"你知道一个词叫做自我实现吗？就是一件事情，本身没有绝对OK的客观逻辑，但因为相信它的人太多了，最后它就真的实现了。香港人都很理性吧，也会相信郑少秋的电视剧一播大盘就会跌，可能第一次第二次是巧合，第三次第四次就是自我实现。缺口其实也有些那意思。","uin":2392015180,"create_time":1481468243,"reply_id":1,"to_uin":2480192381,"reply_like_num":69}]},"is_from_me":0},{"id":230,"my_id":58,"nick_name":"李先森， 你好嘢！","logo_url":"http:\/\/wx.qlogo.cn\/mmhead\/Q3auHgzwzM6EXiaGP9wmCpCTuWnsvfwaMQUTpu3aEZCMe25PGyHkXNg\/132","content":"创业板etf指数基金从长远考虑这个点数可不可以入手了？","create_time":1481467960,"content_id":"11317545842107220026","like_id":10007,"like_num":37,"like_status":0,"is_from_friend":0,"reply":{"reply_list":[{"content":"如果是定投，我觉得可以开始了，如果是重仓一把梭，我觉得目前的位置高了些。","uin":2392015180,"create_time":1481468277,"reply_id":1,"to_uin":2635071483,"reply_like_num":56}]},"is_from_me":0},{"id":239,"my_id":32,"nick_name":"NeverSayNever","logo_url":"http:\/\/wx.qlogo.cn\/mmhead\/s1tuxlxz2ibIENEwsR4hmNH9mzcg5uxB9gV2VicQIx0A8\/132","content":"隐约觉得下一步官老爷要干游资了……把游资再干了，死鱼不喜欢浪太高，不然会被冲上沙滩","create_time":1481467977,"content_id":"54774684293529632","like_id":10005,"like_num":55,"like_status":0,"is_from_friend":0,"reply":{"reply_list":[{"content":"今年已经干了好几次游资了，罚款都罚了好几个，一些一线游资都潜水了，现在又在打击温州配资，基本上谁目标大就整谁，谁投机就弄死谁。","uin":2392015180,"create_time":1481468067,"reply_id":1,"to_uin":12753225,"reply_like_num":55}]},"is_from_me":0},{"id":460,"my_id":10,"nick_name":"      ","logo_url":"http:\/\/wx.qlogo.cn\/mmhead\/Q3auHgzwzM7jCp5Ch4DicRl93DADxS9eGzxL7pRBicic8icd0GjxufiaBoA\/132","content":"那个橘子40块钱一箱呀，哈哈今天我妈带了一箱回来","create_time":1481469304,"content_id":"9608025236255539210","like_id":10016,"like_num":17,"like_status":0,"is_from_friend":0,"reply":{"reply_list":[{"content":"40块一箱估计是不太好的，今年临海橘子小年，好的都要80-100一箱，我已经让老家朋友帮我联系了，下周咱们就玩起来，我先买30箱发给大家。主要运费贵，我全部下来大概要花4000+。今晚就这，大家睡吧\/再见\/再见","uin":2392015180,"create_time":1481469555,"reply_id":1,"to_uin":2237042700,"reply_like_num":54}]},"is_from_me":0},{"id":219,"my_id":22,"nick_name":"方浩","logo_url":"http:\/\/wx.qlogo.cn\/mmhead\/R1AmOVtdvloVP4iaMKqQm9pPt92TBZVfYuBErGnoYy50\/132","content":"解读一下st川化吧，很多人对这个重整方案有疑问","create_time":1481467931,"content_id":"1455298622563287062","like_id":10009,"like_num":29,"like_status":0,"is_from_friend":0,"reply":{"reply_list":[{"content":"送股通常都会除权，比如股价10元，10送10，那以后开盘价就是5元。送股不除权，意思就是开盘价是10元，然后暴跌50%，这就是除权和不除权的区别。但实际交易中可能不会跌50%，因为总有不明真相的群众冲进去捡便宜，他们看到跌40%就忍不住想买。","uin":2392015180,"create_time":1481468446,"reply_id":1,"to_uin":338838115,"reply_like_num":43}]},"is_from_me":0},{"id":231,"my_id":8,"nick_name":"路西法","logo_url":"http:\/\/wx.qlogo.cn\/mmhead\/ajNVdqHZLLBGgMqH4pOKO32KJiaCHvjLTtGUJicOFQUMkJUhibJwIy6IQ\/132","content":"任小姐，为什么你列的港资购买的股票有沪市的？不是深港通港资只能买深市股票吗？","create_time":1481467960,"content_id":"81574979572858888","like_id":10008,"like_num":34,"like_status":0,"is_from_friend":0,"reply":{"reply_list":[{"content":"表格包括深港通和沪港通，所以有上交所的股票，但不影响我要表达的意思。","uin":2392015180,"create_time":1481470118,"reply_id":2,"to_uin":18993155,"reply_like_num":7}]},"is_from_me":0},{"id":360,"my_id":25,"nick_name":"S. Zhang","logo_url":"http:\/\/wx.qlogo.cn\/mmhead\/Q3auHgzwzM5OELsLV7asTT4Ne5kicYxW7LpytpufhAW4lbicGJvhvzRg\/132","content":"现在看大盘看哪个版指比较准","create_time":1481468554,"content_id":"7782129416322154521","like_id":10012,"like_num":32,"like_status":0,"is_from_friend":0,"reply":{"reply_list":[{"content":"看单一股指肯定是不行的，一个成熟的股民至少要看上证指数、沪深300、中小板指、创业板指、中证500这5个指数，如果你嫌麻烦，也要看沪深300和创业板指。","uin":2392015180,"create_time":1481470022,"reply_id":2,"to_uin":1811918201,"reply_like_num":10}]},"is_from_me":0},{"id":389,"my_id":22,"nick_name":"MoCuishle","logo_url":"http:\/\/wx.qlogo.cn\/mmhead\/NGhmO7N2Uiaey8vDGjv9Jy3QByKUVOldvr6CvzHYvibk8\/132","content":"长城信息算中小创吗，要坐牢到什么时候\/发抖","create_time":1481468781,"content_id":"139470193830133782","like_id":10014,"like_num":28,"like_status":0,"is_from_friend":0,"reply":{"reply_list":[{"content":"根据我得到的信息来判断，20日前后大概能复牌，我对盈利的预期已经重新调整回5-7%了....\/擦汗","uin":2392015180,"create_time":1481469240,"reply_id":1,"to_uin":32472935,"reply_like_num":28}]},"is_from_me":0},{"id":451,"my_id":7,"nick_name":"勇","logo_url":"http:\/\/wx.qlogo.cn\/mmhead\/AYfn0IKjIIOPDg0ezp1QgqqsJwuArr9JQY7dSaGmIsxbsGmnTACn0g\/132","content":"恒大凭他幕后股东份量，那是不输国家队的安邦呀，怎么能把他和泥腿子的宝能放一起说含赵量。","create_time":1481469240,"content_id":"10124198361553698823","like_id":10017,"like_num":19,"like_status":0,"is_from_friend":0,"reply":{"reply_list":[{"content":"对安邦背景有兴趣的，到我的微博，搜索关键词“八卦”，然后看2014年12月18日的那篇。","uin":2392015180,"create_time":1481469336,"reply_id":1,"to_uin":2357223621,"reply_like_num":26}]},"is_from_me":0},{"id":355,"my_id":40,"nick_name":"luyun","logo_url":"http:\/\/wx.qlogo.cn\/mmhead\/Q3auHgzwzM4IfmXP55yiciah15ZEEiaeJK8FCibbYpDTQsibtfe8jfSadeA\/132","content":"美的啥时候卖呀，周五已经回本了。","create_time":1481468511,"content_id":"7699492780963266600","like_id":10015,"like_num":19,"like_status":0,"is_from_friend":0,"reply":{"reply_list":[{"content":"我周五一度有盈利的，没卖....结果周末就传来噩耗，虽然直接利空是格力，但美的肯定也有影响，只能继续扛着看看了。\/难过","uin":2392015180,"create_time":1481468984,"reply_id":1,"to_uin":1792677860,"reply_like_num":26}]},"is_from_me":0},{"id":500,"my_id":63,"nick_name":"happy","logo_url":"http:\/\/wx.qlogo.cn\/mmhead\/Q3auHgzwzM681TdszZQcXMCIVwlUrZvofyfDicQpPlVvpDSJycvTfKw\/132","content":"说明董小姐比王石厉害？","create_time":1481469899,"content_id":"8403841660588392511","like_id":10018,"like_num":4,"like_status":0,"is_from_friend":0,"reply":{"reply_list":[{"content":"其实也不能这么说，圣斗士星矢里面有这么一段情节，和冥斗士打，第一个冲上的同伴被对方的绝招打残，然后第二个冲上的就把对方打残，其实大家水平差不多，但里面有一句台词是：对圣斗士来说，同样的招数第二次就不灵了。\/哈欠这下真的睡了，不翻了。","uin":2392015180,"create_time":1481470592,"reply_id":1,"to_uin":1956671863}]},"is_from_me":0},{"id":504,"my_id":47,"nick_name":"生  ","logo_url":"http:\/\/wx.qlogo.cn\/mmhead\/FIJH8afv77Ylhe1akGjoVAd18ic4ppVWB6A204FM9gBc\/132","content":"今天没说左侧模型？","create_time":1481469933,"content_id":"2535711132069396527","like_id":10019,"like_num":2,"like_status":0,"is_from_friend":0,"reply":{"reply_list":[{"content":"补充一下，依然看多，但这次周中可能会有更新。","uin":2392015180,"create_time":1481470452,"reply_id":1,"to_uin":590391255,"reply_like_num":2}]},"is_from_me":0}],"friend_comment":[],"elected_comment_total_cnt":19}


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
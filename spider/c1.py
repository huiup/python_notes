from urllib import request
import re
class Spider():
    url = 'https://www.huya.com/g/lol'
    # url = 'https://www.douyu.com/g_LOL'
    pattern_str = '<span class="txt">([\s\S]*?)</li>'
    name_pattern = '<i class="nick" title="([\s\S]*?)">'
    number_pattern = '<i class="js-num">([\s\S]*?)</i>'
    # pattern_str = '<div class="DyListCover-info">[\s\S]*?</div>'
    def __fetch_content(self):
        r = request.urlopen(Spider.url)
        htmls = r.read()
        htmls_str = str(htmls, encoding='utf-8')
        return htmls_str
    def __analysis(self,htmls):
        root_html = re.findall(Spider.pattern_str, htmls)
        results = []
        for html in root_html:
            name = re.findall(Spider.name_pattern, html)
            number = re.findall(Spider.number_pattern, html)
            res = {'name' : name, 'number' : number}
            results.append(res)
        return results
    
    def __refine(self,results):#数据精炼
        #{'name': ['爱拍-古手羽'], 'number': ['248.3万']}
         l = lambda res : {
            'name' : res['name'][0],#.strip()去空格/换行
            'number' : res['number'][0]#转换为字符串
         }
         return map(l, results)

    def __sort(self,results):
        #指定sorted()按照number大小排序
        results = sorted(results, key=self.__sort_seed, reverse=True)
        return results

    def __sort_seed(self, result):
        r = re.findall('\d*', result['number'])
        number = float(r[0])
        if '万' in result['number']:
            number *= 10000
        return number
    def __show(self, results):
        """ 
        i = 1
        for result in results:
            print('第'+ str(i) +'名：'+result['name']+'---------------'+result['number'])
            i+=1 
        """
        for rank in range(0,len(results)):
            print('rank '+str(rank+1)
                +':' + results[rank]['name']
                +'----'+results[rank]['number'])

    def go(self):
        htmls = self.__fetch_content()
        results = self.__analysis(htmls)
        results = list(self.__refine(results))
        results = self.__sort(results)
        results = self.__show(results)
        # print(results)
spider = Spider()
spider.go()
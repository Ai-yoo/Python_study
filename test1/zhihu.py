import urllib
from urllib import request
import time
import requests
import re

'''
下载图片方法
'''
def download_img(url,x):
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36'
    }
    request = urllib.request.Request(url, None, header)
    response = urllib.request.urlopen(request)
    with open('img/%s.jpg' %x, "wb") as f:
        f.write(response.read())


'''
获取网页html
'''
def get_html(url):
    response=requests.get(url)
    html=response.text
    return html

'''
链接去重
'''
def distinct(imglist):
    new_imglist=list(set(imglist))
    new_imglist.sort(key=imglist.index)
    return new_imglist


def main():
    urls=['https://www.zhihu.com/api/v4/questions/26541011/answers?include=data%5B%2A%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%3Bdata%5B%2A%5D.mark_infos%5B%2A%5D.url%3Bdata%5B%2A%5D.author.follower_count%2Cbadge%5B%2A%5D.topics&limit=5&offset={0}&sort_by=default'.format(str(i)) for i in range(0,6850,5)]
    global x
    x=0
    for url in urls:
        print(x)
        page=request.urlopen(url)
        html_byte=page.read()
        reg=r'https://pic[0-9]{1}\.zhimg\.com/v2-[a-z|0-9]{32}_r\.jpg'
        reg_img=re.compile(reg)
        html=str(html_byte,encoding='utf-8')
        imglist=distinct(reg_img.findall(html))
        print(len(imglist))
        for img in imglist:
            try:
                download_img(img,x)
                x += 1
                # print(img)
            except OSError:
                pass
            continue
    print('总共：',x)



start_time=time.strftime("%H:%M:%S")
main()
end_time=time.strftime("%H:%M:%S")
with open('time.txt','w') as f:
    f.write(start_time)
    f.write('\n')
    f.write(end_time)
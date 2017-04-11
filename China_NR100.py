import re
import urllib.request
import sys

def getdeta(event,gender,type,rank):
    #获取WCAID
    count = 0
    url='https://cubingchina.com/results/rankings?region=China&event='+event+'&gender='+gender+'&type='+type
    con = urllib.request.urlopen(url)
    html = con.read().decode("UTF-8")
    re_id = re.compile(r'(?<=/results/person/)[0-9]{4}[A-Z]{4}[0-9]{2}')
    #匹配WCAID的正则
    id_list = re_id.findall(html)

    for id in id_list:
        #获取姓名和地区
        url='https://cubingchina.com/results/person/'+id
        con = urllib.request.urlopen(url)
        html = con.read().decode("UTF-8")
        re_region = re.compile(r'中国 *(安徽|北京|福建|甘肃|广东|广西|贵州|海南|河北|河南|黑龙江|湖北|湖南|吉林|江苏|江西|辽宁|内蒙古|宁夏|青海|山东|山西|陕西|上海|四川|天津|西藏|新疆|云南|浙江|重庆)')
        re_name = re.compile(r'(?<=<h1 class="text-center">).*(?=</h1>)')
        #匹配地区和姓名的正则
        region = re_region.findall(html)
        name = re_name.findall(html)
        sys.stdout.write(id+'\r')
        for ones in name:
            file.write (ones+',')
        file.write (id+',')
        for ones in region:
            file.write (ones)
        file.write ('\n')
        count += 1
        if count == int(rank):
            break

#主函数
#查询参数字典
gender={'0':'all','1':'male','2':'female'}
type={'0':'single','1':'average'}

#欢迎语
welcome='''
##################################
#   China NR100 Crawler By CSL   #
#                                #
# Gender:0-all;1-male;2-female   #
# Type:0-single;1-average        #
#                           V1.0 #
##################################
'''

print(welcome)

#输入查询参数
event=input("Event:")
g_id=input("Gender:")
t_id=input("Type:")
rank=input("Rank:")

file=open(event+'_'+gender[g_id]+'_'+type[t_id]+'.csv','w')
file.write ('Person,WCAID,Region\n')
getdeta(event,gender[g_id],type[t_id],rank)
file.close
input("Press any key to continue...")

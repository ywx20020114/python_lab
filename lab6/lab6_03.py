import os.path
import urllib.request

cache_path = "cache"  # cache是一个保存html文件的缓存文件夹

#  编写装饰器，实现缓存网页内容功能
def decorator(func):
    def wrapper(*args):
        if os.path.exists(cache_path + "//" + args[0].replace('/','_').replace(':','_').replace('.','_') +".html"):
            print("缓存中存在文件")
            return
        else:
            print("未在缓存中发现目标网页，正在下载......")
            func(*args)
            print("下载成功")
    return wrapper

# 下载网页
@ decorator
def download(url):
    html = urllib.request.urlopen(url).read()
    with open(cache_path + "//" + url.replace('/','_').replace(':','_').replace('.','_') +".html","wb") as f:
        f.write(html)

print("第一次下载")
download('https://nankai.feishu.cn/docx/MgQadT40MogVvsxPTpzcIgebnMf')
print("-------------------------------------------------------")
print("第二次下载")
download('https://nankai.feishu.cn/docx/MgQadT40MogVvsxPTpzcIgebnMf')




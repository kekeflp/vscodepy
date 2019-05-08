import os
import urllib.request
import re

# 打开网页并获取网页源码


def OpenUrlRes(url):
    req = urllib.request.Request(url)
    req.add_header(
        "User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.63 Safari/537.36 Qiyu/2.1.1.2")
    response = urllib.request.urlopen(req)
    htmlMsg = response.read()
    return htmlMsg

# 在网页源码中，查找图片网站


def GetPicAddr(url):
    html = OpenUrlRes(url).decode("utf-8")
#    pattern = re.compile(r"https{0,1}://\S*(.jpg|.png)")
    pictureAddr = re.findall(r"https{0,1}://isujin.com/wp-content/uploads\S*(.jpg|.png)", html)
    print(str(pictureAddr))


def SavePic(url):
    pass


def DownloadPic(folder="WallPaper", page=10):
    os.mkdir(folder)
    os.chdir(folder)

    url = "https://isujin.com/5882"

    GetPicAddr(url)


if __name__ == "__main__":
    DownloadPic()

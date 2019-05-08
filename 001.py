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
    # https{0,1}://isujin.com/wp-content/uploads\S*(.jpg|.png)
    # [a-zA-z]+://[^\s]*\d{4}.jpg
    pictureAddr = re.findall(
        r"https{0,1}://isujin.com/wp-content/uploads\S*.jpg", html)
    return pictureAddr

# 把图片下载并存入文件夹中


def SavePic(url):
    for item in GetPicAddr(url):
        filename = item.split("/")[-1]
        with open(filename, "wb") as f:
            pictrue = OpenUrlRes(item)
            f.write(pictrue)


def DownloadPic(folder="WallPaper", page=10):
    os.mkdir(folder)
    os.chdir(folder)

    url = "https://isujin.com/5882"

    GetPicAddr(url)
    SavePic(url)


if __name__ == "__main__":
    DownloadPic()

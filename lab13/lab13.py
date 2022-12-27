
import threading
import FileOperator

# 多线程拷贝
def MutiThreadCopy(mp4List, outputPath):
    t = threading.Thread(target=FileOperator.CopyFile, args=(mp4List, outputPath))
    t.start()
    t.join()

# 将生成的视频拷贝到指定目录
def Copy(mp4List, outputPath):
    print("进入目录：{0}".format(outputPath))
    print("开始复制")
    MutiThreadCopy(mp4List, outputPath)  # 多线程复制
    print("复制完毕！")

if __name__ == '__main__':
    downloadPath = input("请输入原视频地址")
    outputPath = input("请输入目的存储地址")
    dviInfoList = FileOperator.GetDviInfo(downloadPath)  # 获取dvi文件信息
    if dviInfoList[0] is False:
        print('没有找到.dvi文件！请检查下载目录后重试！')

    else:
        # 在outputDir下新建名为dvi[3]文件夹
        try:
            outputPath = FileOperator.MakeDir(outputPath, dviInfoList[3])
        except Exception as e:
            print( "错误", "已经存在同名文件夹！ Error：" + str(e))

        print("开始遍历获取BV:{0}, 标题:{1} 的所有视频标题,请稍后...".format(dviInfoList[1], dviInfoList[3]))
        localVideoTitleList = FileOperator.GetLocalVideoTitle(downloadPath, dviInfoList[2])
        fileName = FileOperator.GetHtml(localVideoTitleList, dviInfoList[3], outputPath)
        print('已成功获取文件:  {0} ！'.format(fileName))


        # 找到所有downloadPath的.mp4文件
        mp4List = FileOperator.FindSpecialMp4Files(downloadPath, dviInfoList[2])[0]  # mp4真正在的地方
        mp4nameList = FileOperator.FindSpecialMp4Files(downloadPath, dviInfoList[2])[1]
        try:
            mp4nameList.sort(key=FileOperator.GetSeries)
        except Exception as e:
            print( "错误", "存在干扰文件！排序错误，请联系作者！" + str(e))

        s = "查询到以下mp4文件：\n"
        for item in mp4nameList:
            s += (item + '\n')
        print(s)

        # 进行文件解密
        print("开始解密...")
        FileOperator.DecryptMp4(downloadPath, dviInfoList[2])
        print("解密完毕！")
        # 复制
        Copy(mp4List, outputPath)

        # 重命名
        print("开始重命名...")
        FileOperator.DoRename(outputPath, fileName, dviInfoList[2], True)
        print("重命名完毕！")



"""
需要备份的文件和目录由一个列表指定。

备份应该保存在主备份目录中。

文件备份成一个zip文件。

zip存档的名称是当前的日期和时间。

我们使用标准的zip命令，它通常默认地随Linux/Unix发行版提供。Windows用户可以使用Info-Zip程序。注意你可以使用任何地存档命令，
只要它有命令行界面就可以了，那样的话我们可以从我们的脚本中传递参数给它。
"""

import zipfile
def zip_files(files, zip_name):
    zip = zipfile.ZipFile( zip_name, 'w')
    for file in files:
        print ('compressing', file)
        zip.write( file )
    zip.close()
    print ('compressing finished')


files = ['D:\I\'M\\usedbypython\\1.txt']#文件的位置，多个文件用“，”隔开
zip_file = 'D:\I\'M\\usedbypython\\2.zip'#压缩包名字
zip_files(files, zip_file)
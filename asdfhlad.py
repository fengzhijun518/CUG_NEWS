import os.path
import re
import shutil
from win32com import client as wc

# 将doc文件转换为txt文件


def tran(path):
    files = os.listdir(path)        # 得到当前目录下所有文件的名字
    word = wc.Dispatch('Word.Application')
    for file in files:              # 遍历所有的文件
        new = '{}\\{}'.format(path, file)       # 生成完整的文件路径
        print(new)
        doc = word.Documents.Open(new)          #
        tmp = file[:-4]                         # 取文件名字的倒数后四位之前的所有
        new_file_path = os.path.join(r'C:\Users\Administrator\Desktop\案例\txt')  # 新路径（保存用）
        doc.SaveAs('{}\\{}.txt'.format(new_file_path, tmp), 4)                    # 保存文件
        doc.Close()

# 移动匹配文件到指定文件夹


def movefile(path):
    files = os.listdir(path)
    for file in files:
        new = '{}\\{}'.format(path, file)
        file_name = re.findall(r'走私[武器弹药]', file)      # 在文件名中匹配是否有危险两个字
        print(new)
        print(file_name)
        if file_name:
            new_file_path = os.path.join(r'C:\Users\Administrator\Desktop\案例\走私\走私武器、弹药')
            shutil.move(new, new_file_path)


if __name__ == '__main__':
    tran(r'C:\Users\Administrator\Desktop\案例\金融凭证诈骗')
    # movefile(r'C:\Users\Administrator\Desktop\案例\走私\判决书')
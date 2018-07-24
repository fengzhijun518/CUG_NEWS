import os.path
import re
import shutil
from win32com import client as wc
import time


def eachFile(filepath):
    pathDir = os.listdir(filepath)
    a = 0
    word = wc.Dispatch('Word.Application')
    for allDir in pathDir:
        child = os.path.join('%s\%s' % (filepath, allDir))
        # time.sleep(3)
        if os.path.isfile(child):
            doc = word.Documents.Open(child)
            tmp = child[:-4]
            new_name = '{}.txt'.format(tmp)
            new_file_path = os.path.join(r'C:\Users\Administrator\Desktop\案例\2')
            doc.SaveAs('{}\\{}'.format(new_file_path,new_name), 4)
            doc.Close()


            # shutil.move(new_name, new_file_path)
            word.Quit()


            # 移动文件到指定文件夹
            a += 1
            print(child, a)
            # file_name = re.findall(r'危险', child)
            # print(file_name)
            # if file_name:
            #     new_file_path = os.path.join(r'C:\Users\Administrator\Desktop\案例\1')
            #     shutil.move(child, new_file_path)
            # # readFile(child)
            continue
        eachFile(child)


if __name__ == '__main__':
    filenames = r'C:\Users\Administrator\Desktop\案例\金融凭证诈骗'
    eachFile(filenames)
    print('ok')

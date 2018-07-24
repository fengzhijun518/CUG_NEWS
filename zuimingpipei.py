import os.path
import re


def jiance(path,path1):
    # 读取真实罪名（官方给定的）
    with open(path1, 'r') as file:
        list_acc = file.readlines()
    # print(list_acc)
    list_a = []
    for i in range(len(list_acc)):
        list_a.append(list_acc[i][:-1])
    # print(list_a)

    zuiming = {'伪造公司、企业、事业单位、人民团体印章': ['伪造公司印章','伪造企业印章','伪造事业单位印章','伪造人民团体印章'],
               '非法持有、私藏枪支、弹药':['非法持有枪支','非法私藏枪支','非法持有弹药','非法私藏弹药','非法持有枪支弹药'],
               '制造、贩卖、传播淫秽物品':['制造淫秽物品','贩卖淫秽物品','传播淫秽物品'],
               '伪造、变造、买卖国家机关公文、证件、印章':['买卖国家机关公文、证件、印章','伪造国家机关公文、证件、印章','变造国家机关公文、证件、印章'],
               '走私、贩卖、运输、制造毒品':['走私毒品', '贩卖毒品', '运输毒品','制造毒品'],
               }

    # print(
    #     list(zuiming.keys()),list(zuiming.values())
    # )
    zui_value =list(zuiming.values())
    b = list(zuiming.keys())
    # for i in range(len(zui_value)):
    #     for it in zui_value[i]:
    #         print(it, b[i])


    files = os.listdir(path)
    for file in files:
        new = '{}\\{}'.format(path, file)
        print(new)
        with open(new, 'r') as file_r:
            a = file_r.readlines()
            temp_start = 0
            temp_end = 0
            for i,line in enumerate(a):
                pattern_start = re.findall("判决如下", line)
                if pattern_start:
                    temp_start = i
                    # print(i, line)

                pattern_end = re.findall("如不服本判决", line)
                if pattern_end:
                    temp_end = i
                    # print(i, line)

                pattern_end = re.findall("本判决为终审判决", line)
                if pattern_end:
                    temp_end = i
                    # print(i, line)

            list_re = a[temp_start+1:temp_end]

            time = 1
            for line in list_re:
                # .为占位符号{1,9}匹配中间至少1到9个字
                pattern = re.findall('犯.{1,15}罪', line)
                if pattern and time == 1:
                    time += 1
                    pattern_p = re.findall('犯罪', line)
                    if pattern_p:
                        continue
                    else:
                        # 查看犯罪内容
                        print(pattern)
                        for item in pattern:
                            # print(item[1:-1])
                            if item[1:-1] in list_a:
                                print(item[1:-1])
                                print('ok')
                            else:
                                for i in range(len(zui_value)):
                                    # print(zui_value)
                                    # print(1)
                                    for it in zui_value[i]:
                                        # print(1)
                                        # print(item[1:-1])
                                        # print(it)
                                        pattern_z = re.findall(item[1:-1], it)
                                        # print(pattern_z)
                                        if pattern_z:
                                            print(b[i])
                                            print('change')



# def accu(path):
#     with open(path, 'r') as file:
#         list_acc = file.readlines()
#     return list_acc


if __name__ == '__main__':
    jiance(r'C:\Users\Administrator\Desktop\案例\txt',r'C:\Users\Administrator\Desktop\案例\1\zuiming.txt')
    # print(acc_list[2:10])

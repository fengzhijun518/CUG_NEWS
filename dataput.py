import json
import re
# 列表存储json数据
json_list = []
with open(r"D:\pythneil\spider\cail2018_big.json", encoding='utf-8') as load_f:
    # 逐行读取json数据
    lines = load_f.readlines()
    # for line in lines:
    #     json_list.append(line)
    for line in lines:
        load_dict = json.loads(line)
        json_list.append(load_dict)
print(len(json_list))
print(json_list)
# print(json_list[0])

acc_list = []


# 统计罪名
for i in range(len(json_list)):
    if json_list[i]['meta']['accusation'][0] not in acc_list:
        with open('zuiming.txt', 'a') as file:
            file.write(json_list[i]['meta']['accusation'][0])
            file.write('\n')
        acc_list.append(json_list[i]['meta']['accusation'][0])
print(acc_list)
#


# # 统计关于走私的罪名
# for item in acc_list:
#     find_it = re.findall(r'走私', item)
#     if find_it:
#         print(item)

a = 0
# 根据触犯的罪名来寻找条目  走私即条目
# for i in range(len(json_list)):
#     if json_list[i]['meta']['accusation'][0] == '走私':
#         a += 1
#         # print(json_list[i]['fact'])
#         print(i)
#         with open(r'baozha.txt', 'a') as file:
#             # json_str = json.dumps(json_list[i])
#             file.write(str(json_list[i]))
#             file.write('\n')
#         print(json_list[i])
# print(a)
#

# # 根据触犯的法律条目来寻找数据  151即触犯的第151条
# for i in range(len(json_list)):
#     if json_list[i]['meta']['relevant_articles'][0] == 248:
#         print(json_list[i])
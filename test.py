from rdflib import Graph
import os


# 按字符#分割字符串后保留#后字符串
def sharp(s):
    a = s.split('#')
    return a[-1]


# os.walk方法获取当前路径下的root（所有路径）、dirs（所有子文件夹）、files（所有文件）
def file_name(path):
    F = []
    for root, dirs, files in os.walk(path):
        # print root
        # print dirs
        for file in files:
            # print file.decode('gbk')    #文件名中有中文字符时转码
            if os.path.splitext(file)[1] == '.owl':
                t = file
                print(t)  # 打印所有py格式的文件名
                F.append(os.path.join(path, t))  # 将所有的文件名添加到L列表中
    return F

# 处理owl文件
def owlParse(owlFile):
    g = Graph()

    g.parse(owlFile, format="xml")
    print("开始处理文件：", owlFile)
    for s, p, o in g:
        print("hEntity:", sharp(s), "relation:", sharp(p), "tEntity:", sharp(o))


for file in file_name("C:\\Users\\Jacky\\Desktop\\02RDF文件"):
    owlParse(file)

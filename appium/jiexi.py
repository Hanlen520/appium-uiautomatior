f = open("appium_taobao.txt", "r")
while True:
    line = f.readlines()
    if line:
        pass    # do something here
        line=line.strip()
        p=line.rfind('.')
        filename=line[0:p]
        print("create %s"%line)
    else:
        break
f.close()

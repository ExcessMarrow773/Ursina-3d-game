import init
#f = open('saveFile.txt', "r")
#saveContent = f.read()
#f.close()

saveContent = "{'parent': render/scene, 'position': (14, 3, 14), 'model': 'cube', 'origin_y': 0.5, 'texture': 'minecraft/model5.png', 'color': Vec4(1.0, 1.0, 1.0, 1.0), 'highlight_color': Vec4(1.0, 1.0, 1.0, 1.0), 'shader': <ursina.shader.Shader object at 0x00000244CC95EFD0>}"

content = "{'parent': render/scene,"
# print(content)
print('\n\n')
def parse(c):
    dontParse = ["'", "{", "}"]
    tmp = ''
    saveList = []
    for i in range(len(c)):
        if (c[i] == ' ' and c[i-1] == ':') or c[i] == ',':
            saveList.append(tmp)
            tmp = ''
        elif c[i] not in dontParse:
            tmp = tmp+c[i]
        
    print(saveList)
parse(saveContent)
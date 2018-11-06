#黑灰白红橙黄绿青蓝紫,,# 0,,0,,0,,0,,156,,11,,26,,35,,78,,100,,125,
# 11,,26,,  35,,78,,100,,125,,
# 25,,34；,,77,,99,,124,,155

colors = [];
colors.append([[-10,50,50],[10,255,255]])
colors.append([[11,50,50],[25,255,255]])
colors.append([[26,50,50],[34,255,255]])
colors.append([[35,50,50],[77,255,255]])
colors.append([[78,50,50],[99,255,255]])
colors.append([[100,50,50],[124,255,255]])
colors.append([[125,50,50],[155,255,255]])
colors.append([[0,0,0],[180,255,50]])  #黑
colors.append([[0,0,50],[180,50,220]])  #白
colors.append([[0,0,220],[180,50,255]])  #灰



def getcolorindex(color):
    h = color[0]
    s = color[1]
    v = color[2]

    #对颜色的区间进行拆分
    if(color[0]>=170):
        color[0] = color[0]-180

    for k,v in enumerate(colors):
        # print(k)
        begin = v[0]
        end = v[1]
        if color[0]>=begin[0] and color[1]>=begin[1] \
            and color[2]>=begin[2] and color[0]<=end[0] and color[1]<=end[1] and color[2]<=end[2]:
            return k
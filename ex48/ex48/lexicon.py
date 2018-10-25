def convert_number(s):
    try:
        return int(s)
    except ValueError:
        return None
def scan(direc):
    #通过direc参数，获取对应列表[direction,direc],通过方向参数，得到方向列表，创建字典map，使direc一一对应
    #direc=("north south east"),将direc切片，direc.split,返回结果res列表
    d_split = direc.split()
    map = {'north':('direction','north'),'south':('direction','south'),'east':('direction','east')}

    map_verbs = {'go':('verb', 'go'), 'kill':('verb', 'kill'),'eat':('verb', 'eat')}
    map_stops = {'the':('stop', 'the'),'in':('stop', 'in'),'of':('stop', 'of')}
    map_nouns = {'bear':('noun', 'bear'),'princess':('noun', 'princess')} 
    map.update(map_verbs)
    map.update(map_stops)
    map.update(map_nouns)
    res = []
    for word in d_split:
        if convert_number(word) is None and word in map.keys():
            res.append(map.get(word))
        elif convert_number(word) is None and word not in map.keys():
            res.append(("error",word))
        else:
            res.append(("number",int(word)))
    return res
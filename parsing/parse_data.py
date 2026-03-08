#!/usr/bin/env python3

data = ["width", "height", "entry", "exit", "output_file", "perfect"]

def open_file(file_name):
    with open(file_name, "r") as f:
        data_list = f.read()
    return data_list


def parse_data(file_data: list) -> dict:
    if not file_data:
        raise ValueError("missing config params")
    data_dict = {}
    try:
        for item in file_data:
            parts = item.split("=")
            data_dict[parts[0].lower().strip()] = parts[1]
    except Exception:
        return f"error : you need to entre key = value"
    return data_dict

def check_prop(dict_data):
    data_parssed = {}
    
    for key,val in dict_data.items():
        if key == "width" or key == 'height':
            try:
                check = int(float(val))
                data_parssed[key] = check
            except Exception:
                return f"error : value is not correct"
        elif key == "entry" or key == "exit":
            try:
                dis = val.split(',')
                if len(dis) != 2:
                    raise ValueError("key = (+x,+y)")
                if int(dis[0]) < 0 or int(dis[1]) < 0:
                    raise ValueError("key = (+x,+y)")
                l = [int(dis[0]), int(dis[1])]
                t = tuple(l)
                data_parssed[key] = t
            except Exception:
                return f"Error entre valid value : key = (+x,+y)"
        elif key == "output_file":
            pass
    return data_parssed


f = open_file('config.txt').split('\n')
d = parse_data(f)
a = check_prop(d)
print(a)
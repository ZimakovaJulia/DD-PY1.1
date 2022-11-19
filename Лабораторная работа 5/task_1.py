from pprint import pprint

list_of_dict = []

def dict_num(n):
    dict_ = {}
    dict_["bin"] = bin(n)
    dict_["dec"] = n
    dict_["hex"] = hex(n)
    dict_["oct"] = oct(n)
    return dict_

for i in range(16):
    dict_ = []
    dict_ = dict_num(i)
    list_of_dict.append(dict_)

pprint(list_of_dict)

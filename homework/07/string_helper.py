def csv_to_list(csv):
    split_list = csv.split("\n")
    final_list = []
    for i in range(0,len(split_list)):
        name_list = split_list[i].split(",")
        final_list.append(name_list)
    return final_list

lista = csv_to_list("1,Jussi,Virtanen\n2,Pekka,Keinänen")
print(lista)
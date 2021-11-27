input_list = ['2018-01-01', 'yandex', 'cpc', 100, 200, 300]
input_list.reverse()

list_len = len(input_list)
output_dict = {input_list[1] : input_list[0]}
k = 2

while list_len > k:
    # if k == 0:
    #     output_dict[input_list[k+1]] = input_list[k]
    #     k += 2
    #     print(output_dict)
    output_dict[input_list[k]] = dict(list(output_dict.items()))
    del(output_dict[input_list[k-1]])
    k += 1

print(output_dict)

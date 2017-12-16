# slicing on list and strings


my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print my_list[5]  # 5
# list[start:end:stop]
print my_list[0:5]  # 0-4
print my_list[3:8]  # 3-7
print my_list[5:]   # 5- end
print my_list[1:8:2]  # 1-7 step 2
print my_list[-1:2:-1]  # going revers 9-3
print my_list[-1:2:-2]  # going revers 9-3 step 2

sample_url = 'http://sample.com'

print sample_url[7:]  # without http://
print sample_url[-4:]  # only .com
print sample_url[0::2]  # print every second letter

# for i in range(6,-1,-3):
#     for j in range(1,4):
#         print(f'{i+j}',end=' ')
#     print()

counter = 6
stop = -1
step = -3
while stop < counter:
    inner_counter = 1
    inner_stop = 4
    inner_step = 1
    row = ''
    while inner_stop > inner_counter:
        row += f'{counter + inner_counter}'
        inner_counter += inner_step
    print(row)
    counter += step
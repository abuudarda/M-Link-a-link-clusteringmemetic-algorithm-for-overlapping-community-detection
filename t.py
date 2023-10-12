my_list = [(3, 1), (1, 2), (4, 3), (2, 4)]


# Sort each tuple within the list
# sorted_list = [tuple(sorted(t)) for t in my_list]
# # Sort the list of tuples by both elements of each tuple
# sorted_list = sorted(sorted_list, key=lambda x: (x[0], x[1]))
# for index,edge in enumerate(my_list):
#     if(edge[0]>edge[1]):
#         my_list[index]=(edge[1],edge[0])
# print(my_list)

my_list=[tuple(sorted(t)) for t in my_list]
print(my_list)
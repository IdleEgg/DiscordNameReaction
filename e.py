import random
a_file = open("emoji.txt", "r")

list_of_lists = []
for line in a_file:
  stripped_line = line.strip()
  list_of_lists.append(stripped_line)

a_file.close()





print(random.sample(list_of_lists ,k =1))
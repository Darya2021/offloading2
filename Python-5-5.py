my_class= 'paniz zeinab mahnaz merhara mohamad amin reza'.split(" ")

for index, name in enumerate(my_class):
    if index % 3 != 0:
        print(index,name)

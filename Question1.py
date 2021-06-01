f = open('91social.txt','r');
l = f.readlines();
final_list = [];
for i in l:
    final_list.append(i.strip('\n')); 
print(final_list);
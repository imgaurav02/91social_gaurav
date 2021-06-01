f = open('91social.txt','r');
l = str(f.read())
count =1;
for i in l:
    if(i==' ' or i==','):
        count=count+1
print(count)
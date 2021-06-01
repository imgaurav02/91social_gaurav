import json

d={
    "Name":"Gaurav Singh",
    "RollNo":"200231025",
};

#for user input if wants


# n = int(input());
# for _ in range (n):
#     keys = input()
#     d[keys] = input()
# print(d);

json_var = json.dumps(d,indent=4);
print(json_var);
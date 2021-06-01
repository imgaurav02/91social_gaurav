l = [
        {'make': 'Nokia', 'model': '216', 'color': 'Black'},
        {'make': 'Mi Max', 'model': '2','color': 'Gold'}, 
        {'make': 'Samsung', 'model': '7', 'color': 'Blue'}
    ]
print(sorted(l, key = lambda i: (i['color'])))
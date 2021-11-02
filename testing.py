import requests

A = [[1,13/2,-1,0,0],[2,1,0,-1,0],[5,4,0,0,1]]
b = [5,4,20]
c = [2,1,0,0,0]

r = requests.post('http://localhost/primalsimplex', json={"A" : A,"b" : b,"c" : c})

print(r.json())

import pip
import requests
with open ('C:\\Users\\rimkin\\Downloads\\dataset_3378_2.txt') as file:
    a = file.readline().strip
r = requests.get(a)
print(r.text)
s = r.splitlines()
n = len(s)
with open ('C:\\Projects\\GitProjects\\lesson1\\1.txt', 'w') as b:
    b.wrire(n)

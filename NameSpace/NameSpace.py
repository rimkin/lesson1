parents = {}
variables = {'global':[]}

def in_keys(dic, key):
    if key in dic.keys():
        return True
               
def process_create(par, child):
    if in_keys(parents, child):
        parents[child].append(par)
    else:
        parents[child] = par
    if in_keys(variables, par):
        variables[par].append(child)
    else:
        variables[par] = []
        variables[par].append(child)
    
def process_add(par, var):
    if in_keys(variables, par):
        variables[par].append(var)
    else:
        variables[par] = []
        variables[par].append(var)

def process_get(par, var):
    if par == 'global' and var not in variables.get(par):
        return 'None'
    elif in_keys(variables, par):
        value = variables.get(par)
        if var in variables.get(par):
            return par
        else:
            value_1 = parents.get(par)
            return process_get(value_1, var)
    else:
        value_1 = parents.get(par)
        return process_get(value_1, var)

def begining(index):
    if index[0] == 'create':
        process_create(index[2], index[1])
    elif index[0] == 'add':
        process_add(index[1], index[2])
    elif index[0] == 'get':
        print(process_get(index[1], index[2]))

n = int(input())
for i in range(n):
    i = input().strip().split()
    begining(i)
    
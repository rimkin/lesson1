top = {'Name': 'global', 'Child':[]}

def find_child(parent, childname):
    for child in parent['Child']:
        if child['Name'] == childname:
            return child
    return parent

def process_add(par, var):
    parent = top
    child = find_child(parent, par)
    if child == parent:
        t = {}
        t['Name'] = item
        t['Child'] = []
        parent['Child'].append(t)
        parent = t
    else:
        parent = child

def process_create(var):
    pass

def process_get(var):
    pass

def processLine(var):
    list_var = var.strip().split()
    if list_var[0] == 'create':
        process_create(list_var[2], list_var[1])
    elif list_var[0] == 'add':
        process_add(list_var[1], list_var[2])
    elif list_var[0] == 'get':
        process_get(list_var[1:])
    else:
        print('Unsupported type')

indata = ['add global a', 
          'create foo global',
          'add foo b',
          'get foo a',
          'get foo c',
          'create bar foo',
          'add bar a',
          'get bar a',
          'get bar b']


for i in indata:
    processLine(i)

print(top)
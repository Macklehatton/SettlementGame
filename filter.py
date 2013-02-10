#filter

with open('italiannames', 'r') as f:
    content = f.readlines()

content = map(lambda s: s.strip(), content)

male = []
female = []

def name_sort():
    for line in content:
        if str(line[0:2]).isupper():
            if 'm & f' in line[line.find('   '):line.find('   ')+10]:
                male.append(line[:line.find(' ')])
                female.append(line[:line.find(' ')])
            elif 'f & m' in line[line.find('   '):line.find('   ')+10]:
                male.append(line[:line.find(' ')])
                female.append(line[:line.find(' ')])
            elif 'f' in line[line.find('   '):line.find('   ')+4]:
                female.append(line[:line.find(' ')])
            else:
                male.append(line[:line.find(' ')])


name_sort()


print male
print female


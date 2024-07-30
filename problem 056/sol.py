# Python solution file
class Multiset:
    def __init__(self):
        self.elements = {}

    def add(self, val):
        if val in self.elements:
            self.elements[val] += 1
        else:
            self.elements[val] = 1

    def remove(self, val):
        if val in self.elements:
            if self.elements[val] > 1:
                self.elements[val] -= 1
            else:
                del self.elements[val]

    def __contains__(self, val):
        return val in self.elements

    def __len__(self):
        return sum(self.elements.values())
        
# Example usage:

q = int(input())
m = Multiset()
result = []

for _ in range(q):
    operation = input().strip().split()
    op = operation[0]
    
    if op == 'add':
        val = int(operation[1])
        m.add(val)
    elif op == 'remove':
        val = int(operation[1])
        m.remove(val)
    elif op == 'query':
        val = int(operation[1])
        result.append(val in m)
    elif op == 'size':
        result.append(len(m))

for res in result:
    print(res)

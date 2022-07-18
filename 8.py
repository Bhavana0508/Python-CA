#program to find top 3 integers that occur frequently from a given list of sorted and distinct integers with corresponding count values
lst = [[1,2,6],[1,3,4,5,7,8],[1,3,5,6,8,9],[1,5,7,11],[1,4,7,5,8,12]]
nw_lst = []
dct = {}
q = []
nk = []
nr = []
for i in lst:
    for j in i:
        nw_lst.append(j)

nw_lst.sort()

for i in nw_lst:
    x = nw_lst.count(i)
    dct.update({i:x})
q = list(dct.values())
q.sort()
for i in range(8, 11):
    for k in dct.keys():
        if dct[k] == q[i]:
            nk.append(k)
            nr.append(q[i])
            break
print(nk[::-1])
print(nr[::-1])

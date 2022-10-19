

n1 = 2
d1 = 5

n2 = 5
d2 = 7

nfinal = (n1*d2)+(n2*d1)
dfinal = (d1*d2)

n_orig = nfinal
d_orig = dfinal

print(nfinal, '/', dfinal)

while nfinal % dfinal != 0:
    old_n = nfinal
    old_d = dfinal

    nfinal = old_d
    dfinal = old_n%old_d

new_n = n_orig // dfinal
new_d = d_orig// dfinal

print(new_n,'/',new_d)

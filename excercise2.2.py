def sortarray(xs):
    for i in range(len(xs)):
        for j in range(i + 1, len(xs)):
            if xs[i] > xs[j]:
                xs[i], xs[j] = xs[j], xs[i]
    return xs

data = [3,1,5,2,4]
t = sortarray(data)
print(t)
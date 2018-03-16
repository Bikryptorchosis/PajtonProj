# with open("binary", 'bw') as f:
#     f.write(bytes(range(17)))
#
# with open("binary", 'br') as f:
#     for b in f:
#         print(b)

a = 65534
b = 65535
c = 65536
x = 2998302

with open("binary2", 'bw') as f:
    f.write(a.to_bytes(2, 'big'))
    f.write(b.to_bytes(2, 'big'))
    f.write(c.to_bytes(4, 'big'))
    f.write(x.to_bytes(4, 'big'))
    f.write(x.to_bytes(4, 'little'))

with open("binary2", 'br') as file:
    e = int.from_bytes(file.read(2), 'big')
    print(e)
    f = int.from_bytes(file.read(2), 'big')
    print(f)
    g = int.from_bytes(file.read(4), 'big')
    print(g)
    h = int.from_bytes(file.read(4), 'big')
    print(h)
    i = int.from_bytes(file.read(4), 'big')
    print(i)

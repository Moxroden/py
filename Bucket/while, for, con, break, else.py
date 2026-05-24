# while
x = 0; while x < 3: print(x); x += 1  # 0 1 2

# for
for i in range(3): print(i)  # 0 1 2

# continue
for i in range(5): 
    if i == 2: continue
    print(i)  # 0 1 3 4

# break
for i in range(5):
    if i == 3: break
    print(i)  # 0 1 2

# else
for i in range(3):
    if i == 5: break
else:
    print("break не было")  # выполнится
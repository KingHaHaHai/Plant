total = 0
a = 1
while total <= 50:
    print(f"第{a}次")
    print(f"原本Total:{total}, A:{a}")
    total += a
    a += 1
    print(f"加后Total:{total}, A:{a}")
    
print(total)
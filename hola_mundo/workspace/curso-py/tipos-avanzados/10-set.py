primer = {5, 2, 2, 3, 4, 3}
print("primer ", primer)

# primer.add(10)
# print(primer)

# primer.remove(3)
# print(primer)

segundo = [3, 4, 5, 10]
# print(segundo)

segundo = set(segundo)
print("segundo ", segundo)

print("Unión ", primer | segundo)
print("Intersección ", primer & segundo)
print("Diferencia ", primer - segundo)
print("Diferencia simétrica", primer ^ segundo)

if 5 in segundo:
    print(primer)

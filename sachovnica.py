result = 0

for i in range(8 * 8):
    result += 2 ** i
    # print(str(i + 1) + ". " + str(result))

print("\n" + str(result))

temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32,
                30, 28, 24, 23]

hot_temps = list(filter(lambda x: x > 28, temperatures))

print(hot_temps)
print(max(hot_temps))
print(min(hot_temps))
print(round(sum(hot_temps) / len(hot_temps), 2))

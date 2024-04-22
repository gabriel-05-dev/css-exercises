airports = ["Barcelona", "Dublin", "London", "Paris", "Prague", "Rey", "Rome"]
codes = ["BCN", "DUB", "LIS", "LHR", "CDG", "PRG", "RKV", "FCO"]
code = str(input("input code"))
index = codes.index(code)
print(airports[index])


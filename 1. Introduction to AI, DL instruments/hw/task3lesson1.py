a = [10, 6.87, True, "hello", ["1"]]
b = ["world", {'y':'z'}, 11, False, 8.9]
for num, pair in enumerate(zip(a,b)):
  print (num, pair)

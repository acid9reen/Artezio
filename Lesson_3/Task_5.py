def f(s):
  return min(map(float,s.split()),key=abs)


print(f("1 2 -0.5 0.75 22"))

def make_bricks(small, big, goal):
  for i in range(big+1):
    for j in range(small+1):
      if((j + 5*i) == goal):
        return True
  return False

print(make_bricks(3,1,8))
print(make_bricks(3, 1, 9))

print(make_bricks(3, 2, 10))

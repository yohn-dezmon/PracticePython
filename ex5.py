# List Overlap
# https://www.practicepython.org/exercise/2014/03/05/05-list-overlap.html

# Take two lists and return a list that contains only the elements common to both... w/o dupes!
# This program must work on lists that are of two different sizes
import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

def check_for_dupes(list1, list2):
  c = []
  for x in list1:
      if x in list2 and x not in c:
          c.append(x)

  print(c)
  return c

def gen_rando_list(size):
    rando_list = []
    for x in range(size):
        y = random.randint(1,11)
        rando_list.append(y)
    return rando_list


# check_for_dupes(a, b)

aa = gen_rando_list(10)
print(f"List 1: {aa}")
bb = gen_rando_list(11)
print(f"List 2: {bb}")

check_for_dupes(aa, bb)

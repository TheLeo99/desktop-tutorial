from fake_math import divide as div_fake
from true_math import divide as div_true

result1 = div_fake(1, 3)
result2 = div_fake(30, 0)
result3 = div_true(4, 7)
result4 = div_true(1, 0)
print(result1)
print(result2)
print(result3)
print(result4)

print('string input test')

with open('./test_limit.txt', 'r') as f:
   lines = f.readlines()

   for line in lines:
       print(line+ '\n')


# with open('./test_limit.txt', 'w') as f:
#     line = 'test'
#
#     for _ in range(1, 100000000) :
#         f.write(line)
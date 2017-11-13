from munkres import Munkres, print_matrix

matrix = [[0.1,8624,4928,11088,1232,4312,2464],
          [65412,59752,63448,57288,67144,64064,65912],
          [69608,60984,64680,58520,68376,65296,67144],
          [52360,43736,47432,41272,51128,48078,49896],
          [34496,25872,29568,23408,33264,30184,32032],
          [16632,8008,11704,5544,15400,12320,14168],
          [1000000,1000000,1000000,1000000,1000000,1000000,1000000]]
print type(matrix)
print matrix[1][1]
m = Munkres()
indexes = m.compute(matrix)
print_matrix(matrix, msg='Lowest cost through this matrix:')
total = 0
for row, column in indexes:
    value = matrix[row][column]
    total += value
    print '(%d, %d) -> %d' % (row, column, value)
print 'total cost: %d' % total

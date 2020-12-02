try:
   f = open('file.txt')
except IOError, e:
   print e
else:
    print 'wrong'
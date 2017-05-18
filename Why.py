fd = file('large_file.bin', 'wb')
for x in xrange(999999999):
    fd.write('0')
    for x in xrange(999999999):
        fd.write('0')
fd.close()
import sys
from process_one_01 import process_one_file
from process_multi_01 import process_multi_file
#params
#00: file
#01: coin_type: bitcoin / ethereum / cardano
#02: destination:  filesystem / database
#03: date begin
#04: date end

if len(sys.argv) < 5:
    process_one_file(sys.argv[1], sys.argv[2], sys.argv[3])
else:
    process_multi_file(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])


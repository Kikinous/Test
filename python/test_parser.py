import test
from optparse import OptionParser
print "Hello"

parser = OptionParser("test2.py [options]")
parser.add_option("--master", dest="master", action='append',metavar="DEVICE[,BAUD]", help="MAVLink master port and optional baud rate",default=[])
(opts, args) = parser.parse_args()

print opts.master


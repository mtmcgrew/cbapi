import sys
import struct
import socket
import pprint
import optparse 

# in the github repo, cbapi is not in the example directory
sys.path.append('../src/cbapi')

import cbapi 

def build_cli_parser():
    parser = optparse.OptionParser(usage="%prog [options]", description="Add a watchlist")

    # for each supported output type, add an option
    #
    parser.add_option("-c", "--cburl", action="store", default=None, dest="url",
                      help="CB server's URL.  e.g., http://127.0.0.1 ")
    parser.add_option("-a", "--apitoken", action="store", default=None, dest="token",
                      help="API Token for Carbon Black server")
    parser.add_option("-i", "--id", action="store", default=None, dest="id",
                      help="Watchlist ID to delete")
    return parser

def main(argv):
    parser = build_cli_parser()
    opts, args = parser.parse_args(argv)
    if not opts.url or not opts.token or not opts.id:
        print "Missing required param; run with --help for usage"
        sys.exit(-1)

    # build a cbapi object
    #
    cb = cbapi.CbApi(opts.url, token=opts.token)

    # delete the watchlist
    # for the purposes of this test script, hardcode the watchlist type, name, and query string
    #
    print "-> Deleting watchlist [id=%s]..." % (opts.id,)
    watchlist = cb.watchlist_del(opts.id)
    print "-> Watchlist deleted" 

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
import sys
import cowsay

if len(sys.argv) < 2:
    print("too few arguments")
#elif len(sys.argv) > 2:
#    print("too much arguments")
#else:
#    print("Hello, "+ sys.argv[1])

#if len(sys.argv) > 2:
#    sys.exit()
#elif len(sys.argv) < 2:
#    sys.exit()

#for sys in sys.argv[-1:]:
#    print("Hello, "+ sys)

cowsay.trex("Hello, "+ sys.argv[1])

    
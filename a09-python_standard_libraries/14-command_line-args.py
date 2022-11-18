# ************* COMMAND LINE ARGUMENTS ***************
import sys

# type in terminal "python 14-command_line-args.py -a -b -c"
# print(sys.argv)         # ['14-command_line-args.py', '-a', '-b', '-c']


if len(sys.argv) == 1:
    print("USAGE: python3 app.py <password>")
else:
    password = sys.argv[1]
    print("Password", password)


# Try: python 14-command_line-args.py
# result: USAGE: python3 app.py <password>

# Try: python 14-command_line-args.py 1234
# result: Password, 1234

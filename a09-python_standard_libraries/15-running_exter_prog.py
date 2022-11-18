# ************** RUNNING EXTERNAL PROGRAMS ***************
import subprocess   # use to run other programs

# completed = subprocess.run(["ls", "-l"])          # Try in terminal: ls -l

# when we run this program, the output will not print in terminal. It will be available in "standard output"
completed = subprocess.run(["python", "15-example.py"],
                           capture_output=True,
                           text=True,
                           check=True)
# print(type(completed))

# result: args ['ls', '-l'] , return the value we supply
print("args", completed.args)

# result: returncode 0 , meaning successful, any none zero value indicates error
print("returncode", completed.returncode)

# standar error is None because our program run properly
print("stderr", completed.stderr)

# standard output is None because we are not captured any value.
print("stdout", completed.stdout)

# if the returncode is NOT equal to zero, meaning there's an error
# if completed.returncode != 0:
#     print(completed.stderr)

# Instead use of if statement
# we can wrap it into try block

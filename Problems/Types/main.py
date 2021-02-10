# the variable "args" is already defined
my_list = []  # your code here


# further code of the script "process_four_numbers.py"

args = ["process_four_numbers.py", "1", "2", "3", "4"]
for i in range(len(args) - 1):
   print(i)
   my_list.append(int(args[i + 1]))

print(my_list)
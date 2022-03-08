from pathlib import Path
import argparse
import requests
import shutil


# Parsing keyword args
parser = argparse.ArgumentParser()
parser.add_argument("--keyword_1")
parser.add_argument("--keyword_2")
args = parser.parse_args()
kw_1 = args.keyword_1
kw_2 = args.keyword_2


# Traversing a dir path, making folders and files and deletng them,
# finding files based on name/extension
current_dir = Path(__file__).resolve().parents[0]
print (current_dir)

parent_dir = Path(__file__).resolve().parents[1]
print (parent_dir)

stuff_dir = parent_dir.joinpath("stuff")
print (stuff_dir)

# Creating new dirs in target dir
stuff_dir.joinpath("more_stuff/even_more_stuff").mkdir(parents=True, exist_ok=True)
even_more_stuff_dir = Path(stuff_dir.joinpath("more_stuff/even_more_stuff"))
print (even_more_stuff_dir)

# write new file to more_stuff
more_stuff_dir = Path(even_more_stuff_dir).resolve().parents[0]
print (more_stuff_dir)

created_py_file = more_stuff_dir.joinpath("newfile.py")
with created_py_file.open(mode = "w+") as f:
    f.write(r"print ('Hello World')")

created_py_file_2 = more_stuff_dir.joinpath("newfile2.py")
with created_py_file_2.open(mode = "w+") as f:
    f.write(r"print ('Hello World')")

created_txt_file = stuff_dir.joinpath("newtxtfile.txt")
with created_txt_file.open(mode = "w+") as f:
    f.write("Hello World")

# Show immediate contents of given dir
print (f"The contents of {stuff_dir} are: \n{chr(10).join([str(element) for element in stuff_dir.iterdir()])} \n")

# fancy little trick to avoid the limitation for backslashes in f-string expressions {}
# {chr(10).join([list of elements each of which we want on a new row])}

# Show contents of a given dir recursively
# print (f"The entire contents of {stuff_dir} recursvelly are \n {[str(element) for element in stuff_dir.rglob('*')]}")
# print (f"The entire contents of {stuff_dir} recursvelly are: \n {sorted(stuff_dir.rglob('*'))}")
print (f"The entire contents of {stuff_dir} recursvelly are: \n {chr(10).join([str(x) for x in sorted(stuff_dir.rglob('*'))])}")


# finding all .py files in the 'Python' folder
py_files = sorted(parent_dir.rglob('*.py'))
print (py_files)

# finding and deleting all .txt files in the 'Python' folder
txt_files = sorted(parent_dir.rglob('*.txt'))
for txt_file in txt_files:
    Path(txt_file).unlink(missing_ok=True)

# Delete the 'even_more_stuff' directory
even_more_stuff_dir.rmdir()

# Copy a file from more_stuff to stuff - requires shutil
py_file_to_copy = sorted(parent_dir.rglob('*2.py'))[0]
shutil.copy(py_file_to_copy, stuff_dir)

# Rename the copied file in stuff
stuff_dir_files = [file for file in stuff_dir.iterdir() if file.is_file()]
print (f"Stuff dir files: \n{stuff_dir_files}")
for file in stuff_dir_files:
    print (file)
    file.rename(stuff_dir.joinpath('renamed.py'))
stuff_dir_files = [file for file in stuff_dir.iterdir() if file.is_file()]
print (f"Stuff dir files: \n{stuff_dir_files}")


# Move the renamed file from stuff to more_stuff
for file in stuff_dir_files:
    print (f"File name? \n \t {str(file).split(chr(92))[-1]}")
    file.rename(more_stuff_dir.joinpath(str(file).split('\\')[-1]))




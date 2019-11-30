# File Sort

A script which will sort files on user given directory.

## WorkFlow

First user give filepath to the directory in which the script is intended to work, also note that filepath must be absolute path i.e. /home/ubuntu/Desktop/demo_folder. So the script will work inside demo_folder

```base_path = input("Enter file path: ")```

After giving the filepath and hitting enter the script will analyze types of file based on their extensions (.py, .txt, .tar etc.), then it will check if the directories in which these files will be submitted are available or not, if not then create.

```
if not os.path.exists(os.path.join(base_path, 'text_files')):				
	os.makedirs(os.path.join(base_path, 'text_files'))
```

After script makes sure folder is present in base_path (directory from user input), script tries to move files to their respective folders.

```os.rename(os.path.join(dirpath, file), os.path.join(base_path, "text_files", file))```

There exists some chances that one file may be present in different location (child directories), in that situation script tries to rename file name in format like "filename(copy{duplicate_number}).file extension". so if there are 3 files with same name script will name 3 files like:

- demo_text.txt
- demo_text(copy1).txt
- demo_text(copy2).txt

When file manipulation is over, a summary will be present like:

- Total files moved:
- TextFiles Moved:
- ImageFiles Moved:
- DocumentFiles Moved:
- PackageFiles Moved:
- VideoFiles Moved:
- OtherFiles Moved:

Also you can delete empty directories after file sorting is over.

```choice = input("Do you want to remove all empty directories? [Y/n]")```

Thanks @ompks, for the suggestions and assistance :green_heart:

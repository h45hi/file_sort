import os


base_path = os.getcwd()
files = os.popen('find . -maxdepth 1 -type f')

for file in files:

	file = file.replace('./', '').replace('\n', '')
	_,file_ext = os.path.splitext(file)
	
	if file_ext in ['.txt']:

		if not os.path.exists('./text_files'):
			os.makedirs('./text_files')
			os.rename(os.path.join(base_path, file), os.path.join(base_path, "text_files", file))
		os.rename(os.path.join(base_path, file), os.path.join(base_path, "text_files", file))

	elif file_ext in ['.jpg', 'png']:
		
		if not os.path.exists('./photos'):
			os.makedirs('./photos')
			os.rename(os.path.join(base_path, file), os.path.join(base_path, "photos", file))
		os.rename(os.path.join(base_path, file), os.path.join(base_path, "photos", file))

	elif file_ext in ['.docx', '.pdf', '.xlsx', '.xls', '.ppt']:

		if not os.path.exists('./documents'):
			os.makedirs('./documents')
			os.rename(os.path.join(base_path, file), os.path.join(base_path, "documents", file))
		os.rename(os.path.join(base_path, file), os.path.join(base_path, "documents", file))

	elif file_ext in ['.deb', '.exe']:

		if not os.path.exists('./packages'):
			os.makedirs('./packages')
			os.rename(os.path.join(base_path, file), os.path.join(base_path, "packages", file))
		os.rename(os.path.join(base_path, file), os.path.join(base_path, "packages", file))

	elif file_ext in ['.py', '.pyc']:

		pass

	else:

		if not os.path.exists('./others'):
			os.makedirs('./others')
			os.rename(os.path.join(base_path, file), os.path.join(base_path, "others", file))
		os.rename(os.path.join(base_path, file), os.path.join(base_path, "others", file))

print('Execution Ends !')
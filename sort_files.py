import os, pdb


base_path = os.getcwd()

# pdb.set_trace()

for dirpath, dirnames, filenames in os.walk(base_path):

	for file in filenames:

		file_name, file_ext = os.path.splitext(file) # splits file name and file extension

		if file_ext.lower() in ['.txt']: # lower() makes sure .txt and .TXT are goes inside this if block
			if not os.path.exists('./text_files'):				
				os.makedirs('./text_files')
				os.rename(os.path.join(dirpath, file), os.path.join(base_path, "text_files", file))
			os.rename(os.path.join(dirpath, file), os.path.join(base_path, "text_files", file))

		elif file_ext.lower() in ['.jpg', 'png']:
			if not os.path.exists('./images'):				
				os.makedirs('./images')
				os.rename(os.path.join(dirpath, file), os.path.join(base_path, "images", file))
			os.rename(os.path.join(dirpath, file), os.path.join(base_path, "images", file))

		elif file_ext.lower() in ['.docx', '.pdf', '.xlsx', '.xls', '.ppt']:
			if not os.path.exists('./documents'):				
				os.makedirs('./documents')
				os.rename(os.path.join(dirpath, file), os.path.join(base_path, "documents", file))
			os.rename(os.path.join(dirpath, file), os.path.join(base_path, "documents", file))

		elif file_ext.lower() in ['.deb', '.exe']:
			if not os.path.exists('./packages'):				
				os.makedirs('./packages')
				os.rename(os.path.join(dirpath, file), os.path.join(base_path, "packages", file))
			os.rename(os.path.join(dirpath, file), os.path.join(base_path, "packages", file))

		elif file_ext.lower() in ['.py', '.pyc']:
			pass

		else:
			if not os.path.exists('./others'):				
				os.makedirs('./others')
				os.rename(os.path.join(dirpath, file), os.path.join(base_path, "others", file))
			os.rename(os.path.join(dirpath, file), os.path.join(base_path, "others", file))
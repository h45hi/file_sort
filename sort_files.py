import os


base_path = os.getcwd()

txt_counter,img_counter,doc_counter,package_counter,video_counter,other_counter=0, 0, 0, 0, 0, 0

for dirpath, dirnames, filenames in os.walk(base_path):

	for file in filenames:

		file_name, file_ext = os.path.splitext(file) # splits file name and file extension

		if file_ext.lower() in ['.txt']: # lower() makes sure .txt and .TXT are goes inside this if block
			txt_counter += 1
			if not os.path.exists('./text_files'):				
				os.makedirs('./text_files')
				os.rename(os.path.join(dirpath, file), os.path.join(base_path, "text_files", file))
			else:
				os.rename(os.path.join(dirpath, file), os.path.join(base_path, "text_files", file))

		elif file_ext.lower() in ['.jpg', '.png']:
			img_counter += 1
			if not os.path.exists('./images'):				
				os.makedirs('./images')
				os.rename(os.path.join(dirpath, file), os.path.join(base_path, "images", file))
			else:
				os.rename(os.path.join(dirpath, file), os.path.join(base_path, "images", file))

		elif file_ext.lower() in ['.docx', '.pdf', '.xlsx', '.xls', '.ppt']:
			doc_counter += 1
			if not os.path.exists('./documents'):				
				os.makedirs('./documents')
				os.rename(os.path.join(dirpath, file), os.path.join(base_path, "documents", file))
			else:
				os.rename(os.path.join(dirpath, file), os.path.join(base_path, "documents", file))

		elif file_ext.lower() in ['.deb', '.exe']:
			package_counter += 1
			if not os.path.exists('./packages'):				
				os.makedirs('./packages')
				os.rename(os.path.join(dirpath, file), os.path.join(base_path, "packages", file))
			else:
				os.rename(os.path.join(dirpath, file), os.path.join(base_path, "packages", file))

		elif file_ext.lower() in ['.mp4', '.mkv']:
			video_counter += 1
			if not os.path.exists('./videos'):				
				os.makedirs('./videos')
				os.rename(os.path.join(dirpath, file), os.path.join(base_path, "videos", file))
			else:
				os.rename(os.path.join(dirpath, file), os.path.join(base_path, "videos", file))

		elif file_ext.lower() in ['.py', '.pyc']:
			pass

		else:
			other_counter += 1
			if not os.path.exists('./others'):		
				os.makedirs('./others')
				os.rename(os.path.join(dirpath, file), os.path.join(base_path, "others", file))
			else:
				os.rename(os.path.join(dirpath, file), os.path.join(base_path, "others", file))

print(f'Total files moved: {txt_counter+img_counter+doc_counter+package_counter+video_counter+other_counter}\
 	\nTextFiles Moved:{txt_counter}\nImageFiles Moved:{img_counter}\
	\nDocumentFiles Moved:{doc_counter}\nPackageFiles Moved:{package_counter}\
	\nVideoFiles Moved:{video_counter}\nOtherFiles Moved:{other_counter}')
import os


base_path = os.getcwd()

txt_counter,img_counter,doc_counter,package_counter,video_counter,other_counter = 0, 0, 0, 0, 0, 0
txt_dupli, img_dupli, doc_dupli, pack_dupli, vid_dupli, other_dupli = 0, 0, 0, 0, 0, 0

for dirpath, dirnames, filenames in os.walk(base_path):

	for file in filenames:

		file_name, file_ext = os.path.splitext(file) # splits file name and file extension

		if file_ext.lower() in ['.txt']: # lower() makes sure .txt and .TXT are goes inside this if block
			if not os.path.exists('./text_files'):				
				os.makedirs('./text_files')
				try:
					os.rename(os.path.join(dirpath, file), os.path.join(base_path, "text_files", file))
				except FileExistsError:
					txt_dupli += 1
					# renaming and moving file works only on windows, on UNIX systems it replaces same files silently
					os.rename(os.path.join(dirpath, file),\
					 os.path.join(base_path, "text_files", file_name+'('+'copy'+str(txt_dupli)+')'+file_ext))
			else:
				try:
					os.rename(os.path.join(dirpath, file), os.path.join(base_path, "text_files", file))
				except FileExistsError:
					txt_dupli += 1
					os.rename(os.path.join(dirpath, file),\
					 os.path.join(base_path, "text_files", file_name+'('+'copy'+str(txt_dupli)+')'+file_ext))

		elif file_ext.lower() in ['.jpg', '.png']:
			img_counter += 1
			if not os.path.exists('./images'):				
				os.makedirs('./images')
				try:
					os.rename(os.path.join(dirpath, file), os.path.join(base_path, "images", file))
				except FileExistsError:
					img_dupli += 1
					os.rename(os.path.join(dirpath, file),\
					 os.path.join(base_path, "images", file_name+'('+'copy'+str(img_dupli)+')'+file_ext))

			else:
				try:
					os.rename(os.path.join(dirpath, file), os.path.join(base_path, "images", file))
				except FileExistsError:
					img_dupli += 1
					os.rename(os.path.join(dirpath, file),\
					 os.path.join(base_path, "images", file_name+'('+'copy'+str(img_dupli)+')'+file_ext))

		elif file_ext.lower() in ['.docx', '.pdf', '.xlsx', '.xls', '.ppt']:
			doc_counter += 1
			if not os.path.exists('./documents'):				
				os.makedirs('./documents')
				try:
					os.rename(os.path.join(dirpath, file), os.path.join(base_path, "documents", file))
				except FileExistsError:
					doc_dupli += 1
					os.rename(os.path.join(dirpath, file),\
					 os.path.join(base_path, "documents", file_name+'('+'copy'+str(doc_dupli)+')'+file_ext))
			else:
				try:
					os.rename(os.path.join(dirpath, file), os.path.join(base_path, "documents", file))
				except FileExistsError:
					doc_dupli += 1
					os.rename(os.path.join(dirpath, file),\
					 os.path.join(base_path, "documents", file_name+'('+'copy'+str(doc_dupli)+')'+file_ext))

		elif file_ext.lower() in ['.deb', '.exe']:
			package_counter += 1
			if not os.path.exists('./packages'):				
				os.makedirs('./packages')
				try:
					os.rename(os.path.join(dirpath, file), os.path.join(base_path, "packages", file))
				except FileExistsError:
					pack_dupli += 1
					os.rename(os.path.join(dirpath, file),\
					 os.path.join(base_path, "packages", file_name+'('+'copy'+str(pack_dupli)+')'+file_ext))
			else:
				try:
					os.rename(os.path.join(dirpath, file), os.path.join(base_path, "packages", file))
				except FileExistsError:
					pack_dupli += 1
					os.rename(os.path.join(dirpath, file),\
					 os.path.join(base_path, "packages", file_name+'('+'copy'+str(pack_dupli)+')'+file_ext))

		elif file_ext.lower() in ['.mp4', '.mkv']:
			video_counter += 1
			if not os.path.exists('./videos'):
				os.makedirs('./videos')
				try:
					os.rename(os.path.join(dirpath, file), os.path.join(base_path, "videos", file))
				except FileExistsError:
					vid_dupli += 1
					os.rename(os.path.join(dirpath, file),\
					 os.path.join(base_path, "videos", file_name+'('+'copy'+str(vid_dupli)+')'+file_ext))
			else:
				try:
					os.rename(os.path.join(dirpath, file), os.path.join(base_path, "videos", file))
				except FileExistsError:
					vid_dupli += 1
					os.rename(os.path.join(dirpath, file),\
					 os.path.join(base_path, "videos", file_name+'('+'copy'+str(vid_dupli)+')'+file_ext))

		elif file_ext.lower() in ['.py', '.pyc']:
			pass

		else:
			other_counter += 1
			if not os.path.exists('./others'):		
				os.makedirs('./others')
				try:
					os.rename(os.path.join(dirpath, file), os.path.join(base_path, "others", file))
				except FileExistsError:
					other_dupli += 1
					os.rename(os.path.join(dirpath, file),\
					 os.path.join(base_path, "others", file_name+'('+'copy'+str(other_dupli)+')'+file_ext))
				
			else:
				try:
					os.rename(os.path.join(dirpath, file), os.path.join(base_path, "others", file))
				except FileExistsError:
					other_dupli += 1
					os.rename(os.path.join(dirpath, file),\
					 os.path.join(base_path, "others", file_name+'('+'copy'+str(other_dupli)+')'+file_ext))

print(f'Total files moved: {txt_counter+img_counter+doc_counter+package_counter+video_counter+other_counter}\
 	\nTextFiles Moved:{txt_counter}\nImageFiles Moved:{img_counter}\
	\nDocumentFiles Moved:{doc_counter}\nPackageFiles Moved:{package_counter}\
	\nVideoFiles Moved:{video_counter}\nOtherFiles Moved:{other_counter}')
import glob, os
#change this here to your file path. 
folder = 'C:\\Users\\14024381\\Downloads\\test'

#this here will go through folder and change them to mobi for you
for filename in glob.iglob(os.path.join(folder, '*.pdf')):
	os.rename(filename, filename[:-4] + '.mobi')
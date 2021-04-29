import os.path, time

if not os.path.exists('/data/Input/'):
    os.makedirs('/data/Input/')

if not os.path.exists('/data/Output/'):
    os.makedirs('/data/Output/')

time.sleep(5)

if __name__== "__main__":
	while True:
		filelist = sorted(os.listdir('/data/Input/'))

		for file in filelist:
			file_input = os.path.join('/data/Input/', file)
			file_output = os.path.join('/data/Output/', file)
			
			if(file.endswith(".mp3")):
				cmd = "ffmpeg-normalize '" + file_input + "' -c:a libmp3lame -b:a 320k -o '" + file_output + "'"
			else:
				cmd = "ffmpeg-normalize '" + file_input + "' -o '" + file_output + "'"
			print(cmd)
			os.system(cmd)

			cmd = "rm '" + file_input + "'"
			print(cmd)
			os.system(cmd)

		time.sleep(30)

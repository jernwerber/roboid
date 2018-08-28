import os
import time
import random
import subprocess

default_dir_name="sounds"
playable_formats = ['mp3','ogg','wav']
playable_files = []


r  = subprocess.run("findmnt -nr -o TARGET -S /dev/sda1".split(), stdout=subprocess.PIPE)
path_to_usb = str(r.stdout)[2:-3] #we have to strip some characters from stdout  b' and \n'

def check_for_dir(path_to_check, dir_name="sounds"):
	# with only works with python >= 3.6
	# with os.scandir(path_to_usb) as dirs_and_files:
	dirs_and_files = os.scandir(path_to_check)

	# there should be exactly 1 dir with the desired name, default=sounds
	named_dirs = [d for d in dirs_and_files if d.name == dir_name and os.path.isdir(d.path)]
	if len(named_dirs) == 1:
		return True
	else:
		return False

def check_for_files(path_to_check, valid_formats=playable_formats):
	dirs_and_files = os.scandir(path_to_check)
	for d in dirs_and_files:
		if d.name[-4:] in ["." + f for f in playable_formats]:
			playable_files.append(d)
	if len(playable_files) > 0:
		return True
	else:
		return False

def get_sound_files(source="usb"):
	# check if there's a sounds directory and that it has at least one valid sound file
	# otherwise fall back to default sounds
	if source=="usb":
		if check_for_dir(path_to_usb, default_dir_name) and check_for_files(path_to_usb + "/" + default_dir_name):
			print("Found " + str(len(playable_files)) + " file(s):")
			for p in playable_files:
				print(p.name + " (" + p.path + ")")
			return playable_files
	else:
		# load and play our default files? this should probably be handled better...
		return False

def play_sound_file(path_to_file):
	return subprocess.Popen(["aplay",path_to_file])

### some test code here
get_sound_files()

for n in range(4):
	file_to_play = random.choice(playable_files)
	print("Playing " + file_to_play.name + " (" + file_to_play.path + ")")
	p = play_sound_file(file_to_play.path)
	while p.poll() is None:
		print("File is still playing...")
		time.sleep(1)

import os

# specify valid file formats, based on file extensions (easiest way?)
playable_formats = ['mp3','ogg','wav']

def check_for_dir(path_to_check, dir_name="sounds"):
    with os.scandir(path_to_check) as dirs_and_files:
        sounds_dirs = [d for d in dirs_and_files if d.name == dir_name and os.path.isdir(d.path)]
        if len(sounds_dirs) == 1:
            return True
        else:
            return False

# on initialize, look for a usb device that has a folder called sounds
# for now we can give it a path... for the rpi it'll probably be /dev/sda or something like that

path_to_check = "C:\Temp"
has_sounds = check_for_dir(path_to_check)

if has_sounds:
    print("Sounds folder found.")
else:
    print("Error looking for sounds folder.")

valid_files = []
invalid_files = []

with os.scandir(path_to_check + "\sounds") as dirs:
    for d in dirs:
        if d.name[-4:] in ["." + f for f in playable_formats]:
            valid_files.append(d)
        else:
            invalid_files.append(d)

print("Valid files found:")
for f in valid_files:
    print(f.path)
    
print("\nOther files found:")
for f in invalid_files:
    print(f)    

import os

def init():
    os.mkdir('data')
    os.mkdir('firmware')
    os.mkdir('sketch')
    os.mkdir('spiffs')

    f = open(os.path.join('data','README.md'), 'w+')
    f.write(f"Folder where the geXYZ.txt files should be located to feed the scripts.")
    f.close

    f = open(os.path.join('firmware','README.md'), 'w+')
    f.write(f"Folder where the platformio arduino-esp32 project should be located.")
    f.close

    f = open(os.path.join('sketch','README.md'), 'w+')
    f.write(f"Folder where the binaries regarding the sketch will be outputted, i.e partition.bin and firmware.bin.")
    f.close

    f = open(os.path.join('spiffs','README.md'), 'w+')
    f.write(f"Folder where the binaries regarding the SPIFFS will be outputted, i.e. geXYZ.bin files for each target.")
    f.close

    f = open(os.path.join('README.md'), 'w+')
    f.write(f"Root folder of project where the manifest file should be located so as the Python scripts.")
    f.close

if __name__ == "__main__":
    init()
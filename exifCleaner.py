import subprocess
import os

print("""
    ---------------------------------
    EXIF DATA CLEANER:
    ---------------------------------
      """)


cwd = os.getcwd()
inDir = cwd + '\\inExFiles'
outDir = cwd + '\\outExFiles'

fileList = []

def setUp():
    
    if subprocess.run(['exiftool', '--version'], capture_output=True, check=True) == True:
        print("[-] Script requires Exiftool. Run: choco install exiftool ")
        exit(1)
    else:
        print("[+] Exiftool Found")
    
    if os.path.exists(inDir):
        print("[+] Input Folder exits")
    else:
        print("[+] Creating Input ExFiles folder")
        os.mkdir(inDir)

    if os.path.exists(outDir):
        print("[+] Output Folder exists")
    else:
        print("[+] Creating Output ExFiles folder")
        os.mkdir(outDir)


def indexFiles():

    valid_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp','.mp4', '.avi', '.mov', '.mkv', '.wmv']
    
    content = os.listdir(inDir)
    if not content:
        print("[-] Folder Empty. Add files to inExFiles")
        exit(1)

    for fileName in os.listdir(inDir):
        _, file_extension = os.path.splitext(fileName)
        if file_extension in valid_extensions:
            fileList.append(inDir+'\\'+fileName)


def removeMetadata():

    for inFileName in fileList:
        name = inFileName.split('\\')
        outFileName = name[-1]
        print(f"[*] Cleaning {outFileName}")
        finalOutDir = outDir+'\\'+outFileName
        try:
            subprocess.run(['exiftool','-all=',inFileName,'-o',finalOutDir], capture_output=True, check=True)
        except subprocess.CalledProcessError as e:
            print(f"\t\\_[*] File {outFileName} Already Cleaned ")
    

def start():

    setUp()
    indexFiles()
    removeMetadata()
    print("[+]Files Cleaned")


start()

import os
file = open(raw_input("file: ")).red()
percobaan = 0
while True:
    if "exec"  in file and "marshal" in file and "import" in file:
    	kontol = file.replace("exec","x=")
    	percobaan += 1
print("percobaan ke" + str(peercobaan))
else:
print("n/"+file)
try:
os.remove("sc.py")
print("\n file tersimpan di ez.py")
except:
	print("\n gagal")
break
sc = """from sys import stdout
import marshal
from uncompyle6.main import decompile
"""+kontol+"""
decompile(2.7,x, stdout) """
               open("sc.py", "w").write(sc)
               os.system("python2 sc.py > ez.py")
               file = open("ez.py").read()
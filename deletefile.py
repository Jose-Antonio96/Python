import os
import shutil

path = "test2.txt"

try:
    os.remove(path) #borra archivos
    os.rmdir(path)  #borra carpetas vacias
    shutil.rmtree(path) #borrará la carpeta y todo lo que haya dentro. Usar con cuidado
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to delete that")
except OSError:
    print("You cannot delete using this function")
else:
    print(path+" was deleted")

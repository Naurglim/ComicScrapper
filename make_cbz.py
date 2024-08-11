import zipfile
import pathlib
import os
import shutil

FOLDER = "C:/Comics/"


def get_cbz_filename(ruta_original):
    # Asegurarse de que la ruta sea absoluta
    ruta = os.path.abspath(ruta_original)
    
    # Obtener la lista de carpetas en la ruta
    carpetas = []
    while True:
        ruta, carpeta = os.path.split(ruta)
        if carpeta:
            carpetas.append(carpeta)
        else:
            break
    
    # Invertir la lista para tener las carpetas más cercanas al directorio base al principio
    carpetas.reverse()
    
    # Obtener las dos últimas carpetas
    if len(carpetas) >= 2:
        ultimas_dos = carpetas[-2:]
    elif len(carpetas) == 1:
        ultimas_dos = [carpetas[0], '']  # Si solo hay una carpeta, la segunda será una cadena vacía
    else:
        ultimas_dos = ['', '']  # Si no hay carpetas, ambas serán cadenas vacías

    # Concatenar los nombres de las carpetas
    nombre_archivo = ' - '.join(ultimas_dos) + '.cbz'

    # Recupero la ruta hasta la carpeta padre en la ruta original:
    ruta, carpeta = os.path.split(ruta_original)

    return os.path.join(ruta, nombre_archivo)


list_subfolders_with_paths = [f.path for f in os.scandir(FOLDER) if f.is_dir()]

for title_folder in list_subfolders_with_paths:
    issues_folders = [f.path for f in os.scandir(title_folder) if f.is_dir()]
    for issue_folder in issues_folders:
        directory = pathlib.Path(issue_folder)
        print(directory)
        cbz_filename = get_cbz_filename(directory)
        with zipfile.ZipFile(cbz_filename, "w", zipfile.ZIP_DEFLATED) as archive:
            for file_path in directory.iterdir():
                archive.write(file_path, arcname=file_path.name)
        shutil.rmtree(directory)

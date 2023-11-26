import os


path = '/home/sas/Загрузки/'
list_file = os.listdir(path)
files_only = [file for file in list_file if os.path.isfile(os.path.join(path, file))]

for file in files_only:
    extencion = file.split('.')[-1]
    if extencion not in os.listdir(path):
        os.mkdir(f'{path}{extencion}')
    os.rename(f'{path}{file}',f'{path}{extencion}/{file}' )
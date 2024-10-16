import zipfile
import os

def zip_extract(path:str):
    is_zip_file = zipfile.is_zipfile(path)

    if(is_zip_file):
        with zipfile.ZipFile(path, 'r') as zip_ref:
            zip_ref.extractall(param.TEMP)
        os.remove(path)

    elif(cert_handler.check_is_certificate(path)):
        filename = os.path.basename(path)
        shutil.move(path,os.path.join(param.TEMP, filename))
    
    else:
        os.remove(path)
    
    list_file = read_file_input(res=[])

    files: list[File_Repo_Schema] = []
    for file_ in list_file:
        file = parse_file_from_input_cert(file_)

        files.append(file)

        os.remove(file_)

    return files
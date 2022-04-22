import os, json, io

def file_reader(massJson):
    for file_name in massJson:
        if 'ru' in file_name:
            lang = 'en'
        if 'kz' in file_name:
            lang = 'kz'
        with io.open(file_name, 'r', encoding="utf-8") as f:
            print(f)
            json_obj = json.loads(f.read(), strict=False)
            for post in json_obj["posts"]:
                yield post, lang

def get_all_paper_sites(path):
    massFiles = []
    massJson = []
    os.chdir(path)
    for root, dirs, files in os.walk(path, topdown = False):
        for name in files:
            massFiles.append(os.path.join(root, name))
        for name in dirs:
            massFiles.append(os.path.join(root, name))
    for file in massFiles:
        if '.json' in file:
            massJson.append(file)
    new_generator = file_reader(massJson)
    """Structure:
        {
            "title": title,
            "date": date,
            "description": description,
            "text": text of the article,
            "tags": current tag,
            "author": name of the author and source,
            "url": web address
        }
    """
    return new_generator
path = r'D:\data\web_data'
get_all_paper_sites(path)
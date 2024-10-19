

from subprocess import run


async def displayInFile(data:str, filename:str = "movies.html", display:bool = True):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(data)
    run(["code", filename], shell=True)
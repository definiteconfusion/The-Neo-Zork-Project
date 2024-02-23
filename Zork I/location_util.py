import functions

cnt = 19
for i in range(18):
    cmdsAbbr = {
    "n":"north",
    "e":"east",
    "s":"south",
    "w":"west"
    }
    currId = bin(cnt).replace("0", "o").replace("1", "i")
    name = input("Nme: ")
    descrip = input("Desc: ")
    allmve = []
    directions = int(input("Num Dirs: "))
    for dirs in range(directions):
        currMove = []
        currMove.append(cmdsAbbr[input("Dir: ")])
        currMove.append(input("Result: "))
        allmve.append(currMove)
    functions.cmd(f"INSERT INTO locationDetails (id, name, message) VALUES ('{currId}', '{name}', '{descrip}');")
    functions.cmd(f"CREATE TABLE {currId} (command TEXT,result TEXT);")
    for dirs in range(directions):
        functions.cmd(f"INSERT INTO {currId} (command,result) VALUES ('{allmve[dirs][0]}', '{allmve[dirs][1]}');")
    cnt+=1
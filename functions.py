import sqlite3

def cmd(command: str):
    database = "locations.db"
    init = sqlite3.connect(f'{database}')
    cursor = init.cursor()
    cursor.execute(f"{command}")
    if "SELECT" in command:
        type_result = cursor.fetchall()
    elif "PRAGMA" in command:
        type_result = cursor.fetchall()
    else:
        type_result = "ENDED IN ELSE"
        init.commit()
    return type_result

def commandList(sqlResponce):
    # [('west', '0000000010'), ('north', '0000000011'), ('south', '0000000100')]
    cmds = []
    for comds in range(len(sqlResponce)):
        cmds.append(sqlResponce[comds][0])
    return cmds

def commandOut(command, sqlResponce):
    for cmds in range(len(sqlResponce)):
        if command == sqlResponce[cmds][0]:
            return sqlResponce[cmds][1]
import functions
import structs

# currentLocale = "oooooooooi"

# print(functions.cmd(f"SELECT * FROM {currentLocale}"))

# print(functions.commandList([('west', '0000000010'), ('north', '0000000011'), ('south', '0000000100')]))
# print(functions.cmd(f"SELECT * FROM locationDetails WHERE id = '{currentLocale}'")[0])

currentLocale = "obi"
print(functions.cmd(f"SELECT * FROM locationDetails WHERE id = '{currentLocale}'")[0])
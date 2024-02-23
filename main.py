import click
import functions
currentLocale = "obi"
cmdsAbbr = {
    "n":"north",
    "e":"east",
    "s":"south",
    "w":"west"
}
for i in range(10):
    messages = functions.cmd(f"SELECT * FROM locationDetails WHERE id = '{currentLocale}'")[0]
    click.echo(messages[1])
    click.echo(messages[2])
    reqFunc = click.prompt("> ")
    movementPossibilities = functions.cmd(f"SELECT * FROM {currentLocale}")
    localeCommandList = functions.commandList(movementPossibilities)
    if reqFunc == "n" or reqFunc == "e" or reqFunc == "s" or reqFunc == "w":
        reqFunc = cmdsAbbr[reqFunc]
    if reqFunc in localeCommandList:
        cmdOut = functions.commandOut(reqFunc, movementPossibilities)
        currentLocale = bin(int(cmdOut)).replace("0", "o").replace("1", "i")
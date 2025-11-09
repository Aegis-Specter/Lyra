def greetings(argu):
    return "Lyra << Hello Aegis Specter I born on 9 November 2025"

def launches(argu):
    if not argu:
        return "Lyra << Didnt have that ability to open "
    return f"Lyra << Deploying {argu[0]}"

def terminate(argu):
    return "exit"

COMMANDS = {
    "hello": greetings,
    "open" : launches,
    "exit" : terminate
}

def respond (cmd,argu):
    if cmd is None :
            return "Lyra << No command is there "

    func = COMMANDS.get(cmd)
    if func:
       return func(argu)
    else:
        return f"Lyra << That feature is not available '{cmd}'" 



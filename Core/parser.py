def aegis_command(command:str):
    command= command.strip().lower() 
    if not command:
        return None, []
    parts=command.split()
    cmd= parts[0]
    argu= parts[1:]
    return cmd, argu    
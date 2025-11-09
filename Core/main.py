from parser import aegis_command
from responder import respond

print ("Lyra activated sucessfully")

while True:
   aegis_input = input ("Aegis >> ").strip()

   if not aegis_input:
            continue    
   cmd, argu = aegis_command(aegis_input)
   reply = respond(cmd, argu)

   if reply == 'exit':
       print("Lyra << Bye Aegis Specter")
       break
   else:
        print(reply)

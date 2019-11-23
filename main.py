import subprocess as sub
output = str(sub.check_output("netsh wlan show profile", shell=True))
number = output.find("All User Profile")
profiles = output[number::]
networks = profiles.split("All User Profile     : ")
networks.pop(0)
for i in range(len(networks)):
    networks[i] = networks[i][:-4].replace("\\r", "").replace("\\n", "")
    if i == len(networks)-1:
        networks[i] = networks[i][:-1]
for i in range(len(networks)):
    output = str(sub.check_output(f"netsh wlan show profile {networks[i]} key=clear"))
    networks[i] = [networks[i],output[output.find("Key Content")+25:output.find("Cost settings")-8]]

MyNetworks = open("networks.txt", "w")
for i in networks:
    MyNetworks.write(f"{i[0]}:{i[1]}\n")
MyNetworks.close()


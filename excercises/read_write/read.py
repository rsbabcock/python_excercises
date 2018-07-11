# permissions: r: read only, w: write, a: appending, r+: read and write
with open('test.txt', 'w') as testfile:
    testfile.write("hello c25. Hope you're having a great day.")

with open('test.txt', 'a') as testfile:
    testfile.write("hello c25. Hope you're awake.")

nickset = {"poop", 'Fatty'}

nameset = {"Bob", "Joe Bob"}

with open("data/nickname.txt", "w") as nickname:
    for nick in nickset:
        nickname.write(nick + '\n')

with open("data/names.txt", "w") as names:
    for name in nameset:  
        names.write(name + '\n')  
# later, back at the batcave ...

with open("data/names.txt", "r") as names:
    namelist = names.readlines()

with open("data/nicknames.txt", "r") as nicks:
    nicklist = nicks.readlines()

mob_names = [f"{names.strip().split('')[0]}
\"{nicklist[i].strip()}\"
{name.strip().split(' ')[1]}
for i, name in enumerate(namelist)"]
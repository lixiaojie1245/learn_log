



def exist_source_aliasrc(name):
    sa="source ~/.aliasrc"
    with open(name) as f:
        for l in f.readlines():
            if sa in l[:len(sa)]:
                return True
    return False

def write_source_aliasrc(name):
    sa="source ~/.aliasrc"
    with open(name,"w+") as f:
        f.write(sa+"\n")


import os
target=os.path.dirname(__file__)+'/config/.aliasrc'
os.system(f"cp {target} ~/.aliasrc")
for f in ( os.path.expanduser(f) for f in  ["~/.bashrc","~/.zshrc"]):
    if not exist_source_aliasrc(f):
        write_source_aliasrc(f)
        print(f"write to {f}")





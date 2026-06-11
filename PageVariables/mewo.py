## Exposes variables that can change to the Page XML files
__exposed = {
    "@deltaTime": 0
}

def GetExposed(key):
    return __exposed[key]
    
def Update(deltaTime):
    __exposed["@deltaTime"] = deltaTime
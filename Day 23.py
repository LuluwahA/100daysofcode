thisdict={
    "brand":"ford",
    "model":"mustang",
    "year":1966}

if "model" in thisdict:
    print("YES, It's in thisdict")


thisdict={
    "brand":"ford",
    "model":"mustang",
    "year":1966}

print(len(thisdict))

thisdict={
    "brand":"ford",
    "model":"mustang",
    "year":1966}

thisdict["color"]="red"
print(thisdict)

thisdict={
    "brand":"ford",
    "model":"mustang",
    "year":1966}
thisdict.pop("model")
print(thisdict)

thisdict={
    "brand":"ford",
    "model":"mustang",
    "year":1966}
thisdict.popitem()
print(thisdict)

thisdict={
    "brand":"ford",
    "model":"mustang",
    "year":1966}
del thisdict["model"]
print(thisdict)

thisdict={
    "brand":"ford",
    "model":"mustang",
    "year":1966}
thisdict.clear()
print(thisdict)

thisdict={
    "brand":"ford",
    "model":"mustang",
    "year":1966}
del thisdict
print(thisdict)

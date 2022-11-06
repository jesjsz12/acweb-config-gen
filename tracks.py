from ast import For
from importlib.resources import path
import json
import os

print("Where is your tracks folder located?:")
rootdir = input()
tracks = os.listdir(rootdir)
trackslist = []


def addTrack(h):
    number = h['pitboxes']
    number = number.replace('"', "")
    number = int(number)
    trackslist.append({
        'name' : h['name'],
        'config' : '',
        'description' : h['description'],
        'max_slots' : number
    })

def addCTrack(i, C):
    number = i['pitboxes']
    number = number.replace('"', "")
    number = int(number)
    trackslist.append({
        'name' : i['name'],
        'config' : C,
        'description' : i['description'],
        'max_slots' : number
    })



for track in tracks:
    if os.path.exists(os.path.join(rootdir, track, "ui")):
        path = os.path.join(rootdir, track, "ui", "ui_track.json")
        if os.path.exists(path):
            #print(path)
            try:
                f = open(path, "r", encoding='ansi')
                try:
                    g = json.loads(f.read())
                except:
                    #print(path)
                    f.close()
                    f = open(path, "r", encoding='utf-8-sig')
                    g = json.loads(f.read())
                    addTrack(g)
                    f.close()
                else:
                    addTrack(g)
                    f.close()
            except IOError:
                print('error')
            #print(trackslist)
            f.close()

        else:
            for test in os.listdir(os.path.join(rootdir, track, "ui")):
                if test != "Thumbs.db":
                    path = os.path.join(rootdir, track, "ui", test, "ui_track.json")
                    if os.path.exists(path):
                        #print(path)
                        try:
                            f = open(path, "r", encoding='ansi')
                            try:
                                g = json.loads(f.read())
                            except:
                                #print(path)
                                f.close()
                                f = open(path, "r", encoding='utf-8-sig')
                                g = json.loads(f.read())
                                addCTrack(g, test)
                                f.close()
                            else:
                                addCTrack(g, test)
                                f.close()
                        except IOError:
                            print('error')

#print(trackslist)


final = open("tracks.json", "w")
final.write(json.dumps(trackslist, indent=4))
final.close()
#!/usr/bin/python

import json
import sys
import os


filedata = None


def fetch(itemname):
    global filedata

    filename = itemname[0] + ".json"
    try:
        with open(filename, 'r') as f:
            filedata = json.load(f)
            f.close()
            if filedata[itemname] is not None:
                return filedata[itemname]
    except:
        return None
    return None


def append(item):
    global filedata

    if filedata is None:
        filedata = {}

    name = item["name"]
    filedata[name] = item
    filename = name[0] + ".json"
    try:
        os.remove(filename)
    except:
        pass
    with open(filename, 'w') as f:
        json.dump(filedata, f, indent=4)
        f.close()


def getInput(name):
    item = {}
    item["name"] = name
    # fet the category
    while True:
        item["category"] = input("\nEnter the category \n(condiment/dairy/drink/fruit/grain/meat/seafood/spice/vegetable): ").lower()
        if not item["category"] in ['condiment', 'dairy', 'drink', 'fruit', 'grain', 'meat', 'seafood', 'spice', 'vegetable']:
            print("category doesn't match !")
        else:
            break
    # fet the fodmap value
    while True:
        item["fodmap"] = input("\nAdd the fodmap value (low/high/medium): ").lower()
        if not item["fodmap"] in ['low', 'high', 'medium']:
            print("fodmap value doesn't match !")
        else:
            break
    # get the condition
    item["condition"] = input("\nAdd the condition for the item (i.e max 1-2/day), if none press enter: ").lower()
    # get extra information as note
    item["note"] = input("\nAdd extra informations as 'note' that are relavent \n (i.e contains high fat which may trigger IBS) \
            \nif none press enter: ").lower()
    return item


def promptContinue():
    while True:
        query = input("\ndo you wanna continue (y/n): ").lower()
        choice = query[0]
        if query == '' or not choice in ['y','n']:
            print('please answer with y (yes) or n (no) !')
        else:
            return choice

def main():
    name = ""
    while True:
        # get the name
        # print("Enter the item name (i.e mango)")
        name = input("Enter the item name (i.e mango): ").lower()
        if not name.strip():
            print("name can not be empty !")
        else:
            break
    olditem = fetch(name)
    if not olditem is None:
        print("following item already exist as: ")
        json.dump(olditem, sys.stdout, indent=4)
        choice = promptContinue()
        if choice == 'n':
            return
    newitem = getInput(name)
    if not olditem is None:
        print("Changing item detail from :")
        json.dump(olditem, sys.stdout, indent=4)
        print("to :")
        json.dump(newitem, sys.stdout, indent=4)
        choice = promptContinue()
        if choice == 'y':
            append(newitem)
    else:
        print("Adding new item detail as :")
        json.dump(newitem, sys.stdout, indent=4)
        choice = promptContinue()
        if choice == 'y':
            append(newitem)        


if __name__== "__main__":
    main()



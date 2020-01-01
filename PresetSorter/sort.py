# -*- coding: utf-8 -*-

import os
import tkinter as tk
from tkinter import filedialog
from time import sleep


def strip_header():
    start = 88 #end of header
    end   = -10 #start of footer

    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select Preset to Inherit", filetypes=[("HTML Preset", "*.html")])
    with open(file_path, "r", encoding='utf-8') as modfile:
        contents = modfile.readlines()
        header = contents[:start]
        footer = contents[end:]
        #print(header)
        #print(footer)

        #Get lines past the header
        i = 1
        mods = []
        for line in contents:
            if i > start:
                mods.append(line)
            else:
                i += 1
                continue
            i += 1

        #Get the lines with the <tr> for each mod (exactly the same upto the mod name)
        mod_array = []
        mod_lines = ""
        for item in mods:
            mod_lines += item  #Add mod section contents to string
            if item == "        </tr>\n":  #If the end of the mod section is reached
                mod_array.append(mod_lines)  #Append mod table body to array of mods for sorting
                mod_lines = ""  #Clear mod section from string at end of table section
        #Sort the array by character value
        mod_array_new = sorted(mod_array) #sorted mods "alphabetically"
        sorted_mods = ''.join(header) + ''.join(mod_array_new) + ''.join(footer)
        return sorted_mods


#Write the sorted array into a file that works as a preset
file_path = input("Name of new Preset:\n> ")
with open("./Output/" + file_path + ".html", "w", encoding='utf-8') as mods_writefile:
    mods_writefile.write(strip_header())

print("Done")
sleep(2)

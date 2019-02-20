class stripper:
    def strip_header():
        start = 1449 #end of header
        end = -149 #start of footer
        with open("Arma.html", "r", encoding='utf-8') as modfile:
            contents = modfile.readlines()
            header = ''.join(contents)[:start] + "\n"
            footer = ''.join(contents)[end:]


            #Get lines past the header
            i = 1
            mods = []
            for line in contents:
                if i > 83:
                    mods.append(line)
                else:
                    i += 1
                    continue
                i += 1
                
            #Get the lines with the <tr> for each mod (exactly the same upto the mod name)
            mod_array = []
            mod_lines = ""
            i = 1
            for item in mods:
                mod_lines += item
                if i%9 == 0: #ignores footer, gets lines for mods into an array
                    mod_array.append(mod_lines)
                    mod_lines = ""
                i += 1
            #Sort the array by character value
            mod_array_new = sorted(mod_array) #sorted mods "alphabetically"
            sorted_mods = header + ''.join(mod_array_new) + footer
            return sorted_mods

with open("Sorted_Preset.html", "w", encoding='utf-8') as mods_writefile:
    mods_writefile.write(str(stripper.strip_header()))
    #Write the sorted array into a file that works as a preset

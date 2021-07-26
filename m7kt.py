# Mod7 Key Tools (m7kt)
# Thank you Deltara (me) for poorly writing this!

import sys
import os
from types import coroutine
import colorama
import random

verbose = False
file_name = os.path.basename(__file__)

def t10rangen(charlen, conv = False):
    if charlen == 7:
        num = random.randrange(0, 9999999)
    elif charlen == 6:
        num = random.randrange(0, 999999)
    elif charlen == 5:
        num = random.randrange(0, 99999)
    elif charlen == 4:
        num = random.randrange(0, 9999)
    elif charlen == 3:
        num = random.randrange(0, 999)
    elif charlen == 2:
        num = random.randrange(0, 99)
    elif charlen == 1:
        num = random.randrange(0, 9)
    if conv == True:
        return str(num)
    else:
        return num

def split(string):
    return [char for char in string]

def multiple(m, n):
    return True if m % n == 0 else False

# Init shit.
colorama.init()
random.seed()
arglen = len(sys.argv) - 1

# If arguments aren't specified, provide help.
if arglen == 0:
    print(colorama.Fore.GREEN + "Usage: " + file_name + " [options] [id/key]\n")
    print(colorama.Style.RESET_ALL + "Options:")
    print("Generate: -generate, -gen, -g")
    print("Validate: -validate, -val, -v\n")
    print("Type         |  Id")
    print("CD 10-digit  | cd10")
    print("CD 11-digit  | cd11")
    print("OEM 20-digit | oem20\n")
    print("Id is for generation.")
    print("Key is for validation.")
    colorama.deinit()
    sys.exit()

# Option selector.
if sys.argv[1] == "-generate" or sys.argv[1] == "-gen" or sys.argv[1] == "-g":
    if arglen == 2:
        # Key type selector.
        if sys.argv[2] == "cd10" or sys.argv[2] == "10":
            key_type_str = "CD 10-digit"
            key_type = 10
        elif sys.argv[2] == "cd11" or sys.argv[2] == "11":
            key_type_str = "CD 11-digit"
            key_type = 11
        elif sys.argv[2] == "oem20" or sys.argv[2] == "20":
            key_type_str = "OEM 20-digit"
            key_type = 20
        else:
            print(colorama.Fore.RED + "[ERROR] " + colorama.Style.RESET_ALL + "Invalid key type.")
    else:
        print(colorama.Fore.RED + "[ERROR] " + colorama.Style.RESET_ALL + "Missing key type.")
        colorama.deinit()
        sys.exit()
elif sys.argv[1] == "-validate" or sys.argv[1] == "-val" or sys.argv[1] == "-v":
    if arglen == 2:
        # Detect key type based on length.
        keylen = len(sys.argv[2])

        # OEM 20-digit        
        if keylen == 23:
            print(colorama.Fore.MAGENTA + "[INFO] " + colorama.Style.RESET_ALL + "Detected key type is OEM 20-digit.")

            keysplit = split(sys.argv[2])

            # Interpret core parts of the key.
            date = int(keysplit[0] + keysplit[1] + keysplit[2])
            year = keysplit[3] + keysplit[4]
            oem = keysplit[6] + keysplit[7] + keysplit[8]
            sum = int(keysplit[10]) + int(keysplit[11]) + int(keysplit[12]) + int(keysplit[13]) + int(keysplit[14]) + int(keysplit[15]) + int(keysplit[16])

            # Check date.
            if date in range(1, 366):
                date_pass = True
                if verbose == True:
                    print(colorama.Fore.MAGENTA + "[INFO] " + colorama.Style.RESET_ALL + "Passed date check.")
            else:
                date_pass = False
                if verbose == False:
                    print(colorama.Fore.YELLOW + "[WARN] " + colorama.Style.RESET_ALL + "Failed date check.")

            # Check year.
            if year == "95" or year == "96" or year == "97" or year == "98" or year == "99" or year == "00" or year == "01" or year == "02" or year == "03":
                year_pass = True
                if verbose == True:
                    print(colorama.Fore.MAGENTA + "[INFO] " + colorama.Style.RESET_ALL + "Passed year check.")
            else:
                year_pass = False
                if verbose == True:
                    print(colorama.Fore.YELLOW + "[WARN] " + colorama.Style.RESET_ALL + "Failed year check.")

            # Check OEM.
            if oem == "OEM":
                oem_pass = True
                if verbose == True:
                    print(colorama.Fore.MAGENTA + "[INFO] " + colorama.Style.RESET_ALL + "Passed OEM check.")
            else:
                oem_pass = False
                if verbose == True:
                    print(colorama.Fore.YELLOW + "[WARN] " + colorama.Style.RESET_ALL + "Failed OEM check.")

            # Check middle segment first digit.
            if int(keysplit[10]) == 0:
                midsegfirst_pass = True
                if verbose == True:
                    print(colorama.Fore.MAGENTA + "[INFO] " + colorama.Style.RESET_ALL + "Passed middle segment first digit check.")
            else:
                midsegfirst_pass = False
                if verbose == True:
                    print(colorama.Fore.YELLOW + "[WARN] " + colorama.Style.RESET_ALL + "Failed middle segment first digit check.")

            # Check middle segment last digit.
            if int(keysplit[16]) == 0 or int(keysplit[16]) == 8 or int(keysplit[16]) == 9:
                midseglast_pass = False
                if verbose == True:
                    print(colorama.Fore.YELLOW + "[WARN] " + colorama.Style.RESET_ALL + "Failed middle segment last digit check.")
            else:
                midseglast_pass = True
                if verbose == True:
                    print(colorama.Fore.MAGENTA + "[INFO] " + colorama.Style.RESET_ALL + "Passed middle segment last digit check.")

            # Check for remainder.
            if multiple(sum, 7) == True:
                remainder_pass = True
                if verbose == True:
                    print(colorama.Fore.MAGENTA + "[INFO] " + colorama.Style.RESET_ALL + "Passed remainder check.")
            else:
                remainder_pass = False
                if verbose == True:
                    print(colorama.Fore.YELLOW + "[WARN] " + colorama.Style.RESET_ALL + "Failed remainder check.")

            # Print verdict.
            if date_pass == True and year_pass == True and oem_pass == True and midsegfirst_pass == True and midseglast_pass == True and remainder_pass == True:
                print(colorama.Fore.MAGENTA + "[INFO] " + colorama.Style.RESET_ALL + "Key " + sys.argv[2] + " is valid.")
            else:
                print(colorama.Fore.RED + "[ERROR] " + colorama.Style.RESET_ALL + "Key " + sys.argv[2] + " is invalid.")

            colorama.deinit()
            sys.exit()
        # CD 10-digit  
        elif keylen == 11:
            print(colorama.Fore.MAGENTA + "[INFO] " + colorama.Style.RESET_ALL + "Detected key type is CD 10-digit.")

            keysplit = split(sys.argv[2])

            # Interpret core parts of the key.
            init = keysplit[0] + keysplit[1] + keysplit[2]
            sum = int(keysplit[4]) + int(keysplit[5]) + int(keysplit[6]) + int(keysplit[7]) + int(keysplit[8]) + int(keysplit[9]) + int(keysplit[10])

            # Check blacklist.
            if init == "333" or init == "444" or init == "555" or init == "666" or init == "777" or init == "888" or init == "999":
                blacklist_pass = False
                if verbose == True:
                    print(colorama.Fore.YELLOW + "[WARN] " + colorama.Style.RESET_ALL + "Failed blacklist check.")
            else:
                blacklist_pass = True
                if verbose == True:
                    print(colorama.Fore.MAGENTA + "[INFO] " + colorama.Style.RESET_ALL + "Passed blacklist check.")

            # Check last digit.
            if int(keysplit[10]) == 0 or int(keysplit[10]) == 8 or int(keysplit[10]) == 9:
                lastdigit_pass = False
                if verbose == True:
                    print(colorama.Fore.YELLOW + "[WARN] " + colorama.Style.RESET_ALL + "Failed last digit check.")
            else:
                lastdigit_pass = True
                if verbose == True:
                    print(colorama.Fore.MAGENTA + "[INFO] " + colorama.Style.RESET_ALL + "Passed last digit check.")

            # Check remainder.
            if multiple(sum, 7) == True:
                remainder_pass = True
                if verbose == True:
                    print(colorama.Fore.MAGENTA + "[INFO] " + colorama.Style.RESET_ALL + "Passed remainder check.")
            else:
                remainder_pass = False
                if verbose == True:
                    print(colorama.Fore.YELLOW + "[WARN] " + colorama.Style.RESET_ALL + "Failed remainder check.")

            # Print verdict.
            if blacklist_pass == True and lastdigit_pass == True and remainder_pass == True:
                print(colorama.Fore.MAGENTA + "[INFO] " + colorama.Style.RESET_ALL + "Key " + sys.argv[2] + " is valid.")
            else:
                print(colorama.Fore.RED + "[ERROR] " + colorama.Style.RESET_ALL + "Key " + sys.argv[2] + " is invalid.")

            colorama.deinit()
            sys.exit()
        # CD 11-digit  
        elif keylen == 12:
            print(colorama.Fore.MAGENTA + "[INFO] " + colorama.Style.RESET_ALL + "Detected key type is CD 11-digit.")

            keysplit = split(sys.argv[2])

            # Interpret core parts of the key.
            three = int(keysplit[2])
            four = int(keysplit[3])
            sum = int(keysplit[5]) + int(keysplit[6]) + int(keysplit[7]) + int(keysplit[8]) + int(keysplit[9]) + int(keysplit[10]) + int(keysplit[11])

            # Convert fourth digit back, if necessary.
            if four == 1:
                four = 10
            elif four == 2:
                four = 11

            # Check if fourth digit is greater than the third by either two or one.
            if four - three == 1 or four - three == 2:
                greater_pass = True
                if verbose == True:
                    print(colorama.Fore.MAGENTA + "[INFO] " + colorama.Style.RESET_ALL + "Passed greater than check.")
            else:
                greater_pass = False
                if verbose == True:
                    print(colorama.Fore.YELLOW + "[WARN] " + colorama.Style.RESET_ALL + "Failed greater than check.")

            # Check last digit.
            if int(keysplit[11]) == 0 or int(keysplit[11]) == 8 or int(keysplit[11]) == 9:
                lastdigit_pass = False
                if verbose == True:
                    print(colorama.Fore.YELLOW + "[WARN] " + colorama.Style.RESET_ALL + "Failed last digit check.")
            else:
                lastdigit_pass = True
                if verbose == True:
                    print(colorama.Fore.MAGENTA + "[INFO] " + colorama.Style.RESET_ALL + "Passed last digit check.")

            # Check remainder.
            if multiple(sum, 7) == True:
                remainder_pass = True
                if verbose == True:
                    print(colorama.Fore.MAGENTA + "[INFO] " + colorama.Style.RESET_ALL + "Passed remainder check.")
            else:
                remainder_pass = False
                if verbose == True:
                    print(colorama.Fore.YELLOW + "[WARN] " + colorama.Style.RESET_ALL + "Failed remainder check.")

            # Print verdict.
            if greater_pass == True and lastdigit_pass == True and remainder_pass == True:
                print(colorama.Fore.MAGENTA + "[INFO] " + colorama.Style.RESET_ALL + "Key " + sys.argv[2] + " is valid.")
            else:
                print(colorama.Fore.RED + "[ERROR] " + colorama.Style.RESET_ALL + "Key " + sys.argv[2] + " is invalid.")

            colorama.deinit()
            sys.exit()
        else:
            print(colorama.Fore.RED + "[ERROR] " + colorama.Style.RESET_ALL + "Couldn't detect key type.")
            colorama.deinit()
            sys.exit()
    else:
        print(colorama.Fore.RED + "[ERROR] " + colorama.Style.RESET_ALL + "Missing key.")
        colorama.deinit()
        sys.exit()
else:
    print(colorama.Fore.RED + "[ERROR] " + colorama.Style.RESET_ALL + "Invalid option.")
    colorama.deinit()
    sys.exit()

# CD 10-digit generation.
if key_type == 10:
    # First three digits.
    init = t10rangen(3, True)

    # Modify first generated digits if necessary.
    while len(init) != 3:
        strlen = len(init)

        if strlen == 1:
            add = t10rangen(2, True)
            init = init + add
        elif strlen == 2:
            add = t10rangen(1, True)
            init = init + add
        else:
            print(colorama.Fore.MAGENTA + "[ERROR] " + colorama.Style.RESET_ALL + "Invalid string length.")
            colorama.deinit()
            sys.exit()

        strlen = len(init)

    # Check for blacklist.
    if init == "333" or init == "444" or init == "555" or init == "666" or init == "777" or init == "888" or init == "999":
        init = str(int(init) - 1)
    
    valid = False

    while valid != True:
        # Last seven digits.
        end = t10rangen(7, True)

        # Modify last generated digits if necessary.
        while len(end) != 7:
            endlen = len(end)

            if endlen == 1:
                addend = t10rangen(6, True)
                end = end + addend
            elif endlen == 2:
                addend = t10rangen(5, True)
                end = end + addend
            elif endlen == 3:
                addend = t10rangen(4, True)
                end = end + addend
            elif endlen == 4:
                addend = t10rangen(3, True)
                end = end + addend
            elif endlen == 5:
                addend = t10rangen(2, True)
                end = end + addend
            elif endlen == 6:
                addend = t10rangen(1, True)
                end = end + addend
            else:
                print(colorama.Fore.MAGENTA + "[ERROR] " + colorama.Style.RESET_ALL + "Invalid string length.")
                colorama.deinit()
                sys.exit()

            endlen = len(end)

        endsplit = split(end)

        # Check validity.
        if int(endsplit[6]) == 0 or int(endsplit[6]) == 8 or int(endsplit[6]) == 9:
            if verbose == True:
                print(colorama.Fore.YELLOW + "[WARN] " + colorama.Style.RESET_ALL + "Last digit failed check test. Retrying.")
        else:
            if verbose == True:
                print(colorama.Fore.MAGENTA + "[INFO] " + colorama.Style.RESET_ALL + "Last digit passed check test.")
            sum = int(endsplit[0]) + int(endsplit[1]) + int(endsplit[2]) + int(endsplit[3]) + int(endsplit[4]) + int(endsplit[5]) + int(endsplit[6])
            if multiple(sum, 7) != True:
                if verbose == True:
                    print(colorama.Fore.YELLOW + "[WARN] " + colorama.Style.RESET_ALL + "Result failed remainder test. Retrying.")
            else:
                if verbose == True:
                    print(colorama.Fore.MAGENTA + "[INFO] " + colorama.Style.RESET_ALL + "Result passed remainder test.")
                valid = True
    
    # Print final key.
    key = init + '-' + end
    print(colorama.Fore.MAGENTA + "[INFO] " + colorama.Style.RESET_ALL + key_type_str + " key: " + key)

# CD 11-digit generation.
if key_type == 11:
    # First four digits, randomly generate the first three.
    init = t10rangen(3, True)
    # Last of the four digits is the third digit, greater by either one or two.
    splitinit = split(init)
    plus = random.randrange(1, 2)
    fourth = int(splitinit[2]) + plus

    # Overflow if necessary.
    if fourth == 10:
        fourth = 1
        four = init + str(fourth)
    elif fourth == 11:
        fourth = 2
        four = init + str(fourth)
    else:
        four = init + str(fourth)

    valid = False

    while valid != True:
        # Last seven digits.
        end = t10rangen(7, True)

        # Modify last generated digits if necessary.
        while len(end) != 7:
            endlen = len(end)

            if endlen == 1:
                addend = t10rangen(6, True)
                end = end + addend
            elif endlen == 2:
                addend = t10rangen(5, True)
                end = end + addend
            elif endlen == 3:
                addend = t10rangen(4, True)
                end = end + addend
            elif endlen == 4:
                addend = t10rangen(3, True)
                end = end + addend
            elif endlen == 5:
                addend = t10rangen(2, True)
                end = end + addend
            elif endlen == 6:
                addend = t10rangen(1, True)
                end = end + addend
            else:
                print(colorama.Fore.MAGENTA + "[ERROR] " + colorama.Style.RESET_ALL + "Invalid string length.")
                colorama.deinit()
                sys.exit()

            endlen = len(end)

        endsplit = split(end)

        # Check validity.
        if int(endsplit[6]) == 0 or int(endsplit[6]) == 8 or int(endsplit[6]) == 9:
            if verbose == True:
                print(colorama.Fore.YELLOW + "[WARN] " + colorama.Style.RESET_ALL + "Last digit failed check test. Retrying.")
        else:
            if verbose == True:
                print(colorama.Fore.MAGENTA + "[INFO] " + colorama.Style.RESET_ALL + "Last digit passed check test.")
            sum = int(endsplit[0]) + int(endsplit[1]) + int(endsplit[2]) + int(endsplit[3]) + int(endsplit[4]) + int(endsplit[5]) + int(endsplit[6])
            if multiple(sum, 7) != True:
                if verbose == True:
                    print(colorama.Fore.YELLOW + "[WARN] " + colorama.Style.RESET_ALL + "Result failed remainder test. Retrying.")
            else:
                if verbose == True:
                    print(colorama.Fore.MAGENTA + "[INFO] " + colorama.Style.RESET_ALL + "Result passed remainder test.")
                valid = True

    # Print final key.
    key = four + '-' + end
    print(colorama.Fore.MAGENTA + "[INFO] " + colorama.Style.RESET_ALL + key_type_str + " key: " + key)

# OEM 20-digit generation.
if key_type == 20:
    # Date generation
    date = str(random.randrange(1, 366))
    
    while len(date) != 3:
        datelen = len(date)

        if datelen == 1:
            date = "00" + date
        elif datelen == 2:
            date = "0" + date
        else:
            print(colorama.Fore.MAGENTA + "[ERROR] " + colorama.Style.RESET_ALL + "Invalid string length.")
            colorama.deinit()
            sys.exit()

        datelen = len(date)

    # Year generation
    year = str(random.randrange(95, 103))

    if year == "100":
        year = "00"
    elif year == "101":
        year = "01"
    elif year == "102":
        year = "02"
    elif year == "103":
        year = "03"

    valid = False

    while valid != True:
    # Middle seven digits.
        mid = t10rangen(6, True)

        # Modify last generated digits if necessary.
        while len(mid) != 6:
            midlen = len(mid)

            if midlen == 1:
                addmid = t10rangen(5, True)
                mid = mid + addmid
            elif midlen == 2:
                addmid = t10rangen(4, True)
                mid = mid + addmid
            elif midlen == 3:
                addmid = t10rangen(3, True)
                mid = mid + addmid
            elif midlen == 4:
                addmid = t10rangen(2, True)
                mid = mid + addmid
            elif midlen == 5:
                addmid = t10rangen(1, True)
                mid = mid + addmid
            else:
                print(colorama.Fore.MAGENTA + "[ERROR] " + colorama.Style.RESET_ALL + "Invalid string length.")
                colorama.deinit()
                sys.exit()

            midlen = len(mid)

        midseg = "0" + mid
        midsplit = split(midseg)

        # Check validity.
        if int(midsplit[6]) == 0 or int(midsplit[6]) == 8 or int(midsplit[6]) == 9:
            if verbose == True:
                print(colorama.Fore.YELLOW + "[WARN] " + colorama.Style.RESET_ALL + "Last digit failed check test. Retrying.")
        else:
            if verbose == True:
                print(colorama.Fore.MAGENTA + "[INFO] " + colorama.Style.RESET_ALL + "Last digit passed check test.")
            sum = int(midsplit[0]) + int(midsplit[1]) + int(midsplit[2]) + int(midsplit[3]) + int(midsplit[4]) + int(midsplit[5]) + int(midsplit[6])
            if multiple(sum, 7) != True:
                if verbose == True:
                    print(colorama.Fore.YELLOW + "[WARN] " + colorama.Style.RESET_ALL + "Result failed remainder test. Retrying.")
            else:
                if verbose == True:
                    print(colorama.Fore.MAGENTA + "[INFO] " + colorama.Style.RESET_ALL + "Result passed remainder test.")
                valid = True

    # Last five digits.
    end = t10rangen(5, True)

    while len(end) != 5:
        endlen = len(end)

        if endlen == 1:
            addend = t10rangen(4, True)
            end = end + addend
        elif endlen == 2:
            addend = t10rangen(3, True)
            end = end + addend
        elif endlen == 3:
            addend = t10rangen(2, True)
            end = end + addend
        elif endlen == 4:
            addend = t10rangen(1, True)
            end = end + addend
        else:
            print(colorama.Fore.MAGENTA + "[ERROR] " + colorama.Style.RESET_ALL + "Invalid string length.")
            colorama.deinit()
            sys.exit()

        endlen = len(end)

    # Print final key.
    key = date + year + '-OEM-' + midseg + '-' + end
    print(colorama.Fore.MAGENTA + "[INFO] " + colorama.Style.RESET_ALL + key_type_str + " key: " + key)

colorama.deinit()
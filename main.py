# Imports
import fileinput
import re
import os

# ----------------------------------------------------------------------------
# Input Variables

# Replacement pattern order must match the order of replacement text below
# Include all english characters and english special characters (without space)
# searchPattern = r'{"[a-zA-z0-9~@#$^*()_+=[\]{}|\\,.?:-]+"'
searchPattern = r'[a-zA-z0-9~@#$^*()_+=[\]|\\,.?:-]+'
outputFilePath = r'.\output.txt'

costPattern = r'cost [0-9]+'

ignoreTrigger = ';'

# List of vehicles default
vehicleCostHashByUnit = {
    # lightmgcars+some other cars
    'iveco_cammo-mg': 130,
    'iveco_cammo-mk19': 180,
    'hummvee':
        {
            'hummvee': 120,
            'hummvee_m240': 110,
            'hummvee_mk19': 150,
            # tank_destroyer
            'hummvee_tow': 200
        },
    'hmmwv_turret': 150,
    'jeep_cj5_mgun': 120,
    'caiman_m2': 125,

    # heavymgcars
    'maxxpro': 180,

    # transports
    'm939': 50,
    'mtvr':
        {
            'mtvr': 70,
            'mtvr_mgun': 120,
            # logis
            'mtvr_ammo': 100,
            'mtvr_ammo_mgun': 150,
            'mtvr_rem': 100,
            'mtvr_rem_mgun': 150,
        },

    # logis


    # mg
    'm240_tstanok': 50,
    'browning_trenoga': 60,

    # mortar
    'm252': 80,

    # gl
    'mk19_stan': 80,

    # atgm
    'ptur_tow': 100,

    # field_artillery
    'm119': 120,
    'm115': 120,


    # light_mortar_spg


    # lightspgarty
    'lav_rino': 280,

    # heavyspgarty
    'm109':
        {
            'm109': 370,
            'm109a3': 700,
            'm109a6': 1000
        },

    # lightrocketarty
    'm142': 900,

    # heavyrocketarty
    'm270':
        {
            'm270': 1200,
            'm270(1)': 1220
        },

    # light_apc
    'stryker_browning': 220,
    'm113':
        {
            'm113': 150,
            'm113a3': 150,
            # Artillery
            'm113art': 230,
            # tank_destroyer
            'm113a4': 200

        },
    'fav': 230,

    # medium_wheeled_apc
    'lav_25':
        {
            'lav_25': 300,
            'lav25a': 380
        },

    # heavy_apc
    'm2a1': 400,
    'm2a2': 410,
    'm2a3': 420,
    'm551': 350,
    'm67': 390,


    # spg_aa
    'm163':
        {
            'm163': 180,
            'm163a1': 200
        },
    'm2_len': 300,
    'm1097_avenger': 300,

    # medium_tank
    'm48a1': 390,
    'm60a4': 470,
    'mbt70': 600,
    'm1': 540,
    'm1a1': 550,
    'm1a2': 700,
    'm1a2_kom': 750,
    'm1a2_tusk': 950,
    'm1a2_sel': 1000,

    # tank_destroyer
    'm1128': 330,

    # aircraft
    'f4f': 800,
    'uh1_m60': 550,
    'uh-60': 600,
    'uh-60at': 650,
    'mh-6_attack': 700,
    'supercobra': 800,
    'apache': 850,
    'mq-9': 1200
}

fileToSearchDirectory = r'.\FilesToSearch'

# Helpers

# Formatting Helper: Gets filePath from file Name and Directory


def getFilePath(fileDirectory, fileName):
    return r'{filePath}\{fileName}'.format(filePath=fileDirectory, fileName=fileName)


def searchLine(text_to_search):
    # Find pattern in the current line
    stringPatternMatch = re.findall(text_to_search, line)
    # If pattern matches, execute next phase
    if stringPatternMatch:
        # Cost will always accompany string match
        # Get costValue
        costPatternMatch = re.findall(costPattern, line)

        # Check and maybe Update Hash table with info
        checkUpdateHash(stringPatternMatch[0], costPatternMatch)


def checkUpdateHash(stringPatternMatch, costValue):
    # Debugging
    print("stringPatternMatch", stringPatternMatch, "\n")
    # print("Type: ", type(stringPatternMatch), "\n\n")
    # print("vehicleCostHashByUnit", vehicleCostHashByUnit, "\n")
    # print("Type: ", type(vehicleCostHashByUnit), "\n\n")

    if stringPatternMatch in vehicleCostHashByUnit:
        print('Vehicle Already in Table')
    else:
        vehicleCostHashByUnit[stringPatternMatch] = costValue


def writeOutput(outputText):
    # Open output file
    d = open(outputFilePath, 'w')
    # Write start
    d.write("{\n")
    # Write formatted inner contents
    for entry in vehicleCostHashByUnit:
        # Format handling
        if type(vehicleCostHashByUnit[entry]) == list:
            rawCost = vehicleCostHashByUnit[entry][0]
            rawCost = re.findall(r'[0-9]+', rawCost)[0]
        else:
            rawCost = vehicleCostHashByUnit[entry]
        d.write('{}: {},\n'.format(entry, rawCost))
    # Write end
    d.write("}")


# Main Code
for fileName in os.listdir(fileToSearchDirectory):
    # Get filePath for fileinput
    filePath = getFilePath(fileToSearchDirectory, fileName)
    with fileinput.FileInput(filePath) as file:
        for line in file:
            if line[0] != ignoreTrigger:
                searchLine(searchPattern)

# Print final resulting table
print("EndResult = ", vehicleCostHashByUnit)
print(vehicleCostHashByUnit['challenger2_applique'][0])
writeOutput(vehicleCostHashByUnit)

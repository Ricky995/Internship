abbrev={"Kumanovo" : "KU",
        "Skopje" : "SK",
        "Sveti Nikole" : "SN"}

cities={
    'KU' : 'Kumanovo',
    'SK' : 'Skopje',
    'SN' : 'Sveti Nikole'
}

cities['KR']="Kratovo"
cities['BT']="Bitola"
print "Kumanovo's abbreviation is: ", abbrev["Kumanovo"]
print "Skopje's abbreviation is: ", abbrev['Skopje']
print "Sveti Nikole's abbreviation is: ", abbrev["Sveti Nikole"]

for abbreviation,city in cities.items():
    print "%s is abbreviation of the city %s" % (abbreviation,city)

### hazf anasor tekrari list ###
def hazfetekrari(classlist):
    new = []
    for ozv in classlist:
        if ozv not in new:
            new.append(ozv)
    return new

classlist= ["amin", "reza", "meysam", "mahnaz", "reza", "paniz", "farokh", "mobina",\
  "reza", "darya", "paniz", "reza", "paniz"]
print(classlist)
print(len(classlist))
print(hazfetekrari(classlist))
print(len(hazfetekrari(classlist)))

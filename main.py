import re
import jinja2
import mimetypes


# Create the emote pack container
class EmotePack(object):
    name = "Untitled Pack"
    desc = ""
    author = ""
    version = ""
    icon = ""
    emotelist = []


class Emote(object):
    filename = ""
    filetype = ""
    shortcuts = []

inputData = open(r"input\theme", 'r')
inputData = inputData.read()

# Instantiate and fill the pack metadata
InputPack = EmotePack()

try:
    InputPack.name = re.findall(r"Name=(.*)", inputData)[-1]
except IndexError:
    print "Couldn't find a name, skipping"
    pass

try:
    InputPack.desc = re.findall(r"Description=(.*)", inputData)[-1]
except IndexError:
    print "Couldn't find a description, skipping"
    pass
InputPack.desc += " converted by Kline Eto"

try:
    InputPack.author = re.findall(r"Author=(.*)", inputData)[-1]
except IndexError:
    print "Couldn't find an author, skipping"
    pass

# Reopen the pack in line mode
inputFile = open(r"input\theme", 'r')
inputFile = inputFile.readlines()

# Fill the container with Emotes
for line in inputFile:
    if line.startswith('!'):
        line = line.replace('!', '')    # Strip off the leading !
        line = line.split()             # Split into tokens

        thisEmote = Emote()
        thisEmote.filename = line[0]
        thisEmote.filetype = mimetypes.guess_type(line[0])[0]
        thisEmote.shortcuts = line[1:]

        InputPack.emotelist.append(thisEmote)

# Build the output file
env = jinja2.Environment(
    trim_blocks=True,
    lstrip_blocks=True,
    loader=jinja2.FileSystemLoader("./templates")
)

vacuumTemplate = env.get_template("vacuum.jtp")
print vacuumTemplate.render(Emotes=InputPack)
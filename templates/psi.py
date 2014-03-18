from yapsy.IPlugin import IPlugin
import jinja2
import zipfile


class VacuumBackend(IPlugin):
    pack = None
    icondef = ""
        
    def build(self, pack):
        self.pack = pack
        print "[Psi] Building icondef..."
        self.buildicondef()
        print "[Psi] Building zip..."
        self.makeZip()

    def buildicondef(self):
        env = jinja2.Environment(
            trim_blocks=True,
            lstrip_blocks=True
        )

        vacuumTemplate = env.from_string(self.template)
        self.icondef = vacuumTemplate.render(Emotes=self.pack)

    def makeZip(self):
        outzip = zipfile.ZipFile("output/psi.zip", 'w')
        outzip.writestr(self.pack.name+"-psi/icondef.xml", self.icondef)
        for emote in self.pack.emotelist:
            try:
                outzip.write("input/"+emote.filename, self.pack.name+"-psi/"+emote.filename)
            except OSError:
                # The underlying emote file isn't found
                # This throws varying errors, but are all OSError or subclasses
                pass
        outzip.close()


    template = \
"""<?xml version='1.0' encoding='UTF-8'?>
<icondef>
    <meta>
        <name>{{ Emotes.name }}</name>
        <description> {{ Emotes.desc }} </description>
        <author>{{ Emotes.author }}</author>
        <version>{{ Emotes.version }}</version>
    </meta>

    {% for file in Emotes.emotelist %}
    <icon>
        {% for shortcut in file.shortcuts %}
        <text>{{ shortcut }}</text>
        {% endfor %}
        <object mime='{{ file.filetype }}'>{{ file.filename }}</object>
    </icon>

    {% endfor %}
</icondef>"""
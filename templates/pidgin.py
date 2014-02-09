from yapsy.IPlugin import IPlugin
import zipfile


class PidginBackend(IPlugin):
    pack = None

    def build(self, pack):
        self.pack = pack
        print "[Pidgin] Building zip..."
        self.makeZip()

    def makeZip(self):
        outzip = zipfile.ZipFile("output/pidgin.zip", 'w')
        outzip.write("input/theme", "BerachsEmotePack-pidgin/theme")
        for emote in self.pack.emotelist:
            try:
                outzip.write("input/"+emote.filename, "BerachsEmotePack-pidgin/"+emote.filename)
            except OSError:
                # The underlying emote file isn't found
                # This throws varying errors, but are all OSError or subclasses
                pass
        outzip.close()
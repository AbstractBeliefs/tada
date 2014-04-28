from yapsy.IPlugin import IPlugin
import json
import cStringIO
import zipfile


class InstantbirdBackend(IPlugin):
    pack = None
    theme = { "smileys": [] }

    def build(self, pack):
        self.pack = pack
        print "[InstantBird] Building Theme JSON..."
        self.buildTheme()
        print "[InstantBird] Packaging..."
        self.package()

    def buildTheme(self):
        for emote in self.pack.emotelist:
            self.theme['smileys'].append({
                "filename": emote.filename,
                "textCodes": [code for code in emote.shortcuts]
            })

    def package(self):
        jar = cStringIO.StringIO()
        jarZip = zipfile.ZipFile(jar, 'a')
        jarZip.writestr("theme.js", json.dumps(self.theme))

        for emote in self.pack.emotelist:
            try:
                jarZip.write("input/"+emote.filename, emote.filename)
            except OSError:
                pass

        outzip = zipfile.ZipFile("output/instantbird.xpi", "w")
        jarZip.close()
        jar.seek(0)
        outzip.writestr("chrome/skin.jar", jar.read())

        if not self.pack.version:
            self.pack.version = "1.0"

        outzip.writestr("chrome.manifest", self.manifest)
        outzip.writestr("install.rdf", self.rdf % (self.pack.name, self.pack.version, self.pack.desc, self.pack.author))
        outzip.close()


    manifest = "skin\tconverted\tclassic/1.0\tjar:chrome/skin.jar!/"
    rdf = \
"""<?xml version="1.0"?>

<RDF xmlns="http://www.w3.org/1999/02/22-rdf-syntax-ns#" 
    xmlns:em="http://www.mozilla.org/2004/em-rdf#">

  <Description about="urn:mozilla:install-manifest">
    <em:id>emoticons-converted@emotes.spacetechnology.net</em:id>
    <em:name>%s</em:name>
    <em:version>%s</em:version>
    <em:description>%s</em:description>
    <em:creator>%s</em:creator>
    
    <!-- Instantbird -->
    <em:targetApplication>
      <Description>
        <em:id>{33cb9019-c295-46dd-be21-8c4936574bee}</em:id>
        <em:minVersion>0.2a1pre</em:minVersion>
        <em:maxVersion>5.5a1pre</em:maxVersion>
      </Description>
    </em:targetApplication>
  </Description>    
</RDF>"""

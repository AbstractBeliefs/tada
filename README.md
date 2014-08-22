tada
====

Convert emote packs from one format to another

tada expects the following:
* an `input' folder with an unpacked pidgin emote pack
* a `templates' folder with output plugins

and will return:
* output formats zipped in an `output' folder.


This tool was mainly designed for converting Berach's EVE Online Pidgin pack between various formats and is currently deployed as a post-checkout hook, triggered by automated checkouts with the GitHub webhook api.


Currently supported formats
===========================
* Adium
* InstantBird
* Pidgin
* Psi
* Vacuum
* Gajim
* phpBB
* Trillian

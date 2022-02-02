# pip requirements
* shutil
* pdf2image
* natsort
* deep_translator


# Notes
install module [argos - translate](https://github.com/argosopentech/argos-translate) and implement this on the project. 
Either by adding a package in pip (argostranslate) and using the cli edition

You can make a fucking bodge and pipe cat "desired file to translate.txt" || argos-translate --from-lang fr --to-lang es > output.txt
Lol, that was horrible scripting but works.

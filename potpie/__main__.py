# -*- coding: utf-8 -*-
import argparse
import os
import polib

from .pseudo import types

PSEUDO_TYPE_CLASSES = {
    "brackets": types.BracketsPseudoType,
    "unicode": types.UnicodePseudoType,
    "planguage": types.PLanguagePseudoType,
    "extend": types.ExtendPseudoType,
    "mixed": types.MixedPseudoTypes
}


def translate(infile, outfile, type="mixed"):
    po = polib.pofile(infile)

    translator = PSEUDO_TYPE_CLASSES[type]("po")

    for entry in po:
        entry.msgstr = translator.compile(entry.msgid)

    outfile_abspath = os.path.abspath(outfile)
    outfile_dirname = os.path.dirname(outfile_abspath)
    if not os.path.exists(outfile_dirname):
        os.makedirs(outfile_dirname)
    po.save(outfile)

def main():
    parser = argparse.ArgumentParser(description="Create pseudo translation files.")
    parser.add_argument("infile", metavar="infile", help="the path to the source file")
    parser.add_argument("outfile", metavar="outfile", help="the path to save the psuedo translation to")
    parser.add_argument("--type", dest="type", default="mixed", choices=PSEUDO_TYPE_CLASSES.keys(), help="The type of psuedo translation")

    args = parser.parse_args()

    translate(args.infile, args.outfile, type=args.type)

if __name__ == "__main__":
    main()

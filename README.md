![Banner](https://github.com/PinedaVictor/Durtles/blob/main/docs/banner.jpg)

## Description

> Mission - Build directory utilities that automate time-consuming tasks.

Directory utilities are built for common and specific use cases. Professionals, such as IT professionals and NFT artists' can use this to identify spelling errors in a directory. Files with spelling errors can quickly be separated for editing and migrated back to the original directory.

## Features:

- Rename files matching a regular expression
  - As of 4/18/22 - This feature is spacific to exported files from photoshop and intended to be used with [Hashlips Art Engine](https://github.com/HashLips/hashlips_art_engine)
- Check for file spelling erros in a directory
- Seperate misspelled files for editing
  - Able to autmatically migrate back to original directory
- Count how many folders in a directory
- MORE TO COME.....

## Requirements:

- [Python 3](https://www.python.org/)

## How to use:

Ensure you have properly installed Python 3 on your system

1. Clone repository
2. Within [VSCODE](https://code.visualstudio.com/) mkdir called Edit
3. cd into scripts folder
4. Run script of choice in the following format:
   - python3 script.py [Optional CMD Argument]

| Script        | CMD Argument | Description                                                                                            |
| ------------- | :----------: | ------------------------------------------------------------------------------------------------------ |
| count_folders |     none     | Counts folders in Edit directory                                                                       |
| rename        |     none     | Prints preview of files that will be renamed                                                           |
| rename        |      -r      | Renames files                                                                                          |
| spell_checker |     none     | Scans Edit directory and prints misspelled files to the console                                        |
| spell_checker |     -ss      | Places all misspelled files in a directory called Misspelled (removes them from Edit dirctory )        |
| spell_checker |      -m      | Migrates all files in Misspelled directory back to Edit directory in it's correct sub folder (if any). |

## License

[BSD 3](https://github.com/PinedaVictor/Durtles/blob/main/LICENSE)

**Free Software, Hell Yeah!**

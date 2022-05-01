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
2. mkdir called Edit
3. cd into src folder
4. Run in the following format:
   - python3 main.py [Command...] [Option...]

| Command | Option    | Description                                                    |
| ------- | --------- | -------------------------------------------------------------- |
|         | -h, -help | Display help menu                                              |
|         | -pr       | Preview files that will be renamed                             |
|         | -r        | Rename files                                                   |
|         | -c        | Count number of sub directories                                |
| check   |           | Prints Errors found                                            |
| check   | -h, -help | Display check help menu                                        |
| check   | -ps       | If errors found print suggestions                              |
| check   | -ss       | Seperate misspelled files into the misspelled directory        |
| check   | -m        | Migrate files in the misspelled directory back to their origin |

## License

[BSD 3](https://github.com/PinedaVictor/Durtles/blob/main/LICENSE)

**Free Software, Hell Yeah!**

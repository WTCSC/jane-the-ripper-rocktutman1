# Guide to downloading and running the Rocktutman1 Jane-The-Ripper

## Description

The **Rocktutman1 Jane-The-Ripper** is a *unique* and *clean* hash cracker for specific hashes from a wordlist
![flowchart image](https://github.com/WTCSC/jane-the-ripper-rocktutman1/blob/main/images/Jane-The-Ripper-Flowchart.png)
## Requirements

- **Python3** or higher
- *hashlib* module installed
- GIT extension for linux

## Installation 

Clone the git repository

> git clone https://github.com/WTCSC/jane-the-ripper-rocktutman1

## Usage

### For local install

Navigate into the local git-repo 

>cd jane-the-ripper-rocktutman1/

Create your hashes and wordlist file if not already done - they should be formated with one hash/potential word per line and no spaces at start or end of it.
They dont *need* to be in the git repo directory, but it will make entering them into the program a lot easier.
If you are just playing around the repo includes its own files for testing purposes.

After running **HashCracker.py** you should see a screen like this
![terminal screen](https://github.com/WTCSC/jane-the-ripper-rocktutman1/blob/main/images/Jane-The-Ripper-Running.png)

Enter the path to your file(s) when prompted, you **cannot** use ~/ since the program is not running as your user. It should look something like this:
#### If in any other directory
>Enter the relative path to your wordlist: /path/to/wordlist.txt
>Enter the relative path to your hashes: ../hashes.txt
#### If in the repo
>Enter the relative path to your wordlist: wordlist.txt
>Enter the relative path to your hashes: hashes.txt
#### If using the pre-installed files
>Enter the relative path to your wordlist: test_files/test_wordlist.txt
>Enter the relative path to your hashes: test_files/test_hashes.txt


## Configuration

No configuration is curently available

## Testing

* Move into the git-repo (as done earlier)
* Type pytest -v
* Watch as the results print
  ![testresults](https://github.com/WTCSC/jane-the-ripper-rocktutman1/blob/main/images/Jane-The-Ripper-Tests.png)

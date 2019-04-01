# Submit your first assignment

![](https://images.unsplash.com/photo-1483691278019-cb7253bee49f?ixlib=rb-0.3.5&s=bde2973b4155399f086b85ec2337e889&auto=format&fit=crop&w=1000&q=80)
Photo by [Yoann Boyer](https://unsplash.com/photos/i14h2xyPr18)


## Objectives
* Understand the structure of an exercise's repo, and the link to your Github account.
* Learn to test your code locally before submitting your solution.
* Learn the basic git commands to commit modifications to your code and push them to Github.


## Guidelines

During these 10 weeks, you'll work in pairs. A new teammate is assigned to you each day.

Before starting a new challenge, **make sure that you explain to each other what you think you are being asked to do** and **before** starting to write a single line of code. Then you can pair program on one screen, or work side by side, checking up every 10 minutes or so to help one another.

Working in pairs is a common practice in software engineering. The idea is that if you work alone and you get stuck, you can lose several hours digging around for the issue, whereas a fresh pair of eyes would find the problem within seconds. Don't underestimate that!


### Exercice 1
When correct, this exercise will give you 1 green result line out of 3. The other line will be green when you're done with exercise 2.

Move to the exercise folder corresponding to this README file.

* Run `invoke run`. It should all be red (as you have not started coding).
Open the `src/nibble_start.py` file in VSCode. That's where you'll need to edit the code.

* Implement the first `TODO:`, print out `"That's how it starts"` instead of what's currently being printed out
* In the terminal, run `invoke run` and make sure you have one green result.
* Commit your changes and push them
* Go back to `HAL` and refresh the page. You should see your first test has passed.

### Exercice 2
Still in the same file, implement the second `TODO:`. You need to print out the github username of your teammate, if you don't have a teammate, just print out your own username.
This is your first solo assigment

### Exercise 3: Practising command lines (Terminal)
Before going further with nibble challenges, we'll first work on the command lines you've just learnt.

NOTE: **You're not allowed to use Finder (or your file browser)!**

#### tmp directory
First step, we'll create all our files in a directory named tmp.

* Go to your home directory (`~`)
* Check if you have a `tmp` directory here, **if not create it**
* Go to the `tmp` directory
* Create a directory `nibble-tmp` in this directory
* Go to the `nibble-tmp` directory

#### README file
* Inside `nibble-tmp` directory, create a file named `README.md`
* Open the `nibble-tmp` directory in `VSCode`. Write some text in the `README.md` file.

#### Level-1 directory
* Create a `level-1` directory in the `nibble-tmp` directory.
* Go to this directory and create a file named `README-level1.md`
* Display the path where you are

#### Level-2 directory
* Go back to the parent directory
* From `nibble-tmp` directory, create a directory named `level-2` inside the directory `level-1`
* Still from `nibble_tmp` directory, create a file named `configuration` inside the directory `level-2` (which is inside `level-1`)

#### Playing with files
Let's use the `mv` command that you'll use to move/rename folders and files. It's time to act like a real technologist! Use google to find out how to complete the following instructions:

* Move this configuration file from level-2 directory to level-1 directory
* Go to `level-1` directory
* Rename `configuration` file into `config`
* List all files
* Remove `level-2` folder
* Remove `config` file

#### Final words
* Go back to your home (`~`) directory
* Go into the `tmp` folder
* Destroy the `nibble-tmp` folder
* Clear the terminal window

When you're done you can look at the links below.

* [git cheatsheet](http://rogerdudler.github.io/git-guide/files/git_cheat_sheet.pdf)
* [interactive git cheatsheet](http://www.ndpsoftware.com/git-cheatsheet.html)
* Read and practise all of this tutorial: [Learn Enough Command Line to Be Dangerous](http://www.learnenough.com/command-line/)


---

As a quick reminder, here are a couple git commands you might need.

#### `git clone <GITHUB_URL>`
Clone the git repository from `<GITHUB_URL>`

#### `git status`
Show the current status of your git repository

#### `git log`
Show the history of previous commits

#### `git add <FILE_NAME>`
Add `<FILE_NAME>` to the stage

#### `git commit`
"Take a picture", e.g. commit your changes

#### `git push`
Push your photo album to github.

---

And a couple of command line commands.

#### `code .`
Open current directory in `VSCode`.

#### `pwd`
Display the path to your current location.

#### `ls`
List the files and folders at your current location.  
Use `ls -a` for showing hidden files.

#### `cd <FOLDER_NAME>`
Navigate into a subdirectory.

#### `cd ..`
Go up one directory.

#### `mkdir <NEW_FOLDER>`
Create a directory named `<NEW_FOLDER>`.

#### `touch <NEW_FILE>`
Create the file named `<NEW_FILE>`.

#### `mv <FILE_NAME> <FOLDER_NAME>`
Move  `<FILE_NAME>` to `<FOLDER_NAME>`.

#### `mv <FILE_NAME> <NEW_FILENAME>`
Rename `<FILE_NAME>` to `<NEW_FILENAME>`.

#### `cat <FILE_NAME>`
View the content of a file directly from the terminal (without opening a text editor.

---

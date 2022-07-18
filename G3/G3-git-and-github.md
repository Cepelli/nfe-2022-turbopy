Git and Github (and Markdown)
=============================
*Time to complete: 8 hours* 

*Seminar date: 10:00 A.M. Eastern, Friday, June 18, 2021*

Prep
----
1. Read **Sections 1.1 through 1.4** in the [Pro Git book](https://git-scm.com/book/en/v2).
2. If you haven't already, install `git` following the directions in [G2 Development Environment Notes](https://github.com/NRL-Plasma-Physics-Division/turbopy-bootcamp/blob/main/G2/G2-dev-environment-notes.md).
3. Complete the RealPython courses: [Python Git and Github Intro](https://realpython.com/courses/python-git-github-intro/)
4. Review [15 rules for communicating at GitHub](https://ben.balter.com/2014/11/06/rules-of-communicating-at-github/)
5. Complete [this markdown lesson](https://www.markdowntutorial.com) and read [Mastering Markdown (for Git)](https://guides.github.com/features/mastering-markdown/).

Seminar Goals
-------------
Discuss what we learned about Git and GitHub.
 
Homework
--------
1. If you haven't already, fork and clone the turbopy-bootcamp repo following the directions in [G2 Development Environment Notes](https://github.com/NRL-Plasma-Physics-Division/turbopy-bootcamp/blob/main/G2/G2-dev-environment-notes.md).
2. Create a `g3-lastname` branch (using your last name, of course) and commit/push at least one note to the Notes section of this markdown file. Push the changes to your fork.
3. Create a pull request to merge your `g3-lastname` branch in your fork to `turboPy-bootcamp` main in the NRL PPD Team site on GitHub. Be sure to reference the seminar issue in the PR.

Notes
-----
- When cloning a repo, if you have setup `git` to authenticate using an SSH key, you may need to use the clone URL that corresponds with the SSH option and not the HTTPS or GitHub CLI option. 
- Be sure to name branches and files logically and succinctly so as to minimize confusion between editors.
- When forking the organization repository it is possible that not all branches will show up on your personal repository page.
  Double check that all branches appear on your local Git client and if they do then there shouldn't be an issue.
- Always put a commit summary in the imperative form.
- If the push command fails, try checking the SSH key you set up, it might require your passphrase
- Make sure your local repo is up to date with the upstream to avoid merge conflicts. 
- Generally, it's not a good idea to commit directly to main. Instead, create a development branch and merge it with a pull request on github.
- The `.gitignore` file is used for untracked files that you want Git to ignore.
- You can directly edit files in GitHub, but it's better to follow the _local git&#8594;fork&#8594;PR to main_ pathway.
- Pay close attention to markdown to ensure that your text is readable.
- You can force a line break in markdown by putting two spaces, or a backslash, at the end of a line. Learned about it [here](https://gist.github.com/shaunlebron/746476e6e7a4d698b373).
- You can also make text _italicized_ or **bold** by surrounding the text with underscores or asterisks like so: \*italics* or \_italics_ and \*\*bold** or \_\_bold__.
- Git stash is a way to stash changes made to a file that you don't want to commit

- Make sure to comment on your commit so the person reviewing it has a clear idea of the purpose
- [This link](https://en.wikipedia.org/wiki/Markdown#Example) gives other possible formatting additions in Markdown like strikethrough to show edits or completed items: ~~update #1~~.
- Git stash is a way to stash changes made to a file that you don't want to commit
- [This page](https://www.markdownguide.org/basic-syntax/) describes all the basic formating rules for markdown (.md) files. Use them to create lovely and readable text documents for your fellow interns and mentors **:)**
- [Updating Fork](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/syncing-a-fork) (From upstream main branch):
```shell
# start in local main
git checkout main
# add remote for upstream
git remote add upstream https://github.com/NRL-Plasma-Physics-Division/turbopy-bootcamp.git
git fetch upstream
# merge the copied PPD main files in upstream to main
git merge upstream/main 
# push the changes to origin (your fork, implied)
git push 
```
- You can fetch someone else's fork/branch (see [the inspirational gist](https://gist.github.com/elfrank/c08256de9c15e41e1781)):
```shell
# add remote for batman's iambatman repo
git remote add batman git@github.com:batman/iambatman.git
# fetch batman's code in iambatman
git fetch batman 
# switch to savegotham branch, naming it local-branch-name locally
git checkout -b local-branch-name batman/savegotham 
```
- If you are in a development branch and want to revert a modified file that was committed, one way is by reverting it to its unmodified version from main
```shell
#Create a development branch if one does not already exist
git branch dev-branch
#start in your development branch
git checkout dev-branch
#replace a file with the unmodified version in your main branch
git restore -s main foldername/filename
```

- Hello! My name is Jaela Whitfield. This homework allowed me to understand the basics of git and how to clone the main repository, make branches, and lastly stage and commit files.

- Once you're done working with a development branch (merged, messed up, ), you can delete it from both your local repo and remote repo from the command line. It can also be done through the browser on your account.
```shell
#Removing a branch from your remote repo
git push -d origin dev-branch
#Or
git push origin --delete dev-branch
#Removing a local branch
git branch -d dev-branch
#If Git refuses to let you, you can force it with D
git branch -D dev-branch
```

- If you are using the Zsh for your shell and want tab completion for git commands, add the following to your .zshrc file and restart the terminal:
```shell
autoload -Uz compinit && compinit
```
- To set an upstream branch while pushing changes to a new development branch
```shell
git push -u origin dev-branch
```

- Text customization such as **bold** and _italicize_ can be stacked like this: **_hello_** ~~_world_~~


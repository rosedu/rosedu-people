```
git status
```

You will see the files
- untracked: Files that git doesn't know about
- modified: Files you modified
- changes to be commited: Files and changes that will be committed in the repo on the next ```git commit```

```
git add FILES_YOU_WANT_TO_COMMIT
```

You will the files that will be commited in the next ```git commit```. To check that you did exactly what you intended to do run ```git status``` again

```
git commit -m COMMIT_MESSAGE
```

Commits __locally__ the changes that were to be committed in ```git status``` 

At this point you will have the commits only locally and you want to sync them with the remote branch.

If somebody updated the branch before you, you should do a ```git pull origin BRANCH_NAME``` this will try to merge the changes from remote to your local branch. If any conflicts occur, you should try to solve them. 
http://git-scm.com/book/en/Git-Branching-Basic-Branching-and-Merging

After solving the conflicts do a ```git push origin BRANCH_NAME``` to push your commits in the remote repository.

If you want to fetch a branch that was created by another person and work on that
```
git fetch origin
git checkout THE_BRANCH_YOU_WANT_TO_WORK_ON
```

#### Other stuff
Sync your current branch  with master
```
git checkout master # Gets you on the master branch
git pull origin master # syncs the remote master with your local one
git checkout BRANCH_YOU_WORK_ON
git merge master # merge the synced master with your current branch (if the BRANCH_YOU_WORK_ON depends on changes in master, or you have merge conflicts from your branch to master)
```

You should sync master before you start working on any issue

If you have any other questions ask ahead :)

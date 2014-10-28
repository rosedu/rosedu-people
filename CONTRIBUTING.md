These guidelines are here to help people collaborate, learn and contribute to a great Open Source Software project!

## Submitting a bug
If you submit a bug please add a screenshot or description of the __effect__. Github knows to upload pictures from clipboard :).
If you know the steps of __reproducing__ the bug please share them.

## Creating an issue

An issue must be specified so __everyone__ who reads it and knows how People looks like, knows __what__ must be done and __why__.

We want the issues to be specified this way in order to make any developer, new or with experience, understand the __problem__ and implement it as good as he can.

A good starting template is this one. You can copy/paste it from [here](https://raw.github.com/rosedu/rosedu-people/master/doc/issue_template.md).

An example of the workflow is [this one](https://github.com/rosedu/rosedu-people/pull/73)
#### Need

``` gherkin
In order to <the benefit of the issue being solved>
As a <stakeholder e.g. developer, user, company, comunity member, etc.>
I want to <the feature/enhancement that needs to be implemented in the issue>
```

#### Deliverables
_a list of high end benefits that will be delivered when the issue is completed._

_examples:_
- World Peace and harmony
- An ending to World Hunger


#### Prerequisites
_If you already know parts of the code or documents that could help a developer get to the deliverables share them here._
_You can add documents, blogposts, links to code._

- [Mihai B on world peace](http://mihaibivol.worldpeace.org)
- [Current implementation of WorldPeace class](http://somelinktoafile)

#### Solution
_If you know the basic steps of implementing it, share with others!_

## Working on an issue

You already have an issue that follows the format mentioned above and you want to start coding.

To help __others__ understand how you approached the problem please update the issue with a small description of the solution.
If you encounter problems, please share them in the comments.

We follow some conventions for writing code. They are:

    - [PEP8](http://legacy.python.org/dev/peps/pep-0008/)
    - [Google Python Style Guide](https://google-styleguide.googlecode.com/svn/trunk/pyguide.html)

Spend some time reading them before jumping into coding, they will help you write better code.

#### Git, hub and magic
In order to have the code linked with the issue it solves the following flow is preffered.

##### You don't have access to this repo.
- Fork this project and add the upstream remote. Detailed instructions are found [here](https://help.github.com/articles/fork-a-repo)

#### Basic steps
- Create a branch named {{issue_number}}-small-description-of-issue
```
$ git checkout -b 42-end-to-world-hunger
```

- Start working on the issue.
- Use commits that make only one change. Include the issue number in the commit.
```
$ git commit -m "Give food to random strangers #42"
```

- Push to a remote branch named as the local one. Please use the __explicit__ push command.
```
$ git push origin 42-end-to-world-hunger
```

- You think you are done. Run the tests suite
```
./manage.py test
```

- If nothing fails, create a pull request on the issue you are trying to solve.

- Ask for a code review using @reviewer_name tags in comments

- If the pull request can't be merged please rebase the master branch into your branch. You should this before you open the pull request and running the tests, just in case. How to:

 - If working on a fork
  
  ```bash
  $ git fetch upstream
  $ git merge upstream/master
  $ git checkout 42-end-to-world-hunger
  $ git rebase master
  ```
 - If working on the rosedu repo
  
  ```bash
  $ git fetch origin
  $ git merge origin/master
  ```

- More info on [rebase](http://git-scm.com/docs/git-rebase) in case you have conflicts etc.

- Congratulations! You have made a contribution to this project!


Sugested program for Windows: TortoiseHG

# Guides and tutorials #

Add your content here.  Format your content with:
  * HG Book: http://hgbook.red-bean.com/read/
  * http://stackoverflow.com/questions/1711546/how-to-initialize-google-code-project-in-mercurial
  * FAQ: http://mercurial.selenic.com/wiki/FAQ



# Setup progress #
## TortoiseHG ##
_This does not pretend to be a guide to use Mercury in general, but only to setup a repository to this project. For example, the idea of a distributed repository is not discussed nor exploted explicitally here._

_I can only test this method with TortoiseHG over WXP, but other clients and OS must be similar._

First of all,create a new directory, and selecting it, make Tortoise to create a repository. After that, clone the server repository:

`https://einsteniangema.googlecode.com/hg/`

Now, on your local machine you have a full copy of the repository. It is time to start working in the code. When you have done a serial of changes, you must perform a commit. In Tortoise, it is done right-clicking on the directory and selecting HG commit.

Before goin further, we must _configure_ the client. In the `TortoiseHG` tab, select a `Three-way Merge Tool`. kdiff3, for example, is a default in Windows. In `Commit` put your username. Otherwise, it will ask you for it later.

In the open window you must select the files whose change you want to upload. Don't forget to name it with a relevant message. Tip: take a look at the diff tab. In Commit

These changes are only local, not yet uploaded or synchronized. This is done from the Synchronize app. The basic options here are **push** and **pull**.

  * **pull** download all comits from the server. Sugested to do often.
  * **push** upload your commits to the server repository.

You can also use **incoming** and **outgoing** to see what changes would be made by the precedent commands without actually doing them.

All these operations should be made agaisnt another repository. In our case, we will always use the server, but any other repository would work (that means "distributed"). In the repository bar the address of the second should be put. For saving time, onto the _configure_ window you can save the repositories you work with.


Each time a commit is pushed, you should receive an email with the diff.


Note: all this is also valid for the wiki, but its direction is, instead, `https://wiki.einsteniangema.googlecode.com/hg/`

### Advanced features (TODO) ###
  * **Move files**
  * **Rename**
  * **Deleting**
  * **Restoring**
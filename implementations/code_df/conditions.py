"""
Conditions for filtering in or out some items coming from Perceval.

We have two kinds of conditions:

* Those rooted at Code, which are for defining which files
  are source code, and which ones are not. They provide a
  check() method which checks if a filename corresponds to
  source code.

* Those rooted at Commit, which are for conditionally filtering
  the DataFrame of items. They provide a set_commits() method,
  which selects those commits satisfying a given condition,
  as well as a check() method which checks whether a commit in
  the DataFrame has been selected by set_commits() or not.
"""


class Code():
    """
    Root of the hierarchy for deciding if a commit touches source code.

    """

    def __init__(self):
        pass

    def check(self, file):
        """
        Returns the check method of the algorithm to be used.

        :param file: a dictionary, an element of commit['files'] list
            where commit is a structure returned by commit._flatten_data

        :returns Boolean value: True if the file is part of source code,
            False otherwise
        """

        raise NotImplementedError


class Naive(Code):
    """
    Naive condition: all files are source code files
    """

    def check(self, file):
        """
        Check if file is considered as a source code file.

        The naive implementation always returns True.

        :param file: file name to check (full path)
        :returns: Always True in this case (Boolean)
        """

        return True


class DirExclude(Code):
    """
    Consider files in certain directories are not source code.
    """

    def __init__(self, dirs=['tests', 'bin']):

        self.dirs = dirs

    def check(self, file):
        """
        Check if a file path is source code or not.

        If the path is in the list of directories,
        return False. True otherwise.

        :param file: file name to check (full path)

        :returns:    False if in the list of directories (Boolean)
        """

        if any(file.startswith(path) for path in self.dirs):
            return False
        else:
            return True


class PostfixExclude(Code):
    """
    Consider files with certain postfixes as not source code.
    """

    def __init__(self, postfixes=['.md', 'README']):

        self.postfixes = postfixes

    def check(self, file):
        """
        Check if a file path is source code or not.

        If the path last characters match some element in the list
        of postfixes, consider it is not source code.

        :param file: file name to check (full path)

        :returns:    False if in the list of postfixes (Boolean)
        """

        if any(file.endswith(postfix) for postfix in self.postfixes):
            return False
        else:
            return True


class Commit():

    def __init__(self):

        pass

    def set_commits(self, commits):
        """
        Set the DataFrame with commits to be analyzed for condition

        :param commits: commits (DataFrame)
        """

        raise NotImplementedError

    def check(self, commit):
        """
        Check if a commit is in included (check is True).

        If the commit is in the set of included commits, return True.
        False, otherwise.

        :param commit: commit to check (hash as a string)

        :returns:      True if included (Boolean)
        """

        if commit in self.included:
            return True
        else:
            return False


class MasterInclude(Commit):
    """
    Consider as included only commits in master
    """

    def set_commits(self, commits):
        """
        Set the DataFrame with commits to be analyzed for condition

        This method also prepares the set of included commits
        (those in master), so that the check can be done quickly later.

        To find commits in the master branch, this method finds
        the commit annotated with the ref 'HEAD -> refs/heads/master',
        and then goes back, following parents for each commit,
        until the first one present in the data frame.

        :param commits: commits (DataFrame)
        """

        self.commits = commits
        df = self.commits
        todo = set()
        for _, commit in df.iterrows():
            if 'HEAD -> refs/heads/master' in commit['refs']:
                todo.add(commit['hash'])

        self.included = set()
        while len(todo) > 0:
            current = todo.pop()
            self.included.add(current)

            if len(df[df['hash'] == current]['parents']) > 0:
                for parent in df[df['hash'] == current]['parents'].iloc[0]:
                    if parent not in self.included:
                        todo.add(parent)


class EmptyExclude(Commit):
    """
    Consider as excluded empty commits
    """

    def set_commits(self, commits):
        """
        Set the DataFrame with commits to be analyzed for condition

        This method also prepares the set of included commits
        (those which are not empty commits), so that the check
        can be done quickly later.

        To check for empty commits, this method checks the value of
        the `files_action` field which is a count of the number of
        files a commit affects. If this is 0, the commit is an empty
        commit.

        :param commits: commits (DataFrame)
        """

        self.commits = commits
        df = self.commits
        df = df[df['files_action'] != 0]
        self.included = set(df['hash'].tolist())


class MergeExclude(Commit):
    """
    Consider as excluded merge commits
    """

    def set_commits(self, commits):
        """
        Set the DataFrame with commits to be analyzed for condition

        This method also prepares the set of included commits
        (those which are not merge commits), so that the check
        can be done quickly later.

        To check for merge commits, this method checks value of the
        boolean field 'merge' of each commit. If True, the commit is
        a merge commit.

        :param commits: commits (DataFrame)
        """

        self.commits = commits
        df = self.commits
        df = df[~df['merge']]

        self.included = set(df['hash'].tolist())

import os
import subprocess

def testGetGitLastRev(GitRepoDir, gitPath):
    gitCommand = gitPath + "git rev-parse --verify HEAD"
    print ("git Command is %s" % gitCommand)
    os.chdir(GitRepoDir)
    result = subprocess.check_output(gitCommand, shell=True)
    print result.strip()


testGetGitLastRev("/home/jasonli/git/VistA-FOIA/", "/usr/bin/")

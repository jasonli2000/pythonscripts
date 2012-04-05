import os
import subprocess
import sys

def testGetGitLastRev(GitRepoDir, gitPath):
    gitCommand = os.path.join(gitPath,"git") + " rev-parse --verify HEAD"
    print ("git Command is %s" % gitCommand)
    os.chdir(GitRepoDir)
    result = subprocess.check_output(gitCommand, shell=True)
    print result.strip()


gitRepo = sys.argv[1]
gitPath = sys.argv[2]

testGetGitLastRev(gitRepo, gitPath)

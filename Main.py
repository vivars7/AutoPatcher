__author__ = 'Raeseok, Lee'
__license__ = 'MIT'
__email__ = 'irae@realcoder.net'

import json
import os
import shutil
import pathlib
import fnmatch
import datetime

def move_files(src: str, dst: str, pattern: str = '*'):
    if not os.path.isdir(dst):
        pathlib.Path(dst).mkdir(parents=True, exist_ok=True)
    for f in fnmatch.filter(os.listdir(src), pattern):
        shutil.move(os.path.join(src, f), os.path.join(dst, f))

if __name__ == "__main__":
  with open('patch.json', 'rt', encoding='UTF-8') as json_file:
    data = json.load(json_file)
    sourceDir = data['sourceDir'];
    targetDir = data['targetDir'];
    backupDir = data['backupDir'];
    archiveType = data['archiveType'];
    deployList = data['deployList'];

  # backup
  # if backup directory not exists then make it.
  os.makedirs(backupDir, exist_ok=True)
  if archiveType == 'none' or archiveType == '':
    if len(deployList) == 1:
      if type(deployList[0]) == dict:
        if 'pattern' in deployList[0]:
          move_files(targetDir, backupDir, pattern=deployList[0]['pattern'])
    else:
      for target in deployList:
        targetFiles = os.path.join(targetDir, target)
        backupFiles = os.path.join(backupDir, target)

        # if target file exists then backup files.
        if os.path.exists(targetFiles):
          # if target path contains os separator then make child directory.
          if os.path.sep in target:
            backupDir = os.path.join(backupDir, target[:target.rindex(os.path.sep)])
            os.makedirs(backupDir, exist_ok=True)
          
          shutil.copy(targetFiles, backupFiles)
  else:
    backupTime = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')
    shutil.make_archive(os.path.join(backupDir, 'backup-' + backupTime), archiveType, targetDir)

  # file copy
  # copy from source files to target files.
  for target in deployList:
    targetFiles = os.path.join(targetDir, target)
    sourceFiles = os.path.join(sourceDir, target)

    shutil.copy(sourceFiles, targetFiles)

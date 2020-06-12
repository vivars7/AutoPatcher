# Introduction  
This util make easy file copy and backup task.  
  
# Usage  
Need to configure patch.json before using this util.  
  
# How to configure patch.json  
[sourceDir]  
Directory path having source files. 
  
[targetDir]  
Target directory path having original files.  
  
[backupDir]  
Directory path for saving backups. 
  
[archiveType]  
If you want to archiving backups, type to archive type.  
  
zip: ZIP file (if the zlib module is available).  
tar: Uncompressed tar file. Uses POSIX.1-2001 pax format for new archives.  
gztar: gzip'ed tar-file (if the zlib module is available).  
bztar: bzip2'ed tar-file (if the bz2 module is available).  
xztar: xz’ed tar-file (if the lzma module is available). 
  
[deployList]  
If you want to copy files using pattern.  
e.g.  
"deployList": [  
&nbsp;&nbsp;&nbsp;&nbsp;{"pattern":"*.bak"}  
]  
Also, if you want to copy files using just file list  
"deployList": [  
&nbsp;&nbsp;&nbsp;&nbsp;"test.txt", "test2.txt", "ft/a.txt", "new.txt"...  
]  

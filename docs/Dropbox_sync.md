# [Dropbox] Syncronization Strategy

## All Observers need a Dropbox userid and password<br />(or they must all share a single Dropbox Account).

The [DropboxSync.py] and related [dropboxlogin.py] scripts need to be loaded and properly configured on all iOS devices doing RMG Observations.

At the end of each Observation, the DropboxSync.py script should be run (automatically?) to send the new observations to Dropbox where a RMG backend process can pick them up for includion into the RMG backend data set.


[Dropbox]:         http://www.dropbox.com
[DropboxSync.py]:  http://omz-forums.appspot.com/pythonista/post/5780410457915392
[dropboxlogin.py]: https://gist.github.com/omz/4034526

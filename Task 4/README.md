# Periodic task


Write a quick script that will POST a JSON object containing
a random string of your choosing under a field called 'msg' to
https://admin.remote.besic.org/api/statusmessage

The script can be in any language you want. I believe bash would be simplest but I leave it to your discretion.

Then write a cron task that will run your script every minute, assume the script is in the directory `/usr/bin/periodictask`

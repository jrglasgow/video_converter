#! /bin/env python

import os, sys

def convert_file(orig_file_name):
  orig_file_ext = orig_file_name.split('.')[-1]
  print "\n\n\n\n"
  print "Starting to convert %s..." % orig_file_name
  new_file_name = orig_file_name.replace(orig_file_ext, 'mp4')
  # create the command to convert the file
  command = "ffmpeg -i %s -acodec aac -strict -2 -ab 128k -ar 44100 -vcodec h264 -b 800K %s -y" % (orig_file_name, new_file_name)
  command = "time %s" % command
  # convert the file
  exit_code = os.system(command)

  if (exit_code == 0):
    # use qtfaststart to make the new file streaming ready
    os.system("qtfaststart %s" % (new_file_name))
    # move the original file
    orig_file_new_name = orig_file_name.replace('.%s' % orig_file_ext, '_%s' % orig_file_ext)
    move_command = 'mv %s %s' % (orig_file_name, orig_file_new_name)
    os.system(move_command)
    print "\n"
    print "%s created and original file moved to %s" % (new_file_name, orig_file_new_name)
  else:
    os.system("rm %s" % (new_file_name))
    print "Converting %s failed, please try again." % orig_file_name
  pass

if __name__ == "__main__":
  files_to_convert = sys.argv[1:]
  for file_to_convert in files_to_convert:
    convert_file(file_to_convert)

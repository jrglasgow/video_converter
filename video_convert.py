#! /usr/bin/env python

import os, sys, json

def create_video_filter(orig_file_name):
  probe_file = '/tmp/ffprobe-%s.txt' % orig_file_name.split('/')[-1]
  # use ffprobe to get the width of the original file
  probe_command = 'ffprobe -show_streams -select_streams v -of json "%s" 1>&2> "%s"' % (orig_file_name, probe_file)
  #print 'probe_command: %s' % probe_command
  os.system(probe_command)
  probe_file = open(probe_file)
  file_data = json.load(probe_file)
  probe_file.close()

  width = file_data['streams'][0]['width']

  # make sure the width is an even number
  if (width % 2):
    width -= width

  scale_width = width  # the width of the original file rounded down to be even
  scale_height = 'trunc(ow/a/2)*2' # keep the same aspect ratio but make sure the height is also and even number
  video_filter =  '-vf "scale=%s:%s"' % (scale_width, scale_height)
  return video_filter

def convert_file(orig_file_name):
  orig_file_ext = orig_file_name.split('.')[-1]
  print "\n\n\n\n"
  print "Starting to convert %s..." % orig_file_name
  new_file_name = orig_file_name.replace(orig_file_ext, 'mp4')

  # create the video filter
  video_filter = create_video_filter(orig_file_name);
  # create the command to convert the file
  command = 'ffmpeg -i "%s" %s  -acodec aac -strict -2 -ab 128k -ar 44100 -vcodec h264 -vb 800K -y -movflags +faststart "%s" ' % (orig_file_name, video_filter, new_file_name)
  command = "time %s" % command
  #print 'command: %s' % command
  # convert the file
  exit_code = os.system(command)

  if (exit_code == 0):
    # move the original file
    orig_file_new_name = orig_file_name.replace('.%s' % orig_file_ext, '_%s' % orig_file_ext)
    move_command = 'mv "%s" "%s"' % (orig_file_name, orig_file_new_name)
    os.system(move_command)
    print "\n"
    print "%s created and original file moved to %s" % (new_file_name, orig_file_new_name)
  else:
    os.system('rm "%s"' % (new_file_name))
    print "Converting %s failed, please try again." % orig_file_name
  pass

if __name__ == "__main__":
  files_to_convert = sys.argv[1:]
  for file_to_convert in files_to_convert:
    convert_file(file_to_convert)

video_converter.py
===============

Python script to convert a batch of files to H.264/MP4 using ffmpeg

The script has been modified to use the -movflags faststart option now in ffmpeg so qtfaststart is not necessary.

The files are converted to 800kbps video 128k audio with faststart optimizing for web streaming.

Usage
-----
* Convert a single file to H.264/MP4
  * video_converter.py file_name.avi
* Convert multiplt files to H.264/MP4
  * video_converter.py file1.avi file2 .avi file3.avi
  * video_converter.py *.avi

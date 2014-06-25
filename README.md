video_converter.py
===============

Python script to convert a batch of files to H.264/MP4 using ffmpeg

The script has been modified to use the -movflags faststart option now in ffmpeg so qtfaststart is not necessary.

The files are converted to 800kbps video 128k audio with faststart optimizing for web streaming.

After the transcoding is completed successfully the names of the original files are changed to remove the extension. movie.avi is renamed to movie_avi. This is to prevent duplicates in directories which are automatically scanned for video files. With one command 

videoconverter.py *.avi

you can convert all the AVI files in a directory to H.264/MP4 and rename all the old files to not appear as video files while maintaining the old files.

Usage
-----
* Convert a single file to H.264/MP4
  * video_converter.py file_name.avi
* Convert multiplt files to H.264/MP4
  * video_converter.py file1.avi file2 .avi file3.avi
  * video_converter.py *.avi

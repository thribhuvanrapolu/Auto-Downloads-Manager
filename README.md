# project-auto-file-manager

Whenever you download files they get saved in downloads folder or you have to manually select the folder to which location you want to save the file.
Manually selecting the location everytime you download something is pain. 
Most of them select download folder as default location. So whenever you download files, all the files in download folder become a cluter.

What this python code does is whenever u download file it automatically moves them to Documents/Videos/Music/Photos folder based on file extension.

To make this code run on your system edit line 25,53,58,63,68,75 by replacing with the respective file location in your system

## How the Algorithm works:
So whenever you download a file from web browser it saves the file with extension .crdownload and with download completes it saves the file with its original extension(like .mkv,.jpg etc) which basically is just renaming the file.
Whenever the download completes the code calls the function on_moved(as whenver the download completes it renaming the file with orginal extension).

<FileMovedEvent: src_path='/home/anakin513/Downloads/Unconfirmed 198492.crdownload', dest_path='/home/anakin513/Downloads/NewReg - CSE and AI - v3.pptx', is_directory=False>
src_path is file name while downloading and dest_path is the downloaded file name

This function on_moved checks whether src_path ends with '.crdownload' extension and if yes then move the file to respective Documents/Videos/Music/Photos folder based on file extension. 


### WARNING:
whenever you download the file you cant open it from your web browser as the file doesnt exist in download folder location.
 

import os
import imageio

clip = os.path.abspath('_Hello.mp4')

def converter(inputpath, file_format):
    outputpath = os.path.splitext(inputpath)[0] + file_format # split the file name and the file format
    print(f'converting {inputpath} into {outputpath}')
    reader = imageio.get_reader(inputpath)
    fps = reader.get_meta_data()['fps']                       # get the fps from the original file
    writer = imageio.get_writer(outputpath, fps = fps)        # change the fps to the need(fps for now)
    
    for frames in reader:
        writer.append_data(frames)
        #print(f'Frame {frames}')                             # prints each frame
        
    print("done!")
    
converter(clip,'.gif')
    

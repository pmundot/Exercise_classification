import argparse
from workout_classification import exercise



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Workout Classification')
    parser.add_argument('Command', metavar='<command>', choices=['print'], type=str, help='Print only')
    parser.add_argument('-p','--photo',dest='do_photo',metavar='<photos>',default=None,help="Enter photo path")
    parser.add_argument('-v','--video',dest='do_video', metavar='<videos>',default=None,help="Enter video path or 0 for webcam")
    parser.add_argument('-t','--type',dest='do_type', metavar='<type>',default='default',choices=['default','skeleton','angels','classification'],help='How the file shoule be saved')
    parser.add_argument('-s','--save',dest='do_save', metavar='<saves>',default=None,help='Enter file name to save')
    args = parser.parse_args()

    ex = exercise(args.do_photo)
    ex.class_image(args.do_type,args.do_save)
    #typop = {'default':ex.normal_image(),'skeleton':ex.skeleton_image(),'angels':ex.angels_image(),'c':4}
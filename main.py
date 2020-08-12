# import sys,os
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))#存放c.py所在的绝对路径

# sys.path.append(BASE_DIR)
# sys.path.append("./subtitleMaker")
from subtitleMaker import subtitle_maker
# import subtitleMaker.subtitle_maker as subtitle_maker

if __name__=="__main__":

    mp4_path="./resources/mp4/1.mp4"
    wav_path="./resources/out/"+str(mp4_path.split("/")[-1].replace("mp4","wav"))
    subtitle_maker.mp4_to_wav(mp4_path,wav_path)
    print("done!")
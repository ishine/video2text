from subtitleMaker import subtitle_maker

if __name__=="__main__":

    mp4_path="./resources/mp4/1.mp4"
    wav_path="./resources/out/"+str(mp4_path.split("/")[-1].replace("mp4","wav"))
    subtitle_maker.mp4_to_wav(mp4_path,wav_path)
    print("done!")
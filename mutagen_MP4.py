import os
import sys
from mutagen.mp4 import MP4
from mutagen.mp4 import MP4Cover

input_file = sys.argv[1]
tagger = MP4(input_file)

print("Mutagen MP4/M4A tags")
print("1 : Add Tags")
print("2 : Remove Tags")
add_or_delete = int(input("Type number: "))

if add_or_delete == 2:
    print("|")
    tagger.delete()
    tagger.save()
    print("|--All Tags and Covers Successfully Removed.")

elif add_or_delete == 1:
    print("|")

    title = input("|--Title: ")
    tagger['\xa9nam'] = title.split(', ')

    Album = input("|--Album: ")
    tagger['\xa9alb'] = Album.split(', ')

    Artist = input("|--Artist: ")
    tagger['\xa9ART'] = Artist.split(', ')

    Albartist = input("|--Album artist: ")
    tagger['aART'] = Albartist.split(', ')

    genre = input("|--Genre: ")
    tagger['\xa9gen'] = genre.split(', ')

    Released_date = input("|--Released date: ")
    tagger['\xa9day'] = Released_date.split(', ')

    Composer = input("|--Composer: ")
    tagger['\xa9wrt'] = Composer.split(', ')

    Comment = input("|--Comment: ")
    tagger['\xa9cmt'] = Comment.split(', ')

    Grouping = input("|--Grouping: ")
    tagger['\xa9grp'] = Grouping.split(', ')

    Copyright = input("|--Copyright: ")
    tagger['cprt'] = Copyright.split(', ')

    print("|")
    print("|-- 0 : None")
    print("|-- 2 : Clean")
    print("|-- 4 : Explicit")
    Rating = input("|--Rating: ")
    if Rating == "":
        tagger['rtng'] =[]
    else:
        tagger['rtng'] = [int(Rating)]

    print("|")
    print("|-- 0 : Movie")
    print("|-- 1 : Music")
    print("|-- 2 : Audiobook")
    print("|-- 5 : Whacked Bookmark")
    print("|-- 6 : Music Video")
    print("|-- 9 : Short Film")
    print("|-- 10 : TV Show")
    print("|-- 11 : Booklet")
    print("|-- 14 : Ringtone")
    Content = input("|--ContentType: ")
    print("|")
    if Content == "":
        tagger['stik'] = []
    else:
        tagger['stik'] = [int(Content)]

    Work = input("|--Work: ")
    tagger['\xa9wrk'] = Work.split(', ')

    Movemonet = input("|--Movemonet: ")
    tagger['\xa9mvn'] = Movemonet.split(', ')

    Description = input("|--Description: ")
    tagger['desc'] = Description.split(', ')

    LongDescription = input("|--LongDescription: ")
    tagger['ldes'] = LongDescription.split(', ')

    Track = input("|--Track No.: ")
    Trackall = input("|--Total Tracks: ")
    if Track == "":
        if Trackall == "":
            tagger['trkn'] = []
        else:
            tagger['trkn'] = [(0, int(Trackall))]
    else:
        if Trackall == "":
            tagger['trkn'] = [(int(Track), 0)]
        else:
            tagger['trkn'] = [(int(Track), int(Trackall))]

    Disks = input("|--Disk No.: ")
    Disksall = input("|--Total Disks: ")
    if Disks == "":
        if Disksall == "":
            tagger['disk'] = []
        else:
            tagger['disk'] = [(0, int(Disksall))]
    else:
        if Disksall == "":
            tagger['disk'] = [(int(Disks), 0)]
        else:
            tagger['disk'] = [(int(Disks), int(Disksall))]
    
    if Content == "10":
        TVShowname = input("|--TV Show name: ")
        tagger['tvsh'] = TVShowname.split(', ')

        tv_ep = input("|--TV Show Episode: ")
        if tv_ep == "":
            tagger['tves'] = []
        else:
            tagger['tves'] = [int(tv_ep)]

        tv_sn = input("|--TV Show Season: ")
        if tv_sn == "":
            tagger['tvsn'] = []
        else:
            tagger['tvsn'] = [int(tv_sn)]

    print("|")
    print("|--Add Lyrics")
    add_lyrics = input("|--Type 'Yes' or 'No': ")
    if add_lyrics.lower() == "yes":
        print("|--NOTE: To Add Lyrics Save Lyrics in a Text file and Add Text file's Path.")
        lyrics_txt = input("|--Enter Text file's Path: ")
        txt_folder = os.path.dirname(lyrics_txt)
        txt_folder = txt_folder.split('"')
        txt_file = lyrics_txt.split("\\")
        txt_file = txt_file[-1].split('"')
        os.chdir(txt_folder[-1])
        load_lyrics = open(txt_file[0], "r").read()
        tagger["\xa9lyr"] = load_lyrics
    else:
        print("|--No Lyrics Added!")

    print("|")
    print("|--Add more Custom Tags")
    add_custom_tags = input("|--Type 'Yes' or 'No': ")
    if add_custom_tags.lower() == "yes":
        print("|--Add Custom Tags from a Text file")
        add_custom_tags_text = input("|--Type 'Yes' or 'No': ")
        if add_custom_tags_text.lower() == "yes":
            print("|")
            print("|--Text file's content format must be as below.")
            print("|-----------------------------------------")
            print("|-- Tag_Name_1: Tag_Value_1, Tag_Value_2")
            print("|-- Tag_Name_2: Tag_Value_1, Tag_Value_2")
            print("|-----------------------------------------")
            custom_tags_text = input("|--Enter Text file's Path: ")
            print("|")
            custags_txt_folder = os.path.dirname(custom_tags_text)
            custags_txt_folder = custags_txt_folder.split('"')
            custags_txt_file = custom_tags_text.split("\\")
            custags_txt_file = custags_txt_file[-1].split('"')
            os.chdir(custags_txt_folder[-1])
            with open(custags_txt_file[0]) as txt_tags:
                for custags in txt_tags:
                    custags = custags.strip()
                    print("|--" + custags)
                    tag_name_add = custags.split(': ')
                    tag_value_add = tag_name_add[-1].split(', ')
                    tagger['----:com.apple.itunes:' + tag_name_add[0]] = [con.encode() for con in tag_value_add]
        else:
            print("|--Enter Tag Name first and Enter Tag Value second.")
            print("|--When finished, Type 'done' in Tag Name.")
            while True:
                enter_tag_name = input("|--Enter Tag Name: ")
                if enter_tag_name.lower() == "done":
                    break
                else:
                    tag_value = input("|--" + enter_tag_name + ": ")
                    contributor = tag_value.split(', ')
                    tagger['----:com.apple.itunes:' + enter_tag_name] = [con.encode() for con in contributor]
    else:
        print("|--No Additional Tags Added.")
    
    print("|")
    print("|--Add a Cover/Albumart")
    add_cover = input("|--Type 'Yes' or 'No': ")
    if add_cover.lower() == "yes":
        albumart = input("|--Enter Cover's/Albumart's file Path: ")
        albumart_folder = os.path.dirname(albumart)
        albumart_folder = albumart_folder.split('"')
        albumart_file = albumart.split("\\")
        albumart_file = albumart_file[-1].split('"')
        os.chdir(albumart_folder[-1])
        data = open(albumart_file[0], 'rb').read()
        covr = []
        if albumart.endswith('png'):
            covr.append(MP4Cover(data, MP4Cover.FORMAT_PNG))
        elif albumart.endswith('png"'):
            covr.append(MP4Cover(data, MP4Cover.FORMAT_PNG))
        elif albumart.endswith('jpg') or albumart.endswith('jpeg'):
            covr.append(MP4Cover(data, MP4Cover.FORMAT_JPEG))
        elif albumart.endswith('jpg"') or albumart.endswith('jpeg"'):
            covr.append(MP4Cover(data, MP4Cover.FORMAT_JPEG))
        tagger['covr'] = covr
    else:
        print("|--No Cover/Albumart Added.")    
    tagger.save()
    print("|")
    print("|--Successfully Tagged.")
else:
    print("|")
    print("|--Enter a valid number and Try again....")
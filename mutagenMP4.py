import os
import sys
from mutagen.mp4 import MP4, MP4Cover

def main():

    '''
    Tagging script for MP4/M4A files using the python module 'Mutagen'.
    '''

    inputMP4 = sys.argv[1]
    taggerMP4 = MP4(inputMP4)
    tagMode = input(
        f'\nmutagenMP4\
        \n|\
        \n|-- 1 : Add tags\
        \n|-- 2 : Remove tags\
        \n|\
        \n|--tagMode: [1/2] '
    )

    if tagMode == '2':
        taggerMP4.delete()
        taggerMP4.save()
        print(f"|\n|--All 'Tags' and 'Covers' are successfully removed!")

    elif tagMode == '1':
        print('\n' + os.path.basename(os.path.abspath(inputMP4)), '\n|')
        Title = input("|--Title: ")
        Album = input("|--Album: ")
        Artist = input("|--Artist: ")
        albumArtist = input("|--Album Artist: ")
        Genre = input("|--Genre: ")
        releasedDate = input("|--Released Date: ")
        Composer = input("|--Composer: ")
        Comment = input("|--Comment: ")
        Grouping = input("|--Grouping: ")
        Copyright = input("|--Copyright: ")

        taggerMP4['aART'] = albumArtist.split(', ')
        taggerMP4['cprt'] = Copyright.split(', ')
        taggerMP4['\xa9nam'] = Title.split(', ')
        taggerMP4['\xa9alb'] = Album.split(', ')
        taggerMP4['\xa9ART'] = Artist.split(', ')
        taggerMP4['\xa9gen'] = Genre.split(', ')
        taggerMP4['\xa9day'] = releasedDate.split(', ')
        taggerMP4['\xa9wrt'] = Composer.split(', ')
        taggerMP4['\xa9cmt'] = Comment.split(', ')
        taggerMP4['\xa9grp'] = Grouping.split(', ')

        Rating = input(
            f'|\
            \n|-- 0 : None\
            \n|-- 2 : Clean\
            \n|-- 4 : Explicit\
            \n|\
            \n|--Rating: [0/2/4] '
        )
        if not Rating:
            taggerMP4['rtng'] =[]
        else:
            taggerMP4['rtng'] = [int(Rating)]

        contentType = input(
            f'|\
            \n|-- 0  : Movie\
            \n|-- 1  : Music\
            \n|-- 2  : Audiobook\
            \n|-- 5  : Whacked Bookmark\
            \n|-- 6  : Music Video\
            \n|-- 9  : Short Film\
            \n|-- 10 : TV Show\
            \n|-- 11 : Booklet\
            \n|-- 14 : Ringtone\
            \n|\
            \n|--ContentType: [0/1/2/5/6/9/10/11/14] '
        )
        if not contentType:
            taggerMP4['stik'] = []
        else:
            taggerMP4['stik'] = [int(contentType)]

        Work = input("|\n|--Work: ")
        Movemonet = input("|--Movemonet: ")
        Description = input("|--Description: ")
        longDescription = input("|--LongDescription: ")
        
        taggerMP4['\xa9wrk'] = Work.split(', ')
        taggerMP4['\xa9mvn'] = Movemonet.split(', ')
        taggerMP4['desc'] = Description.split(', ')
        taggerMP4['ldes'] = longDescription.split(', ')

        trackNumber = input("|--Track No.: ")
        trackTotal = input("|--Track Total: ")

        if not trackNumber:
            if not trackTotal:
                taggerMP4['trkn'] = []
            else:
                taggerMP4['trkn'] = [(0, int(trackTotal))]
        else:
            if not trackTotal:
                taggerMP4['trkn'] = [(int(trackNumber), 0)]
            else:
                taggerMP4['trkn'] = [(int(trackNumber), int(trackTotal))]

        diskNumber = input("|--Disk No.: ")
        discTotal = input("|--Disk Total: ")

        if not diskNumber:
            if not discTotal:
                taggerMP4['disk'] = []
            else:
                taggerMP4['disk'] = [(0, int(discTotal))]
        else:
            if not discTotal:
                taggerMP4['disk'] = [(int(diskNumber), 0)]
            else:
                taggerMP4['disk'] = [(int(diskNumber), int(discTotal))]
        
        if contentType == '10':
            tvShowName = input("|--TV Show name: ")
            tvShowSeason = input("|--TV Show Season: ")
            tvShowEP = input("|--TV Show Episode: ")

            taggerMP4['tvsh'] = tvShowName.split(', ')
            if not tvShowEP:
                taggerMP4['tves'] = []
            else:
                taggerMP4['tves'] = [int(tvShowEP)]
            if not tvShowSeason:
                taggerMP4['tvsn'] = []
            else:
                taggerMP4['tvsn'] = [int(tvShowSeason)]

        addLyrics = input(f"|\n|--Do you want to add 'Lyrics'? [y/n] ")
        if (addLyrics.lower() == 'y') or (addLyrics.lower() == 'yes'):
            lrcDoc = input(f"|--Save lyrics in a text document and enter it's path\n|--Text document's path: ")
            if lrcDoc.startswith('"') and lrcDoc.endswith('"'):
                lrcDoc = lrcDoc[1:-1]
            Lyrics = open(lrcDoc, 'r').read()
            taggerMP4["\xa9lyr"] = Lyrics
        else:
            print("|--No 'Lyrics' added!")

        addCustomTags = input(f"|\n|--Do you want to add more 'Custom Tags'? [y/n] ")
        if (addCustomTags.lower() == 'y') or (addCustomTags.lower() == 'yes'):
            addTextDoc = input(f'|--Do you want to add tags from a text document? [y/n] ')
            if (addTextDoc.lower() == 'y') or (addTextDoc.lower() == 'yes'):
                textDoc = input(f"|--Text document's path: ")
                if textDoc.startswith('"') and textDoc.endswith('"'):
                    textDoc = textDoc[1:-1]
                print(f'|')
                with open(textDoc) as textTags:
                    for customTags in textTags:
                        customTags = customTags.strip()
                        print(f'|--{customTags}')
                        tagName = customTags.split(': ')
                        tagValue = tagName[1].split(', ')
                        taggerMP4['----:com.apple.itunes:' + tagName[0]] = [value.encode() for value in tagValue]
            elif (addTextDoc.lower() == '') or (addTextDoc.lower() == 'n') or (addTextDoc.lower() == 'no'):
                print(f'|\n|--Type [tag name] first and [tag value] second')
                print(f"|--When finished, Type 'done' in [tag name]\n|")
                while True:
                    tagName = input(f'|--Tag name: ')
                    if tagName.lower() == "done":
                        break
                    tagValue = input(f'|--{tagName}: ')
                    taggerMP4['----:com.apple.itunes:' + tagName] = [value.encode() for value in tagValue.split(', ')]
        else:
            print(f"|--No 'Custom Tags' added!")

        addCover = input(f"|\n|--Do you want to add a 'Cover'? [y/n] ")
        if (addCover.lower() == 'y') or (addCover.lower() == 'yes'):
            albumart = input(f"|--Cover's file path: ")
            if albumart.startswith('"') and albumart.endswith('"'):
                albumart = albumart[1:-1]
            data = open(albumart, 'rb').read()
            coverFile = []
            if os.path.splitext(albumart)[1] == '.png':
                coverFile.append(MP4Cover(data, MP4Cover.FORMAT_PNG))
            elif (os.path.splitext(albumart)[1] == '.jpg') or (os.path.splitext(albumart)[1] == '.jpeg'):
                coverFile.append(MP4Cover(data, MP4Cover.FORMAT_JPEG))
            taggerMP4['covr'] = coverFile
        else:
            print(f"|--No 'Cover' added!")
        taggerMP4.save()
        print(f'|\n|--Successfully Tagged')
    else:
        print(f'|--Invalid response, Try again....')

if __name__ == '__main__':
    main()

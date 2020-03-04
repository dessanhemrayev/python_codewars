def song_decoder(song):
    a=song.replace("WUB", " ")
  
    s=(a.strip()).replace("  ", " ")
    str1=''
    for i in range(len(s)):
     
        if s[i]=='W':
            str1+=" "
            str1+=s[i]
        elif s[i]=='U':
            
            str1+=s[i]
            str1+=" "
        elif s[i]!='W' or s[i]!='U':
            str1+=s[i]
      
    print(str1.strip())

    return 


song_decoder("WU  U B U")
song_decoder("WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB")
song_decoder("WUBAWUBBWUBCWUB")
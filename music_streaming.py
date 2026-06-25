artist_songs={
    "burna boy": ["Last Last", "Common Person", "On the low"],
    "bryson tiller":["Dont", "Exchange", "Right My Wrongs"],
    "drake": ["Marvin Room", "Teenage Fever", "Knife Talk"]
}
# print(artist_songs)
artist_songs["cardi b"]=["WAP", "Hello", "Money"]# add a new key/value pair
# print(artist_songs)
# artist_songs["Drake"].append("fancy")#add a song to an existing file
# print(artist_songs["Drake"])
# artist_songs["Drake"].remove("Marvin Room")

favourite_artist=input("Enter your favourite artist: ")
artist_list=favourite_artist.split(",")
for artist in artist_list:
    artist=artist.strip().lower()
    if artist in artist_songs:
        for song in artist_songs[artist]:
            print(f"{song}")
        else: 
            print(f"No recommendations found")

# print(artist_songs["Drake"])

# for artist,songs in artist_songs.items():
#     print(f"Artist: {artist}")
#     for song in songs: 
#         print(f"song")

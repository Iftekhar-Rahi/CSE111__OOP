class EPL_Team:
    def __init__(self,name,song="No Slogan",title=0):
        self.name=name
        self.song=song
        self.title=title
    def increaseTitle(self,x=1):
        self.title+=x
    def showClubInfo(self):
        return f"Name: {self.name}\nSong: {self.song}\nTotal No of title: {self.title} "
    def changeSong(self,y):
        self.song=y
manu = EPL_Team('Manchester United', 'Glory Glory Man United')
chelsea = EPL_Team('Chelsea')
print('===================')
print(manu.showClubInfo())
print('##################')
manu.increaseTitle()
print(manu.showClubInfo())
print('===================')
print(chelsea.showClubInfo())
chelsea.changeSong('Keep the blue flag flying high')
print(chelsea.showClubInfo())

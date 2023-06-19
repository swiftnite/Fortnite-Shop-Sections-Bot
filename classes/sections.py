import requests
session = requests.Session()

from dateutil.parser import parse
import json
import emoji
from collections import Counter

class sectionsClass:
    def __init__(self, customisation, apiOne, apiOneEnabled, apiTwoEnabled):
        self.customisationJson = {}
        self.customisationJson["heading"] = customisation.heading
        self.customisationJson["footer"] = customisation.footer
        self.customisationJson["language"] = customisation.language
        self.customisationJson["point"] = customisation.point
        self.customisationJson["brackets"] = customisation.brackets
        self.customisationJson["showIfOne"] = customisation.showIfOne
        self.customisationJson["quantitySymbol"] = customisation.quantitySymbol
        self.customisationJson["beforeOrAfter"] = customisation.beforeOrAfter
        self.customisationJson["sortMethod"] = customisation.sortMethod
        self.customisationJson["image"] = customisation.image
        self.customisationJson["imageEnabled"] = customisation.imageEnabled
        self.customisationJson["imageFileType"] = customisation.imageFileType
        self.customisationJson["testMode"] = customisation.testMode

        specialLangs = ['ja', 'zh-cn', 'zh-hant', 'ko']

        if self.customisationJson["language"].lower() in specialLangs:
            self.charLimit = 140
        else:
            self.charLimit = 280

        self.apiOneUrl = apiOne
        self.apiOneEnabled = apiOneEnabled
        self.apiTwoEnabled = apiTwoEnabled

        self.headingEmojis = 0
        self.footerEmojis = 0

        for c in self.customisationJson["heading"]:
            if emoji.is_emoji(c):
                self.headingEmojis+=1

        for c in self.customisationJson["footer"]:
            if emoji.is_emoji(c):
                self.footerEmojis+=1
        
        with open('cache/translations.json', 'r', encoding='utf8') as translator:
            self.translator = json.load(translator)

        self.sFix1=["20", "19", "18", "17", "16", "15", "14", "13", "12", "11", "10", "9B", "8B", "7B", "6B", "5B", "4B", "3B", "2B", "1B", "9C", "8C", "7C", "6C", "5C", "4C", "3C", "2C", "1C"]
        self.sFix2=["9", "8", "7", "6", "5", "4", "3", "2", "1", "B", "C"]
    
    def getTime1(self):
        try:
            if self.apiOneUrl != "https://fn-api.com/api/calendar":
                self.apiOne = session.get(self.apiOneUrl).json()
            else:
                self.apiOne = session.get(self.apiOneUrl).json()['data']
            self.time1 = parse(self.apiOne['currentTime'])
        except:
            self.time1 = parse("1989-12-13T00:00:00.000Z")
        
        return self.time1
    
    def getAuth(self):
        with open('cache/auth.json', 'r') as authi:
            self.authFile = json.load(authi)
    
    def getTime2(self, auth):
        try:
            self.getAuth()
            if not all((self.authFile ['deviceId'], self.authFile ['accountId'], self.authFile ['secret'], self.authFile ['access_token'], self.authFile ['expires_at'])):
                auth.generateAuth()
                self.getAuth()

            self.apiTwo = session.get('https://fortnite-public-service-prod11.ol.epicgames.com/fortnite/api/calendar/v1/timeline', headers={"Authorization": f"Bearer {self.authFile['access_token'] }"}).json()
            self.time2 = parse(self.apiTwo['currentTime'])
        except Exception as e:
            self.time2 = parse("1989-12-13T00:00:00.000Z")
        
        return self.time2
    
    def getSectionNames(self):
        self.sectionsNamesJson = session.get(f'https://fortnitecontent-website-prod07.ol.epicgames.com/content/api/pages/fortnite-game/shop-sections?lang={self.customisationJson["language"]}').json()['sectionList']['sections']

    def pickApi(self, auth):
        if self.apiOneEnabled & self.apiTwoEnabled:
            time1 = self.getTime1()
            time2 = self.getTime2(auth)

            if time1 > time2:
                self.url =  self.apiOne
            else:
                self.url = self.apiTwo

        elif self.apiOneEnabled:
            time1 = self.getTime1()
            self.url =  self.apiOne
            
        elif self.apiTwoEnabled:
            time2 = self.getTime2(auth)
            self.url =  self.apiTwo


    
    def getCurrentSections(self):
        if not self.customisationJson["testMode"]:
            self.currentSectionsJson = self.url['channels']['client-events']['states'][1]['state']['sectionStoreEnds']
        else:
            self.currentSectionsJson = self.url['channels']['client-events']['states'][0]['state']['sectionStoreEnds']
    
    def magicalSortingFunction(self, section):
        return section["length"], section["count"]
    
    def loadCache(self):
        with open('cache/cache.json', 'r') as cache:
            return json.load(cache)
    
    def appendDisplayName(self, name):
        found = False
        for i in self.sectionsNamesJson:
            name = name
            sectionId = i['sectionId']
            if name==sectionId:
                found = True
                try:
                    if i['sectionDisplayName']:
                        name = i['sectionDisplayName']
                    else:
                        found = False
                except:
                    found = False

        if found == False:
            name = name
            for o in self.translator:
                if name.startswith(o):
                    name = self.translator[o][self.customisationJson["language"]]
                    success=True
                else:
                    success=False
            if success==False:
                if name.endswith(tuple(self.sFix1)):
                    name=name[:-2]
                elif name.endswith(tuple(self.sFix2)):
                    name=name[:-1]
        self.x.append(name)
    def formatSection(self, name, quantity, count):
        if (self.customisationJson["showIfOne"]==False) & (count==1):
            quantity = ""
        else:
            if self.customisationJson["beforeOrAfter"]=="after":
                quantity=f'{quantity}{self.customisationJson["quantitySymbol"]}'
                
            else:
                quantity=f'{self.customisationJson["quantitySymbol"]}{quantity}'

        if (self.customisationJson["brackets"] == True) & (quantity != ""):
            quantity = f"({quantity})"
            
        return f'{self.customisationJson["point"]}{name} {quantity}'
        
    def sortSections(self, sections):
        if self.customisationJson["sortMethod"] == "alphabetical":
            sort = sorted(sections)
        else:
            sortList = []
            sort = ""
            count = 1
            for i in sections:
                sortList.append({"name": i, "length": len(i), "count": count})
                count+=1
            sortList.sort(key=self.magicalSortingFunction)
            sort = []
            for i in sortList:
                sort.append(i["name"])

        return sort
    
    def charLimitPrep(self, sorted):
        for i in sorted:
            if self.customisationJson["heading"] in self.txt[-1]:
                if len(self.txt[-1]) + len(f"\n{i}") + self.headingEmojis > self.charLimit:
                    self.txt.append(f"\n{i}")
                else:
                    self.txt[-1] += f"\n{i}"
            else:
                if len(self.txt[-1]) + len(f"\n{i}") > self.charLimit:
                    self.txt.append(f"\n{i}")
                else:
                    self.txt[-1] += f"\n{i}"

        if self.customisationJson["footer"] != "":
            if len(self.txt[-1])+ len(f'\n\n{self.customisationJson["footer"]}') + self.footerEmojis < self.charLimit:
                self.txt[-1] += f'\n\n{self.customisationJson["footer"]}'
        
        return self.txt

    def sections(self):
        try:
            self.getCurrentSections()
        except:
            return None

        self.x = []
        self.toSort = []
        self.txt = []

        self.txt.append(f'{self.customisationJson["heading"]}\n')

        cache = self.loadCache()

        if self.currentSectionsJson != cache:
            try:
                self.getSectionNames()
                for i in self.currentSectionsJson:
                    self.appendDisplayName(i)

                count = Counter(self.x)

                counting = 0

                for name in count:
                    counting+=1
                    quantity = count[name]
                    self.toSort.append(self.formatSection(name, quantity, counting))
                
                sorted = self.sortSections(self.toSort)
                prepared = self.charLimitPrep(sorted)

                with open('cache/cache.json', 'w') as file:
                    json.dump(self.currentSectionsJson, file, indent=3)

                return prepared
            except Exception as e:
                print(f"An error has occurred:\n{e}")
        else:
            return None

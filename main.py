import discord
import random
import os
from webserver import keep_alive
from datetime import date
import names
import threading

import restart

greg_list = ["gpengu", "gmonster", "gheffley", "gfamilyguy", "gdeer", "gggreg"]

game_tags = ["CraftCube", "Ttoomm", "D8nsku", "Melone", "Auf_Ov", "Om4r", "GaspardG", "Oblast","JjGamer", "Snip3r_L0rd", "Dynamite6k", "Flodey","Quag", "QRehtar", "Sulsang", "Hikikoira1", "AmogusGamine", "CtrlLost","Sus", "Sonic_Lover", "Gagde", "Jtom","greg", "Akuw", "Ender_Temnine", "Ouids", "Gumholic", "R", "PadawanAmy", "infsrael", "SPPoop","4ilylove", "Revendicate","Homeless", "Venture", "100psi", "kala", "Mehmet", "Muhammed", "Palestine", "Cyberpunk", "Rotta", "felicia", "zebra", "turtle", "Huckery", "Premol", "mole","slowv"]


swear = ["Helvetti", "Jumalauta", "Paska", "Perkele", "Saatana", "Vittu"]
other_swear = ["Fuck", "Shit", "Bloody hell", "Scheiße", "Son of a bitch", "Asshole", "Bastard", "Bitch", "Cunt", "Dickhead"]

xxx_tag = [0,1,2]
gg_tag = [0,1]

today = date.today()


d2 = today.strftime("%B %d, %Y")
torf = ["True", "False"]

countries = [
  "Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua & Deps",
  "Argentina", "Armenia", "Australia", "Austria", "Azerbaijan", "Bahamas",
  "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin",
  "Bhutan", "Bolivia", "Bosnia Herzegovina", "Botswana", "Brazil", "Brunei",
  "Bulgaria", "Burkina", "Burundi", "Cambodia", "Cameroon", "Canada",
  "Cape Verde", "Central African Rep", "Chad", "Chile", "China", "Colombia",
  "Comoros", "Congo", "Congo {Democratic Rep}", "Costa Rica", "Croatia",
  "Cuba", "Cyprus", "Czech Republic", "Denmark", "Djibouti", "Dominica",
  "Dominican Republic", "East Timor", "Ecuador", "Egypt", "El Salvador",
  "Equatorial Guinea", "Eritrea", "Estonia", "Ethiopia", "Fiji", "Finland",
  "France", "Gabon", "Gambia", "Georgia", "Germany", "Ghana", "Greece",
  "Grenada", "Guatemala", "Guinea", "Guinea-Bissau", "Guyana", "Haiti",
  "Honduras", "Hungary", "Iceland", "India", "Indonesia", "Iran", "Iraq",
  "Ireland {Republic}", "Israel", "Italy", "Ivory Coast", "Jamaica", "Japan",
  "Jordan", "Kazakhstan", "Kenya", "Kiribati", "Korea North", "Korea South",
  "Kosovo", "Kuwait", "Kyrgyzstan", "Laos", "Latvia", "Lebanon", "Lesotho",
  "Liberia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg", "Macedonia",
  "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", "Malta",
  "Marshall Islands", "Mauritania", "Mauritius", "Mexico", "Micronesia",
  "Moldova", "Monaco", "Mongolia", "Montenegro", "Morocco", "Mozambique",
  "Myanmar, {Burma}", "Namibia", "Nauru", "Nepal", "Netherlands",
  "New Zealand", "Nicaragua", "Niger", "Nigeria", "Norway", "Oman", "Pakistan",
  "Palau", "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines",
  "Poland", "Portugal", "Qatar", "Romania", "Russian Federation", "Rwanda",
  "St Kitts & Nevis", "St Lucia", "Saint Vincent & the Grenadines", "Samoa",
  "San Marino", "Sao Tome & Principe", "Saudi Arabia", "Senegal", "Serbia",
  "Seychelles", "Sierra Leone", "Singapore", "Slovakia", "Slovenia",
  "Solomon Islands", "Somalia", "South Africa", "South Sudan", "Spain",
  "Sri Lanka", "Sudan", "Suriname", "Swaziland", "Sweden", "Switzerland",
  "Syria", "Taiwan", "Tajikistan", "Tanzania", "Thailand", "Togo", "Tonga",
  "Trinidad & Tobago", "Tunisia", "Turkey", "Turkmenistan", "Tuvalu", "Uganda",
  "Ukraine", "United Arab Emirates", "United Kingdom", "United States",
  "Uruguay", "Uzbekistan", "Vanuatu", "Vatican City", "Venezuela", "Vietnam",
  "Yemen", "Zambia", "Zimbabwe"
]

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
  print("Logged in as {0.user}".format(client))



@client.event
async def on_message(message):
  username = str(message.author).split("#")[0]
  user_message = str(message.content)
  channel = str(message.channel.name)
  print(f"{username}: {user_message}: ({channel})")

  if message.author == client.user:
    return
#message
#stop posting about baller

  if "!t or f" in message.content:

    await message.channel.send(f"{random.choice(torf)}")

    return
  #random Number
  elif user_message.lower() == "!rnd":
    await message.channel.send(f"{random.randint(0,10)}")
    return
  #t or f  elif user_message.lower() == "!t or f":


  #random maa
  elif user_message.lower() == "!maa":
    await message.channel.send(f"{random.choice(countries)}")
    return
  #baller info
  elif user_message.lower() == "!ballerinfo":
    await message.channel.send(f"<@642441889181728810> on tehnyt minut")
    return
  #random kirosana
  elif user_message.lower() == "!ksana":
    await message.channel.send(f"{random.choice(swear)}")
    return
  
  #random kirosana
  elif user_message.lower() == "!swear":
    await message.channel.send(f"{random.choice(other_swear)}")
    return

  #random kirosana combo
  elif user_message.lower() == "!ksanak":
    await message.channel.send(f"Voi {random.choice(swear)} {random.choice(swear)} {random.choice(swear)} {random.choice(swear)}")
    return
  #random nimi
  elif user_message.lower() == "!nimi":
    await message.channel.send(f"{names.get_full_name()}")
    return
  #nimi male
  elif user_message.lower() == "!nimi m":
    await message.channel.send(f"{names.get_full_name(gender='male')}")
    return
  #nimi female
  elif user_message.lower() == "!nimi n":
    await message.channel.send(f"{names.get_full_name(gender='female')}")
    return
  #female
  elif user_message.lower() == "!pvm":
    await message.channel.send(f"Päivämäärä Tänään: {d2}")
    return


  #greg
  elif user_message.lower() == "!greg":
    gchoice = random.choice(greg_list)
    print (gchoice)
    if gchoice =="gpengu":
      await message.channel.send(f"https://preview.redd.it/m7qrxjibc1x51.jpg?auto=webp&s=1017ae29588f54dbf4668fef34cab0a9ca89a55d")
      return
    elif gchoice =="gmonster":
      await message.channel.send(f"https://assets.reedpopcdn.com/craig_the_halo_infinite_brute_banner.jpg/BROK/resize/690%3E/format/jpg/quality/75/craig_the_halo_infinite_brute_banner.jpg")
      return
    elif gchoice =="gheffley":
      await message.channel.send(f"https://static.wikia.nocookie.net/doawk/images/2/24/Character-_Greg_Heffley.png/revision/latest?cb=20220226050019")
      return

    elif gchoice =="gfamilyguy":
      await message.channel.send(f"https://www.memecreator.org/static/images/memes/5286434.jpg")
      return


    elif gchoice =="gdeer":
      await message.channel.send(f"https://preview.redd.it/gv7zmkqtpuj61.jpg?auto=webp&s=07d15b6a917af8f9cc0d5cd240e1c38cbe104977")
      return

    elif gchoice =="gggreg":
      await message.channel.send(f"https://i.chzbgr.com/full/5137904384/h25B80960/good-guy-greg")
      return
      









    
  elif user_message.lower() == "!sää":
    temp = ["-25"] * 5 + ["-20"] * 17 + ["-15"] * 10 + ["-10"] * 12 + [
      "-5"
    ] * 15 + ["0"] * 22 + ["5"] * 5 + ["10"] * 5 + ["15"] * 5 + ["20"] * 3 + [
      "25"
    ] * 1
    weat = ['ukkostaa'] * 5 + ['sataa'] * 10 + ['sataa lunta'] * 10 + [
      'paistaa aurinko'
    ] * 25 + ["on pilvistä"] * 50
    await message.channel.send(
      f"Huomenna {random.choice(weat)} ja lämpötila on {random.choice(temp)} °C  *(tämä on randomilla tehty ennustus)*"
    )
    return

  elif user_message.lower() == "!uname":
    ggtag = random.choice(gg_tag)
    xtag = random.choice(xxx_tag) 
    if ggtag == 1:
      ggtagvar = "Gamer"
    else:
      ggtagvar = ""
    
    if xtag == 1:
      xtagvar = "xxx"
    else:
      xtagvar = ""
      
    await message.channel.send(f"{xtagvar}{random.choice(game_tags)}{ggtagvar}{random.randint(0,100)}{xtagvar}")
    return

  
    


#maat

  elif user_message.lower() == "!albania":
    await message.channel.send(f"Tirana")
    return

  elif user_message.lower() == "!andorra":
    await message.channel.send(f"Andorra la Vella")
    return

  elif user_message.lower() == "!armenia":
    await message.channel.send(f"Yerevan")
    return

  elif user_message.lower() == "!austria":
    await message.channel.send(f"Vienna")
    return

  elif user_message.lower() == "!azerbaijan":
    await message.channel.send(f"Baku")
    return

  elif user_message.lower() == "!belarus":
    await message.channel.send(f"Minsk")
    return

  elif user_message.lower() == "!belgium":
    await message.channel.send(f"Brussels")
    return

  elif user_message.lower() == "!b&h":
    await message.channel.send(f"Sarajevo")
    return

  elif user_message.lower() == "!bulgaria":
    await message.channel.send(f"Sofia")
    return

  elif user_message.lower() == "!croatia":
    await message.channel.send(f"Zagreb")
    return

  elif user_message.lower() == "!cyprus":
    await message.channel.send(f"Nicosia")
    return

  elif user_message.lower() == "!czechia":
    await message.channel.send(f"Prague")
    return

  elif user_message.lower() == "!denmark":
    await message.channel.send(f"Copenhagen")
    return

  elif user_message.lower() == "!estonia":
    await message.channel.send(f"Tallinn")
    return

  elif user_message.lower() == "!finland":
    await message.channel.send(f"Helsinki")
    return

  elif user_message.lower() == "!france":
    await message.channel.send(f"Paris")
    return

  elif user_message.lower() == "!georgia":
    await message.channel.send(f"Tbilisi")
    return

  elif user_message.lower() == "!germany":
    await message.channel.send(f"Berlin")
    return

  elif user_message.lower() == "!greece":
    await message.channel.send(f"Athens")
    return

  elif user_message.lower() == "!hungary":
    await message.channel.send(f"Budapest")
    return

  elif user_message.lower() == "!iceland":
    await message.channel.send(f"Reykjavík")
    return

  elif user_message.lower() == "!ireland":
    await message.channel.send(f"Dublin")
    return

  elif user_message.lower() == "!italy":
    await message.channel.send(f"Rome")
    return

  elif user_message.lower() == "!kazakhstan":
    await message.channel.send(f"Astana")
    return

  elif user_message.lower() == "!latvia":
    await message.channel.send(f"Riga")
    return

  elif user_message.lower() == "!liechtenstein":
    await message.channel.send(f"Vaduz")
    return

  elif user_message.lower() == "!lithuania":
    await message.channel.send(f"Vilnius")
    return

  elif user_message.lower() == "!luxembourg":
    await message.channel.send(f"Luxembourg")
    return

  elif user_message.lower() == "!malta":
    await message.channel.send(f"Valletta")
    return

  elif user_message.lower() == "!moldova":
    await message.channel.send(f"Chișinău")
    return

  elif user_message.lower() == "!monaco":
    await message.channel.send(f"Monaco")
    return

  elif user_message.lower() == "!montenegro":
    await message.channel.send(f"Podgorica")
    return

  elif user_message.lower() == "!netherlands":
    await message.channel.send(f"Amsterdam")
    return

  elif user_message.lower() == "!north macedonia":
    await message.channel.send(f"Skopje")
    return

  elif user_message.lower() == "!norway":
    await message.channel.send(f"Oslo")
    return

  elif user_message.lower() == "!poland":
    await message.channel.send(f"Warsaw")
    return

  elif user_message.lower() == "!portugal":
    await message.channel.send(f"Lisbon")
    return

  elif user_message.lower() == "!romania":
    await message.channel.send(f"Bucharest")
    return

  elif user_message.lower() == "!russia":
    await message.channel.send(f"Moscow")
    return

  elif user_message.lower() == "!san Marino":
    await message.channel.send(f"San Marino")
    return

  elif user_message.lower() == "!serbia":
    await message.channel.send(f"Belgrade")
    return

  elif user_message.lower() == "!slovakia":
    await message.channel.send(f"Bratislava")
    return

  elif user_message.lower() == "!slovenia":
    await message.channel.send(f"Ljubljana")
    return

  elif user_message.lower() == "!spain":
    await message.channel.send(f"Madrid")
    return

  elif user_message.lower() == "!sweden":
    await message.channel.send(f"Stockholm")
    return

  elif user_message.lower() == "!switzerland":
    await message.channel.send(f"Bern")
    return

  elif user_message.lower() == "!turkey":
    await message.channel.send(f"Ankara")
    return

  elif user_message.lower() == "!ukraine":
    await message.channel.send(f"Kyiv")
    return

  elif user_message.lower() == "!united Kingdom":
    await message.channel.send(f"London")
    return

  elif user_message.lower() == "!vatican City":
    await message.channel.send(f"Vatican City")
    return

  elif user_message.lower() == "!abkhazia":
    await message.channel.send(f"Sukhumi (ei ole maa)")
    return

  elif user_message.lower() == "!artsakh":
    await message.channel.send(f"Stepanakert (ei ole maa)")
    return

  elif user_message.lower() == "!kosovo":
    await message.channel.send(f"Pristina")
    return

  elif user_message.lower() == "!northern Cyprus":
    await message.channel.send(f"Nicosia (ei ole maa)")
    return

  elif user_message.lower() == "!south Ossetia":
    await message.channel.send(f"Tskhinvali (ei ole maa)")
    return

  elif user_message.lower() == "!transnistria":
    await message.channel.send(f"Tiraspol (ei ole maa)")
    return

  elif user_message.lower() == "!åland":
    await message.channel.send(f"Mariehamn (ei ole maa)")
    return

  elif user_message.lower() == "!yugoslavia":
    await message.channel.send(f"Belgrade")
    return

  elif user_message.lower() == "!nazi germany":
    await message.channel.send(f"Berlin")
    return

  elif user_message.lower() == "!german empire":
    await message.channel.send(f"Berlin")
    return

  elif user_message.lower() == "!ussr":
    await message.channel.send(f"Moscow")
    return

  elif user_message.lower() == "???":
    await message.channel.send(f"???")
    return

  elif user_message.lower() == "!ballerping":
    await message.channel.send(f"{round(client.latency *10000)}ms")
    return


    #afrika
  elif user_message.lower() == "!algeria":
    await message.channel.send(f"Algiers")
    return
  elif user_message.lower() == "!angola":
    await message.channel.send(f"Luanda")
    return
  elif user_message.lower() == "!benin":
    await message.channel.send(f"Porto-Novo")
    return
  
  elif user_message.lower() == "!botswana":
    await message.channel.send(f"Gaborone")
    return
  
  elif user_message.lower() == "!burkina faso":
    await message.channel.send(f"Ouagadougou")
    return
  
  elif user_message.lower() == "!burundi":
    await message.channel.send(f"Gitega")
    return
  
  elif user_message.lower() == "!cameroon":
    await message.channel.send(f"Yaoundé")
    return
  
  elif user_message.lower() == "!cape Verde":
    await message.channel.send(f"Praia")
    return
  
  elif user_message.lower() == "!car":
    await message.channel.send(f"Bangui")
    return
  
  elif user_message.lower() == "!chad":
    await message.channel.send(f"N'Djamena")
    return
  
  elif user_message.lower() == "!comoros":
    await message.channel.send(f"Moroni")
    return
  
  elif user_message.lower() == "!drc":
    await message.channel.send(f"Kinshasa")
    return
  
  elif user_message.lower() == "!roc":
    await message.channel.send(f"Brazzaville")
    return
  
  elif user_message.lower() == "!djibouti":
    await message.channel.send(f"Djibouti")
    return
  
  elif user_message.lower() == "!egypt":
    await message.channel.send(f"Cairo")
    return
  
  elif user_message.lower() == "!equatorial guinea":
    await message.channel.send(f"Malabo")
    return
  
  elif user_message.lower() == "!eritrea":
    await message.channel.send(f"Asmara")
    return
  elif user_message.lower() == "!eswatini":
    await message.channel.send(f"Lobamba")
    return
  
  
  elif user_message.lower() == "!ethiopia":
    await message.channel.send(f"Addis Ababa")
    return
  
  
  elif user_message.lower() == "!gabon":
    await message.channel.send(f"Libreville")
    return
  
  elif user_message.lower() == "!the gambia":
    await message.channel.send(f"Banjul")
    return
  elif user_message.lower() == "!ghana":
    await message.channel.send(f"Accra")
    return
  elif user_message.lower() == "!guinea":
    await message.channel.send(f"Conakry")
    return
  elif user_message.lower() == "!guinea-bissau":
    await message.channel.send(f"Bissau")
    return
  elif user_message.lower() == "!ivory coast":
    await message.channel.send(f"Yamoussoukro")
    return
  elif user_message.lower() == "!kenya":
    await message.channel.send(f"Nairobi")
    return
  elif user_message.lower() == "!lesotho":
    await message.channel.send(f"Maseru")
    return
  elif user_message.lower() == "!liberia":
    await message.channel.send(f"Monrovia")
    return
  elif user_message.lower() == "!libya":
    await message.channel.send(f"Tripoli")
    return
  
  
  elif user_message.lower() == "!madagascar":
    await message.channel.send(f"Antananarivo")
    return
  elif user_message.lower() == "!malawi":
    await message.channel.send(f"Lilongwe")
    return
  elif user_message.lower() == "!mali":
    await message.channel.send(f"Bamako")
    return
  elif user_message.lower() == "!mauritania":
    await message.channel.send(f"Nouakchott")
    return
  elif user_message.lower() == "!mauritius":
    await message.channel.send(f"Port Louis")
    return
  elif user_message.lower() == "!morocco":
    await message.channel.send(f"Rabat")
    return
  elif user_message.lower() == "!mozambique":
    await message.channel.send(f"Maputo")
    return
  elif user_message.lower() == "!namibia":
    await message.channel.send(f"Windhoek")
    return
  elif user_message.lower() == "!niger":
    await message.channel.send(f"Niamey")
    return
  elif user_message.lower() == "!nigeria":
    await message.channel.send(f"Abuja")
    return
  elif user_message.lower() == "!rwanda":
    await message.channel.send(f"Kigali")
    return
  elif user_message.lower() == "!senegal":
    await message.channel.send(f"Dakar")
    return
  elif user_message.lower() == "!seychelles":
    await message.channel.send(f"Victoria")
    return
  elif user_message.lower() == "!sierra leone":
    await message.channel.send(f"Freetown")
    return
  elif user_message.lower() == "!somalia":
    await message.channel.send(f"Mogadishu")
    return
  elif user_message.lower() == "!south africa":
    await message.channel.send(f"Bloemfontein, Cape Town, Pretoria")
    return
  
  elif user_message.lower() == "!south sudan":
    await message.channel.send(f"Juba")
    return
  elif user_message.lower() == "!sudan":
    await message.channel.send(f"Khartoum")
    return
  elif user_message.lower() == "!tanzania":
    await message.channel.send(f"Dodoma")
    return
  elif user_message.lower() == "!togo":
    await message.channel.send(f"Lome")
    return
  elif user_message.lower() == "!tunisia":
    await message.channel.send(f"Tunis")
    return
  
  elif user_message.lower() == "!uganda":
    await message.channel.send(f"Kampala")
    return
  
  elif user_message.lower() == "!zambia":
    await message.channel.send(f"Lusaka")
    return
  
  
  elif user_message.lower() == "!zimbabwe":
    await message.channel.send(f"Harere")
    return


  elif user_message.lower() == "!afghanistan":
      await message.channel.send(f"Kabul")
      return
      
  
  
  elif user_message.lower() == "!bahrain":
    await message.channel.send(f"Manama")
    return
  
  elif user_message.lower() == "!bangladesh":
    await message.channel.send(f"Dhaka")
    return
  
  
  elif user_message.lower() == "!bhutan":
    await message.channel.send(f"Thimphu")
    return
  
  elif user_message.lower() == "!brunei":
    await message.channel.send(f"Bandar Seri Begawan")
    return
  
  elif user_message.lower() == "!cambodia":
    await message.channel.send(f"Phnom Penh")
    return
  
  elif user_message.lower() == "!china":
    await message.channel.send(f"Beijing")
    return
  
  elif user_message.lower() == "!east timor":  
    await message.channel.send(f"Dili")
    return
  
  
  
  
  elif user_message.lower() == "!india":
    await message.channel.send(f"New Delhi")
    return
  
  elif user_message.lower() == "!indonesia":
    await message.channel.send(f"Jakarta")
    return
  
  elif user_message.lower() == "!iran":  
    await message.channel.send(f"Tehran")
    return
  
  elif user_message.lower() == "!iraq":
    await message.channel.send(f"Baghdad")
    return
  
  elif user_message.lower() == "!israel":  
    await message.channel.send(f"Jerusalem")
    return
  
  
  
  
  elif user_message.lower() == "!japan":
    await message.channel.send(f"Tokyo")
    return
  
  elif user_message.lower() == "!jordan":
    await message.channel.send(f"Amman")
    return
  
  elif user_message.lower() == "!kuwait":
    await message.channel.send(f"Kuwait City")
    return
  
  elif user_message.lower() == "!kyrgyzstan":
    await message.channel.send(f"Bishkek")
    return
  
  elif user_message.lower() == "!laos":
    await message.channel.send(f"Vientiane")
    return
  
  
  elif user_message.lower() == "!lebanon":
    await message.channel.send(f"Beirut")
    return
  
  elif user_message.lower() == "!malaysia":
    await message.channel.send(f"Kuala Lumpur")
    return
  
  elif user_message.lower() == "!maldives":
    await message.channel.send(f"Malé")
    return
  
  elif user_message.lower() == "!mongolia":  
    await message.channel.send(f"Ulaanbaatar")
    return
  
  elif user_message.lower() == "!myanmar":
    await message.channel.send(f"Naypyidaw")
    return
  
  
  
  
  elif user_message.lower() == "!nepal":
    await message.channel.send(f"Kathmandu")
    return
  
  elif user_message.lower() == "!north korea":
    await message.channel.send(f"Pyongyang")
    return
  
  elif user_message.lower() == "!oman":
    await message.channel.send(f"Muscat")
    return
  
  elif user_message.lower() == "!pakistan":
    await message.channel.send(f"Islamabad")
    return
  
  elif user_message.lower() == "!palestine":
    await message.channel.send(f"Jerusalem, RamallahRamallah")
    return
  
  
  elif user_message.lower() == "!philippines":
    await message.channel.send(f"Manila")
    return
  
  elif user_message.lower() == "!qatar":
    await message.channel.send(f"Doha")
    return
  
  elif user_message.lower() == "!russia":
    await message.channel.send(f"Moscow")
    return
  
  elif user_message.lower() == "!saudi arabia":
    await message.channel.send(f"Riyadh")
    return
  
  elif user_message.lower() == "!singapore":
    await message.channel.send(f"Singapore")
    return
  
  
  elif user_message.lower() == "!south korea":
    await message.channel.send(f"Seoul")
    return
  
  elif user_message.lower() == "!sri lanka":
    await message.channel.send(f"Sri Jayawardenepura Kotte")
    return
  
  elif user_message.lower() == "!syria":
    await message.channel.send(f"Damascus")
    return
  
  elif user_message.lower() == "!taiwan":
    await message.channel.send(f"Taipei")
    return
  
  elif user_message.lower() == "!tajikistan":
    await message.channel.send(f"Dushanbe")
    return
    
  
  
  
  elif user_message.lower() == "!thailand":
    await message.channel.send(f"Bangkok")
    return
  
  elif user_message.lower() == "!turkey":
    await message.channel.send(f"Ankara")
    return
  
  elif user_message.lower() == "!turkmenistan":
    await message.channel.send(f"Ashgabat")
    return
  
  elif user_message.lower() == "!uae":
    await message.channel.send(f"Abu Dhabi")
    return
  
  elif user_message.lower() == "!uzbekistan":
    await message.channel.send(f"Tashkent")
    return
  
  
  elif user_message.lower() == "!vietnam":
    await message.channel.send(f"Hanoi")
    return
  
  elif user_message.lower() == "!yemen":
    await message.channel.send(f"Sana'a, Aden")
    return
  





  elif user_message.lower() == "!?spam100":
    await message.channel.send(f"Aloitetaan Spämmi 100 viestiä")
    await message.channel.send(f"???")
    await message.channel.send(f"???")
    await message.channel.send(f"???")
    await message.channel.send(f"???")
    await message.channel.send(f"???")
    await message.channel.send(f"???")
    await message.channel.send(f"???")
    await message.channel.send(f"???")
    await message.channel.send(f"???")
    await message.channel.send(f"???")
    await message.channel.send(f"???")
    await message.channel.send(f"???")
    await message.channel.send(f"???")
    await message.channel.send(f"???")
    await message.channel.send(f"???")
    await message.channel.send(f"???")
    await message.channel.send(f"???")
    await message.channel.send(f"???")
    await message.channel.send(f"???")
    await message.channel.send(f"???")
    await message.channel.send(f"???")
    await message.channel.send(f"???")
    await message.channel.send(f"???")
    await message.channel.send(f"???")
    await message.channel.send(f"???")
    await message.channel.send(f"???")
    await message.channel.send(f"???")
    await message.channel.send(f"???")
    await message.channel.send(f"???")
    await message.channel.send(f"???")
    await message.channel.send(f"???")
    await message.channel.send(f"???")
    await message.channel.send(f"???")
    await message.channel.send(f"???")
    await message.channel.send(f"???")
    await message.channel.send(f"???")
    await message.channel.send(f"???")
    await message.channel.send(f"???")
    await message.channel.send(f"???")
    await message.channel.send(f"???")
    await message.channel.send(f"???")
    await message.channel.send(f"???")
    await message.channel.send(f"???")
    await message.channel.send(f"???")
    await message.channel.send(f"???")
    await message.channel.send(f"???")
    await message.channel.send(f"???")
    await message.channel.send(f"???")
    await message.channel.send(f"???")
    await message.channel.send(f"???")
    await message.channel.send(f"???")
    await message.channel.send(f"???")
    await message.channel.send(f"???")
    await message.channel.send(f"???")
    await message.channel.send(f"???")
    await message.channel.send(f"???")
    await message.channel.send(f"???")
    await message.channel.send(f"???")
    await message.channel.send(f"???")
    await message.channel.send(f"???")
    await message.channel.send(f"???")
    await message.channel.send(f"???")
    await message.channel.send(f"???")
    await message.channel.send(f"???")
    await message.channel.send(f"???")
    await message.channel.send(f"???")
    await message.channel.send(f"???")
    await message.channel.send(f"???")
    await message.channel.send(f"???")
    await message.channel.send(f"???")
    await message.channel.send(f"???")
    await message.channel.send(f"???")
    await message.channel.send(f"???")
    await message.channel.send(f"???")
    await message.channel.send(f"???")
    await message.channel.send(f"???")
    await message.channel.send(f"???")
    await message.channel.send(f"???")
    await message.channel.send(f"???")
    await message.channel.send(f"???")
    await message.channel.send(f"???")
    await message.channel.send(f"???")
    await message.channel.send(f"???")
    await message.channel.send(f"???")
    await message.channel.send(f"???")
    await message.channel.send(f"???")
    await message.channel.send(f"???")
    await message.channel.send(f"???")
    await message.channel.send(f"???")
    await message.channel.send(f"???")
    await message.channel.send(f"???")
    await message.channel.send(f"???")
    await message.channel.send(f"???")
    await message.channel.send(f"???")
    await message.channel.send(f"???")
    await message.channel.send(f"???")
    await message.channel.send(f"???")
    await message.channel.send(f"???")
    await message.channel.send(f"???")
    await message.channel.send(f"???")

    return
    
        



    
    



def printit():
  threading.Timer(5.0, printit).start()
  print(f"{client.latency *1000}ms")



printit()
keep_alive()
try:
  TOKEN = os.environ.get("DISCORD_BOT_SECRET")
  client.run(TOKEN)
except discord.errors.HTTPException:
  os.system("kill 1")
  restart()
  print("restarting")
  client.run(TOKEN)


if client.latency == "inf":
    print("Restarting")
    os.system("kill 1")
    restart()
    client.run(TOKEN)
else:
  if client.latency == "nan":
    os.system("kill 1")
    restart()
    print("Restarting")
    client.run(TOKEN)





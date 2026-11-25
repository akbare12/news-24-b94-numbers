# news-image-20261124 b94-numbers: 38 stories, hero trio Riyadh / Shanghai / Huawei.
# Angle NUMBERS: 8-number strip, giant numbers in hero scenes, chip on every ALSO item.
# Map from real lat/lon (equirectangular); scenes drawn in code, no photographs.
import os
from PIL import Image, ImageDraw, ImageFont
W,H=1024,1024; OUT=os.path.join(os.environ.get('MAKEFUN_OUTPUT_DIR','out'),'entry.png')
F=lambda s,b=False: ImageFont.truetype('/usr/share/fonts/truetype/dejavu/'+('DejaVuSerif-Bold.ttf' if b=='serif' else 'DejaVuSans-Bold.ttf' if b else 'DejaVuSans.ttf'),s)
im=Image.new('RGB',(W,H),(250,244,230)); d=ImageDraw.Draw(im,'RGBA')
NAVY=(18,32,62); RED=(178,34,34); CREAM=(250,244,230); INK=(20,20,20); GREY=(90,90,90); GOLD=(176,132,32)
def T(x,y,s,f,c=INK,anchor='la'): d.text((x,y),s,font=f,fill=c,anchor=anchor)
def R(x,y,w,h,fc,oc=None): d.rectangle([x,y,x+w,y+h],fill=fc,outline=oc)
def wrap(s,f,w):
    words,lines,cur=s.split(),[],''
    for wd in words:
        t=(cur+' '+wd).strip()
        if d.textlength(t,font=f)<=w: cur=t
        else: lines.append(cur); cur=wd
    if cur: lines.append(cur)
    return lines
def block(x,y,w,lines,f,lh,c=INK): [T(x,y+i*lh,l,f,c) for i,l in enumerate(lines)]; return y+len(lines)*lh
def chip(x,y,s,fc):
    w=int(d.textlength(s,font=F(7,True)))+10; R(x,y,w,12,fc); T(x+5,y+1,s,F(7,True),(255,255,255)); return x+w+4
def scene(x,y,w,h,kind):
    R(x,y,w,h,(30,40,70) if kind in('tower','war','ship') else (70,90,110) if kind=='court' else (24,60,44) if kind=='trophy' else (120,40,40) if kind=='data' else (40,70,90) if kind=='rocket' else (60,60,80))
    if kind=='tower':
        d.polygon([(x+w*0.45,y+h),(x+w*0.45,y+h*0.25),(x+w*0.55,y+h*0.25),(x+w*0.55,y+h)],fill=(200,200,210)); d.polygon([(x+w*0.5,y+h*0.05),(x+w*0.58,y+h*0.25),(x+w*0.42,y+h*0.25)],fill=(230,230,240)); d.ellipse([x+w*0.62,y+h*0.15,x+w*0.80,y+h*0.33],fill=(255,170,40)); d.ellipse([x+w*0.66,y+h*0.19,x+w*0.76,y+h*0.29],fill=(255,220,120))
        for i in range(5): R(x+w*0.08+i*w*0.14,y+h*0.62,w*0.09,h*0.38,(90,95,120))
        d.polygon([(x+w*0.7,y+h*0.3),(x+w*0.78,y+h*0.38),(x+w*0.7,y+h*0.42)],fill=(120,120,130))
    elif kind=='gate':
        R(x+w*0.08,y+h*0.35,w*0.84,h*0.65,RED); R(x+w*0.42,y+h*0.55,w*0.16,h*0.45,(90,10,10))
        for i in range(6): R(x+w*0.12+i*w*0.13,y+h*0.42,w*0.06,h*0.12,GOLD)
        d.polygon([(x+w*0.08,y+h*0.35),(x+w*0.5,y+h*0.08),(x+w*0.92,y+h*0.35)],fill=(120,20,20))
    elif kind=='court':
        R(x+w*0.1,y+h*0.4,w*0.8,h*0.6,(210,205,190)); d.polygon([(x+w*0.05,y+h*0.4),(x+w*0.5,y+h*0.08),(x+w*0.95,y+h*0.4)],fill=(240,235,220))
        for i in range(5): R(x+w*0.15+i*w*0.15,y+h*0.45,w*0.07,h*0.55,(150,145,130))
        d.ellipse([x+w*0.72,y+h*0.55,x+w*0.86,y+h*0.69],fill=(40,80,160)); T(x+w*0.79,y+h*0.55,'H',F(16,True),(255,255,255),anchor='mm')
    elif kind in ('war','ship','heli','strike','market','rocket','trophy','data','chart'):
        d.ellipse([x+w*0.68,y+h*0.12,x+w*0.88,y+h*0.32],fill=(255,200,80))
        if kind=='war':
            for i in range(4): d.polygon([(x+w*(0.1+i*0.2),y+h*0.7),(x+w*(0.16+i*0.2),y+h*0.45),(x+w*(0.22+i*0.2),y+h*0.7)],fill=(70,70,80))
            d.ellipse([x+w*0.3,y+h*0.2,x+w*0.42,y+h*0.32],fill=(255,120,40))
        if kind=='ship': R(x+w*0.1,y+h*0.55,w*0.8,h*0.2,(140,60,40)); R(x+w*0.3,y+h*0.35,w*0.3,h*0.2,(60,90,120)); d.line([x+w*0.1,y+h*0.75,x+w*0.9,y+h*0.75],fill=(80,160,200),width=3)
        if kind=='heli': d.ellipse([x+w*0.3,y+h*0.35,x+w*0.7,y+h*0.6],fill=(90,110,90)); d.line([x+w*0.2,y+h*0.35,x+w*0.8,y+h*0.35],fill=(40,40,40),width=4); d.line([x+w*0.5,y+h*0.6,x+w*0.5,y+h*0.8],fill=(40,40,40),width=3)
        if kind=='strike': d.polygon([(x+w*0.2,y+h*0.7),(x+w*0.5,y+h*0.2),(x+w*0.8,y+h*0.7)],fill=(180,120,60)); R(x+w*0.15,y+h*0.7,w*0.7,h*0.15,(120,80,40))
        if kind=='market': d.line([x+w*0.1,y+h*0.75,x+w*0.35,y+h*0.55,x+w*0.6,y+h*0.6,x+w*0.9,y+h*0.2],fill=(40,200,90),width=4); d.line([x+w*0.1,y+h*0.3,x+w*0.9,y+h*0.3],fill=RED,width=2)
        if kind=='rocket': d.polygon([(x+w*0.45,y+h*0.1),(x+w*0.55,y+h*0.1),(x+w*0.55,y+h*0.6),(x+w*0.45,y+h*0.6)],fill=(230,230,230)); d.polygon([(x+w*0.5,y+h*0.02),(x+w*0.58,y+h*0.18),(x+w*0.42,y+h*0.18)],fill=RED); d.polygon([(x+w*0.5,y+h*0.6),(x+w*0.58,y+h*0.85),(x+w*0.42,y+h*0.85)],fill=(255,160,40))
        if kind=='trophy': d.ellipse([x+w*0.35,y+h*0.2,x+w*0.65,y+h*0.6],fill=GOLD); R(x+w*0.45,y+h*0.6,w*0.1,h*0.25,GOLD); R(x+w*0.35,y+h*0.82,w*0.3,h*0.08,GOLD)
        if kind=='data': R(x+w*0.15,y+h*0.3,w*0.7,h*0.45,(20,20,20)); T(x+w*0.2,y+h*0.35,'! CODE RED',F(13,True),RED); T(x+w*0.2,y+h*0.6,'24h OUTAGE',F(10,True),(255,255,255))
    d.rectangle([x,y,x+w,y+h],outline=NAVY)
# --- header ---
R(0,0,W,3,RED); T(16,8,'THE WORLD ON ONE DAY',F(10,True),RED); T(1008,8,'38 STORIES \u00b7 6 REGIONS \u00b7 13 FIELDS',F(10,True),NAVY,anchor='ra')
T(512,24,'Tuesday 24 November 2026',F(30,'serif'),NAVY,anchor='ma'); T(512,58,'Riyadh tower hit again \u00b7 Shanghai party chief probed \u00b7 Huawei guilty on 10 of 12 counts',F(11,True),RED,anchor='ma')
REG=[('Europe',9,(40,80,160)),('Middle East',8,(178,34,34)),('Asia',8,(200,140,0)),('Africa',2,(24,120,60)),('Americas',7,(90,60,140)),('World/Space',4,(20,110,130))]
x=16
for n,c,col in REG:
    w=int(992*c/38); R(x,76,w,16,col); T(x+w/2,78,f'{n} {c}',F(8,True),(255,255,255),anchor='ma'); x+=w
UTC=[('00:30','Zelensky urges talks'),('02:15','NATO vows space defence'),('08:16','Hanoi hot-pot blast'),('10:42','Saudi strikes Yemen'),('14:27','Riyadh tower hit'),('16:51','Houthis 60 km from Aden'),('18:58','Hormuz ship attack'),('20:41','Huawei guilty')]
T(16,98,'THE DAY IN UTC',F(8,True),RED)
for i,(t,s) in enumerate(UTC): T(16+i*124,110,t,F(9,True),NAVY); T(16+i*124,122,s,F(7),GREY)
NUM=[('11','hurt in Riyadh'),('9','killed in Ukraine'),('50,018','Dow closes'),('+8.99%','Taiex record'),('25','killed in Yemen'),('26','Cikande toll'),('10/12','Huawei counts'),('96','drones at Ukraine')]
T(16,136,'THE DAY IN NUMBERS',F(8,True),RED); R(16,148,992,2,RED)
for i,(n,l) in enumerate(NUM): T(16+i*124,152,n,F(20,True),NAVY); T(16+i*124,176,l,F(7),GREY)

# --- heroes: scene 100px, giant number, deck ends with period ---
HERO=[('1 RIYADH \u00b7 MIDDLE EAST','CONFIRMED',(178,34,34),'tower','11','Houthi drone hits Riyadh\u2019s tallest tower again, 11 hurt','A Houthi drone hit the PIF tower, the tallest in Riyadh, for the second time in a week. At least 11 were hurt: 2 Saudis, 2 Indians, 3 Nepalis and 4 Egyptians. (Saudi officials \u00b7 14:27 UTC)'),('2 SHANGHAI \u00b7 ASIA','OFFICIAL',(40,80,160),'gate','62','China probes Shanghai party chief Chen Jining','Chen Jining, 62, the Shanghai party chief, is probed for serious violations. He is the fourth Politburo member to fall under investigation this year. (CCDI, on record)'),('3 NEW YORK \u00b7 US/TECH','CONFIRMED',(178,34,34),'court','10/12','Huawei guilty on 10 of 12 counts','A US federal jury found Huawei guilty on 10 of 12 counts, including trade-secret theft and bank fraud. It was cleared of racketeering. Sentence is set for Sep 2027. (US court \u00b7 20:41 UTC)')]
for i,(kick,cf,col,kind,big,head,deck) in enumerate(HERO):
    x=16+i*332; R(x,196,320,212,CREAM,NAVY); scene(x+4,200,312,100,kind); bw=int(d.textlength(big,font=F(30,True)))+12; R(x+308-bw,204,bw,36,NAVY); T(x+302,204,big,F(30,True),(255,255,255),anchor='ra')
    T(x+8,308,kick,F(8,True),RED); chip(x+8,322,cf,col)
    block(x+8,338,304,wrap(head,F(12,True),304),F(12,True),14); block(x+8,368,304,wrap(deck,F(9),304),F(9),11)
# --- cards 4-13: mini-scene 48px ---
CARD=[('4 ZAPORIZHZHIA \u00b7 EUROPE','REPORTED','war','Russian attacks kill 9 across Ukraine in a day','Russian attacks killed 9 in Ukraine and wounded 81. (Ukraine officials)'),('5 CAS \u00b7 AFRICA/SPORT','OFFICIAL','trophy','CAS hands Senegal back the AFCON title','CAS gave Senegal the AFCON title back after Morocco forfeited 3-0. (CAS)'),('6 HORMUZ \u00b7 MIDDLE EAST','REPORTED','ship','IRGC attacks container ship in Hormuz','An IRGC attack hit a container ship in Hormuz at 18:58 UTC. (UKMTO)'),('7 NEW YORK \u00b7 WORLD/MARKETS','CONFIRMED','chart','Dow closes above 50,000 for the first time','The Dow closed at 50,018, the first close above 50,000. (Market close)'),('8 REDMOND \u00b7 WORLD/TECH','REPORTED','data','Microsoft declares \u2018Code Red\u2019 after historic outage','Microsoft declared a \u2018Code Red\u2019 after a 24-hour outage. (Reuters)'),('9 ESKISEHIR \u00b7 EUROPE','REPORTED','heli','Turkish military helicopter crash kills 5','A Turkish AS-532 helicopter crashed in Eskisehir, killing all 5. (Officials)'),('10 CARTAGENA \u00b7 AMERICAS','REPORTED','market','Supermarket hostages: 25 held in Cartagena','Gunmen held 25 hostages in a Cartagena supermarket. 5 women were freed. (Officials)'),('11 ADEN \u00b7 MIDDLE EAST','REPORTED','strike','Houthis advance within 60 km of Aden','Houthi forces advanced to within 60 km of Aden in Yemen. (Wires)'),('12 LAHJ \u00b7 MIDDLE EAST','REPORTED','strike','Saudi strikes kill 25, wound 6 in Yemen','Saudi strikes in Wadi Maabaq, Lahj, killed 25 and wounded 6. (Yemen officials)'),('13 JIUQUAN \u00b7 WORLD/SPACE','OFFICIAL','rocket','China names first foreign astronaut for Tiangong','China named the Shenzhou-24 crew, including Pakistan\u2019s Zeeshan Ali. (CMSA)')]
for i,(kick,cf,kind,head,deck) in enumerate(CARD):
    x=16+(i%5)*200; y=416+(i//5)*122; R(x,y,192,118,CREAM,NAVY); scene(x+4,y+4,184,48,kind); T(x+8,y+55,kick,F(7,True),RED); chip(x+8,y+66,cf,(40,80,160) if cf=='OFFICIAL' else (90,90,90) if cf=='REPORTED' else (178,34,34))
    hl=wrap(head,F(9,True),176); block(x+8,y+80,176,hl,F(9,True),9); block(x+8,y+80+len(hl)*9,176,wrap(deck,F(7),176)[:2],F(7),7)

# --- map: equirectangular lat/lon, pins 1-13 only ---
MX,MY,MW,MH=16,660,640,150
R(MX,MY,MW,MH,(190,215,235),NAVY); T(MX+6,MY+4,'WORLD MAP \u00b7 PINS 1-13 ONLY',F(8,True),NAVY)
def ll(lat,lon): return (MX+8+(lon+170)/360*(MW-16), MY+18+(75-lat)/135*(MH-26))
LAND=[((-168,66),(-140,70),(-125,71),(-110,68),(-95,69),(-85,66),(-80,62),(-70,60),(-60,55),(-55,47),(-65,44),(-75,39),(-80,32),(-85,28),(-90,21),(-95,18),(-100,16),(-105,20),(-110,24),(-115,30),(-120,35),(-125,42),(-125,49),(-135,58),(-150,60),(-165,60)),((-80,10),(-75,5),(-70,-5),(-60,-10),(-50,-5),(-40,-10),(-35,-20),(-40,-30),(-50,-35),(-60,-40),(-65,-45),(-70,-50),(-73,-40),(-75,-30),(-80,-20),(-80,-10)),((-17,15),(-10,30),(0,35),(10,37),(20,32),(30,31),(35,28),(40,12),(48,10),(51,12),(43,0),(40,-10),(35,-20),(30,-30),(20,-35),(15,-25),(12,-15),(10,-5),(8,4),(0,5),(-8,5),(-13,8)),((-10,36),(-9,43),(-2,48),(0,50),(5,53),(8,57),(10,59),(18,56),(21,55),(24,58),(28,60),(30,62),(25,65),(20,70),(15,68),(10,62),(5,58),(0,50),(-5,45),(-9,38)),((30,36),(35,42),(40,45),(45,48),(50,50),(55,55),(60,60),(65,68),(70,72),(80,73),(90,75),(100,77),(110,74),(120,73),(130,72),(140,70),(150,68),(158,60),(162,55),(155,50),(145,45),(140,40),(135,35),(130,32),(125,30),(120,25),(110,20),(105,10),(100,8),(95,15),(90,22),(85,20),(80,13),(77,8),(73,20),(68,25),(62,25),(57,26),(52,28),(48,30),(44,30),(40,36),(35,36)),((113,-22),(114,-30),(115,-35),(120,-34),(125,-32),(130,-32),(135,-35),(140,-38),(145,-38),(150,-37),(153,-30),(150,-22),(146,-19),(142,-15),(140,-12),(135,-12),(130,-12),(125,-15),(120,-20),(114,-22))]
for poly in LAND: d.polygon([ll(la,lo) for lo,la in poly],fill=(110,160,110),outline=(60,110,60))
PINS=[(24.7,46.7),(31.2,121.5),(40.7,-74.0),(47.8,35.2),(14.7,-17.4),(26.5,56.3),(40.7,-73.2),(47.7,-122.1),(39.8,30.5),(10.4,-75.5),(12.8,45.0),(13.2,44.6),(39.8,98.5)]
for i,(la,lo) in enumerate(PINS,1):
    px,py=ll(la,lo)
    if i==7: px,py=px+14,py-6
    if i==12: px,py=px-14,py+8
    d.ellipse([px-8,py-8,px+8,py+8],fill=RED,outline=(255,255,255)); T(px,py,str(i),F(8,True),(255,255,255),anchor='mm')
LEG=['1 Riyadh PIF tower','2 Shanghai probe','3 Huawei 10/12','4 Ukraine 9 killed','5 Senegal AFCON','6 Hormuz ship','7 Dow 50,018','8 Redmond Code Red','9 Eskisehir crash','10 Cartagena 25','11 Aden 60 km','12 Lahj 25 killed','13 Tiangong crew']
for i,s in enumerate(LEG): T(676,662+i*12,f'{s}',F(8),INK)
# --- ALSO 14-38 ---
ALSO=[('14 Ankara','Haftar visits Turkey for the first time.','REPORTED'),('15 London','UK sanctions Houthis + 4 officials.','OFFICIAL'),('16 Villavicencio','Car bomb injures 23 people.','REPORTED'),('17 Gaza','Israel kills Hamas internal security chief.','REPORTED'),('18 Baghdad','Iraq orders federal control of Kurdish oilfields.','OFFICIAL'),('19 Gaza','Meningitis alert: 272 cases in October.','OFFICIAL'),('20 DR Congo','Missing Cessna 208; rebels claim shootdown.','CLAIM'),('21 Hanoi','Hot-pot explosion kills at least 6.','REPORTED'),('22 Gulf of Finland','Ukraine hits Russian ship Sparta II.','REPORTED'),('23 Kuala Lumpur','Malaysia to return thousands of migrants.','OFFICIAL'),('24 Ulleungdo','S. Korea shelter order as jets enter ADIZ.','OFFICIAL'),('25 Dhaka','Hasina plans return on 16 Dec.','REPORTED'),('26 The Hague','14 nations endorse ICJ Myanmar ruling.','REPORTED'),('27 Jakarta','Indonesia nominates 2 VP candidates.','OFFICIAL'),('28 China','China sentences official Ma to death for spying.','OFFICIAL'),('29 Brussels','NATO vows defence against space threat.','OFFICIAL'),('30 Mexico City','El Chapo Isidro: US drone aided Fri 20 Nov capture.','REPORTED'),('31 San Salvador','Bukele names 3 soldiers killed in Haiti.','OFFICIAL'),('32 Ottawa','Pentagon rebukes Canada: only 41.9% of air fleet ready.','REPORTED'),('33 Washington','US adds Megaspeed to trade blacklist.','OFFICIAL'),('34 Kyiv','Zelensky urges Ukraine/Russia/US/Europe talks soon.','REPORTED'),('35 Ras Al Khaimah','UAE bus-truck crash kills 13 people.','REPORTED'),('36 London','England record 5,258 heat deaths in summer 2026.','OFFICIAL'),('37 Kourou','Ariane 6 lofts 36 Amazon satellites.','OFFICIAL'),('38 Cikande','Factory-fire toll rises to 26.','REPORTED')]
T(16,818,'ALSO ON TUESDAY \u00b7 25 MORE STORIES',F(10,True),RED)
for i,(city,txt,cf) in enumerate(ALSO):
    x=16+(i%3)*330; y=836+(i//3)*11; s=f'{city}: {txt}' + (' [OFFICIAL]' if cf=='OFFICIAL' else '')
    if cf=='OFFICIAL': T(x,y,'\u25cf',F(8,True),(40,80,160)); T(x+10,y,s,F(7),INK)
    else: T(x,y,s,F(7),INK)
# --- DATE CHECK max 2 lines, footer ---
R(16,936,992,36,RED); T(24,941,'DATE CHECK: All stories happened or were first reported Tue 24 Nov 2026. LEFT OUT (not 24 Nov): Hormuz mine claims, Nvidia Huang return (23 Nov), EU sanctions 22, COP31 no deal (22 Nov), El Chapo arrest Fri 20 Nov.',F(7,True),(255,255,255)); T(24,953,'NOT YET: Shenzhou-24 launch Wed 25 Nov, Huawei sentence Sep 2027, MPR vote 11 Dec. Wires read to 23:00 UTC.',F(7,True),(255,255,255))
T(16,980,'Sources: Saudi officials \u00b7 CCDI \u00b7 US court \u00b7 Ukraine officials \u00b7 CAS \u00b7 UKMTO \u00b7 Reuters \u00b7 CMSA \u00b7 wires. CONFIRMED = 2+ outlets \u00b7 OFFICIAL = on record \u00b7 REPORTED = one outlet \u00b7 CLAIM = one side.',F(7),GREY)
T(512,996,'Scenes are drawn in code, not photographs. Tuesday 24 November 2026 \u00b7 38 stories.',F(8,True),NAVY,anchor='ma')
os.makedirs(os.path.dirname(OUT),exist_ok=True); im.save(OUT,optimize=True); print(OUT,os.path.getsize(OUT))

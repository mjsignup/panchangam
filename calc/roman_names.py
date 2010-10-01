#!/usr/bin/python
# -*- coding: utf-8 -*-

ahoratram = 'Ahoratram'
adhika = 'Adhika'
samvatsara = 'Samvatsara'
ekadashi = 'Ekadashi'
sarva = 'Sarva'
smartha = 'Smartha'
vaishnava = 'Vaishnava'
pradosham = 'Pradosha-Vratam'
chaturthi = 'Sankatahara-Chaturthi'
maha = 'Maha'
arambham = 'Arambha'
navaratri_start = 'Navaratri-'+arambham
durgashtami = 'Durgashtami'
mahanavami = 'Mahanavami/Sarasvati-Puja'
vijayadashami = 'Vijayadashami'
dipavali = 'Dipavali'
skanda = 'Skanda '
shashthi = 'Shashthi-Vratam'

vchaturthi = 'Shrivinayaka-Chaturthi'
ananta_chaturdashi = 'Ananta-Chaturdashi'
rishi_panchami = 'Rishi-Panchami  vratam'
ramanavami = 'Shriramanavami'
shivaratri = 'Mahashivaratri'
janmashtami = 'Shrikrishnajanmashtami'
chitra_purnima = 'Chitra Purnima, Gajendra-Moksha'
varalakshmi_vratam = 'Varalakshmi-Vratam'
yajur_upakarma = 'Yajurveda-Upakarma'
rg_upakarma = 'Rigveda-Upakarma'
sama_upakarma = 'Samaveda-Upakarma'
gayatri_japam = 'Gayatri  japam'
uttarayanam = 'Makara Sankranti/Uttarayana-Punyakalam'
dakshinayanam = 'Dakshinayana-Punyakalam'
mesha_sankranti = 'Mesha Sankranti'
karadayan_nombu = 'Karadayan-Nombu'
akshaya_tritiya = 'Akshaya Tritiya'
shankara_jayanti = 'Shankara-Jayanti'
mahalaya_paksham = 'Mahalaya-Paksha Arambha'
hanumat_jayanti = 'Shri Hanumat Jayanti'
ardra_darshanam = 'Ardra Darshanam'
ratha_saptami = 'Ratha-Saptami'
goda_jayanti = 'Shri Goda Jayanti'
adi_krittika = 'Ashadha Krittika'
phalguni_uttaram = 'Phalguni Uttaram'
mahalaya_amavasya = 'Mahalaya-Amavasya'
uma_maheshvara_vratam = 'Uma-Maheshvara Vratam'
yugadi = 'Yugadi'

chandra_grahanam = 'Chandra-Grahanam'
surya_grahanam = 'Surya-Grahanam'

list_of_festivals = 'Masantara-Vishesha'
chaturmasya_start='Chaturmasasya Arambha'
chaturmasya_end='Chaturmasasya Samapanam'

nakshatra_names={1:'Ashvini',
2:'Apabharani',
3:'Krittika',
4:'Rohini',
5:'Mrigashirsha',
6:'Ardra',
7:'Punarvasu',
8:'Pushya',
9:'Ashresha',
10:'Magha',
11:'Purvaphalguni',
12:'Uttaraphalguni',
13:'Hasta',
14:'Chitra',
15:'Svati',
16:'Vishakha',
17:'Anuradha',
18:'Jyeshtha',
19:'Mula',
20:'Purvashadha',
21:'Uttarashadha',
22:'Shravana',
23:'Shravishtha',
24:'Shatabhishak',
25:'Purvaproshthapada',
26:'Uttaraproshthapada',
27:'Revati'}

masa_names={1:'Mesha',
2:'Vrishabha',
3:'Mithuna',
4:'Karkataka',
5:'Simha',
6:'Kanya',
7:'Tula',
8:'Vrishchika',
9:'Dhanu',
10:'Makara',
11:'Kumbha',
12:'Mina'}

chandra_masa_names={1:'Chaitra',
2:'Vaishakha',
3:'Jyaishtha',
4:'Ashadha',
5:'Shravana',
6:'Bhadrapada',
7:'Ashvina',
8:'Kartika',
9:'Margashirsha',
10:'Pausha',
11:'Magha',
12:'Phalguna'}

tithi_names={1:'Shukla Prathama',
2:'Shukla Dvitiya',
3:'Shukla Tritiya',
4:'Shukla Chaturthi',
5:'Shukla Panchami',
6:'Shukla Shashthi',
7:'Shukla Saptami',
8:'Shukla Ashtami',
9:'Shukla Navami',
10:'Shukla Dashami',
11:'Shukla Ekadashi',
12:'Shukla Dvadashi',
13:'Shukla Trayodashi',
14:'Shukla Chaturdashi',
15:'\\fullmoon Purnima',
16:'Krishna Prathama',
17:'Krishna Dvitiya',
18:'Krishna Tritiya',
19:'Krishna Chaturthi',
20:'Krishna Panchami',
21:'Krishna Shashthi',
22:'Krishna Saptami',
23:'Krishna Ashtami',
24:'Krishna Navami',
25:'Krishna Dashami',
26:'Krishna Ekadashi',
27:'Krishna Dvadashi',
28:'Krishna Trayodashi',
29:'Krishna Chaturdashi',
30:'\\newmoon Amavasya'}

year_names={1:'Prabhava',
2:'Vibhava',
3:'Shukla',
4:'Pramoda',
5:'Prajapati',
6:'Angirasa',
7:'Shrimukha',
8:'Bhava',
9:'Yuva',
10:'Dhatri',
11:'Ishvara',
12:'Bahudhanya',
13:'Pramadhi',
14:'Vikrama',
15:'Vrisha',
16:'Chitrabhanu',
17:'Svabhanu',
18:'Tarana',
19:'Parthiva',
20:'Vyaya',
21:'Sarvajit',
22:'Sarvadhari',
23:'Virodhi',
24:'Vikriti',
25:'Khara',
26:'Nandana',
27:'Vijaya',
28:'Jaya',
29:'Manmatha',
30:'Durmukhi',
31:'Hevilambi',
32:'Vilambi',
33:'Vikari',
34:'Sharvari',
35:'Plava',
36:'Shubhakrit',
37:'Shobhakrit',
38:'Krodhi',
39:'Vishvavasu',
40:'Parabhava',
41:'Plavanga',
42:'Kilaka',
43:'Saumya',
44:'Sadharana',
45:'Virodhikriti',
46:'Paridhavi',
47:'Pramadicha',
48:'Ananda',
49:'Rakshasa',
50:'Nala',
51:'Pingala',
52:'Kalayukti',
53:'Siddharthi',
54:'Raudra',
55:'Durmati',
56:'Dundubhi',
57:'Rudhirodgari',
58:'Raktakshi',
59:'Krodhana',
60:'Akshaya'}

karanam_names={1:'Kimstughna',
2:'Bava',
3:'Balava',
4:'Kaulava',
5:'Taitila',
6:'Garaja',
7:'Vanija',
8:'Vishti',
9:'Bava',
10:'Balava',
11:'Kaulava',
12:'Taitila',
13:'Garaja',
14:'Vanija',
15:'Vishti',
16:'Bava',
17:'Balava',
18:'Kaulava',
19:'Taitila',
20:'Garaja',
21:'Vanija',
22:'Vishti',
23:'Bava',
24:'Balava',
25:'Kaulava',
26:'Taitila',
27:'Garaja',
28:'Vanija',
29:'Vishti',
30:'Bava',
31:'Balava',
32:'Kaulava',
33:'Taitila',
34:'Garaja',
35:'Vanija',
36:'Vishti',
37:'Bava',
38:'Balava',
39:'Kaulava',
40:'Taitila',
41:'Garaja',
42:'Vanija',
43:'Vishti',
44:'Bava',
45:'Balava',
46:'Kaulava',
47:'Taitila',
48:'Garaja',
49:'Vanija',
50:'Vishti',
51:'Bava',
52:'Balava',
53:'Kaulava',
54:'Taitila',
55:'Garaja',
56:'Vanija',
57:'Vishti',
58:'Shakuni',
59:'Chatushpada',
60:'Nagava'}

yogam_names={1:'Vishkumbha',
2:'Priti',
3:'Ayushman',
4:'Saubhagya',
5:'Shobhana',
6:'Atiganda',
7:'Sukarma',
8:'Dhriti',
9:'Shula',
10:'Ganda',
11:'Vriddhi',
12:'Dhruva',
13:'Vyaghata',
14:'Harshana',
15:'Vajra',
16:'Siddhi',
17:'Vyatipata',
18:'Variyana',
19:'Parigha',
20:'Shiva',
21:'Siddha',
22:'Sadhya',
23:'Shubha',
24:'Shukla',
25:'Brahma',
26:'Aindra',
27:'Vaidhriti'}

shukla_ekadashi_names={1:'Kamada',
2:'Mohini',
3:'Pandava Nirjala',
4:'Padma/Devashayani',
5:'Putrada/Pavitropana',
6:'Parivartini',
7:'Pashankusha',
8:'Uttana/Prabodhini',
9:'Vaikuntha',
10:'Putrada',
11:'Jaya',
12:'Amalaki',
13:'Padmini'}

krishna_ekadashi_names={1:'Papavimochini',
2:'Varuthini',
3:'Apara',
4:'Yogini',
5:'Kamika',
6:'Aja',
7:'Indira',
8:'Rama',
9:'Utpanna',
10:'Saphala',
11:'Trisprisha',
12:'Vijaya',
13:'Parama'}

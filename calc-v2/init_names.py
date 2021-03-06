#!/usr/bin/python
# -*- coding: utf-8 -*-

ahoratram = {}
adhika = {}
samvatsara = {}
ekadashi = {}
sarva = {}
smartha = {}
vaishnava = {}
pradosham = {}
chaturthi = {}
maha = {}
arambham = {}
navaratri_start = {}
durgashtami = {}
mahanavami = {}
vijayadashami = {}
dipavali = {}
skanda = {}
shashthi = {}

vchaturthi = {}
ananta_chaturdashi = {}
rishi_panchami = {}
ramanavami = {}
shivaratri = {}
janmashtami = {}
chitra_purnima = {}
varalakshmi_vratam = {}
yajur_upakarma = {}
rg_upakarma = {}
sama_upakarma = {}
gayatri_japam = {}
uttarayanam = {}
dakshinayanam = {}
mesha_sankranti = {}
karadayan_nombu = {}
akshaya_tritiya = {}
shankara_jayanti = {}
mahalaya_paksham = {}
hanumat_jayanti = {}
ardra_darshanam = {}
ratha_saptami = {}
goda_jayanti = {}
adi_krittika = {}
phalguni_uttaram = {}
mahalaya_amavasya = {}
uma_maheshvara_vratam = {}
yugadi = {}

chandra_grahanam = {}
surya_grahanam = {}

list_of_festivals = {}
chaturmasya_start = {}
chaturmasya_end = {}

nakshatra_names = {}
masa_names = {}
chandra_masa_names = {}
tithi_names = {}
year_names = {}
karanam_names = {}
yogam_names = {}
shukla_ekadashi_names = {}
krishna_ekadashi_names = {}

ahoratram['deva']= 'अहोरात्रम्'
adhika['deva']= 'अधिक'
samvatsara['deva']= 'संवत्सरः'
ekadashi['deva']= 'एकादशी'
sarva['deva']= 'सर्व'
smartha['deva']= 'स्मार्थ'
vaishnava['deva']= 'वैष्णव'
pradosham['deva']= 'प्रदोष-व्रतम्'
chaturthi['deva']= 'सङ्कटहर-चतुर्थी'
maha['deva']= 'महा'
arambham['deva']= 'आरम्भः'
navaratri_start['deva']= 'नवरात्रि-'+arambham['deva']
durgashtami['deva']= 'दुर्गाष्टमी'
mahanavami['deva']= 'महानवमी/सरस्वती-पूजा'
vijayadashami['deva']= 'विजयदशमी'
dipavali['deva']= 'दीपावली'
skanda['deva']= 'स्कन्द~'
shashthi['deva']= 'षष्ठी-व्रतम्'

vchaturthi['deva']= 'श्रीविनायक-चतुर्थी'
ananta_chaturdashi['deva']= 'अनन्त-चतुर्दशी'
rishi_panchami['deva']= 'ऋषि-पञ्चमी  व्रतम्'
ramanavami['deva']= 'श्रीरामनवमी'
shivaratri['deva']= 'महाशिवरात्रिः'
janmashtami['deva']= 'श्रीकृष्णजन्माष्टमी'
chitra_purnima['deva']= 'चित्रा~पूर्णिमा, गजेन्द्र-मोक्षः'
varalakshmi_vratam['deva']= 'वरलक्ष्मी-व्रतम्'
yajur_upakarma['deva']= 'यजुर्वेद-उपाकर्म'
rg_upakarma['deva']= 'ऋग्वेद-उपाकर्म'
sama_upakarma['deva']= 'सामवेद-उपाकर्म'
gayatri_japam['deva']= 'गायत्री  जपम्'
uttarayanam['deva']= 'मकर~सङ्क्रान्ति/उत्तरायण-पुण्यकालम्'
dakshinayanam['deva']= 'दक्षिणायन-पुण्यकालम्'
mesha_sankranti['deva']= 'मेष~सङ्क्रान्ति'
karadayan_nombu['deva']= 'कारडयान्-नोम्बु'
akshaya_tritiya['deva']= 'अक्षय तृतीया'
shankara_jayanti['deva']= 'शङ्कर-जयन्ती'
mahalaya_paksham['deva']= 'महालय-पक्ष आरम्भः'
hanumat_jayanti['deva']= 'श्री हनूमत् जयन्ती'
ardra_darshanam['deva']= 'आर्द्रा दर्शनम्'
ratha_saptami['deva']= 'रथ-सप्तमी'
goda_jayanti['deva']= 'श्री गोदा जयन्ती'
adi_krittika['deva']= 'आषाढ कृत्तिका'
phalguni_uttaram['deva']= 'फल्गुनी उत्तरम्'
mahalaya_amavasya['deva']= 'महालय-अमावस्या'
uma_maheshvara_vratam['deva']= 'उमा-महेश्वर व्रतम्'
yugadi['deva']= 'युगादि'

chandra_grahanam['deva']= 'चन्द्र-ग्रहणम्'
surya_grahanam['deva']= 'सूर्य-ग्रहणम्'

list_of_festivals['deva']= 'मासान्तर-विशेषाः'
chaturmasya_start['deva']='चातुर्मासस्य आरम्भः'
chaturmasya_end['deva']='चातुर्मासस्य समापनम्'

nakshatra_names['deva']={1:'अश्विनी',
2:'अपभरणी',
3:'कृत्तिका',
4:'रोहिणी',
5:'मृगशीर्ष',
6:'आर्द्रा',
7:'पुनर्वसू',
8:'पुष्य',
9:'आश्रेषा',
10:'मघा',
11:'पूर्वफल्गुनी',
12:'उत्तरफल्गुनी',
13:'हस्त',
14:'चित्रा',
15:'स्वाति',
16:'विशाखा',
17:'अनूराधा',
18:'ज्येष्ठा',
19:'मूला',
20:'पूर्वाषाढा',
21:'उत्तराषाढा',
22:'श्रवण',
23:'श्रविष्ठा',
24:'शतभिषक्',
25:'पूर्वप्रोष्ठपदा',
26:'उत्तरप्रोष्ठपदा',
27:'रेवती'}

masa_names['deva']={1:'मेष',
2:'वृषभ',
3:'मिथुन',
4:'कर्कटक',
5:'सिंह',
6:'कन्या',
7:'तुला',
8:'वृश्चिक',
9:'धनुः',
10:'मकर',
11:'कुम्भ',
12:'मीन'}

chandra_masa_names['deva']={1:'चैत्र',
2:'वैशाख',
3:'ज्यैष्ठ',
4:'आषाढ',
5:'श्रवण',
6:'भाद्रपद',
7:'आश्विन',
8:'कार्तिक',
9:'मार्गशीर्ष',
10:'पौष',
11:'माघ',
12:'फाल्गुन'}

tithi_names['deva']={1:'शुक्ल~प्रथमा',
2:'शुक्ल~द्वितीया',
3:'शुक्ल~तृतीया',
4:'शुक्ल~चतुर्थी',
5:'शुक्ल~पञ्चमी',
6:'शुक्ल~षष्ठी',
7:'शुक्ल~सप्तमी',
8:'शुक्ल~अष्टमी',
9:'शुक्ल~नवमी',
10:'शुक्ल~दशमी',
11:'शुक्ल~एकादशी',
12:'शुक्ल~द्वादशी',
13:'शुक्ल~त्रयोदशी',
14:'शुक्ल~चतुर्दशी',
15:'\\fullmoon~पूर्णिमा',
16:'कृष्ण~प्रथमा',
17:'कृष्ण~द्वितीया',
18:'कृष्ण~तृतीया',
19:'कृष्ण~चतुर्थी',
20:'कृष्ण~पञ्चमी',
21:'कृष्ण~षष्ठी',
22:'कृष्ण~सप्तमी',
23:'कृष्ण~अष्टमी',
24:'कृष्ण~नवमी',
25:'कृष्ण~दशमी',
26:'कृष्ण~एकादशी',
27:'कृष्ण~द्वादशी',
28:'कृष्ण~त्रयोदशी',
29:'कृष्ण~चतुर्दशी',
30:'\\newmoon~अमावस्या'}

year_names['deva']={1:'प्रभव',
2:'विभव',
3:'शुक्ल',
4:'प्रमोद',
5:'प्रजापति',
6:'आङ्गिरस',
7:'श्रीमुख',
8:'भाव',
9:'युव',
10:'धात्री',
11:'ईश्वर',
12:'बहुधान्य',
13:'प्रमाधि',
14:'विक्रम',
15:'वृष',
16:'चित्रभानु',
17:'स्वभानु',
18:'तारण',
19:'पार्थिव',
20:'व्यय',
21:'सर्वजित्',
22:'सर्वधारी',
23:'विरोधी',
24:'विकृति',
25:'खर',
26:'नन्दन',
27:'विजय',
28:'जय',
29:'मन्मथ',
30:'दुर्मुखी',
31:'हेविलम्बी',
32:'विलम्बी',
33:'विकारी',
34:'शार्वरी',
35:'प्लव',
36:'शुभकृत्',
37:'शोभकृत्',
38:'क्रोधी',
39:'विश्वावसु',
40:'पराभव',
41:'प्लवङ्ग',
42:'कीलक',
43:'सौम्य',
44:'साधारण',
45:'विरोधिकृति',
46:'परिधावी',
47:'प्रमादीच',
48:'आनन्द',
49:'राक्षस',
50:'नल',
51:'पिङ्गल',
52:'कलायुक्ति',
53:'सिद्धार्थी',
54:'रौद्र',
55:'दुर्मति',
56:'दुन्दुभि',
57:'रुधिरोद्गारी',
58:'रक्ताक्षी',
59:'क्रोधन',
60:'अक्षय'}

karanam_names['deva']={1:'किंस्तुघ्न',
2:'बव',
3:'बालव',
4:'कौलव',
5:'तैतिल',
6:'गरज',
7:'वणिज',
8:'विष्टि',
9:'बव',
10:'बालव',
11:'कौलव',
12:'तैतिल',
13:'गरज',
14:'वणिज',
15:'विष्टि',
16:'बव',
17:'बालव',
18:'कौलव',
19:'तैतिल',
20:'गरज',
21:'वणिज',
22:'विष्टि',
23:'बव',
24:'बालव',
25:'कौलव',
26:'तैतिल',
27:'गरज',
28:'वणिज',
29:'विष्टि',
30:'बव',
31:'बालव',
32:'कौलव',
33:'तैतिल',
34:'गरज',
35:'वणिज',
36:'विष्टि',
37:'बव',
38:'बालव',
39:'कौलव',
40:'तैतिल',
41:'गरज',
42:'वणिज',
43:'विष्टि',
44:'बव',
45:'बालव',
46:'कौलव',
47:'तैतिल',
48:'गरज',
49:'वणिज',
50:'विष्टि',
51:'बव',
52:'बालव',
53:'कौलव',
54:'तैतिल',
55:'गरज',
56:'वणिज',
57:'विष्टि',
58:'शकुनि',
59:'चतुष्पाद',
60:'नागव'}

yogam_names['deva']={1:'विष्कुम्भ',
2:'प्रीति',
3:'आयुष्मान्',
4:'सौभाग्य',
5:'शोभन',
6:'अतिगण्ड',
7:'सुकर्मा',
8:'धृति',
9:'शूल',
10:'गण्ड',
11:'वृद्धि',
12:'ध्रुव',
13:'व्याघात',
14:'हर्षण',
15:'वज्र',
16:'सिद्धि',
17:'व्यतीपात',
18:'वारीयन',
19:'परिघ',
20:'शिव',
21:'सिद्ध',
22:'साध्य',
23:'शुभ',
24:'शुक्ल',
25:'ब्रह्म',
26:'ऐन्द्र',
27:'वैधृति'}

shukla_ekadashi_names['deva']={1:'कामद',
2:'मोहिनी',
3:'पाण्डव निर्जल',
4:'पद्म/देवशयनी',
5:'पुत्रद/पवित्रोपान',
6:'परिवर्तिनि',
7:'पाशाङ्कुश',
8:'उत्तान/प्रबोधिनी',
9:'वैकुण्ठ',
10:'पुत्रद',
11:'जया',
12:'अमलकी',
13:'पद्मिनी'}

krishna_ekadashi_names['deva']={1:'पापविमोचिनी',
2:'वरुथिनी',
3:'अपरा',
4:'योगिनी',
5:'कामिक',
6:'अज',
7:'इन्दिरा',
8:'रमा',
9:'उत्पन्न',
10:'सफल',
11:'त्रिस्पृश',
12:'विजया',
13:'परमा'}

ahoratram['iast'] = 'ahorātram'
adhika['iast'] = 'adhika'
samvatsara['iast'] = 'saṃvatsaraḥ'
ekadashi['iast'] = 'ekādaśī'
sarva['iast'] = 'sarva'
smartha['iast'] = 'smārtha'
vaishnava['iast'] = 'vaiṣṇava'
pradosham['iast'] = 'pradoṣa-vratam'
chaturthi['iast'] = 'saṅkaṭahara-caturthī'
maha['iast'] = 'mahā'
arambham['iast'] = 'ārambhaḥ'
navaratri_start['iast'] = 'navarātri-'+arambham['iast']
durgashtami['iast'] = 'durgāṣṭamī'
mahanavami['iast'] = 'mahānavamī/sarasvatī-pūjā'
vijayadashami['iast'] = 'vijayadaśamī'
dipavali['iast'] = 'dīpāvalī'
skanda['iast'] = 'skanda~'
shashthi['iast'] = 'ṣaṣṭhī-vratam'

vchaturthi['iast'] = 'śrīvināyaka-caturthī'
ananta_chaturdashi['iast'] = 'ananta-caturdaśī'
rishi_panchami['iast'] = 'ṛṣi-pañcamī  vratam'
ramanavami['iast'] = 'śrīrāmanavamī'
shivaratri['iast'] = 'mahāśivarātriḥ'
janmashtami['iast'] = 'śrīkṛṣṇajanmāṣṭamī'
chitra_purnima['iast'] = 'citrā~pūrṇimā, gajendra-mokṣaḥ'
varalakshmi_vratam['iast'] = 'varalakṣmī-vratam'
yajur_upakarma['iast'] = 'yajurveda-upākarma'
rg_upakarma['iast'] = 'ṛgveda-upākarma'
sama_upakarma['iast'] = 'sāmaveda-upākarma'
gayatri_japam['iast'] = 'gāyatrī  japam'
uttarayanam['iast'] = 'makara~saṅkrānti/uttarāyaṇa-puṇyakālam'
dakshinayanam['iast'] = 'dakṣiṇāyana-puṇyakālam'
mesha_sankranti['iast'] = 'meṣa~saṅkrānti'
karadayan_nombu['iast'] = 'kāraḍayān-nombu'
akshaya_tritiya['iast'] = 'akṣaya tṛtīyā'
shankara_jayanti['iast'] = 'śaṅkara-jayantī'
mahalaya_paksham['iast'] = 'mahālaya-pakṣa ārambhaḥ'
hanumat_jayanti['iast'] = 'śrī hanūmat jayantī'
ardra_darshanam['iast'] = 'ārdrā darśanam'
ratha_saptami['iast'] = 'ratha-saptamī'
goda_jayanti['iast'] = 'śrī godā jayantī'
adi_krittika['iast'] = 'āṣāḍha kṛttikā'
phalguni_uttaram['iast'] = 'phalgunī uttaram'
mahalaya_amavasya['iast'] = 'mahālaya-amāvasyā'
uma_maheshvara_vratam['iast'] = 'umā-maheśvara vratam'
yugadi['iast'] = 'yugādi'

chandra_grahanam['iast'] = 'candra-grahaṇam'
surya_grahanam['iast'] = 'sūrya-grahaṇam'

list_of_festivals['iast'] = 'māsāntara-viśeṣāḥ'
chaturmasya_start['iast'] = 'cāturmāsasya ārambhaḥ'
chaturmasya_end['iast'] = 'cāturmāsasya samāpanam'

nakshatra_names['iast'] = {1:'aśvinī',
2:'apabharaṇī',
3:'kṛttikā',
4:'rohiṇī',
5:'mṛgaśīrṣa',
6:'ārdrā',
7:'punarvasū',
8:'puṣya',
9:'āśreṣā',
10:'maghā',
11:'pūrvaphalgunī',
12:'uttaraphalgunī',
13:'hasta',
14:'citrā',
15:'svāti',
16:'viśākhā',
17:'anūrādhā',
18:'jyeṣṭhā',
19:'mūlā',
20:'pūrvāṣāḍhā',
21:'uttarāṣāḍhā',
22:'śravaṇa',
23:'śraviṣṭhā',
24:'śatabhiṣak',
25:'pūrvaproṣṭhapadā',
26:'uttaraproṣṭhapadā',
27:'revatī'}

masa_names['iast'] = {1:'meṣa',
2:'vṛṣabha',
3:'mithuna',
4:'karkaṭaka',
5:'siṃha',
6:'kanyā',
7:'tulā',
8:'vṛścika',
9:'dhanuḥ',
10:'makara',
11:'kumbha',
12:'mīna'}

chandra_masa_names['iast'] = {1:'caitra',
2:'vaiśākha',
3:'jyaiṣṭha',
4:'āṣāḍha',
5:'śravaṇa',
6:'bhādrapada',
7:'āśvina',
8:'kārtika',
9:'mārgaśīrṣa',
10:'pauṣa',
11:'māgha',
12:'phālguna'}

tithi_names['iast'] = {1:'śukla~prathamā',
2:'śukla~dvitīyā',
3:'śukla~tṛtīyā',
4:'śukla~caturthī',
5:'śukla~pañcamī',
6:'śukla~ṣaṣṭhī',
7:'śukla~saptamī',
8:'śukla~aṣṭamī',
9:'śukla~navamī',
10:'śukla~daśamī',
11:'śukla~ekādaśī',
12:'śukla~dvādaśī',
13:'śukla~trayodaśī',
14:'śukla~caturdaśī',
15:'\\fullmoon~pūrṇimā',
16:'kṛṣṇa~prathamā',
17:'kṛṣṇa~dvitīyā',
18:'kṛṣṇa~tṛtīyā',
19:'kṛṣṇa~caturthī',
20:'kṛṣṇa~pañcamī',
21:'kṛṣṇa~ṣaṣṭhī',
22:'kṛṣṇa~saptamī',
23:'kṛṣṇa~aṣṭamī',
24:'kṛṣṇa~navamī',
25:'kṛṣṇa~daśamī',
26:'kṛṣṇa~ekādaśī',
27:'kṛṣṇa~dvādaśī',
28:'kṛṣṇa~trayodaśī',
29:'kṛṣṇa~caturdaśī',
30:'\\newmoon~amāvasyā'}

year_names['iast'] = {1:'prabhava',
2:'vibhava',
3:'śukla',
4:'pramoda',
5:'prajāpati',
6:'āṅgirasa',
7:'śrīmukha',
8:'bhāva',
9:'yuva',
10:'dhātrī',
11:'īśvara',
12:'bahudhānya',
13:'pramādhi',
14:'vikrama',
15:'vṛṣa',
16:'citrabhānu',
17:'svabhānu',
18:'tāraṇa',
19:'pārthiva',
20:'vyaya',
21:'sarvajit',
22:'sarvadhārī',
23:'virodhī',
24:'vikṛti',
25:'khara',
26:'nandana',
27:'vijaya',
28:'jaya',
29:'manmatha',
30:'durmukhī',
31:'hevilambī',
32:'vilambī',
33:'vikārī',
34:'śārvarī',
35:'plava',
36:'śubhakṛt',
37:'śobhakṛt',
38:'krodhī',
39:'viśvāvasu',
40:'parābhava',
41:'plavaṅga',
42:'kīlaka',
43:'saumya',
44:'sādhāraṇa',
45:'virodhikṛti',
46:'paridhāvī',
47:'pramādīca',
48:'ānanda',
49:'rākṣasa',
50:'nala',
51:'piṅgala',
52:'kalāyukti',
53:'siddhārthī',
54:'raudra',
55:'durmati',
56:'dundubhi',
57:'rudhirodgārī',
58:'raktākṣī',
59:'krodhana',
60:'akṣaya'}

karanam_names['iast'] = {1:'kiṃstughna',
2:'bava',
3:'bālava',
4:'kaulava',
5:'taitila',
6:'garaja',
7:'vaṇija',
8:'viṣṭi',
9:'bava',
10:'bālava',
11:'kaulava',
12:'taitila',
13:'garaja',
14:'vaṇija',
15:'viṣṭi',
16:'bava',
17:'bālava',
18:'kaulava',
19:'taitila',
20:'garaja',
21:'vaṇija',
22:'viṣṭi',
23:'bava',
24:'bālava',
25:'kaulava',
26:'taitila',
27:'garaja',
28:'vaṇija',
29:'viṣṭi',
30:'bava',
31:'bālava',
32:'kaulava',
33:'taitila',
34:'garaja',
35:'vaṇija',
36:'viṣṭi',
37:'bava',
38:'bālava',
39:'kaulava',
40:'taitila',
41:'garaja',
42:'vaṇija',
43:'viṣṭi',
44:'bava',
45:'bālava',
46:'kaulava',
47:'taitila',
48:'garaja',
49:'vaṇija',
50:'viṣṭi',
51:'bava',
52:'bālava',
53:'kaulava',
54:'taitila',
55:'garaja',
56:'vaṇija',
57:'viṣṭi',
58:'śakuni',
59:'catuṣpāda',
60:'nāgava'}

yogam_names['iast'] = {1:'viṣkumbha',
2:'prīti',
3:'āyuṣmān',
4:'saubhāgya',
5:'śobhana',
6:'atigaṇḍa',
7:'sukarmā',
8:'dhṛti',
9:'śūla',
10:'gaṇḍa',
11:'vṛddhi',
12:'dhruva',
13:'vyāghāta',
14:'harṣaṇa',
15:'vajra',
16:'siddhi',
17:'vyatīpāta',
18:'vārīyana',
19:'parigha',
20:'śiva',
21:'siddha',
22:'sādhya',
23:'śubha',
24:'śukla',
25:'brahma',
26:'aindra',
27:'vaidhṛti'}

shukla_ekadashi_names['iast'] = {1:'kāmada',
2:'mohinī',
3:'pāṇḍava nirjala',
4:'padma/devaśayanī',
5:'putrada/pavitropāna',
6:'parivartini',
7:'pāśāṅkuśa',
8:'uttāna/prabodhinī',
9:'vaikuṇṭha',
10:'putrada',
11:'jayā',
12:'amalakī',
13:'padminī'}

krishna_ekadashi_names['iast'] = {1:'pāpavimocinī',
2:'varuthinī',
3:'aparā',
4:'yoginī',
5:'kāmika',
6:'aja',
7:'indirā',
8:'ramā',
9:'utpanna',
10:'saphala',
11:'trispṛśa',
12:'vijayā',
13:'paramā'}

ahoratram['en'] = 'Ahoratram'
adhika['en'] = 'Adhika'
samvatsara['en'] = 'Samvatsara'
ekadashi['en'] = 'Ekadashi'
sarva['en'] = 'Sarva'
smartha['en'] = 'Smartha'
vaishnava['en'] = 'Vaishnava'
pradosham['en'] = 'Pradosha-Vratam'
chaturthi['en'] = 'Sankatahara-Chaturthi'
maha['en'] = 'Maha'
arambham['en'] = 'Arambha'
navaratri_start['en'] = 'Navaratri-'+arambham['en']
durgashtami['en'] = 'Durgashtami'
mahanavami['en'] = 'Mahanavami/Sarasvati-Puja'
vijayadashami['en'] = 'Vijayadashami'
dipavali['en'] = 'Dipavali'
skanda['en'] = 'Skanda '
shashthi['en'] = 'Shashthi-Vratam'

vchaturthi['en'] = 'Shrivinayaka-Chaturthi'
ananta_chaturdashi['en'] = 'Ananta-Chaturdashi'
rishi_panchami['en'] = 'Rishi-Panchami  vratam'
ramanavami['en'] = 'Shriramanavami'
shivaratri['en'] = 'Mahashivaratri'
janmashtami['en'] = 'Shrikrishnajanmashtami'
chitra_purnima['en'] = 'Chitra Purnima, Gajendra-Moksha'
varalakshmi_vratam['en'] = 'Varalakshmi-Vratam'
yajur_upakarma['en'] = 'Yajurveda-Upakarma'
rg_upakarma['en'] = 'Rigveda-Upakarma'
sama_upakarma['en'] = 'Samaveda-Upakarma'
gayatri_japam['en'] = 'Gayatri  japam'
uttarayanam['en'] = 'Makara Sankranti/Uttarayana-Punyakalam'
dakshinayanam['en'] = 'Dakshinayana-Punyakalam'
mesha_sankranti['en'] = 'Mesha Sankranti'
karadayan_nombu['en'] = 'Karadayan-Nombu'
akshaya_tritiya['en'] = 'Akshaya Tritiya'
shankara_jayanti['en'] = 'Shankara-Jayanti'
mahalaya_paksham['en'] = 'Mahalaya-Paksha Arambha'
hanumat_jayanti['en'] = 'Shri Hanumat Jayanti'
ardra_darshanam['en'] = 'Ardra Darshanam'
ratha_saptami['en'] = 'Ratha-Saptami'
goda_jayanti['en'] = 'Shri Goda Jayanti'
adi_krittika['en'] = 'Ashadha Krittika'
phalguni_uttaram['en'] = 'Phalguni Uttaram'
mahalaya_amavasya['en'] = 'Mahalaya-Amavasya'
uma_maheshvara_vratam['en'] = 'Uma-Maheshvara Vratam'
yugadi['en'] = 'Yugadi'

chandra_grahanam['en'] = 'Chandra-Grahanam'
surya_grahanam['en'] = 'Surya-Grahanam'

list_of_festivals['en'] = 'Masantara-Vishesha'
chaturmasya_start['en'] ='Chaturmasasya Arambha'
chaturmasya_end['en'] ='Chaturmasasya Samapanam'

nakshatra_names['en'] ={1:'Ashvini',
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

masa_names['en'] ={1:'Mesha',
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

chandra_masa_names['en'] ={1:'Chaitra',
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

tithi_names['en'] ={1:'Shukla Prathama',
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

year_names['en'] ={1:'Prabhava',
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

karanam_names['en'] ={1:'Kimstughna',
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

yogam_names['en'] ={1:'Vishkumbha',
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

shukla_ekadashi_names['en'] ={1:'Kamada',
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

krishna_ekadashi_names['en'] ={1:'Papavimochini',
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

ahoratram['telugu']= 'అహోరాత్రమ్'
adhika['telugu']= 'అధిక'
samvatsara['telugu']= 'సంవత్సరః'
ekadashi['telugu']= 'ఏకాదశీ'
sarva['telugu']= 'సర్వ'
smartha['telugu']= 'స్మార్థ'
vaishnava['telugu']= 'వైష్ణవ'
pradosham['telugu']= 'ప్రదోష-వ్రతమ్'
chaturthi['telugu']= 'సఙ్కటహర-చతుర్థీ'
maha['telugu']= 'మహా'
arambham['telugu']= 'ఆరమ్భః'
navaratri_start['telugu']= 'నవరాత్రి-'+arambham['telugu']
durgashtami['telugu']= 'దుర్గాష్టమీ'
mahanavami['telugu']= 'మహానవమీ/సరస్వతీ-పూజా'
vijayadashami['telugu']= 'విజయదశమీ'
dipavali['telugu']= 'దీపావలీ'
skanda['telugu']= 'స్కన్ద~'
shashthi['telugu']= 'షష్ఠీ-వ్రతమ్'

vchaturthi['telugu']= 'శ్రీవినాయక-చతుర్థీ'
ananta_chaturdashi['telugu']= 'అనన్త-చతుర్దశీ'
rishi_panchami['telugu']= 'ఋషి-పఞ్చమీ  వ్రతమ్'
ramanavami['telugu']= 'శ్రీరామనవమీ'
shivaratri['telugu']= 'మహాశివరాత్రిః'
janmashtami['telugu']= 'శ్రీకృష్ణజన్మాష్టమీ'
chitra_purnima['telugu']= 'చిత్రా~పూర్ణిమా, గజేన్ద్ర-మోక్షః'
varalakshmi_vratam['telugu']= 'వరలక్ష్మీ-వ్రతమ్'
yajur_upakarma['telugu']= 'యజుర్వేద-ఉపాకర్మ'
rg_upakarma['telugu']= 'ఋగ్వేద-ఉపాకర్మ'
sama_upakarma['telugu']= 'సామవేద-ఉపాకర్మ'
gayatri_japam['telugu']= 'గాయత్రీ  జపమ్'
uttarayanam['telugu']= 'మకర~సఙ్క్రాన్తి/ఉత్తరాయణ-పుణ్యకాలమ్'
dakshinayanam['telugu']= 'దక్షిణాయన-పుణ్యకాలమ్'
mesha_sankranti['telugu']= 'మేష~సఙ్క్రాన్తి'
karadayan_nombu['telugu']= 'కారడయాన్-నోమ్బు'
akshaya_tritiya['telugu']= 'అక్షయ తృతీయా'
shankara_jayanti['telugu']= 'శఙ్కర-జయన్తీ'
mahalaya_paksham['telugu']= 'మహాలయ-పక్ష ఆరమ్భః'
hanumat_jayanti['telugu']= 'శ్రీ హనూమత్ జయన్తీ'
ardra_darshanam['telugu']= 'ఆర్ద్రా దర్శనమ్'
ratha_saptami['telugu']= 'రథ-సప్తమీ'
goda_jayanti['telugu']= 'శ్రీ గోదా జయన్తీ'
adi_krittika['telugu']= 'ఆషాఢ కృత్తికా'
phalguni_uttaram['telugu']= 'ఫల్గునీ ఉత్తరమ్'
mahalaya_amavasya['telugu']= 'మహాలయ-అమావస్యా'
uma_maheshvara_vratam['telugu']= 'ఉమా-మహేశ్వర వ్రతమ్'
yugadi['telugu']= 'యుగాది'

chandra_grahanam['telugu']= 'చన్ద్ర-గ్రహణమ్'
surya_grahanam['telugu']= 'సూర్య-గ్రహణమ్'

list_of_festivals['telugu']= 'మాసాన్తర-విశేషాః'
chaturmasya_start['telugu']='చాతుర్మాసస్య ఆరమ్భః'
chaturmasya_end['telugu']='చాతుర్మాసస్య సమాపనమ్'

nakshatra_names['telugu']={1:'అశ్వినీ',
2:'అపభరణీ',
3:'కృత్తికా',
4:'రోహిణీ',
5:'మృగశీర్ష',
6:'ఆర్ద్రా',
7:'పునర్వసూ',
8:'పుష్య',
9:'ఆశ్రేషా',
10:'మఘా',
11:'పూర్వఫల్గునీ',
12:'ఉత్తరఫల్గునీ',
13:'హస్త',
14:'చిత్రా',
15:'స్వాతి',
16:'విశాఖా',
17:'అనూరాధా',
18:'జ్యేష్ఠా',
19:'మూలా',
20:'పూర్వాషాఢా',
21:'ఉత్తరాషాఢా',
22:'శ్రవణ',
23:'శ్రవిష్ఠా',
24:'శతభిషక్',
25:'పూర్వప్రోష్ఠపదా',
26:'ఉత్తరప్రోష్ఠపదా',
27:'రేవతీ'}

masa_names['telugu']={1:'మేష',
2:'వృషభ',
3:'మిథున',
4:'కర్కటక',
5:'సింహ',
6:'కన్యా',
7:'తులా',
8:'వృశ్చిక',
9:'ధనుః',
10:'మకర',
11:'కుమ్భ',
12:'మీన'}

chandra_masa_names['telugu']={1:'చైత్ర',
2:'వైశాఖ',
3:'జ్యైష్ఠ',
4:'ఆషాఢ',
5:'శ్రవణ',
6:'భాద్రపద',
7:'ఆశ్విన',
8:'కార్తిక',
9:'మార్గశీర్ష',
10:'పౌష',
11:'మాఘ',
12:'ఫాల్గున'}

tithi_names['telugu']={1:'శుక్ల~ప్రథమా',
2:'శుక్ల~ద్వితీయా',
3:'శుక్ల~తృతీయా',
4:'శుక్ల~చతుర్థీ',
5:'శుక్ల~పఞ్చమీ',
6:'శుక్ల~షష్ఠీ',
7:'శుక్ల~సప్తమీ',
8:'శుక్ల~అష్టమీ',
9:'శుక్ల~నవమీ',
10:'శుక్ల~దశమీ',
11:'శుక్ల~ఏకాదశీ',
12:'శుక్ల~ద్వాదశీ',
13:'శుక్ల~త్రయోదశీ',
14:'శుక్ల~చతుర్దశీ',
15:'\\fullmoon~పూర్ణిమా',
16:'కృష్ణ~ప్రథమా',
17:'కృష్ణ~ద్వితీయా',
18:'కృష్ణ~తృతీయా',
19:'కృష్ణ~చతుర్థీ',
20:'కృష్ణ~పఞ్చమీ',
21:'కృష్ణ~షష్ఠీ',
22:'కృష్ణ~సప్తమీ',
23:'కృష్ణ~అష్టమీ',
24:'కృష్ణ~నవమీ',
25:'కృష్ణ~దశమీ',
26:'కృష్ణ~ఏకాదశీ',
27:'కృష్ణ~ద్వాదశీ',
28:'కృష్ణ~త్రయోదశీ',
29:'కృష్ణ~చతుర్దశీ',
30:'\\newmoon~అమావస్యా'}

year_names['telugu']={1:'ప్రభవ',
2:'విభవ',
3:'శుక్ల',
4:'ప్రమోద',
5:'ప్రజాపతి',
6:'ఆఙ్గిరస',
7:'శ్రీముఖ',
8:'భావ',
9:'యువ',
10:'ధాత్రీ',
11:'ఈశ్వర',
12:'బహుధాన్య',
13:'ప్రమాధి',
14:'విక్రమ',
15:'వృష',
16:'చిత్రభాను',
17:'స్వభాను',
18:'తారణ',
19:'పార్థివ',
20:'వ్యయ',
21:'సర్వజిత్',
22:'సర్వధారీ',
23:'విరోధీ',
24:'వికృతి',
25:'ఖర',
26:'నన్దన',
27:'విజయ',
28:'జయ',
29:'మన్మథ',
30:'దుర్ముఖీ',
31:'హేవిలమ్బీ',
32:'విలమ్బీ',
33:'వికారీ',
34:'శార్వరీ',
35:'ప్లవ',
36:'శుభకృత్',
37:'శోభకృత్',
38:'క్రోధీ',
39:'విశ్వావసు',
40:'పరాభవ',
41:'ప్లవఙ్గ',
42:'కీలక',
43:'సౌమ్య',
44:'సాధారణ',
45:'విరోధికృతి',
46:'పరిధావీ',
47:'ప్రమాదీచ',
48:'ఆనన్ద',
49:'రాక్షస',
50:'నల',
51:'పిఙ్గల',
52:'కలాయుక్తి',
53:'సిద్ధార్థీ',
54:'రౌద్ర',
55:'దుర్మతి',
56:'దున్దుభి',
57:'రుధిరోద్గారీ',
58:'రక్తాక్షీ',
59:'క్రోధన',
60:'అక్షయ'}

karanam_names['telugu']={1:'కింస్తుఘ్న',
2:'బవ',
3:'బాలవ',
4:'కౌలవ',
5:'తైతిల',
6:'గరజ',
7:'వణిజ',
8:'విష్టి',
9:'బవ',
10:'బాలవ',
11:'కౌలవ',
12:'తైతిల',
13:'గరజ',
14:'వణిజ',
15:'విష్టి',
16:'బవ',
17:'బాలవ',
18:'కౌలవ',
19:'తైతిల',
20:'గరజ',
21:'వణిజ',
22:'విష్టి',
23:'బవ',
24:'బాలవ',
25:'కౌలవ',
26:'తైతిల',
27:'గరజ',
28:'వణిజ',
29:'విష్టి',
30:'బవ',
31:'బాలవ',
32:'కౌలవ',
33:'తైతిల',
34:'గరజ',
35:'వణిజ',
36:'విష్టి',
37:'బవ',
38:'బాలవ',
39:'కౌలవ',
40:'తైతిల',
41:'గరజ',
42:'వణిజ',
43:'విష్టి',
44:'బవ',
45:'బాలవ',
46:'కౌలవ',
47:'తైతిల',
48:'గరజ',
49:'వణిజ',
50:'విష్టి',
51:'బవ',
52:'బాలవ',
53:'కౌలవ',
54:'తైతిల',
55:'గరజ',
56:'వణిజ',
57:'విష్టి',
58:'శకుని',
59:'చతుష్పాద',
60:'నాగవ'}

yogam_names['telugu']={1:'విష్కుమ్భ',
2:'ప్రీతి',
3:'ఆయుష్మాన్',
4:'సౌభాగ్య',
5:'శోభన',
6:'అతిగణ్డ',
7:'సుకర్మా',
8:'ధృతి',
9:'శూల',
10:'గణ్డ',
11:'వృద్ధి',
12:'ధ్రువ',
13:'వ్యాఘాత',
14:'హర్షణ',
15:'వజ్ర',
16:'సిద్ధి',
17:'వ్యతీపాత',
18:'వారీయన',
19:'పరిఘ',
20:'శివ',
21:'సిద్ధ',
22:'సాధ్య',
23:'శుభ',
24:'శుక్ల',
25:'బ్రహ్మ',
26:'ఐన్ద్ర',
27:'వైధృతి'}

shukla_ekadashi_names['telugu']={1:'కామద',
2:'మోహినీ',
3:'పాణ్డవ నిర్జల',
4:'పద్మ/దేవశయనీ',
5:'పుత్రద/పవిత్రోపాన',
6:'పరివర్తిని',
7:'పాశాఙ్కుశ',
8:'ఉత్తాన/ప్రబోధినీ',
9:'వైకుణ్ఠ',
10:'పుత్రద',
11:'జయా',
12:'అమలకీ',
13:'పద్మినీ'}

krishna_ekadashi_names['telugu']={1:'పాపవిమోచినీ',
2:'వరుథినీ',
3:'అపరా',
4:'యోగినీ',
5:'కామిక',
6:'అజ',
7:'ఇన్దిరా',
8:'రమా',
9:'ఉత్పన్న',
10:'సఫల',
11:'త్రిస్పృశ',
12:'విజయా',
13:'పరమా'}

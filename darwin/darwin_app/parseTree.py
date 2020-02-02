import json

tree = "((Procnias_tricarunculatus:3.930132661,Procnias_nudicollis:3.930132661):6.551067096,(Procnias_averano:5.143764974,Procnias_albus:5.143764974):5.337434783)"
falcon = "(Parula_pitiayumi:1.31779117011956392602,((((((((Falco_fasciinucha:0.14304310424868599272,Falco_sparverius:0.14304310424868599272):0.00332332917359379199,(Falco_vespertinus:0.05694876652450633209,Falco_amurensis:0.05694876652450633209):0.08941766689777347343):0.02850563991299854064,((((((Falco_pelegrinoides:0.00521580614929656027,Falco_peregrinus:0.00521580614929656027):0.04684524646359532196,(Falco_biarmicus:0.02656521002990316904,(((Falco_rusticolus:0.01624686834689305012,Falco_cherrug:0.01624686834689305012):0.00014155231047045461,Falco_jugger:0.01638842065736350120):0.00060243134863295633,Falco_subniger:0.01699085200599646100):0.00957435802390670804):0.02549584258298871059):0.05226558378304647923,(Falco_moluccensis:0.00511479037431338598,Falco_mexicanus:0.00511479037431338598):0.09921184602162497201):0.04380672020433289127,(Falco_ardosiaceus:0.14483868925874779365,(Falco_femoralis:0.12884655485690160726,(Falco_novaeseelandiae:0.09708930636181219154,Falco_dickinsoni:0.09708930636181219154):0.03175724849508936021):0.01599213440184626966):0.00329466734152342221):0.00677213532029413701,(Falco_berigora:0.12837901581085808811,(Falco_chicquera:0.08949332815118828111,Falco_hypoleucos:0.08949332815118828111):0.03888568765966980700):0.02652647610970728861):0.01345687877864621025,(((Falco_longipennis:0.07303684428861210998,(Falco_concolor:0.05265416536902642330,(Falco_eleonorae:0.03172051874480485284,(Falco_subbuteo:0.01903720383388149071,Falco_cuvierii:0.01903720383388149071):0.01268331491092336040):0.02093364662422156006):0.02038267891958569014):0.00931272562045123986,Falco_alopex:0.08234956990906334984):0.05468104868920079659,Falco_deiroleucus:0.13703061859826420887):0.03133175210094744229):0.00650970263606676092):0.02728478032191533967,(Falco_columbarius:0.20076382805350601046,((Falco_naumanni:0.14022438514309498725,(Falco_rupicoloides:0.06570943859424104028,((Falco_cenchroides:0.03059276246639782912,Falco_tinnunculus:0.03059276246639782912):0.02238666007405025124,((Falco_newtoni:0.02627701393602505098,Falco_araea:0.02627701393602505098):0.01276458921777781988,Falco_punctatus:0.03904160315380286739):0.01393781938664520950):0.01273001605379295992):0.07451494654885391922):0.03660302729186785259,(Falco_severus:0.10589551429637389379,(Falco_zoniventris:0.03859510785698407054,Falco_rufigularis:0.03859510785698407054):0.06730040643938978162):0.07093189813858895298):0.02393641561854320879):0.00139302560368767493):0.21427854795499720608,((Microhierax_melanoleucos:0.14627264454769070556,(Microhierax_fringillarius:0.10571812620033610441,((Microhierax_caerulescens:0.00469842793310315098,Microhierax_erythrogenys:0.00469842793310315098):0.08509438959520822243,Microhierax_latifrons:0.08979281752831137775):0.01592530867202469891):0.04055451834735465666):0.21510060294536578751,(Polihierax_insignis:0.05665912188956512968,Polihierax_semitorquatus:0.05665912188956512968):0.30471412560349142584):0.05506215411913434332):0.11699996540379599408,(((Caracara_plancus:0.13605884306738780243,Caracara_cheriway:0.13605884306738780243):0.05299342490671465900,(Ibycter_americanus:0.16860566217525541077,((Daptrius_ater:0.05717464644560042719,(Milvago_chimango:0.00062623514043745447,Milvago_chimachima:0.00062623514043745447):0.05654841130516297804):0.02258731919272256167,((Phalcoboenus_megalopterus:0.02605180323783427149,(Phalcoboenus_albogularis:0.02139039566279385060,Phalcoboenus_australis:0.02139039566279385060):0.00466140757504041395):0.00060456709491889943,Phalcoboenus_carunculatus:0.02665637033275317092):0.05310559530556981794):0.08884369653693238722):0.02044660579884710963):0.23551524765103901138,Spiziapteryx_circumcincta:0.42456751562514138953):0.10886785139084549645):0.20767382970459280500,((((Micrastur_mirandollei:0.16959183635539040735,(Micrastur_buckleyi:0.04097097199144252716,(Micrastur_ruficollis:0.01969115376411528090,Micrastur_mintoni:0.01969115376411528090):0.02127981822732724973):0.12862086436394778999):0.07001937478300221396,(Micrastur_plumbeus:0.08211816405791570739,Micrastur_gilvicollis:0.08211816405791570739):0.15749304708047678902):0.03223336237883001054,Micrastur_semitorquatus:0.27184457351722257634):0.17359489833084049137,Herpetotheres_cachinnans:0.44543947184806298445):0.29566972487251669266):0.46775073942806122407,Tyto_alba:1.20885993614864095669):0.10893123397092299709)"

tree = tree.replace("(", "{")
tree = tree.replace(")", "}")

falcon = falcon.replace("(", "{")
falcon = falcon.replace(")", "}")
species = []

#subtree = "{Procnias_tricarunculatus:3.930132661,Procnias_nudicollis:3.930132661}"
def baseCaseOne(tree):
    comma = tree.index(",")
    firstColon = tree.index(":", 0, comma)
    secondColon = tree.index(":", comma, len(tree) - 1)
    
    print(str(tree[firstColon + 1:comma]) + ":" + tree[secondColon + 1: len(tree) - 1])
    print()
    temp = "{" + tree[firstColon + 1:comma] + ":\"" + tree[1:firstColon] + "\"," + tree[secondColon + 1: len(tree) - 1] + ":\"" + tree[comma + 1:secondColon] + "\"}"
    if tree[firstColon + 1:comma] == tree[secondColon + 1: len(tree) - 1]:
        temp = "{" + tree[firstColon + 1:comma] + ":[\"" + tree[1:firstColon] + "\",\"" + tree[comma + 1:secondColon] + "\"]}"
    species.append(tree[1:firstColon])
    species.append(tree[comma + 1:secondColon])
    return temp


#Procnias_tricarunculatus:3.930132661
def baseCaseZero(tree):
    try:
        colon = tree.index(":")
    except ValueError:
        return "\"" + tree + "\""
    species.append(tree[:colon])
    return tree[colon + 1:] + ":\"" + tree[:colon] + "\""

def find_parens(s):
    toret = {}
    pstack = []
    for i, c in enumerate(s):
        if c == '{':
            pstack.append(i)
        elif c == '}':
            if len(pstack) == 0:
                raise IndexError("No matching closing parens at: " + str(i))
            toret[pstack.pop()] = i
    if len(pstack) > 0:
        raise IndexError("No matching opening parens at: " + str(pstack.pop()))
    return toret

    

def findSmallestDifference(dic):
    keys = list(dic.keys())
    item = keys.pop()
    min = dic[item] - item
    associatedKey = item
    while len(keys) > 0:
        item = keys.pop()
        if dic[item] - item < min:
            min = dic[item] - item
            associatedKey = item
    return associatedKey

def findBiggestDifference(dic):
    keys = list(dic.keys())
    item = keys.pop()
    max = dic[item] - item
    associatedKey = item
    while len(keys) > 0:
        item = keys.pop()
        if dic[item] - item > max:
            max = dic[item] - item
            associatedKey = item
    return associatedKey


#given {{...}:6.531345,{...}:5.01245}
def switchBiggestColons(tree):
    #print("Switching Biggest: " + tree)
    parens = find_parens(tree)
    #print(str(parens))
    if len(parens) is 1:
        return baseCaseOne(tree)
    if len(parens) is 0:
        return baseCaseZero(tree)
    comma = indexOfSignComma(tree, parens)
    #print("Significant Comma: " + str(comma))
    try:
        firstEnd = parens[1]
    except KeyError:
        firstEnd = tree.index(":", 0, comma) - 1
    try:
        secondEnd = parens[comma + 1]
    except KeyError:
        secondEnd = len(tree) - 2
    firstSub = switchBiggestColons(tree[1:firstEnd + 1])
    secondSub = switchBiggestColons(tree[comma + 1:secondEnd + 1])
    temp = "{" + tree[firstEnd + 2:comma] + ":" + firstSub + "," + tree[secondEnd + 2:len(tree) - 1] + ":" + secondSub + "}"
    if tree[firstEnd + 2:comma] == tree[secondEnd + 2:len(tree) - 1]:
        temp = "{" + tree[firstEnd + 2:comma] + ":[" + firstSub + "," + secondSub + "]}"
    return temp


def indexOfSignComma(tree, parens):
    parens.pop(0)
    index = 0
    comma = tree.index(",", index)
    while commaInParens(comma, parens):
        index = index + 1
        comma = tree.index(",", index)
    return comma

def commaInParens(comma, parens):
    for item in parens:
        if comma > item and comma < parens[item]:
            return True
    return False
        
tree = switchBiggestColons(falcon)
tree = tree.replace(",:", ",")
print(tree)
falconTree = {1.31779117011956392602:"Parula_pitiayumi",0.10893123397092299709:{0.46775073942806122407:{0.20767382970459280500:{0.11699996540379599408:{0.21427854795499720608:{0.02728478032191533967:{0.02850563991299854064:{0.00332332917359379199:{0.14304310424868599272:"Falco_fasciinucha",0.1430431042486859927:"Falco_sparverius"},0.08941766689777347343:{0.05694876652450633209:"Falco_vespertinus",0.0569487665245063320:"Falco_amurensis"}},0.00650970263606676092:{0.01345687877864621025:{0.00677213532029413701:{0.04380672020433289127:{0.05226558378304647923:{0.04684524646359532196:{0.00521580614929656027:"Falco_pelegrinoides",0.0052158061492965602:"Falco_peregrinus"},0.02549584258298871059:{0.02656521002990316904:"Falco_biarmicus",0.00957435802390670804:{0.00060243134863295633:{0.00014155231047045461:{0.01624686834689305012:"Falco_rusticolus",0.0162468683468930501:"Falco_cherrug"},0.01638842065736350120:"Falco_jugger"},0.01699085200599646100:"Falco_subniger"}}},0.09921184602162497201:{0.00511479037431338598:"Falco_moluccensis",0.0051147903743133859:"Falco_mexicanus"}},0.00329466734152342221:{0.14483868925874779365:"Falco_ardosiaceus",0.01599213440184626966:{0.12884655485690160726:"Falco_femoralis",0.03175724849508936021:{0.09708930636181219154:"Falco_novaeseelandiae",0.0970893063618121915:"Falco_dickinsoni"}}}},0.02652647610970728861:{0.12837901581085808811:"Falco_berigora",0.03888568765966980700:{0.08949332815118828111:"Falco_chicquera",0.0894933281511882811:"Falco_hypoleucos"}}},0.03133175210094744229:{0.05468104868920079659:{0.00931272562045123986:{0.07303684428861210998:"Falco_longipennis",0.02038267891958569014:{0.05265416536902642330:"Falco_concolor",0.02093364662422156006:{0.03172051874480485284:"Falco_eleonorae",0.01268331491092336040:{0.01903720383388149071:"Falco_subbuteo",0.0190372038338814907:"Falco_cuvierii"}}}},0.08234956990906334984:"Falco_alopex"},0.13703061859826420887:"Falco_deiroleucus"}}},0.00139302560368767493:{0.20076382805350601046:"Falco_columbarius",0.02393641561854320879:{0.03660302729186785259:{0.14022438514309498725:"Falco_naumanni",0.07451494654885391922:{0.06570943859424104028:"Falco_rupicoloides",0.01273001605379295992:{0.02238666007405025124:{0.03059276246639782912:"Falco_cenchroides",0.0305927624663978291:"Falco_tinnunculus"},0.01393781938664520950:{0.01276458921777781988:{0.02627701393602505098:"Falco_newtoni",0.0262770139360250509:"Falco_araea"},0.03904160315380286739:"Falco_punctatus"}}}},0.07093189813858895298:{0.10589551429637389379:"Falco_severus",0.06730040643938978162:{0.03859510785698407054:"Falco_zoniventris",0.0385951078569840705:"Falco_rufigularis"}}}}},0.05506215411913434332:{0.21510060294536578751:{0.14627264454769070556:"Microhierax_melanoleucos",0.04055451834735465666:{0.10571812620033610441:"Microhierax_fringillarius",0.01592530867202469891:{0.08509438959520822243:{0.00469842793310315098:"Microhierax_caerulescens",0.0046984279331031509:"Microhierax_erythrogenys"},0.08979281752831137775:"Microhierax_latifrons"}}},0.30471412560349142584:{0.05665912188956512968:"Polihierax_insignis",0.0566591218895651296:"Polihierax_semitorquatus"}}},0.10886785139084549645:{0.23551524765103901138:{0.05299342490671465900:{0.13605884306738780243:"Caracara_plancus",0.1360588430673878024:"Caracara_cheriway"},0.02044660579884710963:{0.16860566217525541077:"Ibycter_americanus",0.08884369653693238722:{0.02258731919272256167:{0.05717464644560042719:"Daptrius_ater",0.05654841130516297804:{0.00062623514043745447:"Milvago_chimango",0.0006262351404374544:"Milvago_chimachima"}},0.05310559530556981794:{0.00060456709491889943:{0.02605180323783427149:"Phalcoboenus_megalopterus",0.00466140757504041395:{0.02139039566279385060:"Phalcoboenus_albogularis",0.0213903956627938506:"Phalcoboenus_australis"}},0.02665637033275317092:"Phalcoboenus_carunculatus"}}}},0.42456751562514138953:"Spiziapteryx_circumcincta"}},0.29566972487251669266:{0.17359489833084049137:{0.03223336237883001054:{0.07001937478300221396:{0.16959183635539040735:"Micrastur_mirandollei",0.12862086436394778999:{0.04097097199144252716:"Micrastur_buckleyi",0.02127981822732724973:{0.01969115376411528090:"Micrastur_ruficollis",0.0196911537641152809:"Micrastur_mintoni"}}},0.15749304708047678902:{0.08211816405791570739:"Micrastur_plumbeus",0.0821181640579157073:"Micrastur_gilvicollis"}},0.27184457351722257634:"Micrastur_semitorquatus"},0.44543947184806298445:"Herpetotheres_cachinnans"}},1.20885993614864095669:"Tyto_alba"}}

print(species)


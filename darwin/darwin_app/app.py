from flask import Flask, request, make_response
from flask_cors import CORS
from redis import Redis
import helpers, time

redis = Redis(host='redis', port=6379)
app = Flask(__name__)
CORS(app)
tree = {1.31779117011956392602:"Parula_pitiayumi",0.10893123397092299709:{0.46775073942806122407:{0.20767382970459280500:{0.11699996540379599408:{0.21427854795499720608:{0.02728478032191533967:{0.02850563991299854064:{0.00332332917359379199:{0.14304310424868599272:["Falco_fasciinucha","Falco_sparverius"]},0.08941766689777347343:{0.05694876652450633209:["Falco_vespertinus","Falco_amurensis"]}},0.00650970263606676092:{0.01345687877864621025:{0.00677213532029413701:{0.04380672020433289127:{0.05226558378304647923:{0.04684524646359532196:{0.00521580614929656027:["Falco_pelegrinoides","Falco_peregrinus"]},0.02549584258298871059:{0.02656521002990316904:"Falco_biarmicus",0.00957435802390670804:{0.00060243134863295633:{0.00014155231047045461:{0.01624686834689305012:["Falco_rusticolus","Falco_cherrug"]},0.01638842065736350120:"Falco_jugger"},0.01699085200599646100:"Falco_subniger"}}},0.09921184602162497201:{0.00511479037431338598:["Falco_moluccensis","Falco_mexicanus"]}},0.00329466734152342221:{0.14483868925874779365:"Falco_ardosiaceus",0.01599213440184626966:{0.12884655485690160726:"Falco_femoralis",0.03175724849508936021:{0.09708930636181219154:["Falco_novaeseelandiae","Falco_dickinsoni"]}}}},0.02652647610970728861:{0.12837901581085808811:"Falco_berigora",0.03888568765966980700:{0.08949332815118828111:["Falco_chicquera","Falco_hypoleucos"]}}},0.03133175210094744229:{0.05468104868920079659:{0.00931272562045123986:{0.07303684428861210998:"Falco_longipennis",0.02038267891958569014:{0.05265416536902642330:"Falco_concolor",0.02093364662422156006:{0.03172051874480485284:"Falco_eleonorae",0.01268331491092336040:{0.01903720383388149071:["Falco_subbuteo","Falco_cuvierii"]}}}},0.08234956990906334984:"Falco_alopex"},0.13703061859826420887:"Falco_deiroleucus"}}},0.00139302560368767493:{0.20076382805350601046:"Falco_columbarius",0.02393641561854320879:{0.03660302729186785259:{0.14022438514309498725:"Falco_naumanni",0.07451494654885391922:{0.06570943859424104028:"Falco_rupicoloides",0.01273001605379295992:{0.02238666007405025124:{0.03059276246639782912:["Falco_cenchroides","Falco_tinnunculus"]},0.01393781938664520950:{0.01276458921777781988:{0.02627701393602505098:["Falco_newtoni","Falco_araea"]},0.03904160315380286739:"Falco_punctatus"}}}},0.07093189813858895298:{0.10589551429637389379:"Falco_severus",0.06730040643938978162:{0.03859510785698407054:["Falco_zoniventris","Falco_rufigularis"]}}}}},0.05506215411913434332:{0.21510060294536578751:{0.14627264454769070556:"Microhierax_melanoleucos",0.04055451834735465666:{0.10571812620033610441:"Microhierax_fringillarius",0.01592530867202469891:{0.08509438959520822243:{0.00469842793310315098:["Microhierax_caerulescens","Microhierax_erythrogenys"]},0.08979281752831137775:"Microhierax_latifrons"}}},0.30471412560349142584:{0.05665912188956512968:["Polihierax_insignis","Polihierax_semitorquatus"]}}},0.10886785139084549645:{0.23551524765103901138:{0.05299342490671465900:{0.13605884306738780243:["Caracara_plancus","Caracara_cheriway"]},0.02044660579884710963:{0.16860566217525541077:"Ibycter_americanus",0.08884369653693238722:{0.02258731919272256167:{0.05717464644560042719:"Daptrius_ater",0.05654841130516297804:{0.00062623514043745447:["Milvago_chimango","Milvago_chimachima"]}},0.05310559530556981794:{0.00060456709491889943:{0.02605180323783427149:"Phalcoboenus_megalopterus",0.00466140757504041395:{0.02139039566279385060:["Phalcoboenus_albogularis","Phalcoboenus_australis"]}},0.02665637033275317092:"Phalcoboenus_carunculatus"}}}},0.42456751562514138953:"Spiziapteryx_circumcincta"}},0.29566972487251669266:{0.17359489833084049137:{0.03223336237883001054:{0.07001937478300221396:{0.16959183635539040735:"Micrastur_mirandollei",0.12862086436394778999:{0.04097097199144252716:"Micrastur_buckleyi",0.02127981822732724973:{0.01969115376411528090:["Micrastur_ruficollis","Micrastur_mintoni"]}}},0.15749304708047678902:{0.08211816405791570739:["Micrastur_plumbeus","Micrastur_gilvicollis"]}},0.27184457351722257634:"Micrastur_semitorquatus"},0.44543947184806298445:"Herpetotheres_cachinnans"}},1.20885993614864095669:"Tyto_alba"}}
species = ["Parula_pitiayumi", "Falco_sparverius", "Falco_fasciinucha", "Falco_amurensis", "Falco_vespertinus", "Falco_peregrinus", "Falco_pelegrinoides", "Falco_biarmicus", "Falco_cherrug", "Falco_rusticolus", "Falco_jugger", "Falco_subniger", "Falco_mexicanus", "Falco_moluccensis", "Falco_ardosiaceus", "Falco_femoralis", "Falco_dickinsoni", "Falco_novaeseelandiae", "Falco_berigora", "Falco_hypoleucos", "Falco_chicquera", "Falco_longipennis", "Falco_concolor", "Falco_eleonorae", "Falco_cuvierii", "Falco_subbuteo", "Falco_alopex", "Falco_deiroleucus", "Falco_columbarius", "Falco_naumanni", "Falco_rupicoloides", "Falco_tinnunculus", "Falco_cenchroides", "Falco_araea", "Falco_newtoni", "Falco_punctatus", "Falco_severus", "Falco_rufigularis", "Falco_zoniventris", "Microhierax_melanoleucos", "Microhierax_fringillarius", "Microhierax_erythrogenys", "Microhierax_caerulescens", "Microhierax_latifrons", "Polihierax_semitorquatus", "Polihierax_insignis", "Caracara_cheriway", "Caracara_plancus", "Ibycter_americanus", "Daptrius_ater", "Milvago_chimachima", "Milvago_chimango", "Phalcoboenus_megalopterus", "Phalcoboenus_australis", "Phalcoboenus_albogularis", "Phalcoboenus_carunculatus", "Spiziapteryx_circumcincta", "Micrastur_mirandollei", "Micrastur_buckleyi", "Micrastur_mintoni", "Micrastur_ruficollis", "Micrastur_gilvicollis", "Micrastur_plumbeus", "Micrastur_semitorquatus", "Herpetotheres_cachinnans", "Tyto_alba"]

@app.route('/')
def hello_world():
    app.logger.info(str(redis.ping()))
    return 'Welcome to the Beagle!'

@app.route('/darwin/index')
def darwin_index():
    app.logger.info("BEGINNING TO CALCULATE INDEX")
    species = request.headers['species'].decode('utf-8').split(",")
    app.logger.info(str(species))
    removedTree = helpers.treeOfList(species)
    for _ in range(100):
        removedTree = helpers.pareTree(removedTree)
    darwin = helpers.countDarwin(removedTree)
    app.logger.info("DARWIN INDEX:" + str(darwin))
    response = make_response('Darwin Index: ' + str(darwin), 200)
    return response

@app.route('/contains_bird')
def contains_bird():
    givenSpecies = request.headers['species'].decode('utf-8').split(",")
    app.logger.info(str(givenSpecies))
    for bird in givenSpecies:
        if not bird in species:
            response = make_response('Bird not Found.', 400)
            return response
    response = make_response('Found all birds', 200)
    return response

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
import pandas as pd
#import math
from polls.models import PricingDBSite, PricingDBBuilding, PricingDBBuildingSurface, PricingDBZone



def progtest() :


     SurfId = 1  + PricingDBBuildingSurface.objects.last().id
     BuildId = 1 + PricingDBBuilding.objects.last().id 
     ZoneId = 1 + PricingDBZone.objects.last().id
     i = 0
     ExcelDatas = pd.read_excel('BDD_Prix_CFO.xlsx', sheet_name = 'Sites')

     while i < ExcelDatas["Id"].__len__ :
          
          print("go")
          var = 0
          for ms in PricingDBSite.objects.all():
               if ms.name == ExcelDatas["Nom"].iloc[i]:
                    var+=1
          if var < 1:
          
               mysite = PricingDBSite(name = ExcelDatas["Nom"].iloc[i], excel_ref = ExcelDatas["Id"].iloc[i])
               mysite.save()
               mysite.pricingdbbuilding_set.create(name = ExcelDatas["Nom"].iloc[i], excel_ref = ExcelDatas["Id"].iloc[i])
               
               mybuild = mysite.pricingdbbuilding_set.get(pk = BuildId)
               mybuild.save()
               mybuild.pricingdbbuildingsurface_set.create(name = "SUB", value = ExcelDatas["SUB"].iloc[i])
               mysurf = mybuild.pricingdbbuildingsurface_set.get(pk = SurfId)
               mysurf.save()
               mybuild.pricingdbzone_set.create(name = ExcelDatas["Classification"].iloc[i], classification = ExcelDatas["Classification"].iloc[i], category = ExcelDatas["Categorie"].iloc[i], type = ExcelDatas["Type"].iloc[i])
               myzone = mybuild.pricingdbzone_set.get(pk = ZoneId)
               myzone.save
               SurfId +=1
               ZoneId+=1
               BuildId+=1
               if type(ExcelDatas["Classification2"].iloc[i]) == str :
                    mybuild.pricingdbzone_set.create(name = ExcelDatas["Classification2"].iloc[i], classification = ExcelDatas["Classification2"].iloc[i], category = ExcelDatas["Categorie2"].iloc[i], type = ExcelDatas["Type2"].iloc[i])
                    myzone2 = mybuild.pricingdbzone_set.get(pk = ZoneId)
                    myzone2.save
                    ZoneId+=1
               print(i)
          i+=1
     print("Fin")






from polls.models import PricingDBSite, PricingDBBuilding, PricingDBBuildingSurface, PricingDBZone, PrincingDBProjectPrimInfos, PrincingDBProjectSubPricing, PrincingDBProjectSubPricingContainedBuilding, PrincingDBProjectSubPricingContainedZone, PrincingDBProjectSubPricingTrade, PrincingDBProjectSubPricingSubTrade, PrincingDBProjectSubPricingSubTradeCompanyOffer




def remplirjusquauxCompagnies(mytrade, mysubtrade):

     #MProjectId = 1  + PrincingDBProjectPrimInfos.objects.last().id
     #ProjectId = 1 + PrincingDBProjectSubPricing.objects.last().id 
     from .my_functions import de_batiments_a_companies
     #from .my_functions import printtest
     ExcelDatas2 = pd.read_excel('BDD_Prix_CFO.xlsx', sheet_name = 'SousProjets')

     for mysite in PricingDBSite.objects.all():
          var = 0
          for mp in PrincingDBProjectPrimInfos.objects.all():
               if mp.name == mysite.name :
                    var+=1
          if var < 0.9 :
               m_project = mysite.princingdbprojectpriminfos_set.create(name = mysite.name)
               #printtest(mysite.princingdbprojectpriminfos_set.get(name = mysite.name).name)
               #m_project =  mysite.princingdbprojectpriminfos_set.get(pk = MProjectId)
               #MProjectId+=1 
               m_project.save()
          else:
               m_project = mysite.princingdbprojectpriminfos_set.get(name = mysite.name)
          var2 = 0
          for p in m_project.princingdbprojectsubpricing_set.all():
               i = 0
               while i < ExcelDatas2["Id"].__len__() :
                    if float(ExcelDatas2["ParentId"].iloc[i]) == float(p.project.site.excel_ref):
                         var2+=1
                    i+=1
          
          if var2 < 0.9:
               ii = 0
               while ii < ExcelDatas2["Id"].__len__() :
                    if float(mysite.excel_ref) == float(ExcelDatas2["ParentId"].iloc[ii]):
                         myproject = m_project.princingdbprojectsubpricing_set.create(name = ExcelDatas2["Nom"].iloc[ii]) #, considered_surface = )
                         #myproject = m_project.princingdbprojectsubpricing_set.get(pk = ProjectId)
                         #ProjectId+=1
                         myproject.save()
                         de_batiments_a_companies(mysite, myproject, mytrade, mysubtrade)
                         
                    ii+=1
          else:
               #print("var2")
               #print(var2)
               iii = 0
               while iii < ExcelDatas2["Id"].__len__() :
                    
                    if float(mysite.excel_ref) == float(ExcelDatas2["ParentId"].iloc[iii]):
                        #printtest(iii)
                        for pr in m_project.princingdbprojectsubpricing_set.all():
                             #printtest(iii)
                             #printtest(pr.name)
                             if pr.name != ExcelDatas2["Nom"].iloc[iii]:
                                   
                                   myproject = m_project.princingdbprojectsubpricing_set.create(name = ExcelDatas2["Nom"].iloc[iii]) #, considered_surface = )
                                   #myproject = m_project.princingdbprojectsubpricing_set.get(pk = ProjectId)
                                   #ProjectId+=1
                                   myproject.save()
                                   
                                   de_batiments_a_companies(mysite, myproject, mytrade, mysubtrade)
                    iii+=1
     #print("salut")




def de_batiments_a_companies(mysite, myproject, mytrade, mysubtrade):
        #print("coucou")
        #print(myproject.id)
        #ContBuildId = 1 + PrincingDBProjectSubPricingContainedBuilding.objects.last().id
        #ContZoneId = 1 + PrincingDBProjectSubPricingContainedZone.objects.last().id
        #TradeId = 1 + PrincingDBProjectSubPricingTrade.objects.last().id
        #SubTradeId = 1 + PrincingDBProjectSubPricingSubTrade.objects.last().id
        #CompanyId = 1 + PrincingDBProjectSubPricingSubTradeCompanyOffer.objects.last().id
     
        ExcelDatas1 = pd.read_excel('BDD_Prix_CFO.xlsx', sheet_name = 'Entreprises')
        surftot = 0
        for building in mysite.pricingdbbuilding_set.all():
             contbuild = myproject.princingdbprojectsubpricingcontainedbuilding_set.create(building_name = building.name)
             #contbuild = myproject.princingdbprojectsubpricingcontainedbuilding_set.get(pk = ContBuildId)
             #ContBuildId+=1
             contbuild.save()
             for zone in building.pricingdbzone_set.all():
                  contzone = contbuild.princingdbprojectsubpricingcontainedzone_set.create(zone_name = zone.name)
                  #contzone = contbuild.princingdbprojectsubpricingcontainedzone_set.get(pk = ContZoneId)
                  #ContZoneId+=1
                  contzone.save()
             for surface in building.pricingdbbuildingsurface_set.filter(name="SUB"):
                  surftot = surftot + surface.value
        myproject.considered_surface = surftot
        myproject.save()
        thetrade = myproject.princingdbprojectsubpricingtrade_set.create(name = mytrade)
        #thetrade = myproject.princingdbprojectsubpricingtrade_set.get(pk = TradeId)
        #TradeId +=1
        thetrade.save()
        thesubtrade = thetrade.princingdbprojectsubpricingsubtrade_set.create(name = mysubtrade)
        #thesubtrade = thetrade.princingdbprojectsubpricingsubtrade_set.get(pk = SubTradeId)
        #SubTradeId +=1
        thesubtrade.save()
        i = 0
        while i < ExcelDatas1["Id"].__len__() :
          if float(mysite.excel_ref) == float(ExcelDatas1["Id"].iloc[i]):
               company = thesubtrade.princingdbprojectsubpricingsubtradecompanyoffer_set.create(name = ExcelDatas1["Entreprise"].iloc[i])
               #company = thesubtrade.princingdbprojectsubpricingsubtradecompanyoffer_set.get(pk = CompanyId)
               #CompanyId+=1
               company.save()
          i+=1
   

def printtest(kl):
     print("voila mon test")
     print(kl)


def groupes(trade, subtrade):
     postes = pd.read_excel('BDD_Prix_CFO.xlsx', sheet_name = 'postesditri')
     mes_groupes = pd.read_excel('BDD_Prix_CFO.xlsx', sheet_name = subtrade)

     
     for c in PrincingDBProjectSubPricingSubTradeCompanyOffer.objects.all():
          i = 0
          num = 1
          while i < mes_groupes["id"].__len__() :
               
               if float(c.excel_p_ref) == float(mes_groupes["parentID"].iloc[i]):
                    if c.name == mes_groupes["prestat"].iloc[i]:
                         gr = c.princingdbprojectsubpricingsubsubtradegroup_set.create(name = str(c.name) +" groupe : "+str(num), group_price = mes_groupes["Prix"].iloc[i], excel_ref= mes_groupes["id"].iloc[i])
                         gr.save()
                         num+=1
                         for k in [1,2,3,4,5,6,7,8,9]:
                              if mes_groupes[k].iloc[i] == "oui":
                                   poste = gr.princingdbprojectsubpricingsubsubtrade_set.create(name = postes["Postes"].iloc[k-1])
                                   poste.save()
               i+=1
from .models import PrincingDBProjectSubPricingSubSubTradeGroup, PrincingDBProjectPriceDetail
def sousdetail():
     details = pd.read_excel('BDD_Prix_CFO.xlsx', sheet_name = 'SousDetailDistri')
     i=0
     while i  < details["id"].__len__() :
          for gr in PrincingDBProjectSubPricingSubSubTradeGroup.objects.all():
               if float(gr.excel_ref) == float(details["parentID"].iloc[i]):
                    detail = gr.princingdbprojectpricedetail_set.create(name = details["Travaux"].iloc[i], measure_unity = details["unite"].iloc[i], unity_price = details["pu"].iloc[i], quantity = details["qt"].iloc[i], price = details["Prix"].iloc[i],)
                    detail.save
          i+=1

def bigclear():
     for d in PrincingDBProjectPriceDetail.objects.all():
          d.delete


def sql_to_json_P1(parents,childs):
     from .models import PricingDBSite
     import re
     import pandas as pd
     import json
     
     mychildinfos = {}

     mychilds = []
     parentchilds = []
     parentsAndChilds=[]
     parentInfolist = pd.DataFrame(parents._meta.fields)
     childInfolist = pd.DataFrame(childs._meta.fields)
     #print(len(childInfolist[0]))
     parentstable = re.sub("'>","",re.sub("<class 'polls.models.","",str(parents)))
     childstable = re.sub("'>","",re.sub("<class 'polls.models.","",str(childs)))
     nb_de_parents=0
     for myParent1 in parents.objects.all():
          parentsAndChilds.append({id : myParent1.id})
          print("nom du site :"+str(myParent1.name))
          print(getattr(myParent1,re.sub("polls."+parentstable+".","",str(parentInfolist[0][1]))))
          if myParent1.name == getattr(myParent1,re.sub("polls."+parentstable+".","",str(parentInfolist[0][1]))):
               print("oui!!!!")
               parentsAndChilds[nb_de_parents].update({"name":  getattr(myParent1,re.sub("polls."+parentstable+".","",str(parentInfolist[0][1])))})
          if len(parentInfolist[0]) > 1:
               for k in range(2, len(parentInfolist[0])):
                    if "xcel" not in str(parentInfolist[0][k]):
                         

                         parentsAndChilds[nb_de_parents].update({re.sub("polls."+parentstable+".","",str(parentInfolist[0][k])):  getattr(myParent1,re.sub("polls."+parentstable+".","",str(parentInfolist[0][k])))})
                         
                         #print("voilà le nouveau parametre :" + str(re.sub("polls."+parentstable+".","",str(parentInfolist[0][k])))+" est egal à : "+ str(getattr(myParent1,re.sub("polls."+parentstable+".","",str(parentInfolist[0][k])))))
                         
          nb_de_parents+=1

     #print("nb_de_parents est egal à")
     #print(nb_de_parents)
    
     for myParent in parentsAndChilds:
          parentchilds.clear()
          for mychild in childs.objects.all():

        
               if getattr(mychild,re.sub("polls."+childstable+".","",str(childInfolist[0][1]))).id != None and  myParent["id"] != None and float(myParent["id"]) == float(getattr(mychild,re.sub("polls."+childstable+".","",str(childInfolist[0][1]))).id):




                    
                    if len(childInfolist[0]) > 1 :
                
                
                
                         for j in range(2, len(childInfolist[0])):
                              if "xcel" not in str(childInfolist[0][j]):
                                
                                #print("coucou")


                                   mychildinfos[re.sub("polls."+childstable+".","",str(childInfolist[0][j]))] = getattr(mychild,re.sub("polls."+childstable+".","",str(childInfolist[0][j])))

                #print(getattr(mychild,re.sub("polls."+childstable+".","",str(childInfolist[0][2]))))
                #mychilds.append({"parentrefind": myindex})
                    parentchilds.append(mychildinfos.copy())
                #mychilds[-1]["datas"] = mychildinfos
                #print(mychildinfos)
          #myParent[str(childs)] = parentchilds.copy()
          for ii in  range(0,nb_de_parents):
               if parentsAndChilds[ii]["id"] == myParent["id"]:
                    parentsAndChilds[ii].update({str(childs) : parentchilds.copy()})


     #with open("second.json",'w') as fi:
        #json.dump(parentsAndChilds, fi, indent=4)


    

     myjson = json.dumps(parentsAndChilds)     
     #parsed = json.loads(myjson)

     # print(json.dumps(parsed, indent=4))
     #print("a ce stade on est à /n")
     #print(myjson)
     return myjson





    


def mergetwinsjsons(json1,json2):
     import json
     list1 = json.loads(json1)
     list2 = json.loads(json2)
     listf = []
     for l in range(0,len(list1)):
        listf.append(list1[l])
        for kk,vv in list2[l].items():
            if type(vv) == list:
                    #on verifie qu'elle n'est pas dejà présente
                    ver=False
                    for k, v in listf[l].items():
                        if k == kk:
                            ver=True
                    if ver == False:
                        listf[l][kk] = vv
     myjson = json.dumps(listf)     
     #parsed = json.loads(myjson)
     #with open("third.json",'w') as fi:
          #json.dump(parsed, fi, indent=4)
     return myjson







def mergesuccessingjsons(json1,json2):
     import json
     listp = json.loads(json1)
     listc = json.loads(json2)
     listf = []
     for l1 in range(0,len(listp)):
          listf.append(listp[l1])
          for k,v in listp[l1].items():
               if type(v) == list:
                 #   print("ma liste vaut :" + str(v))
                    if len(v) != 0:
                          for lv1 in range (0,len(v)):
                                if len(listc)!=0:
                                      for l2 in range (0,len(listc)):
                                            if listc[l2]["id"] == v[lv1]["id"]:
                                                  for kk, vv in listc[l2].items():
                                                        if type(vv) == list:
                                                              if len(vv)!=0:
                                                                    listf[l1][k][lv1].update({kk : vv})
     myjson = json.dumps(listf)     
     #parsed = json.loads(myjson)
     #with open("fourth.json",'w') as fi:
          #json.dump(parsed, fi, indent=4)
     return myjson

from polls.my_functionsMAJ import sql_to_json_P1, mergesuccessingjsons, mergetwinsjsons
import re
import pandas as pd
import json
from polls.models import PricingDBSite, PricingDBBuilding, PricingDBBuildingSurface, PricingDBZone, PrincingDBProjectPrimInfos, PrincingDBProjectSubPricing, PrincingDBProjectSubPricingContainedBuilding, PrincingDBProjectSubPricingContainedZone, PrincingDBProjectSubPricingTrade, PrincingDBProjectSubPricingSubTrade, PrincingDBProjectSubPricingSubTradeCompanyOffer, PrincingDBProjectSubPricingSubSubTradeGroup, PrincingDBProjectSubPricingSubSubTrade, PrincingDBProjectPriceDetail, PricingDBZoneSurface, PricingDBSiteSurface, PricingDBZoneSurface




def finaljson():


     dot = {7 : PricingDBSite, "bis6" : PricingDBBuilding, "bissubbis6" : PricingDBBuildingSurface, "subbis6" : PricingDBZone, 6 : PrincingDBProjectPrimInfos, 5 : PrincingDBProjectSubPricing, "bis4" : PrincingDBProjectSubPricingContainedBuilding, "subbis4" : PrincingDBProjectSubPricingContainedZone, 4 : PrincingDBProjectSubPricingTrade, 3 : PrincingDBProjectSubPricingSubTrade, 2 : PrincingDBProjectSubPricingSubTradeCompanyOffer, 1 : PrincingDBProjectSubPricingSubSubTradeGroup, "bis0" : PrincingDBProjectSubPricingSubSubTrade, 0 : PrincingDBProjectPriceDetail, "subsubbis6" : PricingDBZoneSurface, "ter6" : PricingDBSiteSurface}

     doj ={}

     for k in range(0,8):
          if dot[k].objects.count() == 0:
               dot[k].objects.create()
     for kk in ["bis0","bis4","subbis4","bis6","subbis6","bissubbis6","subsubbis6"]:
          if dot[kk].objects.count() == 0:
               dot[kk].objects.create()


     for i in reversed(range(1,8)):
          
          doj[i] = sql_to_json_P1(dot[i],dot[i-1])

   #  print("pour i est egal à : 1 , json 1 de base c'est ")
    # print(doj[1])
    

##########################################
########################################
#c'est la qu'il faut que je m'assurer que les Twin ont exactement le meme nombre de ligne dans le même order


     doj["b1"] = sql_to_json_P1(dot[1],dot["bis0"])#OK
     doj["4poursucc"]=sql_to_json_P1(dot["bis4"],dot["subbis4"])#OK
     doj["5prebis"]=sql_to_json_P1(dot[5],dot["bis4"])#OK
     doj["b5"] = mergesuccessingjsons(doj["5prebis"],doj["4poursucc"])#OK

     #print("ma premiere succession : Doj4 pour succ est egal à ")
     #print(doj["4poursucc"])
     #print("ma premiere succession : Doj5 preis qui vient de 5 et bis 4")
     #print(doj["5prebis"])
     #print("avec la cle de bis 4 qui vaut ")
    # print(dot["bis4"].objects.last().project.id)
    # print("RESULT ")
     #print(doj["b5"])


     doj["6poursucc"]=sql_to_json_P1(dot["subbis6"],dot["subsubbis6"])#OK
     doj["6prebis1"]=sql_to_json_P1(dot["bis6"],dot["subbis6"])#OK
     doj["6bis1"] = mergesuccessingjsons(doj["6prebis1"],doj["6poursucc"])#OK
     doj["6bis2"]=sql_to_json_P1(dot["bis6"],dot["bissubbis6"])#OK
     doj["6bisT"] = mergetwinsjsons(doj["6bis1"],doj["6bis2"])#OK


     
     doj["7prebis1"]=sql_to_json_P1(dot[7],dot["bis6"])#OK
     doj["7bis1"] = mergesuccessingjsons(doj["7prebis1"],doj["6bisT"])#OK

     doj["7bis2"]=sql_to_json_P1(dot[7],dot["ter6"])#OK
     doj["b7"] = mergetwinsjsons(doj["7bis1"],doj["7bis2"])#OK

     for ind in [1,5,7]:
          list1 = doj[ind]
          list2 = doj["b"+str(ind)]
          doj["new"+str(ind)] = mergetwinsjsons(list1, list2)


     for ii in [1,5,7]:
               
               doj[ii] = doj["new"+str(ii)]

     for j in range(1,7):
          if j == 1:
               listp = doj[j+1]
               listc = doj[j]
               doj["fin"+str(j)] = mergesuccessingjsons(listp,listc)
               #print(doj["fin"+str(j)])
          elif j > 0.99 :
               listp = doj[j+1]
               listc = doj["fin"+str(j-1)]
               doj["fin"+str(j)] = mergesuccessingjsons(listp,listc)
               #print("à j égal à : "+str(j))
               #print(doj["fin"+str(j)])
     myjson = doj["fin6"]
     parsed = json.loads(myjson)
     with open("finalV2.json",'w') as fi:
          json.dump(parsed, fi, indent=4)
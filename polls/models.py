from django.db import models
import datetime
from django.utils import timezone
# Create your models here.

#model pour la DB de pricing



SurfaceType = models.TextChoices("SurfaceType","SHAB SHON SDP SUB SUN SuperSTRUnknownType CoveredParking InfraSTRUnknownType TotalExtern GreenAera ExternalParking")


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    
    #on défini ci dessous ce qu'on veut que ça renvoie par définition si on appel un objetc de cette table
    #sinon ca me renvoie l'id par défaut
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
    
class Response(models.Model):
    
    text = models.CharField(max_length=200)
    
    def __str__(self):
        return self.id

class PricingDBSite(models.Model):
    name = models.CharField(max_length=200)
    excel_ref = models.CharField(max_length=200,default="")
    def __str__(self):
        return self.name

class PricingDBSiteSurface(models.Model):
    site = models.ForeignKey(PricingDBSite, on_delete=models.CASCADE,default = 1)
    name = models.CharField(max_length=200,choices=SurfaceType,default="") 
    #Il faudra que je change ça pour un "textChoice"
    value = models.FloatField(default=0.0)
    def __str__(self):
        return self.name

class PricingDBBuilding(models.Model):
    site = models.ForeignKey(PricingDBSite, on_delete=models.CASCADE,default = 1)
    name = models.CharField(max_length=200,default="")
    construction_date = models.CharField(max_length=200,default='XXX')
    excel_ref = models.CharField(max_length=200,default="")
    def __str__(self):
        return self.name


class PricingDBBuildingSurface(models.Model):
    building = models.ForeignKey(PricingDBBuilding, on_delete=models.CASCADE,default = 1)
    name = models.CharField(max_length=200,default="") 
    #Il faudra que je change ça pour un "textChoice"
    value = models.FloatField(default=0.0)
    def __str__(self):
        return self.name
    
class PricingDBZone(models.Model):
    building = models.ForeignKey(PricingDBBuilding, on_delete=models.CASCADE,default = 1)
    name = models.CharField(max_length=200,default="")
    classification = models.CharField(max_length=200,default="") 
    #Il faudra que je change ça pour un "textChoice"
    type = models.CharField(max_length=200, default="")
    #Il faudra que je change ça pour un "textChoice"
    category = models.IntegerField(default="0") 
    #Il faudra que je change ça pour un "IntegerChoice"
    excel_ref = models.CharField(max_length=20,default="")
    def __str__(self):
        return self.name




class PricingDBZoneSurface(models.Model):
    zone = models.ForeignKey(PricingDBZone, on_delete=models.CASCADE)
    name = models.CharField(max_length=200,choices=SurfaceType,default="") 
    #Il faudra que je change ça pour un "textChoice"
    value = models.FloatField(default=0.0)
    def __str__(self):
        return self.name
#****************************************************************************************************************
class PrincingDBProjectPrimInfos(models.Model):
    site = models.ForeignKey(PricingDBSite, on_delete=models.CASCADE,default = 1)
    name = models.CharField(max_length=200,default="")
    project_date = models.CharField(max_length=200, default='XXX')
    def __str__(self):
        return self.name
    

class PrincingDBProjectSubPricing(models.Model):
    project = models.ForeignKey(PrincingDBProjectPrimInfos, on_delete=models.CASCADE,default = 1)
    name = models.CharField(max_length=200,default="")
    considered_surface = models.FloatField(default=0.0)
    def __str__(self):
        return self.name

class PrincingDBProjectSubPricingContainedBuilding(models.Model):
    project = models.ForeignKey(PrincingDBProjectSubPricing, on_delete=models.CASCADE,default = 1)
    building_id = models.IntegerField(default=0)
    #Il faudra que je change ça pour un "IntegerChoice"
    building_name = models.CharField(max_length=200,default="")
    #Il faudra que je change ça pour un "textChoice"
    def __str__(self):
        return self.building_name
    
class PrincingDBProjectSubPricingContainedZone(models.Model):
    building = models.ForeignKey(PrincingDBProjectSubPricingContainedBuilding, on_delete=models.CASCADE,default = 1)
    zone_id = models.IntegerField(default=0)
    #Il faudra que je change ça pour un "IntegerChoice"
    zone_name = models.CharField(max_length=200,default="")
    #Il faudra que je change ça pour un "textChoice"
    def __str__(self):
        return self.zone_name
    
class PrincingDBProjectSubPricingTrade(models.Model):
    project = models.ForeignKey(PrincingDBProjectSubPricing, on_delete=models.CASCADE,default = 1)
    name = models.CharField(max_length=200,default="")
    #Il faudra que je change ça pour un "textChoice"
    used_index_name = models.CharField(max_length=200,default="")
    index_value_at_project_date  =  models.FloatField(default=0.0)
    def __str__(self):
        return self.name


class PrincingDBProjectSubPricingSubTrade(models.Model):
    trade = models.ForeignKey(PrincingDBProjectSubPricingTrade, on_delete=models.CASCADE,default = 1)
    name = models.CharField(max_length=200,default="")
    #Il faudra que je change ça pour un "textChoice"
    def __str__(self):
        return self.name


class PrincingDBProjectSubPricingSubTradeCompanyOffer(models.Model):
    sub_trade = models.ForeignKey(PrincingDBProjectSubPricingSubTrade, on_delete=models.CASCADE,default = 1)
    name = models.CharField(max_length=200)
    company_offer_sub_trade_price =  models.FloatField(default=0.0)
    
    excel_p_ref = models.CharField(max_length=200,default="")
    def __str__(self):
        return self.name

class PrincingDBProjectSubPricingSubSubTradeGroup(models.Model):
    company = models.ForeignKey(PrincingDBProjectSubPricingSubTradeCompanyOffer, on_delete=models.CASCADE,default = 1)
    name = models.CharField(max_length=200)
    group_price =  models.FloatField(default=0.0)
    excel_ref = models.CharField(max_length=200,default="")
    excel_p_ref = models.CharField(max_length=200,default="")
    company_ref = models.CharField(max_length=200,default="")
    def __str__(self):
        return self.name

class PrincingDBProjectSubPricingSubSubTrade(models.Model):
    group = models.ForeignKey(PrincingDBProjectSubPricingSubSubTradeGroup, on_delete=models.CASCADE,default = 1)
    name = models.CharField(max_length=200,default="")
    #Il faudra que je change ça pour un "textChoice"
    def __str__(self):
        return self.name
    
class PrincingDBProjectPriceDetail(models.Model):
    group = models.ForeignKey(PrincingDBProjectSubPricingSubSubTradeGroup, on_delete=models.CASCADE,default = 1)
    name = models.CharField(max_length=200)
    measure_unity = models.CharField(max_length=200)
    unity_price =  models.FloatField(default=0.0)
    quantity =  models.FloatField(default=0.0)
    price =  models.FloatField(default=0.0)
    def __str__(self):
        return self.name





#****************************************************************************************************************#****************************************************************************************************************
#****************************************************************************************************************
#****************************************************************************************************************
#****************************************************************************************************************
#****************************************************************************************************************


#model pour les projets de chiffrage

class POPDBSite(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    

class POPDBSiteSurface(models.Model):
    site = models.ForeignKey(POPDBSite, on_delete=models.CASCADE,default = 1)
    name = models.CharField(max_length=200,choices=SurfaceType)  
    #Il faudra que je change ça pour un "textChoice"
    value = models.FloatField(default=0.0)
    def __str__(self):
        return self.name


class POPDBBuilding(models.Model):
    site = models.ForeignKey(POPDBSite, on_delete=models.CASCADE,default = 1)
    name = models.CharField(max_length=200)
    construction_date = models.CharField(max_length=200,default='XXX')
    def __str__(self):
        return self.name


class POPDBBuildingSurface(models.Model):
    building = models.ForeignKey(POPDBBuilding, on_delete=models.CASCADE,default = 1)
    name = models.CharField(max_length=200,choices=SurfaceType) 
    value = models.FloatField(default=0.0)
    def __str__(self):
        return self.name

class POPDBZone(models.Model):
    building = models.ForeignKey(POPDBBuilding, on_delete=models.CASCADE,default = 1)
    name = models.CharField(max_length=200)
    classification = models.CharField(max_length=200) 
    #Il faudra que je change ça pour un "textChoice"
    type = models.CharField(max_length=200, default="")
    #Il faudra que je change ça pour un "textChoice"
    category = models.IntegerField(default="0") 
    #Il faudra que je change ça pour un "IntegerChoice"

    def __str__(self):
        return self.name




class POPDBZoneSurface(models.Model):
    zone = models.ForeignKey(POPDBZone, on_delete=models.CASCADE,default = 1)
    name = models.CharField(max_length=200,choices=SurfaceType) 
    value = models.FloatField(default=0.0)
    def __str__(self):
        return self.name


#****************************************************************************************************************
#****************************************************************************************************************


class POPDBProjectPrimInfos(models.Model):
    site = models.ForeignKey(POPDBSite, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    
    project_date = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class POPDBProjectSubPricing(models.Model):
    project = models.ForeignKey(POPDBProjectPrimInfos, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    considered_surface = models.FloatField(default=0.0)
    chosen_trade = models.CharField(max_length=200)
    #Il faudra que je change ça pour un "IntegerChoice"
   #**************************         Calculs         ************************************
    used_index_name = models.CharField(max_length=200)
    index_value_at_pricing_rroject_date  =  models.FloatField(default=0.0)

    chosen_sub_trade = models.CharField(max_length=200)

  #**************************         Calculs         ************************************
    calculated_coeficient =  models.FloatField(default=0.0)
    def __str__(self):
        return self.name


class POPDBProjectSubPricingContainedBuilding(models.Model):
    project_sub_project = models.ForeignKey(POPDBProjectSubPricing, on_delete=models.CASCADE)
    building_id = models.IntegerField(default=0)
    #Il faudra que je change ça pour un "IntegerChoice"
    building_name = models.CharField(max_length=200)
    #Il faudra que je change ça pour un "textChoice"
    def __str__(self):
        return self.building_name


class POPDBProjectSubPricingContainedZone(models.Model):
    building = models.ForeignKey(POPDBProjectSubPricingContainedBuilding, on_delete=models.CASCADE)
    zone_id = models.IntegerField(default=0)
    #Il faudra que je change ça pour un "IntegerChoice"
    zone_name = models.CharField(max_length=200)
    #Il faudra que je change ça pour un "textChoice"
    def __str__(self):
        return self.zone_name


class POPDBAvailableSusSubTradeGroup(models.Model):
    project_sub_project = models.ForeignKey(POPDBProjectSubPricing, on_delete=models.CASCADE)
    group_name = models.CharField(max_length=200)
    validation = models.BooleanField()
    def __str__(self):
        return self.groupe_name

class POPDBContainedSubSubTradeInAvailableGroup(models.Model):
    group = models.ForeignKey(POPDBAvailableSusSubTradeGroup, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    #Il faudra que je change ça pour un "textChoice"
    def __str__(self):
        return self.name
    
class POPDBChosenSusSubTradeGroup(models.Model):
    project_sub_project = models.ForeignKey(POPDBProjectSubPricing, on_delete=models.CASCADE)
    group_name = models.CharField(max_length=200)
    def __str__(self):
        return self.group_name

class POPDBContainedSubSubTradeInChosenGroup(models.Model):
    group = models.ForeignKey(POPDBChosenSusSubTradeGroup, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    #Il faudra que je change ça pour un "textChoice"
    def __str__(self):
        return self.name
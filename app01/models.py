from django.db import models


# Create your models here.

class VesVoyageInfo(models.Model):
    Vessel = models.CharField(max_length=32, unique=True, primary_key=True)
    ImpVoy = models.CharField(max_length=32, null=False)
    ExpVoy = models.CharField(max_length=32, null=False)
    VesType = models.CharField(max_length=12, null=False)
    PlaBerThgTim = models.DateTimeField(auto_now_add=True, null=True)  # 计划靠泊
    PlaUnbThgTim = models.DateTimeField(auto_now_add=True, null=True)  # 计划离泊
    ReaBerThgTim = models.DateTimeField(auto_now_add=True, null=True)  # 实际靠泊
    ActUnbTim = models.DateTimeField(auto_now_add=True, null=True)  # 实际离泊
    PlaBerThgPos = models.IntegerField(null=True)
    ActBerPos = models.IntegerField(null=True)
    BerThgDir = models.CharField(max_length=4, null=True)
    VesDrauMax = models.FloatField(null=True)
    PlaClosCustTim = models.DateTimeField(auto_now_add=True, null=True)
    ClosCustTim = models.DateTimeField(auto_now_add=True, null=True)
    OpAssSign = models.CharField(max_length=12, null=True)
    EntPlanMakSig = models.CharField(max_length=32, null=True)
    TaskFiniSig = models.BooleanField()
    UnBSta = models.NullBooleanField()
    # PlaLoaGPCtnFotNum
    # PlaLoaEmpCtnFotNum
    # PlaLoaDraCtnFotNum
    # PlaLoaGPCtnFotFivNum
    # PlaLoaEmpCtnFotFivNum
    # PlaLoaDraCtnFotFivNum


class VesStruc(models.Model):
    VesName = models.CharField(max_length=6, null=False,primary_key=True,default="SMU01")
    VesLeng = models.IntegerField(null=True)
    VesWidth = models.IntegerField(null=True)
    # VesFrLeng = models.IntegerField(null=True)
    TweBayNum = models.IntegerField(null=True)
    FotBayNum = models.IntegerField(null=True)
    FotBayCom = models.CharField(max_length=32, null=True)
    EngRomPos = models.IntegerField(null=True)
    EngRomWid = models.IntegerField(null=True, default=60)

    DeckHeg = models.IntegerField(null=True)
    DeckWidMax = models.IntegerField(null=True)
    CabHeg = models.IntegerField(null=True)
    CabWidMax = models.IntegerField(null=True)

    # MidBayDeaWit = models.BooleanField(default=False)
    # RefCtnCap = models.FloatField(null=True)
    # VesEntBerSpd = models.CharField(max_length=18, null=True)
    # VesBerSpd = models.CharField(max_length=18, null=True)
    # HigCtnCap = models.FloatField(null=True)
    # CapCtnFotFiv = models.FloatField(null=True)
    # VesEmpGrvHeg = models.CharField(max_length=10, null=True)
    # VesAtt = models.CharField(max_length=10, null=True)
    # LoadWeigth = models.IntegerField(null=True)
    # DeckCapWegt = models.IntegerField(null=True)
    # CabCap = models.IntegerField(null=True)
    # DanCtnAlw = models.BooleanField(default=False)

class BayStruc(models.Model):
    VesName = models.CharField(max_length=12)
    BayNo = models.CharField(max_length=6)
    BaySiz = models.CharField(max_length=6, null=True)
    BayCom = models.CharField(max_length=6, null=True)
    DeckHeg = models.IntegerField(null=True)
    DeckWidMax = models.IntegerField(null=True)
    CabHeg = models.IntegerField(null=True)
    CabWidMax = models.IntegerField(null=True)
    HatCovKind = models.CharField(max_length=60, null=True,verbose_name="舱盖板")
    HatCovSiz = models.IntegerField(null=True)
    BayX = models.IntegerField(null=True)
    BayY = models.IntegerField(null=True)
    class Meta:
        unique_together = ("VesName","BayNo")


class BayInfo(models.Model):
    VesName = models.CharField(max_length=12)
    BayId = models.CharField(max_length=12)


# class VesBayStruc(models.Model):
#     VesName = models.CharField(max_length=12)
#     BayNo = models.CharField(max_length=6)
#     BaySiz = models.CharField(max_length=6, null=True)
#     BayCom = models.CharField(max_length=6, null=True)
#     DeckHeg = models.IntegerField(null=True)
#     DeckWidMax = models.IntegerField(null=True)
#     CabHeg = models.IntegerField(null=True)
#     CabWidMax = models.IntegerField(null=True)
#     HatCovKind = models.CharField(max_length=6, null=True)
#     HatCovSiz = models.IntegerField(null=True)
#     BayX = models.IntegerField(null=True)
#     BayY = models.IntegerField(null=True)
#     class Meta:
#         unique_together = ("VesName","BayNo")


class BayTierStruc(models.Model):
    VesType = models.CharField(max_length=6, null=False)
    BayNo = models.CharField(max_length=6, null=False)
    TireNo = models.CharField(max_length=6, null=False)
    DeckCagSig = models.BooleanField()
    BayWid = models.IntegerField(null=True)
    BayHigh = models.IntegerField(null=True)
    CellSpeSig = models.CharField(max_length=6, null=True)
    RefSig = models.CharField(max_length=6, null=True)


class VesImpSto(models.Model):
    Vessel = models.CharField(max_length=32, unique=True, primary_key=True)
    Voyage = models.CharField(max_length=20, unique=True)
    VesCellNo = models.CharField(max_length=20, null=True)
    ColNo = models.IntegerField(null=True)
    DeckCagSig = models.CharField(max_length=20, null=True)
    CtnNo = models.CharField(max_length=20, null=True)
    CtnTyp = models.CharField(max_length=20, null=True)
    Size = models.CharField(max_length=20, null=True)
    Status = models.CharField(max_length=20, null=True)
    CtnWegt = models.IntegerField(null=True)
    Owner = models.CharField(max_length=20, null=True)
    GForce = models.CharField(max_length=20, null=True)
    StaPort = models.CharField(max_length=20, null=True)
    UnloadPort = models.CharField(max_length=20, null=True)
    DesPort = models.CharField(max_length=20, null=True)
    StrPickAwayCtn = models.CharField(max_length=20, null=True)
    CtnOpeSta = models.CharField(max_length=20, null=True)
    PlaCtnCel = models.CharField(max_length=20, null=True)


class VesExpSto(models.Model):
    Vessel = models.CharField(max_length=32, unique=True, primary_key=True)
    Voyage = models.CharField(max_length=20, unique=True)
    VesCellNo = models.CharField(max_length=20, null=True)
    ColNo = models.IntegerField(null=True)
    DeckCagSig = models.CharField(max_length=20, null=True)
    CtnNo = models.CharField(max_length=20, null=True)
    CtnTyp = models.CharField(max_length=20, null=True)
    Size = models.CharField(max_length=20, null=True)
    Status = models.CharField(max_length=20, null=True)
    CtnWegt = models.IntegerField(null=True)
    GForce = models.CharField(max_length=20, null=True)
    StaPort = models.CharField(max_length=20, null=True)
    UnloadPort = models.CharField(max_length=20, null=True)
    DesPort = models.CharField(max_length=20, null=True)
    CtnOpeSta = models.CharField(max_length=20, null=True)
    PlaCtnCel = models.CharField(max_length=20, null=True)
    YardCel = models.CharField(max_length=20, null=True)

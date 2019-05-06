from django.shortcuts import render, redirect, HttpResponse
from app01 import models
from django.http import JsonResponse
import json

# Create your views here.

def vessel(request):
    return render(request, "vessel.html")

import time
def vessel3(request):

    if request.method == "POST":
        bayNum = request.POST.get("bayNum")
        vesLeng = request.POST.get("vesLeng")
        engRomMar = request.POST.get("engRom")
        vesName = request.POST.get("vesName")
        engRomWid = request.POST.get("engRomWid")

        bayNum = int(bayNum)
        engRomMar = int(engRomMar)
        engRomWid = int(engRomWid)
        marLeft = 30
        maxLeft = marLeft + 100
        TwBay = []
        marlist = []
        for i in range(1, bayNum * 2, 2):
            if maxLeft <= engRomMar:
                TwBay.append(i)
                marlist.append(marLeft)
                marLeft += 40
                maxLeft = marlist[len(marlist) - 1]

            elif engRomMar + engRomWid > maxLeft > engRomMar:
                marLeft += engRomWid
                TwBay.append(i)
                marlist.append(marLeft)
                marLeft += 40
                maxLeft = marlist[len(marlist) - 1]

            else:
                TwBay.append(i)
                marlist.append(marLeft)
                marLeft += 40

        bayDic = dict(zip(TwBay, marlist))
        engRomMar = engRomMar + 110
        t = time.time()

    return render(request,'vessel3.html',locals())

def vessel2(request):

    return render(request, "vessel2.html")

def part_bay(request):
    return render(request, "part_bay.html")

def bookCont(request):
    VesName = request.POST.get("VesName")
    bayNo = request.POST.get("BayNo")
    ves_obj = models.VesStruc.objects.get(VesName=VesName)
    edit_obj = models.BayStruc.objects.get(BayNo=bayNo,VesName=VesName)

    DeckWidMax = request.POST.get("rowNum")
    DeckHeg = request.POST.get("tierNum_up")
    CabHeg = request.POST.get("tierNum_down")

    DeckWidMax = int(DeckWidMax)
    DeckHeg = int(DeckHeg)
    CabHeg = int(CabHeg)

    ves_obj.DeckWidMax = DeckWidMax
    ves_obj.DeckHeg = DeckHeg
    ves_obj.CabHeg = CabHeg
    ves_obj.save()

    edit_obj.DeckWidMax = DeckWidMax
    edit_obj.DeckHeg = DeckHeg
    edit_obj.CabHeg = CabHeg
    edit_obj.save()

    if request.method == "POST":
        rowNum = request.POST.get("rowNum")
        rowNum = int(rowNum)

        tierNum_up = request.POST.get("tierNum_up")
        tierNum_up = int(tierNum_up)

        tierMax_up = tierNum_up * 2 + 80
        tierNum_down = request.POST.get("tierNum_down")
        tierNum_down = int(tierNum_down)

        tierMax_down = tierNum_down * 2
        rowList = []
        tierList = []
        htmls = ""
        htmls2 = ""

        # 层
        for i in range(tierMax_up, 81, -2):
            tierList.append(str(i))

        for j in range(tierMax_down, 1, -2):
            if j < 10:
                j = "0" + str(j)
                tierList.append(j)
            else:
                tierList.append(str(j))

        if rowNum % 2 == 0:
            rowStart = rowNum
            for i in range(rowStart, 1, -2):
                if i < 10:
                    i = "0" + str(i)
                    rowList.append((i))
                else:
                    rowList.append(str(i))

            for j in range(1, rowStart, 2):
                if j < 10:
                    j = "0" + str(j)
                    rowList.append(j)
                else:
                    rowList.append(str(j))

        else:
            rowStart = rowNum
            for i in range(rowStart - 1, -1, -2):
                if i < 10:
                    i = "0" + str(i)
                    rowList.append(i)
                else:
                    rowList.append(str(i))
            for j in range(1, rowStart, 2):
                if j < 10:
                    j = "0" + str(j)
                    rowList.append(j)
                else:
                    rowList.append(str(j))

        for tier in tierList:
            if tier == '82':
                htmls += "<div id='t82'><tr style='border-bottom:0px solid red'><td style='width:20px'>{}</td>".format(tier)
                htmls2 += "<div id='t82'><tr style='border-bottom:0px solid red'><td style='width:20px'>{}</td>".format(tier)
                for row in rowList:
                    # if tier == '82':
                    htmls += "<td style='width:10px;border-bottom:0px solid red' class='active item'  row_id={} tier_id={}></td></div>".format(
                    # htmls += "<td style='width:10px;border-bottom:3px solid red' class='active item'  row_id={} tier_id={}></td>".format(
                        row,tier)
                    htmls2 += "<td style='width:10px;border-bottom:0px solid red' class='another_active item'  row_id={} tier_id={}></td>".format(
                        row,tier)
                    # htmls += "<td class='active item'  row_id={} tier_id={}><button style='width:auto;height: auto' class='btn btn-info'></button></td>".format(tier,row)
                htmls += "</tr></div>"
                htmls2 += "</tr></div>"
            else:
                htmls += "<tr><td style='border:0px;width:20px'>{}</td>".format(tier)
                htmls2 += "<tr><td style='border:0px;width:20px'>{}</td>".format(tier)
                for row in rowList:

                    htmls += "<td style='width:10px' class='active item' row_id={} tier_id={}></td>".format(row,tier)
                    htmls2 += "<td style='width:10px' class='another_active item' row_id={} tier_id={}></td>".format(row,tier)
                    # htmls += "<td class='active item'  row_id={} tier_id={}><button style='width:auto;height: auto' class='btn btn-info'></button></td>".format(tier,row)
                htmls += "</tr>"
                htmls2 += "</tr>"

        bayList=[]
        for i in rowList:
            for j in tierList:
                row_tier = str(bayNo)+str(i)+str(j)
                bayList.append(row_tier)

        bayList = json.dumps(bayList)

    bay = bayNo
    if len(bay)<2:
        bay = bay.slice[1:2]
        bay = int(bay)
    else:
        bay=int(bay)

    if bay % 2 == 0:
         return render(request, "part_bay4.html", locals())
    else:
         return render(request, "part_bay3.html", locals())


def bay(request):
    print("bay" * 6)
    # if request.method == "POST":
    vesLen = request.POST.get("vesLen")
    post_data = json.loads(request.POST.get("post_data"))
    print(post_data)
    print(vesLen)
    return HttpResponse("666")

import pymysql

def createVes(request):
    veslen = request.POST.get("vesLen")
    engRomWid = request.POST.get("engRomWid")
    # print(veslen)
    engRomPos = request.POST.get("engRomPos")
    vesName = request.POST.get("vesName")
    engRomPos = int(engRomPos)
    engRomPos -= 110
    # print(engRomPos)
    # bayNum = request.POST.get("bayNum")
    FotBayNum = request.POST.get("FotBayNum")
    TweBayNum = request.POST.get("TweBayNum")
    twBayList = json.loads(request.POST.get("twBayList"))
    foBayList = json.loads(request.POST.get("foBayList"))
    FotBayCom = request.POST.get("FotBayCom")
    VesWidth = 400

    models.VesStruc.objects.create(VesName=vesName,VesLeng=veslen, EngRomWid=engRomWid,EngRomPos=engRomPos,
                                   VesWidth=VesWidth,TweBayNum=TweBayNum,FotBayNum=FotBayNum,
                                   FotBayCom=FotBayCom)

    for t in twBayList:
        if len(t)<2:
            t = "0"+t
            models.BayStruc.objects.update_or_create(VesName=vesName,BayNo=t,BaySiz=20)
        else:
            t = t
            models.BayStruc.objects.update_or_create(VesName=vesName,BayNo=t,BaySiz=20)
        # models.BayStruc.objects.create(BayNo=t)
        # bayList.append(t)
    for f in foBayList:
        if len(f)<2:
            f = "0"+f
            models.BayStruc.objects.create(VesName=vesName,BayNo=f,BaySiz=40)
        else:
            f = f
            models.BayStruc.objects.create(VesName=vesName,BayNo=f,BaySiz=40)
        # models.BayStruc.objects.create(BayNo = f)

    return render(request, "part_bay2.html", locals())


def createBay(request):

    bayList = json.loads(request.POST.get("bayList"))
    vesName = request.POST.get("vesName")
    engRoomNum = request.POST.get("engRoomNum")
    engRoomList = json.loads(request.POST.get("engRoomList"))
    bayNo = json.loads(request.POST.get("bay"))
    bayNo = str(bayNo)
    if len(bayNo) == 1:
        bayNo = "0"+str(bayNo)
    print(bayNo)
    engRoom = str(engRoomNum)
    engRoom += ''.join(engRoomList)
    engRoom = str(engRoom)
    print(engRoom)
    for i in bayList:
            models.BayInfo.objects.update_or_create(VesName=vesName,BayId=str(i))

    bay_obj = models.BayStruc.objects.get(VesName = vesName,BayNo = bayNo)
    bay_obj.HatCovKind = engRoom
    bay_obj.save()
    return HttpResponse("666")


def Ves(request):

    # conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='', db='ConTerminalDB')
    # cursor = conn.cursor()
    # new_id = cursor.execute('SELECT MAX(id) FROM app01_VesStruc')
    # # new_id = cursor.lastrowid
    # # print("数据库" * 7)
    # # print(new_id)
    # # new_id = 152
    # obj = models.VesStruc.objects.filter(id = new_id).first()
    # vesLen = obj.VesLeng


    return render(request,'conVes.html',locals())

def part_bay2(request):
    vesObj = models.VesStruc.objects.all()

    # bay=["01","03","05"]
    return render(request, "part_bay2.html",{"vesObj":vesObj,"bayNo":bayNo})

def bayNo(request):

    name = request.POST.get("VesName")
    vessel = str(name)
    # print(vessel)
    bayNo = []
    # bayObj = models.BayStruc.objects.filter(VesName='2')
    bayObj = models.BayStruc.objects.filter(VesName=vessel)
    # bayObj = models.BayStruc.objects.all()
    for bay in bayObj:
        bayNo.append(bay.BayNo)
    # return render(request,"part_bay2.html",locals())
    return JsonResponse(bayNo,safe=False)


def check_vesName(request):
    if request.method == "POST":
        id = request.POST.get("id")
        # 去数据库中查询用户名是否已经被注册
        ret = models.VesStruc.objects.filter(VesName=id)
        if ret:
            # 用户名已经存在
            msg = "该船舶名称已经存在！"
        else:
            msg = "该船舶名称可用"

        return HttpResponse(msg)



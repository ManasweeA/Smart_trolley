from django.shortcuts import render, redirect
from .models import *
import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar

pro = []

def home(request):
    return render(request,'home.html',{})


def list1(request):
	global pro
	billdata = bill.objects.all()
	for i in billdata:
		i.price = int(i.price)
	context = {'billdata':billdata}
	return render(request,'list.html',context)

def scanner(request):
		global pro
		context = {}
		l=[]
		cap = cv2.VideoCapture(0)
		font = cv2.FONT_HERSHEY_PLAIN

		while True:
			_, frame = cap.read()


			decodedObjects = pyzbar.decode(frame)
			for obj in decodedObjects:
			    #print("Data ->", obj.data)
			    cv2.putText(frame, str(obj.data), (50, 50), font, 2,
				                (255, 0, 0), 3)
			    a=str(obj.data)         
			    l.append(a)          
				    
			cv2.imshow("SCAN HERE", frame)

			key = cv2.waitKey(1)
			if cv2.waitKey(20) & 0xFF == ord('q'):
			    cap.release()
			    break
		cv2.destroyAllWindows()
		#print("Scanned : ",l)
		product_list = []
		for i in l:
			product = str(i)
			temp = len(i)
			product = product[2:temp-1]
			product = product.replace(" ", "")
			if product not in product_list:
			    product_list.append(product)
				
		print("Product list : ",product_list)
		pro = product_list
			
			
		xyz = inv.objects.all()
		temp = []
		maintemp = []
		for i in xyz:
			temp = []
			tid = i.id
			temp.append(tid)
			tname = i.name
			tname = tname.replace(" ","")
			temp.append(tname)
			tprice = i.price
			temp.append(tprice)
			maintemp.append(temp)
		print(maintemp)
		search_ids = []
		for i in pro:
			for j in range(len(maintemp)):
			    if i == maintemp[j][1]:
			        search_id = maintemp[j][0]
			        search_ids.append(search_id)
		print(search_ids)

		for i in search_ids:
			c = inv.objects.filter(id=i)
			if((len(c))>0):
			    b = c[0]
			    print("--------------------------")
			    print(b.name)
			    print(b.price)
			    lnum = bill.objects.all()
			    lennum = len(lnum)
			    num = "num" + str(lennum+1)
			    obj = bill(pid=b.id,name=b.name,price=b.price,num=num)
			    obj.save()
		return redirect('list')

    
def bill1(request):

    context = {}
    total = 0
    L = []
    if request.method=="POST":
        data = request.POST
        for i in range(len(data)-1):
            num = 'num' + str(i+1)
            obj = bill.objects.filter(num=num)
            q = int(obj[0].price) * int(data[num])
            d = {'name':obj[0].name,'price':obj[0].price, 'quant':data[num], 'price':q}
            L.append(d)
            total = total + q
        print(total)
        print(L)
        b = bill.objects.all()
        context = {'billdata':L, 'total':total}
    return render(request, 'bill.html', context)





def exit(request):
    global pro
    bill.objects.all().delete()
    pro = []
    return render(request,'exit.html',{})

def location(request):
    return render(request,'location.html',{})

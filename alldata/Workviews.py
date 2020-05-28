from django.shortcuts import render,HttpResponse, redirect
from .storework import Worksubmit
# Create your views here.
def work(request):
    if request.method=='POST' and 'submit2' in request.POST:
        id=request.POST.get('unique')
        fromhour=request.POST.get('from')
        leader=request.POST.get('leader')
        mentor=request.POST.get('mentor')
        member=request.POST.get('member')
        description=request.POST.get('description')
        tohour=request.POST.get('to')
        print('html work id:',id)
        print('html from hour:' ,fromhour)
        print('html leader:' ,leader)
        print('html mentor:' ,mentor)
        print('html member:' ,member)
        print('html dscription:' ,description)
        print('html tohour:' ,tohour)
        print('submitted')
        if id != "":
            user=Worksubmit()
            user.uniqueID=id
            user.work_from=fromhour
            user.Team_Leader=leader
            user.Mentor=mentor
            user.Member_Name=member
            user.Work_Description=description
            user.work_to=tohour
            user.save()
        else:
            print('Field is null')
        # return redirect('/')
    #return redirect('/')
    return render(request,'Work.html')

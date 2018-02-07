
import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
import time,random,sys,json,codecs,threading,glob,re,os,subprocess

satpam = LINETCR.LINE() # Login Pake Akun Kicker Kalian
#satpam.login(token="token anda")#ganti dgn token kalian
satpam.login(token="EpWYYMjmEWUba52UlKA1.8nezDhK7HGW9hVtLK4qvGq.4AyYmATuAvCztvMdCZ5xnyhRST1FUx3coUoPztOJtEw=")
satpam.loginResult()

cl = LINETCR.LINE() #Luffy
#cl.login(token="token anda")#ganti dgn token kalian
cl.login(token="EpWYYMjmEWUba52UlKA1.8nezDhK7HGW9hVtLK4qvGq.4AyYmATuAvCztvMdCZ5xnyhRST1FUx3coUoPztOJtEw=")
cl.loginResult()

ki = LINETCR.LINE() #Zorro
#ki.login(token="token anda")#ganti dgn token kalian
ki.login(token="EpWYYMjmEWUba52UlKA1.8nezDhK7HGW9hVtLK4qvGq.4AyYmATuAvCztvMdCZ5xnyhRST1FUx3coUoPztOJtEw=")
ki.loginResult()

kk = LINETCR.LINE() #Sanji
#kk.login(token="token anda")#ganti dgn token kalian
kk.login(token="EpWYYMjmEWUba52UlKA1.8nezDhK7HGW9hVtLK4qvGq.4AyYmATuAvCztvMdCZ5xnyhRST1FUx3coUoPztOJtEw=")
kk.loginResult()

kc = LINETCR.LINE() #Ussop
#kc.login(token="token anda")#ganti dgn token kalian
kc.login(token="

print "login success Boss"
reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage =""" ^[One Piece Bot]^
OWNER •Eehun•
http://line.me/ti/p/~sarehun

Command bot for owner :
======================
> Set/Status
> Help
> Admin menu
> Gn (ganti nama grup)
> kick mid (kick + mid target)
> Invite mid (Invite + mid target)
> Admin add @ (tambah admin + tag kontak)
> Admin remove @ (hapus admin + tag kontak)
> Adminlist/adminlist (list admin)
> Allbio: ... (bikin status di bio bot)
> Myname:...
> Cancel (membatalkan undangan)
> Buka qr 
> Tutup qr
> Info Group (info grup tsb)
> Message change: ... 
> /invitemeto: ... (/invitemeto: id group)
> Kuy/One piece/Join OP (Bot masuk group)owner/creator
> Kuya/Koplak OP (bot masuk group)bot
> Koplak join (bot masuk room)
> Bye op/Kabur all/Kaboor all/One piece left (klr dari room)
> Kabur OP(klr Room)
> Bot like (semua bot ngelike status akun utama)
> Like temen (semua bot ngelike status temen)
> Kill ..(kick banned)
> Ready op (ratakan)
> Nk .. (kick tag member)
> LG (list group)
> Bot out/Op bye (klr dari semua group)


> Add on/off
> Comment on/off
> Jam on
> Change clock
> Jam Update

[ command di atas hanya utk owner bot => Ehun


Command bot for admin :
=======================
> Admin menu
> Help
> Keyword
> Spam: ...
> Bot? (cek kontak bot)
> Me
> My mid (cek mid kita sendiri)
> Mid Bot (cek mid bot)
> Cctv (ngeset Reader)
> Ciduk (ngecek yg ngintip) 
> Tag all/Tagall (tag semua member)
> Blacklist @ 
> Banned @
> Mid @
> Unban @
> Up/up/Up Chat/Up chat/up chat/Upchat/upchat (naik chat spam)
> GBc ... (ngeBC ke semua group yg ada bot trsbt)
> Absen/Absen bot/Absen dulu/Respon
> Speed/Sp
> Ban
> Unban
> Creator
> Banlist
> Cek ban
> Kill ban
> Clear

******************"""

keyword =""" ^[One Piece Bot]^
bot chat :
==========
> Wkwkwk/Wkwk/Wk
> Hehehe/Hehe/He
> Galau
> Galau
> You
> Hadeuh
> Please
> Haaa
> Lol
> Hmmm/Hmm/Hm
> Welcome
> #welcome
> Woy/woy/Woi/bot/Bot

keywordiseng :
===============
> Apakah [sebutkan kata yg anda mau]
> Berapa besar cinta [sebutkan kata yg anda mau]
> Adakah [sebutkan kata yg anda mau]
> Cakepkah [sebutkan kata yg anda mau]
> Siapakah cewek [sebutkan kata yg anda mau]
> Siapakah cowok [sebutkan kata yg anda mau]
******************#"""

Setgroup =""" 
    [Admin Menu]
==============
||[Protect QR]
||- Qr on/off
||[Protect Join]
||- Join on/off
||[Mid Via Contact]
||- Contact on/off
||-[Cancel Invited]
||- Cancel all
==============
   ONE PIECE BOT
==============#"""
KAC=[cl,ki,kk,kc,ks,ka,kb,ko,ke,ku]
mid = cl.getProfile().mid #Luffy
Amid = ki.getProfile().mid #Zorro
Bmid = kk.getProfile().mid #Sanji
Cmid = kc.getProfile().mid #Ussop
Dmid = ks.getProfile().mid #Chooper
Emid = ka.getProfile().mid #Franky
Fmid = kb.getProfile().mid #Brook
Gmid = ko.getProfile().mid #Nami
Hmid = ke.getProfile().mid #Robin
Imid = ku.getProfile().mid #Rebecca
Smid = satpam.getProfile().mid #Akun Utama
mid1 = k1.getProfile().mid #Backup

Bots=[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Smid,mid1]
admin=["ub3808de9f7df35f57fb366d157f9790a"]
owner=["ub3808de9f7df35f57fb366d157f9790a"]
wait = {
    'contact':False,
    'autoJoin':True,
    'autoCancel':{"on":True,"members":1},
    'leaveRoom':True,
    'timeline':True,
    'autoAdd':True,
    'message':"""тerima Kasih Sudah Menambahkan Aku Jadi Teman
≫ Aku Ga Jawab PM Karna aq Cuma Bot Protect ≪
≫ ONE PIECE BOT PROTECT ≪

Ready:

≫ bot protect ≪
≫ SelfBot ≪


ṡȗƿƿȏяṭєԀ ɞʏ:
  
☆ FS3I FAMILY ☆
☆ ONE PIECE BOT PROTECT ☆
☆ SMULE VOICE FAMILY ☆
☆ FOUNDER COMMUNITY ☆
☆ ASOSIATION FOUNDER INDONESIA ☆
☆ Generasi Kickers Killers ☆


Minat? Silahkan PM!
Idline: http://line.me/ti/p/~alrahmantoganteng""",
    "lang":"JP",
    "comment":"Thanks for add me",
    "commentOn":False,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "cName":"™1™ ",
    "cName2":"™2™ ",
    "cName3":"™3™ ",
    "cName4":"™4™ ",
    "cName5":"™5™ ",
    "cName6":"™Franky™ ",
    "cName7":"™Brook™ ",
    "cName8":"™Nami™ ",
    "cName9":"™Robin™ ",
    "cName10":"™Rebecca™ ",
    "cName11":"",
    "cName12":"™ONE PIECE BOT™ ",
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "Protectgr":True,
    #"Protectjoin":True, # Ga Kepake(Yang Gabung langsung di kick :D) Udah  Udah ada Protect Cancell
    "Protectcancl":True,
    "protectionOn":True,
    "atjointicket":True
    }

         wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }

setTime = {}
setTime = wait2['setTime']


def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 
def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))

        #------Protect Group Kick start------#
        if op.type == 11:
          if wait["Protectgr"] == True:
            if op.param2 not in Bots:
              G = random.choice(KAC).getGroup(op.param1)
              G.preventJoinByTicket = True
              random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
              random.choice(KAC).updateGroup(G)
              random.choice(KAC).sendText(op.param1,random.choice(KAC).getContact(op.param2).displayName + "Jangan Buka Kode QR Woooyyy")
        #------Protect Group Kick finish-----#

        #------Cancel Invite User start------#
        if op.type == 13:
          if wait["Protectcancl"] == True:
            if op.param2 not in Bots:
              group = cl.getGroup(op.param1)
              gMembMids = [contact.mid for contact in group.invitee]
              random.choice(KAC).cancelGroupInvitation(op.param1, gMembMids)
        #------Cancel Invite User Finish------#
            
        if op.type == 13: 
            if op.param3 in mid:
                if op.param2 in Amid:
                    G = Amid.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    Amid.updateGroup(G)
                    Ticket = Amid.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                    G.preventJoinByTicket = True
                    Amid.updateGroup(G)
                    Ticket = Amid.reissueGroupTicket(op.param1)

            if op.param3 in Amid:
                if op.param2 in mid:
                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    ki.updateGroup(X)
                    Ti = ki.reissueGroupTicket(op.param1)

            if op.param3 in Bmid:
                if op.param2 in Amid:
                    X = ki.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ki.updateGroup(X)
                    Ti = ki.reissueGroupTicket(op.param1)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    kk.updateGroup(X)
                    Ti = kk.reissueGroupTicket(op.param1)

            if op.param3 in Cmid:
                if op.param2 in Bmid:
                    X = kk.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kk.updateGroup(X)
                    Ti = kk.reissueGroupTicket(op.param1)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    kc.updateGroup(X)
                    Ti = kc.reissueGroupTicket(op.param1)
                
            if op.param3 in Dmid:
                if op.param2 in Cmid:
                    X = kc.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kc.updateGroup(X)
                    Ti = kc.reissueGroupTicket(op.param1)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    ks.updateGroup(X)
                    Ti = ks.reissueGroupTicket(op.param1)
                
            if op.param3 in Emid:
                if op.param2 in Dmid:
                    X = ks.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ks.updateGroup(X)
                    Ti = ks.reissueGroupTicket(op.param1)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    ka.updateGroup(X)
                    Ti = ka.reissueGroupTicket(op.param1)
                
            if op.param3 in Fmid:
                if op.param2 in Emid:       
                    X = ka.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ka.updateGroup(X)
                    Ti = ka.reissueGroupTicket(op.param1)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    kb.updateGroup(X)
                    Ti = kb.reissueGroupTicket(op.param1)
                
            if op.param3 in Gmid:
                if op.param2 in Fmid:
                    X = kb.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kb.updateGroup(X)
                    Ti = kb.reissueGroupTicket(op.param1)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    ko.updateGroup(X)
                    Ti = ko.reissueGroupTicket(op.param1)
                
            if op.param3 in Hmid:
                if op.param2 in Gmid:
                    X = ko.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ko.updateGroup(X)
                    Ti = ko.reissueGroupTicket(op.param1)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    ke.updateGroup(X)
                    Ti = ke.reissueGroupTicket(op.param1)
                    
            if op.param3 in Imid:
                if op.param2 in mid:
                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    ku.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)        

        if op.type == 13:
            print op.param1
            print op.param2
            print op.param3
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:

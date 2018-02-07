
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

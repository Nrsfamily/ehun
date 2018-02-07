
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

#!/usr/python2
#Author = D@rk_Devil#666
#Mulai
#mengimport
import os
#membuat baner header
kepala = """=================================
        AlbatRossCreate
         D@rk_Devil#666
================================="""
        
#memprint
os.system('clear')
os.system('sleep 1')
print kepala
os.system('sleep 2')
print "Dibuat oleh D@rk_Devil#666"
#memberikan input
judul = raw_input("Judul Sc mu : ")
nama = raw_input("Hack by : ")
img9 = raw_input("Link gambar : ")
img10 = raw_input("Link background : ")
pesanrhs = raw_input("Pesan, br untuk enter : ")
warna = raw_input("Warna text(red) : ")
lagu1 = raw_input("Kode lagu : ")

#membuat scnya
fo = open("defaceku.html", "w")
#menulis script
script1 = """<html><head><title>"""
script2 = judul
script3 = """</title></head>
<body>
<br>
<link href='http://fonts.googleapis.com/css?family=Orbitron:700' rel='stylesheet' type='text/css'>
<link href='http://fonts.googleapis.com/css?family=Anton' rel='stylesheet' type='text/css'>
<link href='http://fonts.googleapis.com/css?family=Josefin Sans' rel='stylesheet' type='text/css'>
<body bgcolor="#000000" background="""
script4 = img9
script5 = """><div class='CenterDiv'><center><h1><center><font color=\"red\" face=Orbitron>""" 
script6 = nama 
script7 = """<h1></font><img src="""
script8 = img10
script9 = """ width=450px height=340px><body onload="init()"></body><body><div id="bulle"></div>""" 
script10 = """<script language=\"JavaScript\">var i=0var j=0var texteNE, affichevar texte=\"<br><br><br><br><br><font face=Orbitron color=""" 
script11 = warna
script12 = """ size=4>""" 
script13 = pesanrhs
script14 = """<br><br></font><br></b></div>\"var ie = (document.all);var ne = (document.layers); function init(){texteNE='';machine_a_ecrire();}function machine_a_ecrire(){texteNE=texteNE+texte.charAt(i)affiche='<font face=Orbitron size=1 color=#ffffff><strong>Messenge : '+texteNE+'</strong></font>'if (texte.charAt(i)=="<") {j=1}if (texte.charAt(i)==">") {j=0}if (j==0) {if (document.getElementById) { // avec internet explorerdocument.getElementById("bulle").innerHTML = affiche;}}if (i<texte.length-1){i++setTimeout("machine_a_ecrire()",70)}elsereturn}</script><font face="Orbitron" size="1"><blink><span style="color: rgb(255, 255, 255);"><b><font color=lime size=4></font></b></u></blink><br></font></b><a href="/index.php"><img style="position:fixed;bottom:0px;z-index:1000;right:-10px;" src="http://static1.squarespace.com/static/5706c12007eaa0b82399660d/5706c68bf0bc33987cae6c71/577d5c5d37c581fd0e25c10b/1469717705608/insult-145142_1280.png" type="image/gif" width="150"></a></body><!-- CSS --><style>.CenterDiv{width:650px;border:1px #ff0000 solid;padding:5px;margin:0px auto; background: url('http://i.imgur.com/sDbaMsW.gif');}</style><br><br><br><iframe width="0" height="0" src="http://www.youtube.com/v/""" 
script15 = lagu1
script16 = """&autoplay=1" frameborder="0"></iframe>"""
#menyalin
fo.write(script1)
fo.write(script2)
fo.write(script3)
fo.write(script4)
fo.write(script5)
fo.write(script6)
fo.write(script7)
fo.write(script8)
fo.write(script9)
fo.write(script10)
fo.write(script11)
fo.write(script12)
fo.write(script13)
fo.write(script14)
fo.write(script15)
fo.write(script16)

os.system("sleep 3")
print "Script berhasil dibuat"
print "WA : 089652884613"

fo.close()

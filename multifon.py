# -*- coding: utf-8 -*-
from Tkinter import *
import tkMessageBox
import requests
import xml.etree.ElementTree as ET
import base64
import os

URL = 'https://sm.megafon.ru/sm/client/routing'
URL_SW = 'https://sm.megafon.ru/sm/client/routing/set'


root = Tk()
root.geometry('250x250+800+300')
root.title("MULTIFONAMA")
root.resizable(False, False)

icon = """AAABAAMAEBAAAAEAIABoBAAANgAAACAgAAABACAAqBAAAJ4EAAAwMAAAAQAgAKglAABGFQAAKAAA
ABAAAAAgAAAAAQAgAAAAAAAABAAAEgsAABILAAAAAAAAAAAAAPz5/P+Ci3z/OVcf/z1dJf9BYCj/
Q18u/0ZgMv83VR7/KUsL/yhKCv8vURP/Ql4u/3B9Z//Mzsn/+vr5//79/v/6+fz/VmhD/zVjA/80
ZAD/NGQB/zRkAP81ZAH/NGQA/zRkAP81ZAD/NGQB/zVkAf8yYgT/LEsS/+Ll4v/+/v7//P39/3iE
b/81YwT/NWQB/zVkAf81ZAH/NWQB/zVkAf81ZAH/NWQB/zVkAf81ZAH/MWUA/zBWCv/S1tD//v7+
//3++v+or6b/NGMF/zVlAP81YwL/M2QB/zNkAf8zZAL/NGUD/zNkA/81ZAH/NWQB/zJkAv8vVwj/
09bT//7+/v/8/fv/3uHe/y1TCf82ZgH/NWQD/zNjBP8yZAL/NGQF/zNjBf8zYgb/NWQC/zVkAf80
ZAL/LVkG/9TW1P/+/v7//P39//z7+P9LYzT/MFoI/zBbBf8pTAv/KU0K/yZMCP8pTQf/JkoH/y5U
DP81ZAH/M2MC/yxXBv/X2dX//v79//f39/+ts6r/QmMs/y9YC/8kRgj/JkkN/yNNCv8lRQf/IToJ
/ylJEP8qUhL/MmQE/zRkA/8uUgr/4+Xf//3+/P+9xLr/XqgV/06VFP8sTg7/JVAO/yhRF/8kSBP/
IT4O/x0/D/8kTRH/K2cO/zRlA/81ZAX/MFMS/6m2of/4+PT/ZJs6/2PICP9evAv/JEsQ/y1zDf8j
UxX/HUgQ/yNPEf8mYBH/KGcM/yNXDf83ZAf/LVMN/1WeEP9guBH/Yo87/2TAC/9myAb/Z8gI/zhe
Gf8kURD/NZUH/zaVBv8thAf/MZIL/y9xCf8tUA7/SVo9/1mGMf9nxwv/Zs0E/2nKB/9iyAT/ZsgE
/16cIv/T283/aYhb/zCYA/8smAX/MJoD/zWXBP8xaxf/pKqk//b39f/DyMD/W6cO/2LJAv9kywL/
Y8YH/2PEDv+Zqoz/+vv2/2qKXP8vkgj/LIIM/zKPCP8wign/LHkS/+/w7//9/f7/+/35/5Cngf9h
vQ7/Y80F/z50F/9OjR3/5+jl//n89/99j3X/L3c6/yyDaf8vcTL/MHtI/zZ5Ef/u7u7//v7+//38
/P/8+/T/lqqP/1ecFf+HiIT/Y3Bd//z8+//7/Pv/0NPR/zR3Hv80lAv/L48O/zqMEP9ukmX//f39
///////9/v3//fz9//f49f+Znpf/+vr6/97e3v/8/Pz//f39//z7+//T1tD/haJ9/3mRbv+fqJv/
9fXy//7+/v/+/v7//v7+//7+/v/+/v7/+/v7//7+/v/+/v7//v7+//7+/v/+/v7/+vz8//38/f/9
+/7/+/36//v8+//+/v7//v7+//7+/v/+/v7//v7+//7+/v8AAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKAAAACAAAABAAAAAAQAg
AAAAAAAAEAAAEgsAABILAAAAAAAAAAAAAP36/v/79v7/5OTp/42Vjv9DUzr/M0gp/0RYPP9LWkP/
TF1E/05fR/9QXU7/U19S/1dhVf9YYlj/TVlL/yY6GP8fNRD/HDEP/xswDv8aLw7/HjQS/zVLKv9I
WT//XWtb/5Wdlf/f4dr/9/j2//n5+f/4+Pj/+vr6//79/v/+/v7//Pn6//z7/P9qb2f/LUMT/zlg
Df81Ygv/MmAK/zRiC/81Ygv/NGEL/zVgDP81Xw3/NF4M/zVfDP81YAz/NGEH/zRiBv81Ywf/NWQG
/zVjBv81Ywn/MmEH/zRgDv8uVRD/I0IQ/ygyG/9obWH/2NrV//r6+v/6+/r//f3+//7+/v/4+fj/
+/f+/21zaf80VA7/NmIG/zRkAf80ZAD/NGQB/zRkAP8zZAD/NGUA/zRlAP80ZAD/NGQB/zVlAP80
ZAH/NGQA/zRlAP81ZQD/NWUA/zRkAf81ZQH/NGQB/zRjAv8zYQT/M2AJ/zFWD/8mNx3/4+fk//z8
/P/+/v3//v7+//r7+v/89/7/io6H/yxKDf80YQb/NGQB/zVkAf80YwD/NWQB/zVkAf80YwD/NGMA
/zVkAf81ZAH/NGMA/zVkAf81ZAH/NGMA/zRjAP81ZAH/NGMA/zRjAP81ZAH/NWQB/zRkAf8wZQH/
M2AH/yc+FP+vta7/+vz5//79/v/+/v7//P79//v6/f+4vLb/IToO/zViBv80YwD/NWQB/zRjAP81
ZAH/NWQB/zVkAf80YwD/NWQB/zVkAf80YwD/NWQB/zVkAf80YwD/NWQB/zVkAf81ZAH/NWQB/zVk
Af81ZAH/NGQB/y9lAP80ZAT/LEYS/6ivpf/7/fn//v7+//7+/v/8/f7//v79/+Hj4f8kNxb/N2MH
/zVkAf81ZAH/NGMA/zVkAf81ZAH/NWQB/zRjAP81ZAH/NWQB/zRjAP81ZAH/NWQB/zRjAP81ZAH/
NWQB/zRjAf81ZAH/NWQB/zVkAf8zZAD/MGUB/zRkA/8tSQ//qK+l//z8/P////////////z9/f/+
/vr/+vz8/z5ONv82ZAj/NWQB/zRkAP80YwD/NWQB/zRjAf80YwD/NGMA/zVjAP81YwD/NWMB/zVj
Af81ZAH/NGMB/zVkAf81ZAH/NGMB/zVkAf81ZAH/NWQB/zNjAf8wYwP/M2ME/yxJEP+orqf//Pv9
/////////////Pz9//7/9v/5+fz/bnts/zFfCv81YwP/N2cB/zVkAf80YQT/NWUC/zNlA/8xYwH/
MWQA/zJlAf8xZAH/M2QE/zJgCv81bAD/MWII/zNoBP81ZAH/NWQC/zVkAv81ZAH/NWUB/zJkA/8x
YQT/K08K/6qvrP/9/fz//v79//7+/v/7/P3//v/2//r6/P+mr6f/Kk8M/zRiA/83aAH/NmUB/zRh
BP80ZwD/M2YB/zFiA/8xZAH/MmYB/zFjAv80ZQT/MmII/zNoAf8yYQj/M2UC/zVlAf81ZAH/NWQB
/zVkAf81ZAH/M2QD/zBhBP8qUQn/qq+s//7++//+/v3//v7+//v9/f/+/vv//fv9/9vi2f8gOBD/
NWIF/zdnAP81YwP/NWEG/zZoAf81aQH/MlwL/zFgBv80ZgL/NWIJ/zVlBP80YwT/M18J/zVhCv8y
YAb/NGME/zZlAv82ZgD/NWQB/zVkAf8yYwP/MWEF/ypQCP+rr6z//v36//79/v/+/v7/+v79//79
/v/9+/v/+fr1/0FMOf81YAj/NWQD/yxXB/8tVgb/N2gC/zdmBv8iQA//IUUJ/zNfBv8fRAn/Ml8G
/zRiBP8jRAr/LVYH/yFHBv8vVw3/NWEH/zVkAf81ZQH/NGMB/zJjA/8xYgX/KE4H/62yr//+/fn/
/v39//7+/v/6/v3//fz+//78+//8/Pb/io2K/y1UB/80Xwn/KlEM/yVLCv81ZAL/N2MJ/xUpDv8Z
NAr/NVwR/xUvCf8zXAj/NmAH/xcsCf8tUgr/HTsH/x4+Df80XA7/NWQD/zVlAf80YwH/MmMD/zFi
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
Jf9vgm//+vj6//3++f/3+v7/+/z1//nz+v9qd23/LXgX/y6JD/9AhRf/LJkH/yyVB/8whhT/PowP
/ziXCP80iRn/a4Fk//z7+//9/f3//v7+///////9/v7/+v77//z6/P/9+/z/+Pj0/+fr5/8uNyn/
fYl5/6enp//i4uH/Gx0Z/8fIxv/7+/v//v39//3+/v/7+/v/+vn6/+Pn4v8+XTf/N4Ab/zWYCv8u
mgT/MJAO/y6PEP85kBD/O3wZ/z5cN//d5OH//f3+//7+/v/+/v7///////7+/v/+/v7//v7+//7+
/v/+/v7//v79/8XFxv/z8/P/+Pj4//j4+P+MjIz/9vb2//j4+P/+/v7//v7+//z8/P/6+vr/+vn7
/+Th6v9wgXH/NGQn/ydiDv8pYAz/JkkY/ytFIP9qeGL/4+Tc//r3+f/+/f7//v7+//7+/v//////
/v7+///////////////////////+/v7/+Pj4//r6+v/8/Pz/+/v7//n5+f/7+/v/+/v7//7+/v/+
/v7//f39//39/f/9/fz//Pvx//v89v/r7+3/z9PS/8XJx//Q0c//7Ovs//z5/f/7/Pz/+/32//3+
/f/+/v7//v7+///////+/v7//v7+//7+/v/+/v7//v7+//7+/v/8/Pz//v7+//7+/v/+/v7//v7+
//7+/v/+/v7//v7+//7+/v/+/v7//v7+//7+/f/9/Pr//vv9//77/v//+/7//vz9//z8/v/6+/3/
+fv9//j++//3/vf//f79//7+/v/+/v7//v7+//7+/v/+/v7//v7+//7+/v/+/v7//v7+//7+/v/+
/v7//v7+//7+/v/+/v7//v7+//7+/v/+/v7//v7+//7+/v/+/v7//P7+//b8/f/4/fv//P38//38
/f/9+f7//vz+//3+9//+/vf//vv9//34/v/+/f7//v7+//7+/v///////v7+//7+/v/+/v7//v7+
//39/f/+/v7//v7+//7+/v8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACgAAAAwAAAAYAAAAAEAIAAAAAAAACQAABIL
AAASCwAAAAAAAAAAAAD9+/7//fj+//jz/f/59/3/6+7x/7S8tP9gbF3/Nkcy/z9OO/9VY1L/X2pc
/2FrXv9jbl//ZnFj/2hzZf9tdG3/cXhz/3Z9eP96gXz/fIJ//36Egf95gXv/NEAx/xotEf8RJAj/
DiAG/wsbBv8LGwX/ChsF/wobBf8NHwj/IDEa/zpLNP9SXk3/ZnBj/5aflf/N087/7O7r//f49P/5
+fn/+vj8//r5+//4+Pj/+vr6//f49//+/v7//v7+//7+/v/9+/3//Pf8//z5/f/Fxsf/NTs1/xcn
C/8mQQz/NFUX/yxPEP8pTA7/KkwQ/yxNE/8sTRL/KkwR/ypLEf8oRRT/JkIU/yQ+Ef8kPRD/IzsQ
/yM7EP8nQRT/L00W/zhaGP84Whj/OFsW/zlbF/84WxX/OFsV/zdaF/82WRj/NVkW/zVZGP8zVRr/
JEIQ/xYuC/8JHQb/MDot/3+Ddv/V2M//+fr1//b39f/7+/v/+Pj4//3+/f/9/f3//f3+//7+/v/8
+/r//Pn7//v7+v+UmZH/GCgK/z1YGf88ZAz/NWMF/zRlCP8yYwb/MGEE/zJjBf8yYwX/MWIF/zJi
Bf8yYQT/NGMG/zNiB/8yYAb/NGMG/zRjB/8yYQT/NGQF/zNkAv80ZQL/NWYD/zVmA/81ZwL/NWcC
/zVnAv82ZwX/NGYG/zJkBP80ZAn/MF0J/zFcEf8uVhL/NUsh/yItE/8iKhv/eHx0/+Di3//29vb/
/Pz8//r6+v/+/v7//v7+//7+/v/5+vb/+ff8//v3/v+ZnZb/GS0J/zpeD/83Ygf/NGMB/zRkAf80
ZAD/NGQA/zVlAf81ZQH/M2UA/zNkAP80ZQH/NGYA/zRlAP80ZQD/NWUB/zRkAf81ZQD/NWUB/zRk
Af80ZQH/NWUA/zVmAP81ZgD/NWYA/zVlAf80ZQH/NWUB/zVmAf80ZAH/NWUC/zNiAv8zYQT/NGAK
/zNcDP80WBP/GTMH/zdDNP/q7ur/+vz8//z8/P/+/v7//v7+//7+/v/7/fn/+fb7//v1//+3t7P/
ESIG/zhcDf84Ywn/M2ED/zRjAP80YwD/NGMA/zRjAP80YwD/NGMA/zRjAP80YwD/NGMA/zRjAP81
ZAH/NWQB/zRjAP80YwD/NGMA/zRjAP80YwD/NGMA/zRjAP80YwD/NGMA/zRjAP80YwD/NGMA/zRj
AP80YwD/NWQB/zVkAf80YwH/MGMB/zJmA/8zYQb/OV0Y/xYlDf+mrab/+Pv6//3+/P/+/v3//v7+
//7+/v/8/vv/+/n7//v3///Q0c3/Dh0G/zhaE/80Xwb/NGQC/zVkAf81ZAH/NGMA/zRjAP81ZAH/
NWQB/zVkAf80YwD/NGMA/zRjAP81ZAH/NWQB/zVkAf80YwD/NGMA/zVkAf81ZAH/NGMA/zRjAP80
YwD/NWQB/zVkAf81ZAH/NGMA/zRjAP81ZAH/NWQB/zVkAf80YwD/MmYC/y9kAf8zYwT/NFsQ/yEz
E/+GjIT/9/r2//v8+P/+/f7//v7+//7+/v/7//z/+/r9//v5/v/l5uP/IzAf/zFRFP82YQf/M2MB
/zRjAP81ZAH/NWQB/zRjAP81ZAH/NWQB/zVkAf81ZAH/NGMA/zRjAP81ZAH/NWQB/zVkAf80YwD/
NWQB/zVkAf81ZAH/NWQB/zRjAP81ZAH/NWQB/zVkAf81ZAH/NGMA/zVkAf81ZAH/NWQB/zVkAf80
YwD/MWUB/y9lAP80ZgP/Nl0O/yU6E/9/h3z/+f32//v8+v/+/v7//v7+//7+/v/8/v7//v7+//39
/v/8/Pr/P0Y+/ytFE/85Ywv/NWUB/zRjAP81ZAH/NWQB/zRjAP81ZAH/NWQB/zVkAf81ZAH/NGMA
/zRjAP81ZAH/NWQB/zVkAf81ZAH/NWQB/zVkAf81ZAH/NWQB/zRjAP81ZAH/NWQB/zVkAf81ZAH/
NGMA/zVkAf81ZAH/NWQB/zVkAf80ZAD/MWUA/zBmAP8zZgH/NV4K/yg/Ef9/iHz/+/74//z9+///
///////////////7/f7//v79//7+/f/9/v7/cnly/yhAFf81YAn/NWYB/zVkAf81ZAH/NGMA/zRj
AP81ZAH/NWQB/zVkAf81ZAH/NGMA/zRjAP81ZAH/NWQB/zVkAf80YwD/NGMA/zVkAf81ZAH/NGMA
/zRjAP81ZAH/NWQB/zVkAf81ZAH/NGMA/zVkAf81ZAH/NWQB/zVkAf8zZAD/MGQA/zFlAf80ZQH/
NV4K/yhAEP9/iHz//P76//z8/P/////////////////7/f3//v78//3++v/9/f7/sbaz/yE2E/82
YQr/NWYB/zVkAf80ZAD/NGMA/zRkAP81ZAH/NWQB/zVkAf80YwD/NGMA/zRjAP80YwD/NGMA/zRj
AP81YwD/NGMA/zVkAf81ZAH/NGMA/zRjAf81ZAD/NWQB/zRjAP81ZAH/NGMA/zVkAf81ZAH/NWQB
/zVkAf80YwD/MWIC/zBkA/8zZQL/NV0M/yhAEf9/h33//P37//z7/f/////////////////8/P7/
/v75//7++P/7+/z/09fW/yU3G/8zYA3/NWcB/zVjA/81ZQD/NmYA/zRjAf81YwL/NWMC/zVkAf80
ZAH/M2MB/zRkAf80ZAH/NGQB/zRlAf80ZAH/NGQB/zRjA/80YQf/M2UB/zVoAf8zYwP/M2IF/zVn
Af80YwH/NGMB/zVkAf81ZAH/NWQB/zRjAP80ZAD/MmMC/zBjBP8yYwP/M18I/ydDD/9/iH///Pz9
//z8/f/+/v7////////////7+/7//f74//7/9f/7+vz/8/b5/zhJNP8rVgv/N2gG/zVjBP83ZwH/
N2cA/zVjAf80YAT/NGMD/zVmAv8zZQP/MWMD/y9jAf8wZAD/MWUB/zFlAf8wYwH/MWYB/zJjB/8x
XQ//MWgD/zVvAP8wYwf/MGAM/zVrAv81ZAH/NWQC/zVkAv81ZAL/NWQC/zRjAP81ZAH/NGYA/zFj
Bf8xYQb/MmIC/ydIDP+CiYP//Pv+//3++v/9/f3//f39//39/f/7+/7//f75//7/9v/7+/z/9vj8
/2p3av8rUQ//MmAF/zVjA/83aAH/N2gB/zVkAf80YQT/NGQB/zRmAf8zZgH/MmQD/zBiAv8xYwH/
MmYA/zFlAv8xZAL/MmYB/zNkB/8xXwv/MmgC/zNpAf8yYgf/MWEI/zVoAf81ZQH/NWUB/zVkAf81
ZAH/NWQB/zVkAf80ZAH/NWYA/zJjBf8wYQb/MWIC/yZIDP+CiYP//Pv+//7++v/+/v3//v7+//7+
/v/7/P7//P76//7/9//9+/z/+Pn7/6y1qv8XMQv/MFoH/zVkAf83aAH/N2gA/zRjAv80YAX/NGUB
/zZoAP80aAD/M2MD/zJgBv8yYgL/MmcB/zJmAf8yYwP/NGYB/zRkBf8zYQf/NGgB/zJjBP8zYAj/
M2ME/zNjAv81ZQH/NWUA/zVlAf81ZQH/NWQB/zVkAf81ZAL/NGUB/zJjBf8wYQb/MWIC/yZIC/+C
iYP//Pv+//7++f/+/f7//v7+//7+/v/7/f7/+/38///+/P///f7/+Pj4/9zj2P8bLBT/MVUO/zZk
A/81ZgD/N2cC/zRhBf80Xwj/OGYG/zZpAP83awH/M2EF/zJaEP8xXQr/M2UB/zRlA/82YQ3/N2YH
/zRiBf80YgX/NGQB/zNaEP80Xg3/NmUE/zBcCf8yYAb/N2YF/zZmAv82ZgD/NmUB/zVkAv80YwL/
NGUB/zJiBf8wYQb/MmID/yVGCf+CiYP//fv+//7++P/+/f7//v7+//7+/v/6/v3/+/3+///9/v/+
/P3/+/v4//j69P9BSz3/KkcO/zVjA/82ZQL/NWIE/ylUBf8rVQb/NWMF/zhpAf82aAL/N18R/xo6
Cv8YOwb/NGAF/zRhBf8qUQ3/JE4C/zRgB/80YgX/NmMG/x49Cf8oTgf/NWUD/xo+BP8xWg7/Ml0G
/zdkBv80YwD/NmcB/zVkAf80YwH/NGUA/zFiBf8wYQb/MmID/yNECf+EjIX//fv9//7++P/+/f7/
/v7+//7+/v/5/v3/+/3+///8/v/++/3/+vr1//v79v+NkYz/HzYL/zNgBP82YwX/M14I/yZNDf8l
Swn/M18F/zdnAf81ZAL/OFsb/w4jCf8QKwf/Nl0P/zNaC/8dOw7/Gj8B/zVfCf80YAb/N2EM/wwg
BP8nSQv/N2MG/xQvCv8hQQz/NVwT/zRfCf81YwP/NmYA/zVkAf8zYgD/NGQA/zFiBf8wYQb/MmMD
/yJCCv+LlYz//Pr9//7+9//9/f3//v7+//7+/v/5/vz//P3+//78/v///f3//fv2//78+P/W1tj/
GywP/zRgCf8xXAf/N18P/yRKCv8aPgn/NV4I/zZlAf84ZwT/M1Ia/wUUA/8KIAP/NVoU/zVbEf8Z
Mg7/HUAC/zZfC/81Xgf/NVsM/wkWBf8nRg3/OGQH/w4nBf8QLgX/M1cZ/zNcC/81YwT/NWYB/zVk
Af81YgH/NGQB/zFjA/8xYgX/M2MD/yBAC/+Rm5L/+/n8//79+P/+/fz//v79//39/f/w8/X/+Pr6
//r59v/9+fj/9/Tz//P09P/j6eb/LDwt/y9YCf8yXBD/NVwW/yBGBv8PJQz/NWAI/zhqAf80bQP/
MEwY/wsRCP8IHgP/LF4M/zBkCv8VMAf/JUYI/zVgBf87XQn/MUsS/wMQAf8xUhf/OV8H/xUrB/8X
OBH/LUwf/zheDf82YgT/MmcB/zJgCf83YQb/NWQC/zRoAv84awH/N2MF/yA3D/+Znpr/+/r9//7+
+P/+/vf//f/6//38/v/4+vz/+Pn2//j49f/48/b/0tLU/1xlWv8bMxb/FTEM/x9DAv82Ywr/M18J
/yJGC/8EEAX/MVgO/zhoAv8wbQL/LEoU/xcgEf8NKAj/KV8I/y9jDP8XLwr/JUIJ/zZhA/84WQf/
K0AU/wMUAf8yVBn/NVcO/xUxCP8tXBz/GDgN/zddCv80YgP/MWgB/zBgC/83YQj/NWYB/zFlAf80
ZAL/OF0O/yA1EP+ttaX/+/v5//38/P/9/vv//f78//7+/f/6+/r/+vn3//Du8P+8vr3/KDMp/yhN
FP9bniD/U4Yp/xIvA/85Zwb/OWgD/yNAD/8EEwX/IT8N/zZmCP8saQT/I0kP/yI6Gv8VNQ3/K1sK
/zJcEv8YKg7/HjUI/zdjA/85Xg//Fi4L/wQZAf81VB7/LUoZ/xQ7Bv88eyD/EDgF/zhfDP80YwL/
MmkA/zBgCf83YQf/NGUC/zBlAf81YwT/OFsS/xkmEP/Lzcj//v73//7+8//++/7//fz+//7//P/+
/Pz/9fH3/9fZ2f8rPSP/TH0f/265Jv9lvxL/aaot/w4qBP8yWwj/PWYH/yM9EP8jPhX/EzII/ypX
Dv8uYw3/HkcN/ypNH/8XPRD/K1cN/zNVGP8RIQz/DyME/zpkCf8uVw//FC4P/w8nB/8zThv/HjgY
/yFTDP9EkB3/F0gL/zBXC/83ZAL/MmgA/zJiB/83YQb/M2EL/zJoBP84bQH/NlsN/yEmIP/u6fP/
+/b4//3/7f/9+v///fz+//z++f/7+Pr/8O7w/0NSQf9QgSH/bMMR/2nQBP9hxA3/bLkm/xxEBP8p
TQz/OVsP/yNAEP8tVw3/LFkV/xc8Dv8xXBr/GkQL/y5ZIv8XPxD/Kk0R/zNRHv8QKgv/DyUH/zle
D/8iShL/H0UT/xUwDP8sRRb/EiwP/yxyEP84kQz/KGIS/x9CCP84ZQT/MmcB/zNiBf81YQT/NWII
/zZoBf83Zgb/JEkI/yIzHf92fnr/1NvT//b87//8+vr/+vv4//r89//z9fT/jJiJ/y5VFf9uuh//
atIC/2fVAf9gxQz/acEY/zBhEP8kRhD/N1oW/xw8C/8pXgb/Q4UZ/w87Cf8tTBn/Gj0Q/y1cJv8T
Og7/K0sY/x48E/8vWyP/ECsI/zdXGf8QMwj/M2gZ/xo2Df8hOQz/DC4H/zmPE/8ykwf/N3Uf/xEw
A/85ZQT/M2YB/zBkAv80YgP/N2gC/zRhBv8xVRb/ETYG/2CQL/9JfB3/IUMW/2R6Yf/Y383/+/3x
//r89v/b4t7/KUsb/2GoHv9lwwv/YsgI/2DHCf9exgP/ZsUI/0aFGP8YQwb/N2IR/x09EP8nWg//
P5AL/zBzGv8SKAb/EjIM/zhmNP8QLg7/JkAb/xQ3Cv89fSb/ETYF/zBKHf8HKAf/PoMa/yM/FP8T
KgP/IlIS/zCRCP8tlgb/LWsW/xIqBv88Ywj/NmUC/zFlA/8zYwP/NWED/zhcE/8UNAj/PGwa/268
GP9pxQv/Xq0i/zNmGv8pORr/f4h0/+bn5P90iHH/Rn0f/27GFP9mzAT/YcUK/2HDDv9fywH/ZckF
/1unIP8PPgX/NVwX/yNCGf8gTQ7/PZUH/zeOEf8gTA7/BSkD/zhrLf8RNgz/DycL/zFjGv8/iRn/
EjUH/x8xGf8SQQr/Po8W/yRLGP8GJwL/OHYX/zKNDf8zgBb/DT4F/ylKFf82Ygf/NmQE/zRjAv81
YwX/NFQX/yE7E/8mVgr/a7cZ/2vMBP9mygb/ZcIT/2e8Hf9jnyP/Ml0P/yw/KP8sVx3/ZrEp/2nK
B/9p0gH/ZMoC/2PGCf9gygT/ZssF/2O4FP8XRwj/LlIa/y9QE/8JKAP/N4IR/zCWBv8zhhP/EUkH
/zx6Iv8XTAn/GUsL/z6JE/85jgj/FTcJ/wQaBv8lcQj/NZQN/yBaE/8bUwf/P4wN/ziEGv8XOg7/
HUEL/zNfCf89bAr/NGAG/ztjE/8uUQ7/GDUN/ydOEf9ssSf/btAH/2nSAf9kxwj/ZcYM/2fOBf9m
yg7/Z8AZ/1mZIv9Jihr/ZLwQ/23RBP9ozwH/ZMcG/2PDD/9ixgn/YsUF/23HFf8zaRP/HEQH/ztg
B/8RJwP/Kloe/zOQDf81kQn/NYUU/z2PEf83hAv/PYgY/zqRBv87mAf/IFsM/w1BBP8zjQ3/MZUG
/zmIGv9BihL/PYsI/x1aCf8cQAr/Nl8R/zRhBf80Xgb/O18Y/xszCv8IFgT/PW4W/223H/9svRn/
ZsQL/2XNAv9l0AH/Zs0C/2fGDf9nwRb/aMUO/2rECv9ktxf/bM4J/2fNAf9pzQL/ZMYI/2TEDf9k
xwj/acsK/2bIBv9epiL/FjUJ/zJJDP8mOA//EzEQ/zqLFv82mAX/MZID/zeaAf84mAL/NZUD/zec
BP8xlgL/No4L/zWJEv8xlg3/LZYG/zOQCf9BmAT/PYYK/wozAv8yXgb/M1oL/zdWHf8mPBb/DxsM
/ztFOv9daFn/RHsW/2/IEf9oxwr/Z8YR/2LJBf9k1QD/aNEC/2fFCv9mxgj/a88E/2rPAf9pwxH/
Y8gD/2bLAf9nygL/ZMYE/2nKB/9mywH/ackG/2vKCv9gpiT/MEAs/zo7Nf8cIRP/CSIG/z+OFP8x
lQH/NJ0C/zGeAf8yoAD/Mp4A/y+YAf8xlwX/MZkC/zGWB/8skQn/L5UJ/zGUB/86mQL/MnMJ/xcw
FP85XxL/LUoT/w8aCv8hJCX/jI6U/+nv6P/Y48v/KUse/1ifGv9tyg//ZskH/2LJBf9i0AD/Zs8A
/2fJA/9r0QH/aM0A/2fLAf9lxAz/YcYG/2PGBP9lxwL/aMsD/2fKAf9qzgH/a8QK/2KoHP8xWyH/
xMvD//f08//S0NP/HS0g/zyPBf8xlQH/MJ0A/yuYAv8tnAH/Lp8B/y+WBf8wlgb/Lp4A/y6YBP8y
kgf/MpQH/zSYCv85nAX/K2cM/xkoIf8YJhL/GSMX/3qBeP/d4dv/+Pv2//f69P/7/fX/nKKj/ylI
F/9jrhL/bc4H/2TKAf9iygD/Y8oA/2XKAf9oywL/ZssB/2XKAf9ixwX/YMcE/2HHA/9lyQP/ZsgC
/2rJB/9pxAz/Z6kh/ydEGf+zw63/8/js//v2+P/v6/H/Hysg/zqKC/80lQP/Mp0A/yuUBv8qlgf/
LJ0A/y+WBv8zmAb/L54A/zCXAv84lAL/N5gC/zGWBv80mgX/MGwP/yErJ/9xdHj/1drZ//L48f/3
+vL/+vv0//z8+f/39Pb/8/L6/1hhWv9Abhb/b8IU/2fKAf9jyAL/YsgD/2LKAf9kxgb/Y8wB/2XO
Af9jzAH/YcoB/2PKAf9kywL/YsUE/2bBDP9uvSD/IkUM/4yQlf/x+uv/8PTj//33/P/t7ej/HSwa
/zeAGP82lQb/Mp4B/yqSCf8rkA//K5oC/yyXBf80mwT/Lp4B/zGXAf8+mAH/Op4A/y+XBf8xmQf/
N3gS/0xaSP/3+/P/9/v3//b4+f/49v3/+fb9//z6+//9/Pr/+/r1/9zf2P8nOx//WpoW/2nHBP9k
yQH/X8gD/2DKA/9iygH/YswB/2PMAP9jywT/adAC/2fMA/9l0AL/YMQP/2bADv9SjhL/N0E3/+zx
8P/2/PL/9vby//35+v/o5en/Gi4a/zqJE/87lgT/LaAB/yqZCv81ihr/LZIQ/x+bA/8pmAH/IZsD
/ymWCP82lQX/L6UC/yqYBP8rlg3/MYMb/yY6H//v7+3/+/z6//r6+//9/P7//fz+//7+/v/+//z/
+/30//f89/+vtrH/JkkQ/2e0FP9s0gj/YMwE/17JCv9gygP/Ys4B/2TPAf9lxRP/Zs0B/2XNAf9i
ywL/Y8wP/2m+G/8xXQ7/qa+q//T69P/4/vb/+/z7///9+f/m4un/Gy4Z/z6PEf84nAL/M54D/zaW
CP8/jg3/PJUN/zObBf8tmQP/NZoC/zWUCP80kRP/MZkF/zacBP8tngP/M5AQ/yVHG//R1M///Pz8
//39/f/8/Pz//v7+//7+/f/9/v3/+v32//n7+P/z9fj/aXtm/zppFf9muBT/ZswK/2HNCP9gxwj/
Ys8D/2fWAP9OoRT/ZMkE/2jJCf9lyA3/YckI/1+pIP82Tin/7/Hr//b59v/0+/X/+/z6//798//s
6+z/HS8b/zeIEP8klQj/MYUW/yNmDf8eXwn/HVkK/yVmD/8sixX/UYgM/zdgDf8bVhn/LWML/0OF
CP81ngL/M5IO/x1HGf/Dx8P//Pz8//z8/P/+/v7//v7+//7+/v/+/f3//fz6//v6+f/39fr/5efq
/2J0YP89aRz/abgc/2nLDf9hxwn/Y8kM/2rRA/88gRr/Z8QP/2O0Hv9lvhb/Y8UK/0R7If96hHT/
/Pn6//n7+P/2/fn/+Pv6//398P/19fH/IzEj/zp4FP80iRr/DTsQ/zqQfP81q5X/RKeW/w83Jv86
dSr/IEwQ/yh3aP9Gq6//JV1J/ydlEP8xlQX/QI0T/x9AGv++wL3/+vr6//v7+//9/f3//v7+//7+
/v/+/v3//Pn8//z6+f/9/ff/+fb5//Lx+P+Mm4r/KVMY/1adFP9lxQv/ZcMQ/23AF/8zYx3/brQk
/x5PCf9PlRX/bL8f/x9DE//N0sv//fj8//z++//3/Pz/+Pv9//z97v/7+/b/SVJM/yxcFP83hRr/
E0Yg/2bm3/9D8/D/S+Dc/xFMMf9Agir/EE0L/0XBt/9U5ej/G1Q6/yp4HP8ylwT/R40O/y9IHv/O
z8z/+/v7//v7+//9/f3///////////////7//fr+///9+v/9/+v//v/v//36/f/29fv/tcK6/yNA
G/9apBf/cccQ/1SNIP8QJQf/RGgi/xUoFP9AcBj/W5ok/z9WP//x8vL//fn7//z++//3+/3/9/r9
//z+7//59vb/kpGX/xw7Df9DiRX/HVcO/xhJJP8YPiv/HUgi/y1qGf9Bjw3/NWkN/xY8Hv8YRSb/
KWMO/0GKCv88nAT/QI0N/zNOIv/x8vD/+vr6//z8/P/+/v7//////////////v///Pv+//7++v/+
/+3//v7v//36/P/38vz/8O/4/4uTj/8tUA3/cLAh/yA+E/8UGgv/ICYU/4yOi/8vSRn/QW0l/4aW
i//49/v//v34//z/+f/3+v3/9vn+//398f/9+Pr/4Nzn/x40Hf8udxj/LYwS/zKBEv9IeyD/PIUS
/y6bCP8smQX/MYwL/z97Hf9EfhP/QJoK/z+WCP8wjwn/NXsg/3B8a//7+/r//f39//39/f/+/v7/
///////////+/v7/+v77//v++//9+/z//vv8//37/P/49/X/8PLt/9je3P8hKCD/L0Ua/4SPgv8h
ISD/ZGNj/87Nz/8iKxz/LT4m/9Xa1//4+Pv//f34//3+/P/7/P7/+vz9//r69v/59fj/9/T6/4OP
g/8cShD/OI0b/yyQCP81lwj/Lp4D/yKdAv8olAn/IJMN/yKTC/8zlQr/MJ0K/zOKEP85fib/J0cm
/9zi3//8+/z//v7+//7+/v/+/v7////////////+/v7//P78//3+/f/8+/7//Pv9//38/f/9/vn/
+v31//r9+P9xcHT/VldW//Dx7//Y2Nj/9PT0/9/f3/8YGBj/VVRU//b29v/6+/r//f39//39/f/+
/f3//v7+//v6+v/9/Pz/9/j2//H07/9idGT/KFAc/zyDH/82kg7/M5sI/zKYBv81kw7/MYoP/zaP
Ff88jBP/QIcX/ztuIP8iPBv/vMW8//L3+P/8/f7//v7+//7+/v/+/v7////////////+/v7//v7+
/////////////////////////v////7///38/f/w8PD/7u7u//n5+f/6+vr/+fn5//T09P9XWFf/
tra2//j4+P/49/j//Pz8//7+/v/+/v7//v7+//39/P/39/f//Pz9//j2+f/x7Pf/iZCQ/y5KLP8u
ZR7/NHgZ/zeAEf84fw3/PHQg/zZiIv8mTBX/GjUP/0dYP//K0cH/9vTz//n1+f/+/f7//v7+//7+
/v/+/v7////////////+/v7//v7+//////////////////////////////////7+/v/39/f/+Pj4
//z8/P/6+vr/+Pj4//n5+f/n5+f/9PT0//j4+P/6+vr/+fn5//7+/v/+/v7//v7+//r6+v/8/Pz/
/f39//z6+//69fj/9fT1/9vi2v+VppX/WHFX/z5SO/84UDX/NkUz/0FHQP9xdW//vL+5//Hw7v/5
+Pj/+ff3//79+//+/v3//f39//7+/v/+/v7////////////+/v7//v7+////////////////////
//////////////7+/v/6+vr/+/v7//r6+v/9/f3//f39//z8/P/7+/v//Pz8//z8/P/8/Pz//v7+
//7+/v/+/v7//v7+//39/f/9/f3//f39//7+/P/9/u///v7y//z8+P/7+/3/+vn+//n4/P/09Pf/
9vb2//39/f/8+/7//Pn///z6/v/7/P3/+v33//r+9P/9/vz//f39//7+/v/+/v7/////////////
/////v7+//7+/v/+/v7//v7+//7+/v/+/v7//v7+//39/f/9/f3//f39//7+/v/+/v7//v7+//7+
/v/+/v7//v7+//7+/v/+/v7//v7+//7+/v/+/v7//v7+//7+/v/+/v7//v7+///9/f/+/vj//v35
//77/P/++v///vn+///6/v/++/7//vz+//v8/v/6+/7/+Pn+//n7/v/3/vv/9v74//f/9f/8/v3/
/f39//7+/v/+/v7///////7+/v/+/v7//v7+//7+/v/+/v7//v7+//7+/v/+/v7//v7+//7+/v/+
/v7//v7+//7+/v/+/v7//f39//7+/v/+/v7//v7+//7+/v/9/f3//v7+//7+/v/+/v7//v7+//7+
/v/+/v7//v7+//39/v/6+v7/+/r+//v7/v/9/P3///79///+/P/+/fz///39//39/f/8/Pv/+vz5
//v9+//7/fz/+vz8//r8+//9/f3//v7+//7+/v/+/v7///////7+/v/+/v7//v7+//7+/v/+/v7/
/v7+//39/f/+/v7//f39//7+/v/+/v7//v7+//7+/v/+/v7//v7+//7+/v/+/v7//v7+//7+/v/+
/v7//v7+//7+/v/+/v7//v7+//7+/v/+/v7//v7+//v+/v/1/f3/9f38//j++v/7/vv//P38//v6
/v/8+P7//fn////8/f/+/vj//v/0///+9v//+/z//vf///73/v///f///v7+//7+/v/+/v7/////
///////+/v7//v7+//7+/v/+/v7//v7+//7+/v/+/v7//v7+//7+/v/+/v7//v7+//7+/v8AAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA="""

icondata= base64.b64decode(icon)
tempFile= "icon.ico"
iconfile= open(tempFile,"wb")
iconfile.write(icondata)
iconfile.close()
root.wm_iconbitmap(tempFile)
os.remove(tempFile)

#root.iconbitmap(default='icon.ico')


def Check():
    #global phone_entry, password_entry
    #print phone_entry.get()
    #print password_entry.get()
    login = phone_entry.get()+'@multifon.ru'
    password = password_entry.get()
    data = {'login': login, 'password': password }
    req = requests.get(URL, params=data)                          #если будет ругатссо на ssl, то добавить , verify=False (актуально для py2exe)
    
    tree = ET.fromstring(req.content)
    code = tree.findall('result')
    description = code[0].find('description').text
    result = code[0].find('code').text
    if result == '200':
        route = tree.findall('routing')
        route_type = route[0].text
        if route_type == '0':
            text = u'Телефон'
        elif route_type == '1':
            text = u'МультиФон (SIP)'
        elif route_type == '2':
            text = u'телефон и МультиФон'
            
    elif result == '101':
        text = u'Неверный пароль'
        
    elif result == '404':
        text = u'Номер не найден'
    else:
        text = u'Что-то пошло не так!'
    #print req.text
    #print code[0].find('code').text
    #print code[0].find('description').text
    tkMessageBox.showinfo('AZAZA', text)
    
def Switch():
    login = phone_entry.get()+'@multifon.ru'
    password = password_entry.get()
    route_rb = choice.get()
    
    if route_rb == 0:
        tkMessageBox.showinfo(u'ВАРНИНГ!!!', u'Выбери режим маршрутизации!')
        return
    elif route_rb == 1:
        route = '0'
    elif route_rb == 2:
        route = '1'
    elif route_rb == 3:
        route = '2'
    else:
        tkMessageBox.showinfo(u'ВАРНИНГ!!!', u'Что-то пошло не так!')
    
    #print route
    
    data = {'login': login, 'password': password, 'routing': route }
    req = requests.get(URL_SW, params=data)
    tree = ET.fromstring(req.content)
    code = tree.findall('result')
    description = code[0].find('description').text
    result = code[0].find('code').text
    
    if result == '200':
        text = u'Переключено'
            
    elif result == '101':
        text = u'Неверный пароль'
        
    elif result == '404':
        text = u'Номер не найден'
    else:
        text = u'Что-то пошло не так!'
    
    tkMessageBox.showinfo('AZAZA', text)
    
    
    
def Nofreez_check():                                         #указать этот эвент в кнопке, если не охота наблюдать фризы её
    root.after(100, Check)

btn_check = Button(root,                                     #кнопка проверки
             text=u"Проверить",     
             width=11,height=1,    
             bg="white",fg="black", command=Check) 
             
btn_switch = Button(root,                                    #кнопка переключения
             text=u"Переключить",     
             width=11,height=1,    
             bg="white",fg="black", command=Switch) 
             
phone_entry = Entry(root, width=14, borderwidth=2)                          #номер телефона
password_entry = Entry(root, width=14, borderwidth=2 )                       #пароль

label_phone = Label(root, text=u'Номер телефона')                            #лейблы
label_password = Label(root, text=u'Пароль')

choice = IntVar()
rbut_phone = Radiobutton(root, text=u'Телефон', variable=choice, value=1)                #радиобаттоны
rbut_sip = Radiobutton(root, text=u'Мультифон (SIP)', variable=choice, value=2)
rbut_phone_sip = Radiobutton(root, text=u'Телефон и SIP', variable=choice, value=3)

#btn_check.bind("<Button-1>", Check)      

                   
btn_check.place(x=2, y=3)
btn_switch.place(x=2, y=40)
phone_entry.place(x=2, y=80)
label_phone.place(x=100, y=80)
password_entry.place(x=2, y=120)
label_password.place(x=100, y=120)
rbut_phone.place(x=2, y=160)
rbut_sip.place(x=2, y=180)
rbut_phone_sip.place(x=2, y=200)
root.mainloop()
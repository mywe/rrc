import os
import datetime

CSS_DEFINE = '''<style> \n
	table.table1 \n
	{ \n
		font-family: \"Trebuchet MS\", sans-serif; \n
		font-size: 13px; \n
		font-weight: bold; \n
		line-height: 1.2em; \n
		font-style: normal; \n
		border-collapse:separate; \n
	} \n
	.table1 thead th \n
	{ \n
		padding:15px;\n
		color:#fff;\n
		text-shadow:1px 1px 1px #568F23;\n
		border:1px solid #93CE37; \n
		border-bottom:3px solid #9ED929;\n
		background-color:#9DD929;\n
		background:-webkit-gradient\n
				   ( \n
				   linear,\n
				   left bottom,\n
				   left top,\n
				   color-stop(0.02, rgb(123,192,67)),\n
				   color-stop(0.51, rgb(139,198,66)),\n
				   color-stop(0.87, rgb(158,217,41))\n
				   );\n
		background: -moz-linear-gradient \n
					(\n
					center bottom,\n
					rgb(123,192,67) 2%,\n
					rgb(139,198,66) 51%,\n
					rgb(158,217,41) 87%\n
					);\n
		-webkit-border-top-left-radius:5px;\n
		-webkit-border-top-right-radius:5px;\n
		-moz-border-radius:5px 5px 0px 0px;\n
		border-top-left-radius:5px;\n
		border-top-right-radius:5px;\n
	}\n
	.table1 thead th:empty\n
	{\n
	background:transparent;\n
	border:none;\n
	}\n
	.table1 tbody th\n
	{\n
		color:#fff;\n
		text-shadow:1px 1px 1px #568F23;\n
		background-color:#9DD929;\n
		border:1px solid #93CE37;\n
		border-right:3px solid #9ED929;\n
		padding:0px 10px;\n
		background:-webkit-gradient\n
				   (\n
				   linear,\n
				   left bottom,\n
				   right top,\n
				   color-stop(0.02, rgb(158,217,41)),\n
				   color-stop(0.51, rgb(139,198,66)),\n
				   color-stop(0.87, rgb(123,192,67))\n
				   );\n
		background: -moz-linear-gradient\n
					(\n
					left bottom,\n
					rgb(158,217,41) 2%,\n
					rgb(139,198,66) 51%,\n
					rgb(123,192,67) 87%\n
					);\n
		-moz-border-radius:5px 0px 0px 5px;\n
		-webkit-border-top-left-radius:5px;\n
		-webkit-border-bottom-left-radius:5px;\n
		border-top-left-radius:5px;\n
		border-bottom-left-radius:5px;\n
	}\n
	.table1 tbody td\n
	{\n
	padding:10px;\n
	text-align:center;\n
	background-color:#DEF3CA;\n
	border: 2px solid #E7EFE0;\n
	-moz-border-radius:2px;\n
	-webkit-border-radius:2px;\n
	border-radius:2px;\n
	color:#666;\n
	text-shadow:1px 1px 1px #fff;\n
	}\n
	</style>\n
		</head>\n
		<style>\n
		*{\n
	margin:0;\n
	padding:0;\n
	}\n
	body\n
	{\n
		height: 100%\n
		font-family: Georgia, serif;\n
		font-size: 20px;\n
		font-style: normal;\n
		font-weight: normal;\n
		letter-spacing: normal;\n
		background: #ffffff;\n
		border-left:20px solid #1D81B6;\n
		-moz-box-shadow:0px 0px 16px #aaa;\n
	}\n
	#content\n
	{\n
		background-color:#fff;\n
		width:auto;\n
		padding:40px;\n
		margin:0 auto;\n
	}\n
	.head\n
	{\n
		font-family:\"Trebuchet MS\",sans-serif;\n
		color:#1D81B6;\n
		font-weight:normal;\n
		font-size:40px;\n
		font-style:normal;\n
		letter-spacing:3px;\n
		border-bottom:3px solid #f0f0f0;\n
		padding-bottom:10px;\n
		margin-bottom:10px;\n
	}\n
	.head a\n
	{\n
		color:#1D81B6;\n
		text-decoration:none;\n
		float:right;\n
		text-shadow:1px 1px 1px #888;\n
	}\n
	.head a:hover\n
	{\n
	color:#f0f0f0;\n
	}\n
	#content h1\n
	{\n
		font-family:\"Trebuchet MS\",sans-serif;\n
		color:#1D81B6;\n
		font-weight:normal;\n
		font-style:normal;\n
		font-size:40px;\n
		text-shadow:1px 1px 1px #aaa;\n
	}\n
	#content h2\n
	{\n
		font-family:\"Trebuchet MS\",sans-serif;\n
		font-size:15px;\n
		font-style:normal;\n
		background-color:#f0f0f0;\n
		margin:40px 0px 30px -40px;\n
		padding:0px 40px;\n
		clear:both;\n
		width:37%;\n
		color:#aaa;\n
		text-shadow:1px 1px 1px #fff;\n
	}\n
	#footer\n
	{\n
		font-family:Helvetica,Arial,Verdana;\n
		text-transform:uppercase;\n
		font-size:10px;\n
		font-style:normal;\n
		background-color:#f0f0f0;\n
		padding-top:10px;\n
		padding-bottom:10px;\n
	}\n
	.white_content{\n
	display: none;\n
	position: absolute;\n
	top: 25%;  left: 25%;\n
	width: 50%;\n
	height: 50%;\n
	padding: 16px;\n
	border: 1px solid black;\n
	background-color: white;\n
	z-index:1002;\n
	overflow:auto\n
	}\n
	.big_white_content{\n
	display: none;\n
	position: absolute;\n
	top: 10%;  left: 10%;\n
	width: 80%;\n
	height: 80%;\n
	padding: 16px;\n
	border: 1px solid black;\n
	background-color: white;\n
	z-index:1002;\n
	overflow:auto\n
	}\n
	</style>\n
	<body id=\"body\">\n
	<div id=\"content\" style=\"text-align:center\">\n
	<a class=\"back\" href=\"\"></a>\n
	<span class=\"scroll\"></span>\n
	<p class=\"head\">\n
	TOPN问题智能分析工具\n
	</p>\n'''

AXIS_DEFINE_BYHOUR = '''function drawAxis(){\n
		ctx.beginPath();\n
		ctx.moveTo(20,320);\n
		ctx.lineTo(470,320);\n
		ctx.stroke();\n
		ctx.moveTo(20,320);\n
		ctx.lineTo(20,30);\n
		ctx.lineTo(17,38);\n
		ctx.lineTo(23,38);\n
		ctx.lineTo(20,30);\n
		ctx.stroke();\n
		ctx.moveTo(470,320);\n
		ctx.lineTo(470,30);\n
		ctx.lineTo(467,40);\n
		ctx.lineTo(473,40);\n
		ctx.lineTo(470,30);\n
		ctx.stroke();\n
		for (var i=1; i<=24; i++)\n
		{\n
			ctx.fillText(i, 20 + 18*i, 335);\n
		}\n
		ctx.fillText(\"/h\",465,335);\n
	}'''

AXIS_DEFINE_BYDIST = '''function drawAxis()\n
	{\n
		ctx.strokeStyle='rgba(33,33,33,1)';\n
		ctx.beginPath();\n
		ctx.moveTo(20,320);\n
		ctx.lineTo(620,320);\n
		ctx.stroke();\n
		ctx.moveTo(20,320);\n
		ctx.lineTo(20,30);\n
		ctx.lineTo(17,38);\n
		ctx.lineTo(23,38);\n
		ctx.lineTo(20,30);\n
		ctx.stroke();\n
		ctx.moveTo(620,320);\n
		ctx.lineTo(620,30);\n
		ctx.lineTo(617,38);\n
		ctx.lineTo(623,38);\n
		ctx.lineTo(620,30);\n
		ctx.stroke();\n
		var j=0;\n
		var i=0;\n
		for (;i<3000;)\n
		{\n
			ctx.fillText(i, 20+27*j, 335);\n
			i=i+200;\n
			j=j+1;\n
		}\n
		for(;i<=9000;)\n
		{\n
			ctx.fillText(i,23+27*j,335);\n
			i=i+1000;\n
			j++;\n
		}\n
		ctx.fillText(\"/m\",620,335);\n
	}'''

clr = ["\"Red\"","\"Blue\"","\"ForestGreen\"","\"Black\"","\"LawnGreen\"","\"Purple\"","\"Green\"","\"Violet\"","\"Sienna\"","\"GoldenRod\""]

def getHtmlHead(cellID):
	htmlHead = '<html>\n<head>\n'
	htmlHead = htmlHead + '<title>' + cellID + '</title>\n'
	htmlHead = htmlHead + '<meta http-equiv=\"Content-Type\" content=\"text/html; charset=UTF-8\"/>\n'
	htmlHead = htmlHead + CSS_DEFINE
	return htmlHead

def getDropReasonTable(cellID, cellName, dropResons):
	htmlDropReason = '<h2>' + cellID + '_' + cellName + '_' + '掉话原因</h2>\n'
	htmlDropReason = htmlDropReason + '<div>\n<table>\n<tr>\n<td>\n<div style=\'fixed:left\'>\n<table>\n<tr>\n'
	dropResonList = dropResons.split('|')

	htmlDropReason = htmlDropReason + '<td bgcolor=\"#d1d1d1\" style=\"border:5px solid #d1d1d1\">设备类</td>\n'
	if len(dropResonList[0].split('=')[1]) > 0:
		htmlDropReason = htmlDropReason + '<td bgcolor=\"f12339\"; colspan=\"3\" style=\"text-align:center\" '
	else:
		htmlDropReason = htmlDropReason + '<td bgcolor=\"9dd929\"; colspan=\"3\" style=\"text-align:center\" '
	htmlDropReason = htmlDropReason + 'onClick=\"document.getElementById(\'cell1\').style.display=\'block\'\">RSSI问题</td>\n'

	if len(dropResonList[1].split('=')[1]) > 0:
		htmlDropReason = htmlDropReason + "<td bgcolor=\"f12339\"; colspan=\"3\" style=\"text-align:center\" "
	else:
		htmlDropReason = htmlDropReason + "<td bgcolor=\"9dd929\"; colspan=\"3\" style=\"text-align:center\" "
	htmlDropReason = htmlDropReason + "onClick=\"document.getElementById('cell2').style.display='block'\">RSSI主分集不均衡</td>\n"

	if len(dropResonList[2].split('=')[1]) > 0:
		htmlDropReason = htmlDropReason + "<td bgcolor=\"f12339\"; colspan=\"3\" style=\"text-align:center\" "
	else:
		htmlDropReason = htmlDropReason + "<td bgcolor=\"9dd929\"; colspan=\"3\" style=\"text-align:center\" "
	htmlDropReason = htmlDropReason + "onClick=\"document.getElementById('cell3').style.display='block'\">设备告警</td>\n"

	htmlDropReason = htmlDropReason + "</tr>\n<tr>\n<td bgcolor=\"#d1d1d1\" style=\"border:5px solid #d1d1d1\"参数类</td>\n"
	if len(dropResonList[3].split('=')[1]) > 0:
		htmlDropReason = htmlDropReason + "<td bgcolor=\"f12339\"; colspan=\"3\" style=\"text-align:center\" "
	else:
		htmlDropReason = htmlDropReason + "<td bgcolor=\"9dd929\"; colspan=\"3\" style=\"text-align:center\" "
	htmlDropReason = htmlDropReason + "onClick=\"document.getElementById('cell4').style.display='block'\">邻区问题</td>\n"

	if len(dropResonList[4].split('=')[1]) > 0:
		htmlDropReason = htmlDropReason + "<td bgcolor=\"f12339\"; colspan=\"3\" style=\"text-align:center\" "
	else:
		htmlDropReason = htmlDropReason + "<td bgcolor=\"9dd929\"; colspan=\"3\" style=\"text-align:center\" "
	htmlDropReason = htmlDropReason + "onClick=\"document.getElementById('cell5').style.display='block'\">载波不同步</td>\n"

	mmlChangeInfo = dropResonList[5].split('=')[1].split(';')
	if len(mmlChangeInfo) > 0 and mmlChangeInfo[0] == '1':
		htmlDropReason = htmlDropReason + "<td bgcolor=\"f12339\"; colspan=\"3\" style=\"text-align:center\" "
	else:
		htmlDropReason = htmlDropReason + "<td bgcolor=\"9dd929\"; colspan=\"3\" style=\"text-align:center\" "
	htmlDropReason = htmlDropReason + "onClick=\"document.getElementById('cell6').style.display='block'\">参数变化</td>\n"

	htmlDropReason = htmlDropReason + "</tr>\n<tr>\n<td bgcolor=\"#d1d1d1\" style=\"border:5px solid #d1d1d1\">周边基站影响</td>\n"
	if len(dropResonList[6].split('=')[1]) > 0:
		htmlDropReason = htmlDropReason + "<td bgcolor=\"f12339\"; colspan=\"1\" style=\"text-align:center\" "
	else:
		htmlDropReason = htmlDropReason + "<td bgcolor=\"9dd929\"; colspan=\"1\" style=\"text-align:center\" "
	htmlDropReason = htmlDropReason + "onClick=\"document.getElementById('cell7').style.display='block'\">新增载波</td>\n"

	if len(dropResonList[7].split('=')[1]) > 0:
		htmlDropReason = htmlDropReason + "<td bgcolor=\"f12339\"; colspan=\"1\" style=\"text-align:center\" "
	else:
		htmlDropReason = htmlDropReason + "<td bgcolor=\"9dd929\"; colspan=\"1\" style=\"text-align:center\" "
	htmlDropReason = htmlDropReason + "onClick=\"document.getElementById('cell8').style.display='block'\">载波关停</td>\n"

	if len(dropResonList[8].split('=')[1]) > 0:
		htmlDropReason = htmlDropReason + "<td bgcolor=\"f12339\"; colspan=\"3\" style=\"text-align:center\" "
	else:
		htmlDropReason = htmlDropReason + "<td bgcolor=\"9dd929\"; colspan=\"3\" style=\"text-align:center\" "
	htmlDropReason = htmlDropReason + "onClick=\"document.getElementById('cell9').style.display='block'\">载波长期关停</td>\n"

	if len(dropResonList[9].split('=')[1]) > 0:
		htmlDropReason = htmlDropReason + "<td bgcolor=\"f12339\"; colspan=\"1\" style=\"text-align:center\" "
	else:
		htmlDropReason = htmlDropReason + "<td bgcolor=\"9dd929\"; colspan=\"1\" style=\"text-align:center\" "
	htmlDropReason = htmlDropReason + "onClick=\"document.getElementById('cell10').style.display='block'\">载波恢复</td>\n"

	if len(dropResonList[10].split('=')[1]) > 0:
		htmlDropReason = htmlDropReason + "<td bgcolor=\"f12339\"; colspan=\"3\" style=\"text-align:center\" "
	else:
		htmlDropReason = htmlDropReason + "<td bgcolor=\"9dd929\"; colspan=\"3\" style=\"text-align:center\" "
	htmlDropReason = htmlDropReason + "onClick=\"document.getElementById('cell11').style.display='block'\">邻区设备告警</td>\n"

	htmlDropReason = htmlDropReason + "</tr>\n<tr>\n<td bgcolor=\"#d1d1d1\" style=\"border:5px solid #d1d1d1\">覆盖类</td>\n"
	if len(dropResonList[11].split('=')[1]) > 0:
		htmlDropReason = htmlDropReason + "<td bgcolor=\"f12339\"; colspan=\"3\" style=\"text-align:center\" "
	else:
		htmlDropReason = htmlDropReason + "<td bgcolor=\"9dd929\"; colspan=\"3\" style=\"text-align:center\" "
	htmlDropReason = htmlDropReason + "onClick=\"document.getElementById('cell12').style.display='block'\">弱覆盖</td>\n"

	if len(dropResonList[12].split('=')[1]) > 0:
		htmlDropReason = htmlDropReason + "<td bgcolor=\"f12339\"; colspan=\"3\" style=\"text-align:center\" "
	else:
		htmlDropReason = htmlDropReason + "<td bgcolor=\"9dd929\"; colspan=\"3\" style=\"text-align:center\" "
	htmlDropReason = htmlDropReason + "onClick=\"document.getElementById('cell13').style.display='block'\">越区覆盖</td>\n"

	if len(dropResonList[13].split('=')[1]) > 0:
		htmlDropReason = htmlDropReason + "<td bgcolor=\"f12339\"; colspan=\"3\" style=\"text-align:center\" "
	else:
		htmlDropReason = htmlDropReason + "<td bgcolor=\"9dd929\"; colspan=\"3\" style=\"text-align:center\" "
	htmlDropReason = htmlDropReason + "onClick=\"document.getElementById('cell14').style.display='block'\">载波间话务不均衡</td>\n"

	htmlDropReason = htmlDropReason + "</tr>\n<tr>\n<td bgcolor=\"#d1d1d1\" style=\"border:5px solid #d1d1d1\">其他</td>\n"
	if len(dropResonList[14].split('=')[1]) > 0:
		htmlDropReason = htmlDropReason + "<td bgcolor=\"f12339\"; colspan=\"3\" style=\"text-align:center\" "
	else:
		htmlDropReason = htmlDropReason + "<td bgcolor=\"9dd929\"; colspan=\"3\" style=\"text-align:center\" "
	htmlDropReason = htmlDropReason + "onClick=\"document.getElementById('cell15').style.display='block'\">用户行为导致高掉话</td>\n"

	if len(dropResonList[15].split('=')[1]) > 0:
		htmlDropReason = htmlDropReason + "<td bgcolor=\"f12339\"; colspan=\"3\" style=\"text-align:center\" "
	else:
		htmlDropReason = htmlDropReason + "<td bgcolor=\"9dd929\"; colspan=\"3\" style=\"text-align:center\" "
	htmlDropReason = htmlDropReason + "onClick=\"document.getElementById('cell16').style.display='block'\">A2掉话高</td>\n"

	if len(dropResonList[16].split('=')[1]) > 0:
		htmlDropReason = htmlDropReason + "<td bgcolor=\"f12339\"; colspan=\"3\" style=\"text-align:center\" "
	else:
		htmlDropReason = htmlDropReason + "<td bgcolor=\"9dd929\"; colspan=\"3\" style=\"text-align:center\" "
	htmlDropReason = htmlDropReason + "onClick=\"document.getElementById('cell17').style.display='block'\">终端问题或隐性故障</td>\n"

	htmlDropReason = htmlDropReason + "</tr>\n</table>\n</div>\n</td>\n"
	return htmlDropReason

def getCellSwitchInfo(cellID):
	cellIDInfo = cellID.split('_')
	fileName = 'result/' + 'BSC'
	fileName = fileName + cellIDInfo[0] + '所有切换关系输出结果.txt'

	srcFile = open(fileName, 'r')
	keyWord = '源小区'
	bFound = False
	switchInfos = []
	switchTitle = []
	splitCh = ''
	for line in srcFile.readlines():
		if bFound == False and line.find(keyWord) == -1:
			continue
		elif bFound == False and line.find(keyWord) != -1:
			bFound = True
			splitCh = line[line.find(keyWord) + len(keyWord)]
			switchTitle = line.split(splitCh)
			continue
		else:
			lineInfo = line.split(splitCh)
			nSize = len(lineInfo)
			if lineInfo[0] == cellID and lineInfo[nSize - 4] != '不调整':
				switchInfos.append(lineInfo)

	srcFile.close()
	
	result = ""
	if len(switchInfos) == 0:
		return result

	result = result + "<td colspan=\"2\">\n<table class=\"table1\">\n<thead>\n"

	for info in switchTitle:
		result = result + "<th>" + info + "</th>\n"
	result = result + "</thead>\n<tbody>\n"
	for infos in switchInfos:
		result = result + "<tr>\n"
		for i in range(0, len(infos) - 2):
			result = result + "<td>" + infos[i] + "</td>\n"
		result = result + "</tr>\n"
	result = result + "</tbody>\n</table>\n</td>\n"
	return result

def getMMLChangeInfo(mmlInfo):
	result = "<td colspan=\"2\">\n<table class=\"table1\">\n<thead>\n"
	result = result + "<th>基站名称</th>\n"
	result = result + "<th>服务类型</th>\n"
	result = result + "<th>指配门限</th>\n"
	result = result + "<th>硬指配业务优先类型</th>\n"
	result = result + "<th>射频增益</th>\n"
	result = result + "<th>基带增益</th>\n"
	result = result + "<th>导频信道增益</th>\n"
	result = result + "<th>是否驻留</th>\n"
	result = result + "<th>twoway数量</th>\n"
	result = result + "<th>激活集搜索窗</th>\n"
	result = result + "<th>相邻集搜索窗</th>\n"
	result = result + "<th>TADD</th>\n"
	result = result + "<th>TDROP</th>\n"
	result = result + "<th>PN复用距离</th>\n"
	result = result + "</thead>\n<tbody>\n"
	result = result + "<tr>\n"

	mmlInfoList = mmlInfo.split(';')
	nSize = len(mmlInfoList)
	for i in range(1, nSize):
		result = result + "<td>" + mmlInfoList[i] + "</td>\n"

	result = result + "</tr>\n"
	result = result + "</tbody>\n</table>\n</td>\n"

	return result

def genTendencyChartByH(countByH, color):
	result = ""

	if len(countByH) == 0:
		return result

	vals = []
	for val in countByH:
		vals.append(float(val))

	maxVal = max(vals)
	minVal = min(vals)

	xByH = []
	yByH = []

	nSize = len(vals)
	for i in range(0, nSize):
		xByH.append(20 + 18 * (i + 1))
		if maxVal == minVal:
			yByH.append(310)
		else:
			yByH.append(310 - ((vals[i] - minVal) / (maxVal - minVal)) * 270)
	
	result = result + "ctx.strokeStyle=" + color + ";\n"
	result = result + "ctx.fillStyle=" + color + ";\n"
	result = result + "ctx.beginPath();\n";
	result = result + "ctx.moveTo(" + str(xByH[0]) + "," + str(yByH[0]) + ");\n"
	result = result + "ctx.fillText(" + str(vals[0]) + "," + str(xByH[0]) + "," + str(yByH[0] - 3) + ");\n"
	for i in range(1, nSize):
		result = result + "ctx.lineTo(" + str(xByH[i]) + "," + str(yByH[i]) + ");\n"
		result = result + "ctx.fillText(" + str(vals[i]) + "," + str(xByH[i]) + "," + str(yByH[i] - 3) + ");\n"
	result = result + "ctx.stroke();\n"

	return result

def getCanvasByH(infoByH, index):
	result = "<td bgcolor=\"#DEF3CA\">\n<div style='float:left'>\n"
	result = result + "<canvas width='650' height='340' id='canvas" + str(index) + "'>\n"
	result = result + "</canvas>\n<script>\n"
	result = result + "var canvas=document.getElementById('canvas" + str(index) + "');\n"
	result = result + "var ctx=canvas.getContext('2d');\n" + AXIS_DEFINE_BYHOUR + "\n"
	result = result + "function drawChart(){\nctx.save();\n"

	clrIdx = 0
	xPos = 5
	idx = -1
	i = 0
	for info in infoByH:
		if info[0].find('掉话次数') != -1:
			idx = i
			break
		else:
			i = i + 1

	if idx != -1:
		result = result + genTendencyChartByH(infoByH[idx][1:], clr[clrIdx])
		result = result + "ctx.fillStyle=" + clr[clrIdx] + ";\n"
		result = result + "ctx.fillRect(" + str(xPos) + ",10,10,10);\n"
		result = result + "ctx.fillText(\"" + infoByH[idx][0] + "\"," + str(xPos + 15) + ",20);\n"
		xPos = xPos + 180
		clrIdx = clrIdx + 1

	for info in infoByH:
		if info[0].find('掉话次数') != -1:
			continue

		result = result + genTendencyChartByH(info[1:], clr[clrIdx])
		result = result + "ctx.fillStyle=" + clr[clrIdx] + ";\n"
		result = result + "ctx.fillRect(" + str(xPos) + ",10,10,10);\n"
		result = result + "ctx.fillText(\"" + info[0] + "\"," + str(xPos + 15) + ",20);\n"
		xPos = xPos + 180
		clrIdx = clrIdx + 1

	result = result + "ctx.restore();\n}function draw(){\nctx.clearRect(0,0,canvas.width,canvas.height);\nctx.save();\ndrawAxis();\n"
	result = result + "drawChart();\nctx.restore();\n}\nctx.fillStyle='rgba(100,140,230,1)';\nctx.strokeStyle='rgba(33,33,33,1)';\ndraw();\n</script>\n</div>\n</td>\n"

	return result

def getTendencyChartByD(countByD, color):
	result = ""
	if len(countByD) == 0:
		return result

	vals = []
	for val in countByD:
		vals.append(float(val))

	maxVal = max(vals)
	minVal = min(vals)

	xByH = []
	yByH = []

	nSize = len(vals)
	for i in range(0, nSize):
		xByH.append(20 + 27 * i)
		if maxVal == minVal:
			yByH.append(310)
		else:
			yByH.append(310 - ((vals[i] - minVal) / (maxVal - minVal)) * 270)

	result = result + "ctx.strokeStyle=" + color + ";\n"
	result = result + "ctx.fillStyle=" + color + ";\n"
	result = result + "ctx.beginPath();\n"
	result = result + "ctx.moveTo(" + str(xByH[0]) + "," + str(yByH[0]) + ");\n"
	result = result + "ctx.fillText(" + str(vals[0]) + "," + str(xByH[0]) + "," + str(yByH[0] - 3) + ");\n"
	for i in range(1, nSize):
		result = result + "ctx.lineTo(" + str(xByH[i]) + "," + str(yByH[i]) + ");\n"
		result = result + "ctx.fillText(" + str(vals[i]) + "," + str(xByH[i]) + "," + str(yByH[i] - 3) + ");\n"
	result = result + "ctx.stroke();\n"
	return result

def getCanvasByD(infoByD, index):
	result = "<td bgcolor=\"#DEF3CA\">\n<div style='float:left'>\n"
	result = result + "<canvas width='650' height='340' id='canvas" + str(index) + "'>\n"
	result = result + "</canvas>\n<script>\n"
	result = result + "var canvas=document.getElementById('canvas" + str(index) + "');\n"
	result = result + "var ctx=canvas.getContext('2d');\n" + AXIS_DEFINE_BYDIST + "\n"
	result = result + "function drawChart(){\nctx.save();\n"

	clrIdx = 0
	xPos = 5
	idx = -1
	i = 0
	for info in infoByD:
		if info[0].find('掉话次数') != -1:
			idx = i
			break
		else:
			i = i + 1

	if idx != -1:
		result = result + getTendencyChartByD(infoByD[idx][1:], clr[clrIdx])
		result = result + "ctx.fillStyle=" + clr[clrIdx] + ";\n"
		result = result + "ctx.fillRect(" + str(xPos) + ",10,10,10);\n"
		result = result + "ctx.fillText(\"" + infoByD[idx][0] + "\"," + str(xPos + 15) + ",20);\n"
		xPos = xPos + 180
		clrIdx = clrIdx + 1

	for info in infoByD:
		if info[0].find('掉话次数') != -1:
			continue

		result = result + getTendencyChartByD(info[1:], clr[clrIdx])
		result = result + "ctx.fillStyle=" + clr[clrIdx] + ";\n"
		result = result + "ctx.fillRect(" + str(xPos) + ",10,10,10);\n"
		result = result + "ctx.fillText(\"" + info[0] + "\"," + str(xPos + 15) + ",20);\n"
		xPos = xPos + 180
		clrIdx = clrIdx + 1

	result = result + "ctx.restore();\n}function draw(){\nctx.clearRect(0,0,canvas.width,canvas.height);\nctx.save();\ndrawAxis();\n"
	result = result + "drawChart();\nctx.restore();\n}\nctx.fillStyle='rgba(100,140,230,1)';\nctx.strokeStyle='rgba(33,33,33,1)';\ndraw();\n</script>\n</div>\n</td>\n"

	return result

def getRssiInfoByH(cellInfos):
	RSSIByH = []
	for cellInfo in cellInfos:
		if cellInfo[0] == 'CDR掉话次数':
			info = ['掉话次数']
			for i in range(31, 55):
				info.append(cellInfo[i])
			RSSIByH.append(info)
		elif cellInfo[0] == 'RSSI主集':
			info = ['RSSI主集']
			for i in range(31, 55):
				info.append(cellInfo[i])
			RSSIByH.append(info)
		elif cellInfo[0] == 'RSSI分集':
			info = ['RSSI分集']
			for i in range(31, 55):
				info.append(cellInfo[i])
			RSSIByH.append(info)
	return RSSIByH

def getAlarmInfoByH(cellInfos):
	bFound = False
	alarmInfos = []
	alarmType = []
	alarmInfo = []
	for info in cellInfos:
		if info[0] == '告警次数':
			alarmInfo = info
			break

	if len(alarmInfo) == 0:
		return alarmInfos
	for i in range(31, 55):
		if len(alarmInfo[i]) == 0:
			continue
		infoList = alarmInfo[i].split(';')
		for info in infoList:
			if len(info) == 0:
				continue
			alarm = info.split(':')

			if alarm[0] not in alarmType:
				alarmType.append(alarm[0])
				tmpAlarm = ['0' for j in range(0, 25)]
				tmpAlarm[0] = alarm[0]
				alarmInfos.append(tmpAlarm)

			idx = alarmType.index(alarm[0])
			alarmInfos[idx][i - 30] = alarm[1]

	return alarmInfos

def getDroReasonDialog(dropResons, cellInfos, index):
	dropResonList = dropResons.split('|')

	rssiByH = getRssiInfoByH(cellInfos)

	resultHtml = "<div id=\"cell1\" class=\"white_content\">\n"
	resultHtml = resultHtml + "<a href=\"#\" onClick=\"document.getElementById('cell1').style.display='none'\" style=\"color:black;z-index:9999\">Close</a>\n"
	resultHtml = resultHtml + "<table>\n<tr>\n" + "<td bgcolor=\"#d1d1d1\" style=\"border:5px solid #d1d1d1\">规则</td>\n"
	resultHtml = resultHtml + "<td bgcolor=\"9dd929\" style=\"text-align:center\">从CDR中解码获得的RSSI全天掉话平均值、从性能数据解码获得的RSSI主集全天均值或者RSSI分集全天均值中任何一个>-93</td>"
	resultHtml = resultHtml + "</tr>\n<tr>\n<td bgcolor=\"#d1d1d1\" style=\"border:5px solid #d1d1d1\">内容</td>\n"
	resultHtml = resultHtml + getCanvasByH(rssiByH,index)
	index = index + 1
	resultHtml = resultHtml + "</tr>\n</table></div>\n"

	resultHtml = resultHtml + "<div id=\"cell2\" class=\"white_content\">\n"
	resultHtml = resultHtml + "<a href=\"#\" onClick=\"document.getElementById('cell2').style.display='none'\" style=\"color:black;z-index:9999\">Close</a>\n"
	resultHtml = resultHtml + "<table>\n<tr>\n" + "<td bgcolor=\"#d1d1d1\" style=\"border:5px solid #d1d1d1\">规则</td>\n"
	resultHtml = resultHtml + "<td bgcolor=\"9dd929\" style=\"text-align:center\">性能数据中得出的RSSI全天主集平均值和全天分集平均值差距超过5dbm</td>"
	resultHtml = resultHtml + "</tr>\n<tr>\n<td bgcolor=\"#d1d1d1\" style=\"border:5px solid #d1d1d1\">内容</td>\n"
	resultHtml = resultHtml + getCanvasByH(rssiByH,index)
	index = index + 1
	resultHtml = resultHtml + "</tr>\n</table></div>\n"

	resultHtml = resultHtml + "<div id=\"cell3\" class=\"white_content\">\n"
	resultHtml = resultHtml + "<a href=\"#\" onClick=\"document.getElementById('cell3').style.display='none'\" style=\"color:black;z-index:9999\">Close</a>\n"
	resultHtml = resultHtml + "<table>\n<tr>\n" + "<td bgcolor=\"#d1d1d1\" style=\"border:5px solid #d1d1d1\">规则</td>\n"
	resultHtml = resultHtml + "<td bgcolor=\"9dd929\" style=\"text-align:center\">全网1187条告警类型分为CE不足、锁星问题、传输问题、RSSI问题、小区退服、驻波比问题、不影响业务告警和其他告警8大类</td>"
	resultHtml = resultHtml + "</tr>\n<tr>\n<td bgcolor=\"#d1d1d1\" style=\"border:5px solid #d1d1d1\">内容</td>\n"
	idx = -1
	nSize = len(rssiByH)
	if nSize > 0:
		for i in range(0, nSize):
			if rssiByH[i] == '掉话次数':
				idx = i
				break
	alarmInfos = getAlarmInfoByH(cellInfos)
	if idx != -1:
		alarmInfos.append(rssiByH[idx])
	resultHtml = resultHtml + getCanvasByH(alarmInfos, index)
	resultHtml = resultHtml + "</tr>\n</table></div>\n"

	resultHtml = resultHtml + "<div id=\"cell4\" class=\"big_white_content\">\n"
	resultHtml = resultHtml + "<a href=\"#\" onClick=\"document.getElementById('cell4').style.display='none'\" style=\"color:black;z-index:9999\">Close</a>\n"
	resultHtml = resultHtml + "<table>\n<tr>\n" + "<td bgcolor=\"#d1d1d1\" style=\"border:5px solid #d1d1d1\">规则</td>\n"
	resultHtml = resultHtml + "<td bgcolor=\"9dd929\" style=\"text-align:center\">根据PSMM结果显示建议调整的邻区</td>"
	resultHtml = resultHtml + "</tr>\n<tr>\n<td bgcolor=\"#d1d1d1\" style=\"border:5px solid #d1d1d1\">内容</td>\n"
	if len(dropResonList[3].split('=')[1]) > 0:
		resultHtml = resultHtml + getCellSwitchInfo(cellInfos[0][1])
	else:
		resultHtml = resultHtml + "<td>\n无</td>\n"
	resultHtml = resultHtml + "</tr>\n</table></div>\n"

	resultHtml = resultHtml + "<div id=\"cell5\" class=\"white_content\">\n"
	resultHtml = resultHtml + "<a href=\"#\" onClick=\"document.getElementById('cell5').style.display='none'\" style=\"color:black;z-index:9999\">Close</a>\n"
	resultHtml = resultHtml + "<table>\n<tr>\n" + "<td bgcolor=\"#d1d1d1\" style=\"border:5px solid #d1d1d1\">规则</td>\n"
	resultHtml = resultHtml + "<td bgcolor=\"9dd929\" style=\"text-align:center\">283频点的邻区不在201频点的邻区中</td>"
	resultHtml = resultHtml + "</tr>\n<tr>\n<td bgcolor=\"#d1d1d1\" style=\"border:5px solid #d1d1d1\">内容</td>\n"
	dropReason = dropResonList[4].split('=')[1]
	if len(dropReason) > 0:
		resultHtml = resultHtml + "<td>\n" + dropReason + "</td>\n"
	else:
		resultHtml = resultHtml + "<td>\n无</td>\n"
	resultHtml = resultHtml + "</tr>\n</table></div>\n"

	resultHtml = resultHtml + "<div id=\"cell6\" class=\"big_white_content\">\n"
	resultHtml = resultHtml + "<a href=\"#\" onClick=\"document.getElementById('cell6').style.display='none'\" style=\"color:black;z-index:9999\">Close</a>\n"
	resultHtml = resultHtml + "<table>\n<tr>\n" + "<td bgcolor=\"#d1d1d1\" style=\"border:5px solid #d1d1d1\">规则</td>\n"
	resultHtml = resultHtml + "<td bgcolor=\"9dd929\" style=\"text-align:center\">当前各项软参与昨日对比发生变化，以红色提醒某项变化的参数可能影响TOPN结果，并显示各项参数值</td>"
	resultHtml = resultHtml + "</tr>\n<tr>\n<td bgcolor=\"#d1d1d1\" style=\"border:5px solid #d1d1d1\">内容</td>\n"
	resultHtml = resultHtml + getMMLChangeInfo(dropResonList[5].split('=')[1])
	resultHtml = resultHtml + "</tr>\n</table></div>\n"

	resultHtml = resultHtml + "<div id=\"cell7\" class=\"white_content\">\n"
	resultHtml = resultHtml + "<a href=\"#\" onClick=\"document.getElementById('cell7').style.display='none'\" style=\"color:black;z-index:9999\">Close</a>\n"
	resultHtml = resultHtml + "<table>\n<tr>\n" + "<td bgcolor=\"#d1d1d1\" style=\"border:5px solid #d1d1d1\">规则</td>\n"
	resultHtml = resultHtml + "<td bgcolor=\"9dd929\" style=\"text-align:center\">MML中新增的载波有用户呼叫记录</td>"
	resultHtml = resultHtml + "</tr>\n<tr>\n<td bgcolor=\"#d1d1d1\" style=\"border:5px solid #d1d1d1\">内容</td>\n"
	dropReason = dropResonList[6].split('=')[1]
	if len(dropReason) > 0:
		resultHtml = resultHtml + "<td>\n" + dropReason + "</td>\n"
	else:
		resultHtml = resultHtml + "<td>\n无</td>\n"
	resultHtml = resultHtml + "</tr>\n</table></div>\n"

	resultHtml = resultHtml + "<div id=\"cell8\" class=\"white_content\">\n"
	resultHtml = resultHtml + "<a href=\"#\" onClick=\"document.getElementById('cell8').style.display='none'\" style=\"color:black;z-index:9999\">Close</a>\n"
	resultHtml = resultHtml + "<table>\n<tr>\n" + "<td bgcolor=\"#d1d1d1\" style=\"border:5px solid #d1d1d1\">规则</td>\n"
	resultHtml = resultHtml + "<td bgcolor=\"9dd929\" style=\"text-align:center\">"
	resultHtml = resultHtml +"全天全网中9-22点间有任何一个小时出现某个载波性能呼叫次数为0，并且该载波该小时的呼叫次数标准值不是0。该载波优先级前10的邻区则可能受到该载波的影响，并计算该载波掉话次数与半个月来排名第10位的高掉话次数的比值，如果比值>2，则认为掉话指标恶化"
	resultHtml = resultHtml + "</td>" + "</tr>\n<tr>\n<td bgcolor=\"#d1d1d1\" style=\"border:5px solid #d1d1d1\">内容</td>\n"
	dropReason = dropResonList[7].split('=')[1]
	if len(dropReason) > 0:
		resultHtml = resultHtml + "<td>\n" + dropReason + "</td>\n"
	else:
		resultHtml = resultHtml + "<td>\n无</td>\n"
	resultHtml = resultHtml + "</tr>\n</table></div>\n"

	resultHtml = resultHtml + "<div id=\"cell9\" class=\"white_content\">\n"
	resultHtml = resultHtml + "<a href=\"#\" onClick=\"document.getElementById('cell9').style.display='none'\" style=\"color:black;z-index:9999\">Close</a>\n"
	resultHtml = resultHtml + "<table>\n<tr>\n" + "<td bgcolor=\"#d1d1d1\" style=\"border:5px solid #d1d1d1\">规则</td>\n"
	resultHtml = resultHtml + "<td bgcolor=\"9dd929\" style=\"text-align:center\">某载波全天呼叫次数为0，且半个月来该载波全天总呼叫次数的平均值不为0，则该载波优先级前10的邻区可能受该载波长期关停影响</td>"
	resultHtml = resultHtml + "</tr>\n<tr>\n<td bgcolor=\"#d1d1d1\" style=\"border:5px solid #d1d1d1\">内容</td>\n"
	dropReason = dropResonList[8].split('=')[1]
	if len(dropReason) > 0:
		resultHtml = resultHtml + "<td>\n" + dropReason + "</td>\n"
	else:
		resultHtml = resultHtml + "<td>\n无</td>\n"
	resultHtml = resultHtml + "</tr>\n</table></div>\n"

	resultHtml = resultHtml + "<div id=\"cell10\" class=\"white_content\">\n"
	resultHtml = resultHtml + "<a href=\"#\" onClick=\"document.getElementById('cell10').style.display='none'\" style=\"color:black;z-index:9999\">Close</a>\n"
	resultHtml = resultHtml + "<table>\n<tr>\n" + "<td bgcolor=\"#d1d1d1\" style=\"border:5px solid #d1d1d1\">规则</td>\n"
	resultHtml = resultHtml + "<td bgcolor=\"9dd929\" style=\"text-align:center\">如果长期关停的载波后来在CDR中有呼叫记录，并且该载波的邻区与原来的邻区有5个以上相同，则载波优先级前10的邻区可能受到该载波恢复的影响。</td>"
	resultHtml = resultHtml + "</tr>\n<tr>\n<td bgcolor=\"#d1d1d1\" style=\"border:5px solid #d1d1d1\">内容</td>\n"
	dropReason = dropResonList[9].split('=')[1]
	if len(dropReason) > 0:
		resultHtml = resultHtml + "<td>\n" + dropReason + "</td>\n"
	else:
		resultHtml = resultHtml + "<td>\n无</td>\n"
	resultHtml = resultHtml + "</tr>\n</table></div>\n"

	resultHtml = resultHtml + "<div id=\"cell11\" class=\"white_content\">\n"
	resultHtml = resultHtml + "<a href=\"#\" onClick=\"document.getElementById('cell11').style.display='none'\" style=\"color:black;z-index:9999\">Close</a>\n"
	resultHtml = resultHtml + "<table>\n<tr>\n" + "<td bgcolor=\"#d1d1d1\" style=\"border:5px solid #d1d1d1\">规则</td>\n"
	resultHtml = resultHtml + "<td bgcolor=\"9dd929\" style=\"text-align:center\">全网1187条告警类型分为CE不足、锁星问题、传输问题、RSSI问题、小区退服、驻波比问题、不影响业务告警和其他告警8大类</td>"
	resultHtml = resultHtml + "</tr>\n<tr>\n" + "<td bgcolor=\"#d1d1d1\" style=\"border:5px solid #d1d1d1\">内容</td>\n"
	dropReason = dropResonList[10].split('=')[1]
	if len(dropReason) > 0:
		resultHtml = resultHtml + "<td>\n" + dropReason + "</td>\n"
	else:
		resultHtml = resultHtml + "<td>\n无</td>\n"
	resultHtml = resultHtml + "</tr>\n</table></div>\n"

	resultHtml = resultHtml + "<div id=\"cell12\" class=\"white_content\">\n"
	resultHtml = resultHtml + "<a href=\"#\" onClick=\"document.getElementById('cell12').style.display='none'\" style=\"color:black;z-index:9999\">Close</a>\n"
	resultHtml = resultHtml + "<table>\n<tr>\n" + "<td bgcolor=\"#d1d1d1\" style=\"border:5px solid #d1d1d1\">规则</td>\n"
	resultHtml = resultHtml + "<td bgcolor=\"9dd929\" style=\"text-align:center\">平均掉话ECIO 《-14，并且每个距离段中 CDR呼叫次数最大的那个距离掉话次数也是最大</td>"
	resultHtml = resultHtml + "</tr>\n<tr>\n<td bgcolor=\"#d1d1d1\" style=\"border:5px solid #d1d1d1\">内容</td>\n"
	dropReason = dropResonList[11].split('=')[1]
	if len(dropReason) > 0:
		resultHtml = resultHtml + "<td>\n近距离弱覆盖，可能输出功率不足，站点过低或者严重阻挡</td>\n"
	else:
		resultHtml = resultHtml + "<td>\n无</td>\n"
	resultHtml = resultHtml + "</tr>\n</table></div>\n";

	resultHtml = resultHtml + "<div id=\"cell13\" class=\"white_content\">\n"
	resultHtml = resultHtml + "<a href=\"#\" onClick=\"document.getElementById('cell13').style.display='none'\" style=\"color:black;z-index:9999\">Close</a>\n"
	resultHtml = resultHtml + "<table>\n<tr>\n" + "<td bgcolor=\"#d1d1d1\" style=\"border:5px solid #d1d1d1\">规则</td>\n"
	resultHtml = resultHtml + "<td bgcolor=\"9dd929\" style=\"text-align:center\">"
	resultHtml = resultHtml + "根据频点掉话距离降序排序，跟据前一半的距离求平均得出掉话距离参考值。以掉话小区的方位角为中心，以该角度的正负30度，掉话距离参考值画扇形。如果扇形区域内室外站数量大于8，则是越区覆盖。如果扇形区域内室外站数量>8并且ECIO<-10，则是越区覆盖，可能是直放站引起"
	resultHtml = resultHtml + "</td></tr>\n<tr>\n<td bgcolor=\"#d1d1d1\" style=\"border:5px solid #d1d1d1\">内容</td>\n"
	dropReason = dropResonList[12].split('=')[1]
	if len(dropReason) > 0:
		resultHtml = resultHtml + "<td>\n" + dropReason + "</td>\n"
	else:
		resultHtml = resultHtml + "<td>\n无</td>\n"
	resultHtml = resultHtml + "</tr>\n</table></div>\n"

	resultHtml = resultHtml + "<div id=\"cell14\" class=\"white_content\">\n"
	resultHtml = resultHtml + "<a href=\"#\" onClick=\"document.getElementById('cell14').style.display='none'\" style=\"color:black;z-index:9999\">Close</a>\n"
	resultHtml = resultHtml + "<table>\n<tr>\n" + "<td bgcolor=\"#d1d1d1\" style=\"border:5px solid #d1d1d1\">规则</td>\n"
	resultHtml = resultHtml + "<td bgcolor=\"9dd929\" style=\"text-align:center\">同个扇区除数据优先的所有载波的全天呼叫次数中，如果最高次数是最低的两倍以上，则话务不均衡</td>"
	resultHtml = resultHtml + "</tr>\n<tr>\n<td bgcolor=\"#d1d1d1\" style=\"border:5px solid #d1d1d1\">内容</td>\n"
	dropReason = dropResonList[13].split('=')[1]
	if len(dropReason) > 0:
		resultHtml = resultHtml + "<td>\n" + dropReason + "</td>\n"
	else:
		resultHtml = resultHtml + "<td>\n无</td>\n"
	resultHtml = resultHtml + "</tr>\n</table></div>\n"

	resultHtml = resultHtml + "<div id=\"cell15\" class=\"white_content\">\n"
	resultHtml = resultHtml + "<a href=\"#\" onClick=\"document.getElementById('cell15').style.display='none'\" style=\"color:black;z-index:9999\">Close</a>\n"
	resultHtml = resultHtml + "<table>\n<tr>\n" + "<td bgcolor=\"#d1d1d1\" style=\"border:5px solid #d1d1d1\">规则</td>\n"
	resultHtml = resultHtml + "<td bgcolor=\"9dd929\" style=\"text-align:center\">一天内某个载波下某个用户掉话占比超过几个用户掉话总次数的50%或者一天内某个载波下某个呼叫号码掉话次数占比超过所有呼叫号码呼叫掉话次数的50%</td>"
	resultHtml = resultHtml + "</tr>\n<tr>\n<td bgcolor=\"#d1d1d1\" style=\"border:5px solid #d1d1d1\">内容</td>\n"
	dropReason = dropResonList[14].split('=')[1]
	if len(dropReason) > 0:
		resultHtml = resultHtml + "<td>\n" + dropReason + "</td>\n"
	else:
		resultHtml = resultHtml + "<td>\n无</td>\n"
	resultHtml = resultHtml + "</tr>\n</table></div>\n"

	resultHtml = resultHtml + "<div id=\"cell16\" class=\"white_content\">\n"
	resultHtml = resultHtml + "<a href=\"#\" onClick=\"document.getElementById('cell16').style.display='none'\" style=\"color:black;z-index:9999\">Close</a>\n"
	resultHtml = resultHtml + "<table>\n<tr>\n" + "<td bgcolor=\"#d1d1d1\" style=\"border:5px solid #d1d1d1\">规则</td>\n"
	resultHtml = resultHtml + "<td bgcolor=\"9dd929\" style=\"text-align:center\">ERASUARE掉话次数占A2与ERASUARE掉话总次数的比例<90%，则是A2掉话高</td>"
	resultHtml = resultHtml + "</tr>\n<tr>\n" + "<td bgcolor=\"#d1d1d1\" style=\"border:5px solid #d1d1d1\">内容</td>\n"
	dropReason = dropResonList[15].split('=')[1]
	if len(dropReason) > 0:
		resultHtml = resultHtml + "<td>\n" + dropReason + "</td>\n"
	else:
		resultHtml = resultHtml + "<td>\n无</td>\n"
	resultHtml = resultHtml + "</tr>\n</table></div>\n"

	resultHtml = resultHtml + "<div id=\"cell17\" class=\"white_content\">\n"
	resultHtml = resultHtml + "<a href=\"#\" onClick=\"document.getElementById('cell17').style.display='none'\" style=\"color:black;z-index:9999\">Close</a>\n"
	resultHtml = resultHtml + "<table>\n<tr>\n" + "<td bgcolor=\"#d1d1d1\" style=\"border:5px solid #d1d1d1\">规则</td>\n"
	resultHtml = resultHtml + "<td bgcolor=\"9dd929\" style=\"text-align:center\">某个载波全天所有满足RSSI平均值<-93并且全天平均掉话ECIO>-10 的掉话的次数与全天掉话总次数的比例超过60%</td>"
	resultHtml = resultHtml + "</tr>\n<tr>\n" + "<td bgcolor=\"#d1d1d1\" style=\"border:5px solid #d1d1d1\">内容</td>\n"
	resultHtml = resultHtml + "<td>\n无</td>\n"
	resultHtml = resultHtml + "</tr>\n</table></div>\n"
	return resultHtml

def getResult(date, cellID):
	resultFile = open('result/' + date + '.csv', 'r')
	bFound = False
	cellInfos = []
	nLine = 0
	for line in resultFile.readlines():
		infos = line.split(',')
		if bFound == False and infos[1] != cellID:
			continue
		elif infos[1] == cellID:
			cellInfos.append(infos)
			nLine = nLine + 1
			bFound = True
		else:
			break
	resultFile.close()

	html = getHtmlHead(cellID)
	html = html + getDropReasonTable(cellID, cellInfos[0][2], cellInfos[nLine - 1][len(cellInfos[nLine - 1]) - 1])
	html = html + "</table>\n</div>\n"

	index = 1
	dropCountByH = []
	dropCountByD = []
	cellIDInfo = cellID.split('_')
	for info in cellInfos:
		if info[0] == 'CDR掉话次数':
			countByH = ['0' for i in range(0,25)]
			countByD = ['0' for i in range(0,24)]
			countByH[0] = cellIDInfo[4] +'_掉话次数'
			countByD[0] = cellIDInfo[4] +'_掉话次数'
			for i in range(9, 31):
				countByD[i - 8] = info[i]
			for i in range(31, 55):
				countByH[i - 30] = info[i]
			dropCountByH.append(countByH)
			dropCountByD.append(countByD)
		elif info[0] == '呼叫次数':
			countByH = ['0' for i in range(0,25)]
			countByD = ['0' for i in range(0,24)]
			countByH[0] = cellIDInfo[4] +'_呼叫次数'
			countByD[0] = cellIDInfo[4] +'_呼叫次数'
			for i in range(9, 31):
				countByD[i - 8] = info[i]
			for i in range(31, 55):
				countByH[i - 30] = info[i]
			dropCountByH.append(countByH)
			dropCountByD.append(countByD)
	html = html + "<div>\n<table>\n<tr>\n"
	html = html + getCanvasByH(dropCountByH, index)
	index = index + 1
	html = html + getCanvasByD(dropCountByD, index)
	index = index + 1

	ecioByH = []
	ecioByD = []
	for info in cellInfos:
		if info[0] == 'CDR掉话次数':
			countByH = ['0' for i in range(0,25)]
			countByD = ['0' for i in range(0,24)]
			countByH[0] = cellIDInfo[4] +'_掉话次数'
			countByD[0] = cellIDInfo[4] +'_掉话次数'
			for i in range(9, 31):
				countByD[i - 8] = info[i]
			for i in range(31, 55):
				countByH[i - 30] = info[i]
			ecioByH.append(countByH)
			ecioByD.append(countByD)
		elif info[0] == '掉话Ecio':
			countByH = ['0' for i in range(0,25)]
			countByD = ['0' for i in range(0,24)]
			countByH[0] = cellIDInfo[4] +'_掉话Ecio'
			countByD[0] = cellIDInfo[4] +'_掉话Ecio'
			for i in range(9, 31):
				countByD[i - 8] = info[i]
			for i in range(31, 55):
				countByH[i - 30] = info[i]
			ecioByH.append(countByH)
			ecioByD.append(countByD)
		elif info[0] == 'ECIO优良比':
			countByD = ['0' for i in range(0,24)]
			countByD[0] = cellIDInfo[4] +'_ECIO优良比'
			for i in range(9, 31):
				countByD[i - 8] = info[i]
			ecioByD.append(countByD)
	html = html + "</tr>\n<tr>\n"
	html = html + getCanvasByH(ecioByH, index)
	index = index + 1
	html = html + getCanvasByD(ecioByD, index)
	index = index + 1
	html = html + "</tr>\n</table>\n</div>\n"

	html = html + getDroReasonDialog(cellInfos[nLine - 1][len(cellInfos[nLine - 1]) - 1], cellInfos, index)
	html = html + "<div id=\"footer\" style=\"text-align:center\"<p>佛山无线网优中心</p><p>修改建议请联系彭雯婷:18144797979</p></div>\n</body>\n</html>"
	return html

def getTopNCell(date):
	topN = []
	if os.path.exists('result/' + date + 'topNFile.csv') == False:
		return topN

	topNFile = open('result/' + date + 'topNFile.csv', 'r')
	lineIdx = 1
	for line in topNFile.readlines():
		if lineIdx == 1:
			lineIdx = lineIdx + 1
			continue
		lineIdx = lineIdx + 1
		topN.append(line.split(',')[0])
	topNFile.close()
	return topN

def getCellConnectInfo(date, cells):
	cellConnectInfo = []
	if os.path.exists('result/' + date + 'CellConnectInfo.csv') == False:
		return cellConnectInfo

	cellIdxDict = dict()
	for i in range(len(cells)):
		cellIdxDict[cells[i]] = i
		cellConnectInfo.append(list())
	
	cellConnectInfoFile = open('result/' + date + 'CellConnectInfo.csv', 'r')
	for line in cellConnectInfoFile.readlines():
		vecMem = line.split(',')
		if vecMem[0] in cells:
			idx = cellIdxDict[vecMem[0]]
			cellConnectInfo[idx] = vecMem
			cells.remove(vecMem[0])
			if len(cells) == 0:
				break
	cellConnectInfoFile.close()
	return cellConnectInfo

def getTopNCountInMonth(d, cells):
	topNCount = dict()
	for cell in cells:
		topNCount[cell] = 1

	for i in range(-29, 0):
		d1 = d + datetime.timedelta(days=i)
		dStr = d1.strftime('%Y%m%d')
		fileName = 'result/' + dStr + 'topNFile.csv'

		if os.path.exists(fileName) == False:
			continue

		topNFile = open(fileName, 'r')
		for line in topNFile.readlines():
			line = line.split(',')

			if line[0] in cells:
				topNCount[line[0]] += 1

		topNFile.close()
		
	return topNCount
#result = getResult('20150410', '2_1601_1601_1_283')
#testFile = open('test.html','wb')
#testFile.write(result.encode('UTF-8'))
#testFile.close()
#print(result)
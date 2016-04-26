# -*- coding: UTF-8 -*-
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import datetime
import os
import genResult
import xlop
import time
import xlrd

from tornado.options import define, options

define("port", default = 8080, help = "run on the given port", type = int)

def findCellIDInResultFile(resultFileName, cellID):
	bFound = False
	resultFile = open(resultFileName, 'r')
	nLine = 0
	cellInfos = []

	for line in resultFile.readlines():
		infos = line.split(',')
		if bFound == False and infos[1] != cellID:
			continue
		elif infos[1] == cellID:
			bFound = True
			nLine = nLine + 1;
			cellInfos.append(infos)
		elif bFound == True and infos[1] != cellID:
			break

	resultFile.close()

	if bFound == True and cellInfos[nLine - 1][0] == '掉话原因':
		bFound = True
	else:
		bFound = False
	return bFound

class HomeHandler(tornado.web.RequestHandler):
	"""docstring for HomeHandler"""
	def get(self):
		sercheTime = super().get_argument("DateTime", None)
		serchCell_name = super().get_argument("CellID", None)
		serchCell_date = super().get_argument("Date", None)

		if sercheTime != None:
			ymd = sercheTime.split('-')
			d = ymd[0] + ymd[1] + ymd[2]
			dir = os.listdir('result')
			print(d)
			print(dir)
			
			dates = [d]
			if d in dir:
				self.render('date_serch.html', dates=dates)
			else:
				self.write('There is no target dir!')
		elif serchCell_name != None and serchCell_date != None:
			topNFile = open('result/' + serchCell_date + 'topNFile.csv')
			bFound = False
			topN = 0
			for line in topNFile.readlines():
				if topN == 0:
					topN = topN + 1
					print(topN)
					continue
				else:
					infos = line.split(',')
					print(infos[0])
					if infos[0] == serchCell_name:
						bFound = True
						break
					else:
						topN = topN + 1
			topNFile.close()

			if bFound == True:
				self.render('result/' + serchCell_date + '/TOP' + str(topN) + '.html')
			else:
				bFound = findCellIDInResultFile('result/' + serchCell_date + '.csv', serchCell_name)
				if bFound == True:
					self.write(genResult.getResult(serchCell_date, serchCell_name))
				else:
					self.write('CellID not found!')
		else:
			print('hello world')
			d = datetime.date.today()
			d = d + datetime.timedelta(-1)
			date = d.strftime("%Y%m%d")
			topN = genResult.getTopNCell(date)
			topNCount = genResult.getTopNCountInMonth(d, topN)
			datas = genResult.getCellConnectInfo(date, topN)
			self.render('result/index.html', datas=datas, date=date, topNCount=topNCount)

class CallDropTopNHandler(tornado.web.RequestHandler):
	def get(self):
		d = datetime.date.today()
		d = d + datetime.timedelta(-1)
		date = d.strftime("%Y%m%d")
		topN = genResult.getTopNCell(date)
		topNCount = genResult.getTopNCountInMonth(d, topN)
		datas = genResult.getCellConnectInfo(date, topN)
		self.render('result/calldrop_topn.html', datas=datas, date=date, topNCount=topNCount)

class HistoryTopNHandler(tornado.web.RequestHandler):
	def get(self):
		datas = []
		date = time.strftime("%Y%m%d")
		choseDate = super().get_argument("choseDate", None)
		if choseDate != None:
			topN = genResult.getTopNCell(choseDate)
			datas = genResult.getCellConnectInfo(choseDate, topN)
			date = choseDate
		self.render('result/history_topn.html', datas=datas, date=date)

class HistoryCarrierHandler(tornado.web.RequestHandler):
	def get(self):
		datas = []
		date = time.strftime("%Y%m%d")
		choseDate = super().get_argument("choseDate", None)
		inputCell = super().get_argument("cellID", None)
		if choseDate != None and inputCell != None:
			cells = [inputCell]
			datas = genResult.getCellConnectInfo(choseDate, cells)
			date = choseDate

		self.render('result/history_carrier.html', datas=datas, date=date)

class HistoryRecordHandler(tornado.web.RequestHandler):
	def get(self):
		datas = list()
		self.render('result/history_record.html', datas=datas)
	def post(self):
		type = super().get_argument("type", None)
		print(type)
		row = super().get_body_argument("idx")
		row = int(row)
		print(row)

		rowData = []
		carrier = super().get_body_argument('carrier', '')
		rowData.append(carrier)
		name = super().get_body_argument('name', '')
		rowData.append(name)
		person = super().get_body_argument('person', '')
		rowData.append(person)
		ship = super().get_body_argument('ship', '')
		rowData.append(ship)
		solution = super().get_body_argument('solution', '')
		rowData.append(solution)
		instruction = super().get_body_argument('instruction', '')
		rowData.append(instruction)
		sdate = super().get_body_argument('sdate', '')
		rowData.append(sdate)
		edate = super().get_body_argument('edate', '')
		rowData.append(edate)
		progress = super().get_body_argument('progress', '')
		rowData.append(progress)
		note = super().get_body_argument('note', '')
		rowData.append(note)
		
		print(rowData)
		xlop.updateRowInfo('result/TOPN问题解决统计.xlsx', row, rowData)

		self.set_status(200)

class HistoryRecordDownloadHandler(tornado.web.RequestHandler):
	def get(self):
		print("get method")
		filename='2G掉话处理记录.csv'
		self.set_header("Content-Type", "text/csv;charset=UTF-8")
		self.set_header("Content-Disposition", "attachment; filename=%s"%(filename))
		self.write(xlop.transTopNInfoToCSV().encode('UTF-8-sig'))
		self.finish()

	def post(self):
		print("post method")

class HistoryRecordSerchHandler(tornado.web.RequestHandler):
	def get(self):
		carrier = super().get_argument('carrier')
		datas = xlop.readCarrierInfo(carrier)
		self.render('result/history_record_serch.html', datas=datas)

	def post(self):
		idx = super().get_body_argument('idx')
		idx = int(idx)

		rowData = []
		carrier = super().get_body_argument('carrier', '')
		rowData.append(carrier)
		name = super().get_body_argument('name', '')
		rowData.append(name)
		person = super().get_body_argument('person', '')
		rowData.append(person)
		ship = super().get_body_argument('ship', '')
		rowData.append(ship)
		solution = super().get_body_argument('solution', '')
		rowData.append(solution)
		instruction = super().get_body_argument('instruction', '')
		rowData.append(instruction)
		sdate = super().get_body_argument('sdate', '')
		rowData.append(sdate)
		edate = super().get_body_argument('edate', '')
		rowData.append(edate)
		progress = super().get_body_argument('progress', '')
		rowData.append(progress)
		note = super().get_body_argument('note', '')
		rowData.append(note)

		print(rowData)
		row = xlop.getRowIdx('result/TOPN问题解决统计.xlsx', idx, carrier)
		xlop.updateRowInfo('result/TOPN问题解决统计.xlsx', row, rowData)

		self.set_status(200)

class HistoryInterfereHandler(tornado.web.RequestHandler):
	def get(self):
		datas = xlop.readInterfereInfo()
		self.render('result/history_interfere.html', datas=datas)
	def post(self):
		idx = super().get_body_argument('idx')
		idx = int(idx)
		
		rowData = []
		reponsible = super().get_body_argument('reponsible', '')
		rowData.append(reponsible)
		area = super().get_body_argument('area', '')
		rowData.append(area)
		owner = super().get_body_argument('owner', '')
		rowData.append(owner)
		address = super().get_body_argument('address', '')
		rowData.append(address)
		tel = super().get_body_argument('tel', '')
		rowData.append(tel)
		logitude = super().get_body_argument('logitude', '')
		rowData.append(logitude)
		latitude = super().get_body_argument('latitude', '')
		rowData.append(latitude)
		t = super().get_body_argument('type', '')
		rowData.append(t)
		num = super().get_body_argument('num', '')
		rowData.append(num)
		edate = super().get_body_argument('edate', '')
		rowData.append(edate)
		solution = super().get_body_argument('solution', '')
		rowData.append(solution)
		infectNum = super().get_body_argument('infectNum', '')
		rowData.append(infectNum)
		days = super().get_body_argument('days', '')
		rowData.append(days)
		note = super().get_body_argument('note', '')
		rowData.append(note)

		print(rowData)
		xlop.updateRowInfo('result/干扰源信息汇总.xlsx', idx, rowData)
		self.set_status(200)
		
class HistoryInterfereDownloadHandler(tornado.web.RequestHandler):
	def get(self):
		print("get method")
		filename='干扰源详情.csv'
		self.set_header("Content-Type", "text/csv;charset=UTF-8")
		self.set_header("Content-Disposition", "attachment; filename=%s"%(filename))
		self.write(xlop.transInterfereInfoToCSV().encode('UTF-8-sig'))
		self.finish()

	def post(self):
		print("post method")

class CountSubmitHandler(tornado.web.RequestHandler):
	def get(self):
		choseDate = super().get_argument("date-range-picker", None)
		datas = [0, 0, 0, {}, {}]
		if choseDate != None:
			dateStrs = choseDate.split('-')
			sdate = datetime.datetime.strptime(dateStrs[0].strip(), '%m/%d/%Y')
			edate = datetime.datetime.strptime(dateStrs[1].strip(), '%m/%d/%Y')
			datas = xlop.getCountInfo(sdate, edate)

		self.render('result/count.html', datas=datas)

class RatioCountHandler(tornado.web.RequestHandler):
	def get(self):
		choseDate = super().get_argument("date-range-picker", None)
		datas = [0, 0, 0, {}, {}]
		if choseDate != None:
			dateStrs = choseDate.split('-')
			sdate = datetime.datetime.strptime(dateStrs[0].strip(), '%m/%d/%Y')
			edate = datetime.datetime.strptime(dateStrs[1].strip(), '%m/%d/%Y')
			datas = xlop.getRatioCountInfo(sdate, edate)

		self.render('result/ratio_count.html', datas=datas)
		
class RatioRecordHandler(tornado.web.RequestHandler):
	def get(self):
		datas = xlop.readRatioAllInfo()
		self.render('result/ratio_record.html', datas=datas)
	def post(self):
		idx = super().get_body_argument('idx')
		idx = int(idx)
		
		rowData = []
		carrier = super().get_body_argument('carrier', '')
		rowData.append(carrier)
		name = super().get_body_argument('name', '')
		rowData.append(name)
		person = super().get_body_argument('person', '')
		rowData.append(person)
		ship = super().get_body_argument('ship', '')
		rowData.append(ship)
		solution = super().get_body_argument('solution', '')
		rowData.append(solution)
		instruction = super().get_body_argument('instruction', '')
		rowData.append(instruction)
		sdate = super().get_body_argument('sdate', '')
		rowData.append(sdate)
		edate = super().get_body_argument('edate', '')
		rowData.append(edate)
		progress = super().get_body_argument('progress', '')
		rowData.append(progress)
		note = super().get_body_argument('note', '')
		rowData.append(note)

		print(rowData)
		xlop.updateRowInfo('result/双流比TOPN问题解决统计.xlsx', idx, rowData)
		self.set_status(200)
		
class RatioRecordDownLoadHandler(tornado.web.RequestHandler):
	def get(self):
		print("get method")
		filename='4G双流比处理记录.csv'
		self.set_header("Content-Type", "text/csv;charset=UTF-8")
		self.set_header("Content-Disposition", "attachment; filename=%s"%(filename))
		self.write(xlop.trans4GTopNInfoToCSV().encode('utf-8-sig'))
		self.finish()

	def post(self):
		print("post method")

class RatioRecordSerchHandler(tornado.web.RequestHandler):
	def get(self):
		carrier = super().get_argument('carrier')
		datas = xlop.readRatioSerchInfo(carrier)
		self.render('result/ratio_record_serch.html', datas=datas)
	def post(self):
		idx = super().get_body_argument('idx')
		idx = int(idx)

		rowData = []
		carrier = super().get_body_argument('carrier', '')
		rowData.append(carrier)
		name = super().get_body_argument('name', '')
		rowData.append(name)
		person = super().get_body_argument('person', '')
		rowData.append(person)
		ship = super().get_body_argument('ship', '')
		rowData.append(ship)
		solution = super().get_body_argument('solution', '')
		rowData.append(solution)
		instruction = super().get_body_argument('instruction', '')
		rowData.append(instruction)
		sdate = super().get_body_argument('sdate', '')
		rowData.append(sdate)
		edate = super().get_body_argument('edate', '')
		rowData.append(edate)
		progress = super().get_body_argument('progress', '')
		rowData.append(progress)
		note = super().get_body_argument('note', '')
		rowData.append(note)

		print(rowData)
		row = xlop.getRowIdx('result/双流比TOPN问题解决统计.xlsx', idx, carrier)
		xlop.updateRowInfo('result/双流比TOPN问题解决统计.xlsx', row, rowData)

		self.set_status(200)
		
class RatioTopNHandler(tornado.web.RequestHandler):
	def get(self):
		datas = list()
		edate = datetime.date.today() + datetime.timedelta(-1)
		sdate = edate + datetime.timedelta(-6)

		sdate = sdate.strftime("%Y%m%d")
		edate = edate.strftime("%Y%m%d")
		datas = xlop.getRatioTopN(sdate=sdate, edate=edate)
		self.render('result/ratio_topn.html', datas=datas, date=edate)

class RRCTopNHandler(tornado.web.RequestHandler):
	def get(self):
		datas = list()
		date = datetime.date.today() + datetime.timedelta(-1)
		datas = xlop.getRRCTopN(date)

		date = date.strftime("%Y%m%d")
		self.render('result/rrc_topn.html', datas=datas, date=date)
	
class RRCCountHandler(tornado.web.RequestHandler):
	def get(self):
		choseDate = super().get_argument("date-range-picker", None)
		datas = [0, 0, 0, {}, {}]
		if choseDate != None:
			dateStrs = choseDate.split('-')
			sdate = datetime.datetime.strptime(dateStrs[0].strip(), '%m/%d/%Y')
			edate = datetime.datetime.strptime(dateStrs[1].strip(), '%m/%d/%Y')
			datas = xlop.getRccCountInfo(sdate, edate)

		print(datas)
		self.render('result/rrc_count.html', datas=datas)

class RRCRecordHandler(tornado.web.RequestHandler):
	def get(self):
		datas = xlop.readRccAllInfo()
		self.render('result/rrc_record.html', datas=datas)
		
	def post(self):
		idx = super().get_body_argument('idx')
		idx = int(idx)
		
		rowData = []
		carrier = super().get_body_argument('carrier', '')
		rowData.append(carrier)
		name = super().get_body_argument('name', '')
		rowData.append(name)
		person = super().get_body_argument('person', '')
		rowData.append(person)
		grid = super().get_body_argument('grid', '')
		rowData.append(grid)
		reason = super().get_body_argument('reason', '')
		rowData.append(reason)
		solution = super().get_body_argument('solution', '')
		rowData.append(solution)
		instruction = super().get_body_argument('instruction', '')
		rowData.append(instruction)
		sdate = super().get_body_argument('sdate', '')
		rowData.append(sdate)
		edate = super().get_body_argument('edate', '')
		rowData.append(edate)
		progress = super().get_body_argument('progress', '')
		rowData.append(progress)
		note = super().get_body_argument('note', '')
		rowData.append(note)

		print(rowData)
		xlop.updateRowInfo('result/RRCTOPN问题解决统计.xlsx', idx, rowData)
		self.set_status(200)

class RRCRecordDownloadHandler(tornado.web.RequestHandler):
	def get(self):
		print("get method")
		filename='RRC连接处理情况.csv'
		self.set_header("Content-Type", "text/csv;charset=UTF-8")
		self.set_header("Content-Disposition", "attachment; filename=%s"%(filename))
		self.write(xlop.transRccInfoToCSV().encode('utf-8-sig'))
		self.finish()

	def post(self):
		print("post method")

class ErabDropTopNHandler(tornado.web.RequestHandler):
	def get(self):
		datas = list()
		date = datetime.date.today() + datetime.timedelta(-1)
		date = date.strftime("%Y%m%d")
		self.render('result/erab_drop_topn.html', datas=datas, date=date)

class ErabSuccessTopnHandler(tornado.web.RequestHandler):
	"""docstring for ErabSuccessTopn"""
	def get(self):
		datas = list()
		date = datetime.date.today() + datetime.timedelta(-1)
		date = date.strftime("%Y%m%d")
		self.render('result/erab_success_topn.html', datas=datas, date=date)


class ReasonHandler(tornado.web.RequestHandler):
	def get(self):
		self.render('result/reason.html', datas=list())
		
def main():
	tornado.options.parse_command_line()
	application = tornado.web.Application([(r"/", HomeHandler),
											(r"/calldrop_topn", CallDropTopNHandler),
											(r"/history_topn", HistoryTopNHandler),
											(r"/history_carrier", HistoryCarrierHandler),
											(r"/history_record", HistoryRecordHandler),
											(r"/history_record_download", HistoryRecordDownloadHandler),
											(r"/history_record_serch", HistoryRecordSerchHandler),
											(r"/history_interfere", HistoryInterfereHandler),
											(r"/history_interfere_download", HistoryInterfereDownloadHandler),
											(r"/count", CountSubmitHandler),
											(r"/ratio_count", RatioCountHandler),
											(r"/ratio_record", RatioRecordHandler),
											(r"/ratio_record_download", RatioRecordDownLoadHandler),
											(r"/ratio_record_serch", RatioRecordSerchHandler),
											(r"/ratio_topn", RatioTopNHandler),
											(r"/rrc_topn", RRCTopNHandler),
											(r"/rrc_count", RRCCountHandler),
											(r"/rrc_record", RRCRecordHandler),
											(r"/rrc_record_download", RRCRecordDownloadHandler),
											(r"/erab_drop_topn", ErabDropTopNHandler),
											(r"/erab_success_topn", ErabSuccessTopnHandler)],
											static_path =os.path.join(os.path.dirname(__file__), "result"))
	http_server = tornado.httpserver.HTTPServer(application)
	http_server.listen(options.port)
	tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
	main()
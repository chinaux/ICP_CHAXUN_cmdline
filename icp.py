import sys,urllib
import string
import time
import sys 
reload(sys) 
sys.setdefaultencoding('utf8')

from HTMLParser import HTMLParser


class MyHTMLParser(HTMLParser):
	def __init__(self):
		HTMLParser.__init__(self)
		self.record = ''
		self.index = 0
		self.file_object = open('gotICP.csv', 'w')
	def handle_data(self, data):
		if data.strip() != '':
			#print data.strip()
			if data.strip().isdigit():
				self.record += data.strip()
				self.index += 1
			else:
				self.record += ','
				self.record += data.strip()
				self.index += 1

			self.index = self.index % 8
			if self.index == 0:
				#self.record.replace('\n','')
				self.record += '\n'
				print self.record.encode("gbk")
				self.file_object.write(self.record.encode("gbk"))
				self.record = ''
						
		#self.links.append(data)
	def close(self):
		HTMLParser.close(self)	
		self.file_object.close()

if __name__ == "__main__":

	cmd_num = len(sys.argv)
	if cmd_num != 3:
		print 
		print "usage:"+sys.argv[0]+" icp incr"
		print "\tie:"+sys.argv[0]+" 09091971 200"
		print
		exit(0)
	

	icp = sys.argv[1]
	if len(icp) != 8 :
		print "icp length isn't 8"
		exit(0)
	
	incr= string.atoi(sys.argv[2])
	
	icp_number_str = icp[2:8]
	
	if icp[2] == '0':
		icp_year_str = icp[0:3]
	else:
		icp_year_str = icp[0:2]
	
	icp_number_begin = string.atoi(icp_number_str)


	print 'begin ...'
	parser = MyHTMLParser()
	
	for i in range(0, incr,1):
		icp_tmp = icp_number_begin+i
	
		if len(str(icp_tmp)) == 6:
			icp_year_str = icp[0:2]
		
		#print icp_year_str+str(icp_tmp)
			
		url="http://www.icpchaxun.com/beian.aspx?icpType=-4&icpValue=%E4%BA%ACicp%E5%A4%87"+icp_year_str+str(icp_tmp)+"%E5%8F%B7"
		#url="http://www.icpchaxun.com/beian.aspx?icpType=-4&icpValue=%E4%BA%ACicp%E5%A4%87"+icp_year_str+str(icp_tmp)+"%E5%8F%B7"
		print url
		wp = urllib.urlopen(url)
		content = wp.read()

		#print content
		begin =  content.find("<tbody>")
		end  = content.find("</tbody>");
		content = content[begin:end+8]
		#print content
		parser.feed(content)
		
		
		time.sleep(i%10)	
		
	parser.close()
	print 'complete '

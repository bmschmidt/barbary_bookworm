import re


def snippetyielder(docbreaks):
	for doc in docbreaks:
		yield doc
			# elif re.match(r"(.*NDA.*)",line):
			# 	print line	
			# elif re.match(r"(.*NR\&L.*)",line):
			# 	print line
			# elif re.match(r"(.Am\. State Paper.*)",line):
			# 	print line
			# elif re.match(r"(.*\[Statutes.*)",line):
			# 	print line
			# elif re.match(r"(.*NYPL.*)",line):
			# 	print line
			# elif re.match(r"(.*\[Treaties.*)",line):
			# 	print line	
			# elif re.match(r"(.*\[LC.*)",line):
			# 	print line
			# elif re.match(r"(.*\[GAO.*)",line):
			# 	print line
	#print line
				#print line


#snippetyielder()

 class document:
  	def _init_(self, doc):
  		self.doc = doc
  		
  	def raw_text(self):
		pass
 	def metadata(self):
		pass
 	def get_date(self):
		pass
 	def does_this_look_suspicious(self):
		pass




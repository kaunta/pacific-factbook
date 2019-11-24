PYTHON3=python3

all: report.html flag_report.html name_report.html

report.html:
	$(PYTHON3) -m pacific-factbook > $@

flag_report.html:
	$(PYTHON3) -m pacific-factbook.flag > $@

name_report.html:
	$(PYTHON3) -m pacific-factbook.name > $@

clean:
	-rm report.html flag_report.html name_report.html

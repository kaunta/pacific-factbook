PYTHON3=python3

report.html:
	$(PYTHON3) -m pacific-factbook > $@

clean:
	-rm report.html

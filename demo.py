from pyLabOn import Report

my_report=Report("demo")

my_report.add_plain_content("Hello, pyLabOn")

sub_para=my_report.add_sub_paragraph("SubParagraph")

sub_para.add_table(["index"],[[i] for i in range(0,10)])

sub_para.add_plain_content("There is a Table")

my_report.compile()



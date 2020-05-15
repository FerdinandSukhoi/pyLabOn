from pyLabOn import Report

# Name can be anything you like;
# you may specific path if the report files should not be generated in ./
my_report=Report("demo")

# You can also add formula, code, and anything
my_report.add_plain_content("Hello, pyLabOn")

# The return value of .add_sub_paragraph() is the sub paragraph created
# You can add sub paragraphs to sub paragraph in the same way
sub_para=my_report.add_sub_paragraph("SubParagraph")

# Add contents to the sub paragraph just like to the report
sub_para.add_plain_content("There is a Table")

# Add a Table to the sub paragraph
# (List,List[List] [,Align=0])->Table
# Align: 0=Central, -1=Left, 1=Right
# Align can be a list or a single int
# The return value of .add_table() is the table created
sub_para.add_table(["index"],[[i] for i in range(0,10)])

# This command generates .md to my_report.MarkdownFilePath, and .pdf to my_report.PDFPath
# If you just want a Markdown file, use my_report.save_to_file() instead
my_report.compile()



## Read Data from Google Sheets

Google Sheets is an online spreadsheet service from Google that lets you create spreadsheets in the cloud. Reading Google Sheets is different from reading a Microsoft Excel or CSV file using Python. So in this project, I’m going to walk you through how to read data from Google Sheets using Python for Data Science.

You can easily create a spreadsheet in Google Sheets, it is very same as Microsoft Excel spreadsheets. For this task, you need to have a spreadsheet on Google Sheets that you can create or upload an Excel file to Google Sheets.

### Read Data From Excel Sheets using Python

Reading data from Google Sheets is not possible in an IDE or a code editor in our systems. For this task, you need to use Google Colab, another service from Google for creating Jupyter notebooks.

To read a dataset from Google Sheets, I’ll be using a dataset that’s already uploaded to my Google Sheets.

After running the code, you will get a link in the output which is nothing but the authentication process to get the code you need to connect Google Colab with Sheets. Just click on the link and you will be taken to your authentication code. Copy the code and paste it into the text box, and hit enter.

### Final Step: Using Python Pandas

You’ve connected Google Colab to Sheets, now let’s read Google Sheets using Python for data science using Pandas library in Python.

### Summary

If you implement this code in an IDE or code editor, you will get errors, so only use this method in Google Colab.
## Extract Text from Pdf

To extract text from a PDF is not an easy task, there is a lot to do here. But for some help, I use a Python package known as `pdf2image`, which can be easily installed by using the pip command;

```py
pip install pdf2image
```

The biggest challenge we face while we extract text from PDF file is that PDF files come in different file formats. So first we need to prepare a function so that we can convert every format of a PDF file into our desired one.

### Extract Text From PDF Using Python

First, we need to import all the packages. You need `pdf2image` to convert PDF files to `ppm` image files.

We also need to manipulate the paths to join and rename text files, so we import the os and sys packages. We call a `PIL` library and imports the image with `pytesseract`.

Then, we need to initialize the path of your documents and the counter to be used later in the pdf extract function to count your documents in the folder. Next step is to delete some unrequired files from our pdf files.

Then we need to sort the pdf files according to their types. I start this by creating to lists one for pdf files and one for Docx files because these two types are the most used pdf file types. Finally, we can extract text from PDF files. First, we prints the name of each file from which the text is extracted. Depending on the size of the document, extracting text may take some time.

Now after running the function if you will go to the directory you will see a text file by the name of `result1.txt` with all the text extracted from the PDF file.

### Summary

I hope you liked this project on how to extract text from PDF files by using Python.
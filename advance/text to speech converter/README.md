## Text to Speech Converter

Text to speech is the generation of speech synthesized from the text. The technology is used to communicate with users when reading a screen is not possible or impractical. This not only opens up apps and information to use in new ways but can also make the world more accessible to people who cannot read text on a screen.

The technology behind the TTS has evolved over the past few decades. Using natural language processing, it is now possible to produce very natural speech that includes changes in pitch, speed, pronunciation and inflexion.

### Text to Speech with Python

I simply start with importing all the necessary libraries that we need for this task to create a program that takes the text of an article online and converts it into speech. If you have face any error in importing the libraries, then you must have not installed any of these libraries. You can easily install any library in python, by writing a very simple command in your terminal;

```py
pip install package name
```

Now after installing and importing the libraries, we need to get an article from online sources so that we can create a program to convert text to speech from that article.

Download and parse the article, and download the `punkt` package if you have already downloaded it before you can skip downloading it if you will still download it again, it will give you a reminder that it is already available in your system which will not harm anything.

Define a variable to store the article. Then, choose the language of speech. Note `en` means English. You can also use `pt-br` for Portuguese and there are others.

Finally we need to pass the text and language to the engine to convert the text to speech and store it in a variable. Mark slow as False to tell the plug-in that the converted audio should be at high speed.

### Running Text to Speech Program

We have converted the article for text-to-speech, so now the next step is to save this speech to mp3 file. Then, play the converted audio file from text to speech in Windows, using the Windows command `start` followed by the name of the mp3 file.

### Summary

I hope you liked this project on converting text to speech using python.
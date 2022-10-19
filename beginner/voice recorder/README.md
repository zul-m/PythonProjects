## Voice Recorder

A voice recorder is found in every smartphone and computer today. It is an application that is used to record sound and save it in a specific file format, which can be listened to and transferred to another device. If you want to know how to make a voice recorder using [Python](https://thecleverprogrammer.com/2021/06/19/fundamentals-of-python/), this project is for you.

### Voice Recorder using Python

You must have used a voice recorder on your smartphone or your computer once in your life. We generally use it to record a voice message, and some video creators use it to record the voice for their videos. To create a voice recorder using the Python programming language, you need to use the [sounddevice](https://python-sounddevice.readthedocs.io/en/0.4.3/) library in Python. If you have never used this library before, you can easily install it by using the pip command mentioned below.

```ps1
pip install sounddevice
```

The sounddevice library will help you to record your voice, but to save your voice in a specific file format, you need to use the [SciPy](https://scipy.org/) library in Python, which can be installed by using the pip command.

```ps1
pip install SciPy
```

In the code, I have defined a Python function to record and save your recorded files. It takes two parameters:
 1. The first parameter is seconds, where you will enter the number of seconds you want to record your voice.
 2. The second parameter is the file, where you will input the name by which you want your recorded file to be saved. For example, **voice.wav**.

After running the above code, it will show you a message that the recording has started, and after the number of seconds that you have given as input, it will show you that the recording is complete. Once completed, it will automatically be saved to the same directory where your Python file is located.

### Summary

A voice recorder is found in every smartphone and computer today. It is an application that is used to record sound and save it in a specific file format, which can be listened to and transferred to another device.
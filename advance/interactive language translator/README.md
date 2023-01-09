## Interactive Language Translator

You can easily translate any language using Google translator, but creating your translator will be a satisfying experience as a programmer. The [googletrans](https://thecleverprogrammer.com/2020/08/10/translate-using-python/) API created by Google developers was used earlier to translate any text using Python. But now the new API from the Google developers known as `google_trans_new` is used for the same task.

You can use this API for every task that you can do with the google translator. You can easily install this library in your systems by using the pip command.

```py
pip install google_trans_new
```

To make a translator more interactive I create an interactive user interface by using the `streamlit` library in Python.

Since we are using the `streamlit` library here, we need to run the code using the **streamlit run file_name.py** command in your terminal. After running the file a link will open in your default browser with an interactive user interface. In the text field, you can enter any text in any language, once you hit enter it will translate it to French as I have mentioned ‘fr’ as our target language in the above code.

### Summary

This is how we can create a language translator using Python using the Google translation API developed by Google developers. You can try this app with more languages and a more interactive user interface.
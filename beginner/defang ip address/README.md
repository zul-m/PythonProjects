## Defang IP Address

A user’s IP address is defanged to prevent the user from clicking on a malicious link. The problem with Defanging IP addresses is one of the common coding interview questions for someone who is planning data science.

Solving the problem of changing an IP address is good for someone who is a newbie for practising the concept of string manipulation. It is very easy to understand because it is only based on the concepts of replacing and join. There are so many unique ways to solve this problem, which is why this is one of the favourite questions for interview coding.

### Defanging IP Address: Problem Statement

To convert an IP address to a defanged IP address, we need to replace `"."` with `"[.]"`. During coding interviews, a standard problem for changing an IP address is that you receive a valid IP address, you must return a defanged version of that IP address.

This is generally a warm-up question for coding interviews. Solving this question quickly will give a good impression that you know how to understand a problem statement quickly because there is not much that you need to solve this problem. You just need to replace every `"."` with `"[.]"`.

### Defang IP Address using Python

Now let’s see how to write a program to defang an Ip address using Python. Here you simply need to treat `"."` as a separator and split the string. Then you have to rejoin an empty string and select `"[.]"` as the new separator.

This is how easy it is to defang an Ip address using Python. You can also defang an IP address using the C++ programming language.

### Output

```
1[.]1[.]2[.]3
```

### Summary

I hope you liked this project on how to defang an IP address using Python and C++ programming languages.
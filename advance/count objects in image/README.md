## Count Objects in Image

Counting objects in an image is the task of [computer vision](https://thecleverprogrammer.com/2021/03/08/how-to-learn-computer-vision/). There are many computer vision libraries that you can use for this task, such as `OpenCV`, `TensorFlow`, `PyTorch`, `Scikit-image`, and `cvlib`. 

You must have not heard much about the `cvlib` library in Python. Well, this is a very simple, high level, and easy to use computer vision library in Python.

By using the features of this library we can count the number of objects in an image using Python. To use this library, make sure you have `OpenCV` and `TensorFlow` installed in your systems. You can easily install it by using the pip command.

```py
pip install cvlib
```

### Count Objects in an Image using Python

Now let’s see how to use the `cvlib` library to count the number of objects in an image using the Python programming language. I will first read an image by using the `OpenCV` library, then I will detect all the objects using `cvlib` and count the number of particular objects. The image that I am going to use for this task is shown below.

<p align="center">
 <img width="60%" src="./cars.png" align="center" alt="Cars" />
</p>

As you can see the image that I am using here for the task of counting objects in an image using Python contains vehicles in it. So I will first detect all the vehicles and then count the number of cars out of them.

### Output

```
Number of cars in this image: 11
```

### Summary

So this is how you can count the number of objects by using the `cvlib` library in Python. You can use this library for all the tasks of computer vision.
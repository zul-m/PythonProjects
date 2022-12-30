## Choropleth Map

A choropleth map is a shaded map where the intensity of the colour indicates the intensity or quantity of a particular feature. In Data Science, the choropleth maps are used to visualize the distribution of a feature in a geographical area.

For example, a world map that shows the regions of the maximum covid-19 cases for a particular month will be showing the regions with varying intensities of the blue colour. Here the dark blue colour will represent the highest affected areas by the covid-19, and the light blue colour will be representing the areas with comparatively fewer covid-19 cases.

### Choropleth Map using Python

Now let’s see how to visualize a choropleth map using Python. For this task, I will be using the `plotly` library in Python. First, I will import the necessary Python libraries and the dataset that we need to visualize choropleth maps using Python.

The dataset that I am using here is based on the agricultural exports of the United States. Then, I visualize choropleth maps with this dataset using Python.

### Output

```
  code       state category  total exports   beef  pork  ...  veggies fresh  veggies proc  total veggies  corn  wheat   cotton
0   AL     Alabama    state        1390.63   34.4  10.6  ...            5.5           8.9          14.33  34.9   70.0   317.61
1   AK      Alaska    state          13.31    0.2   0.1  ...            0.6           1.0           1.56   0.0    0.0     0.00
2   AZ     Arizona    state        1463.17   71.3  17.9  ...          147.5         239.4         386.91   7.3   48.7   423.95
3   AR    Arkansas    state        3586.02   53.2  29.4  ...            4.4           7.1          11.45  69.5  114.5   665.44
4   CA  California    state       16472.88  228.7  11.1  ...          803.2        1303.5        2106.79  34.6  249.3  1064.95

[5 rows x 17 columns]
```

### Summary

So this is how you can visualize choropleth maps with Python by using the `Plotly` library in Python. There are more data visualization tools in Python that you can use for this task but to visualize a choropleth map `Plotly` library is best in my opinion.
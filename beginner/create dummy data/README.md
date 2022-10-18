## Create Dummy Data

If you are learning [Data Science](https://thecleverprogrammer.com/2021/06/06/best-websites-to-learn-data-science/) and find it hard to create a dataset for practice from scratch, you can either download a dataset from Kaggle or create fake data. If you want to learn how to create a dummy dataset in just a few lines of code, this project is for you.

### Create Dummy Data using Python

To create dummy data using Python, we can use the faker library. The faker library generates fake data randomly. If you have never used this library before, you can easily install it by using the pip command mentioned below in your command prompt or terminal:

```ps1
pip install faker
```

Now let’s look at some examples of this library before creating a dummy dataset. The code will return a fake name, address, and text randomly. You can learn more about creating fake data using the faker library from [here](https://faker.readthedocs.io/en/master/).

### Output

```
Michael Taylor
USNS Wood
FPO AA 58416
Bag home week personal artist.
Economic wonder smile expert specific. Six include amount. Here work still statement minute.
```

Every time you run the code, you will get different results. Now let’s see how to create fake data for creating a dummy dataset using Python. The Faker().profile() method returns fake data about job profiles containing 13 columns. Run the `dummy-data.py` file.

```
                         job                   company  ...                       mail   birthdate
0            Naval architect              Henry-Nelson  ...      brandybrown@gmail.com  1908-09-30
1        Call centre manager  Baker, Peters and Jacobs  ...          ncarter@gmail.com  2004-03-20
2       Nurse, mental health                 Baird LLC  ...  frederickcarrie@gmail.com  1910-01-26
3    Clinical cytogeneticist               Schultz LLC  ...          mhodges@yahoo.com  1951-10-08
4  Psychologist, counselling              Phillips PLC  ...       emcmahon@hotmail.com  1928-03-18

[5 rows x 13 columns]
```

### Summary


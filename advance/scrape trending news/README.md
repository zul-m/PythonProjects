## Scrape Trending News

Most of the datasets that you find from different data sources on the internet are created by collecting data from websites. Using the GoogleNews API in Python, we can scrape trending updates based on any keyword or country. It allows you to retrieve information on any keyword which can be the name of any country, any event or even the name of a person who is trending on Google. If you have never used this API before, you can easily install it on your systems using the pip command.

```py
pip install googlenews
```

Now let’s see how to scrape trending news using Python. I will first import the necessary Python libraries and then I will scrape the latest trending news about Malaysia. As the returning output will be in the form of a dictionary so I will convert it into a pandas DataFrame.

In the DataFrame, I have dropped the column “img” as it is of no use. As the resulting output is now in the DataFrame we cannot click on the links to read the complete news. So to read the complete news, I will run a `for` loop on the resulting dictionary so that we can get the complete link of the news article.

### Output

```
Title: Search continues for 9 campers caught in Malaysia landslide
News: KUALA LUMPUR: The search for missing campers caught in a deadly landslide 
at an unlicensed campsite in Malaysia continued for a third day on Sunday 
(Dec 18)...
Read full news: https://www.channelnewsasia.com/asia/malaysia-landslide-search-9-missing-24-dead-fathers-organic-farm-batang-kali-3152996
Title: PBM reinstates 2 Supreme Council members | Free Malaysia Today
News: Parti Bangsa Malaysia president Larry Sng had suspended 13 of the party's 
Supreme Council members in October.
Read full news: https://www.freemalaysiatoday.com/category/nation/2022/12/18/pbm-reinstates-2-supreme-council-members/
Title: Heads must roll following landslide tragedy | Free Malaysia Today
News: The regular recurrence of these deadly landslides merits a Royal Commission
of Inquiry (RCI) being established.
Read full news: https://www.freemalaysiatoday.com/category/opinion/2022/12/18/heads-must-roll-following-landslide-tragedy/
Title: Muhyiddin says did not take single sen as NRC chief, denies Puad Zarkashi's claims
News: KUALA LUMPUR, Dec 18 — Perikatan Nasional chairman Tan Sri Muhyiddin Yassin
has denied receiving any money when he was the chairman of the National
Recovery...
Read full news: https://www.malaymail.com/news/malaysia/2022/12/18/muhyiddin-says-did-not-take-single-sen-as-nrc-chief-denies-puad-zarkashis-claims/45910
Title: 9 bodies remain unidentified from Batang Kali landslide | Free Malaysia Today
News: Hulu Selangor police chief Suffian Abdullah has urged anyone with
information or who could positively identify the bodies to visit Hospital
Sungai Buloh.
Read full news: https://www.freemalaysiatoday.com/category/nation/2022/12/18/9-bodies-remain-unidentified-from-batang-kali-landslide/      
Title: Auto-resign clause in unity govt MoU unconstitutional, says lawyer
News: Bersih also 'alarmed' by the condition in the pact which requires MPs from
the five parties to vote in favour of government bills or lose their seat.
Read full news: https://www.freemalaysiatoday.com/category/nation/2022/12/18/auto-resign-clause-in-unity-govt-mou-unconstitutional-says-lawyer/
Title: As former foes lead Malaysia, wary public hopes unity is not ‘just for show’
News: While relieved that politicians are finally coming together 'for the
people', Malaysians remain wary about the stability of a government formed
by bitter...
Read full news: https://www.scmp.com/week-asia/politics/article/3203618/umno-hails-anwar-zahid-speaks-chinese-malaysians-hope-political-unity-not-just-show
Title: King attends gathering with Malaysian diaspora in Qatar
News: KUALA LUMPUR, Dec 18 — Yang di-Pertuan Agong Al-Sultan Abdullah
Ri'ayatuddin Al-Mustafa Billah Shah on Saturday attended a gathering with
the Malaysian...
Read full news: https://www.malaymail.com/news/malaysia/2022/12/18/king-attends-gathering-with-malaysian-diaspora-in-qatar/45900
Title: GRS drops Bersatu as coalition member | Free Malaysia Today
News: Gabungan Rakyat Sabah deputy chairman Maximus Ongkili said this was decided
at the coalition's Supreme Council meeting on Dec 9.
Read full news: https://www.freemalaysiatoday.com/category/nation/2022/12/18/grs-drops-bersatu-as-coalition-member/
Title: Bersatu gugur sebagai komponen GRS | Free Malaysia Today
News: Timbalan pengerusi GRS itu berkata dalam mesyuarat Ahli Majlis Tertinggi,
pada 9 Dis, juga mengekalkan Hajiji Noor sebagai pengerusi.
Read full news: https://www.freemalaysiatoday.com/category/bahasa/tempatan/2022/12/18/bersatu-gugur-sebagai-komponen-grs/
```

### Summary

So this is how you can scrape trending updates based on any keyword from all around the world.
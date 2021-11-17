# sentence-segmentation-for-chinese-historical-texts

# Description

This is a pre-trained LSTM model. This model can help you to segement unpunctuated historical Chinese texts, such as

>閔頔宗儒子字樂全元宗己巳生忠烈乙酉登科

to

>閔頔/宗儒子/字樂全/元宗己巳/生忠烈/乙酉/登科

Everyone can use it under CC BY-NC-SA 4.0 license.

We created this model on 2018： 

>  Xu Han, Hongsu Wang, Sanqian Zhang, Qunchao Fu, and Jun S Liu. 2018. “[Sentence Segmentation for Classical Chinese Based on LSTM with Radical Embedding](https://projects.iq.harvard.edu/files/cbdb/files/sentence_segmentation_for_classical_chinese_based_on_lstm_with_radical_embedding.pdf).”


We found that there is no project has opened their pre-trained sentence segmentation models to the public yet. Although this is an old model, we think that it still can help some projects.

This repository is not a competitor of any current sentence segmentation or punctuation model. If you have the fund, please DO pay for current commercial sentence segmentation or punctuation model or create the model by yourself.

This repository is only for those projects and scholars who 1) want to analysis millions records of historical Chinese texts, so that a high correction rate of punctuation is not an essential condition for your argument; And 2) can't create their own model; And 3) can't afford a commercial model.

If you also want to help these projects or scholars, we also opened our training data here. If you want, you can also create your own model by these training data. Or add more training data.

# Requirement

Python 2.7, flask, tqdm, numpy, scipy, theano

Notes: We highly suggest you deploy it in a virtual environment by conda or other tools.

# Directories

break-sent-api: The model to segment sentences.

training-data: The training data.

# Usage

1. Run break-sent-api/app.py

2. After you see something like this in your own command-line/terminal
```
  Serving Flask app "app" (lazy loading)
  Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
  Debug mode: on
  Restarting with stat
  Debugger is active!
  Debugger PIN: 223-736-038
  Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```
You can use these URLs to upload your texts:

For middle period China:

http://127.0.0.1:5000/upload/tang

For late imperial China:

http://127.0.0.1:5000/upload/qing

For Tang Dynasty Epitaphs:

http://127.0.0.1:5000/upload/muzhi

Notes: The results of the difference between the first two URLs is not big enough. You can use either of them for general purposed segmentation.

3. Please put the text which you want to segment to a text file, and then use the "Choose File" button to upload your file. After you click "Submit", it will start segmentation. After it finishes, it will download the result for you automatically.

Notes: Please remove the lines which include less than 3 characters and blank lines in your upload text file.


# Licence

 [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International license](https://creativecommons.org/licenses/by-nc-sa/4.0/)

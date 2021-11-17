# Sentence segmentation model for chinese historical texts 漢語古文斷句預訓練模型

# Description

This is a pre-trained LSTM model. This model can help you to segment unpunctuated historical Chinese texts, such as 這是基於 LSTM 的預訓練模型。此模型可幫助您為漢語古文斷句。譬如，可將這樣無標點符號的句子

>閔頔宗儒子字樂全元宗己巳生忠烈乙酉登科

to 點斷為

>閔頔/宗儒子/字樂全/元宗己巳/生忠烈/乙酉/登科

Everyone can use it under CC BY-NC-SA 4.0 license. 任何人都可以在 CC BY-NC-SA 4.0 許可證下使用此預訓練模型

We created this model on 2018： 我們在 2018 年建立此模型：

>  Xu Han, Hongsu Wang, Sanqian Zhang, Qunchao Fu, and Jun S Liu. 2018. “[Sentence Segmentation for Classical Chinese Based on LSTM with Radical Embedding](https://projects.iq.harvard.edu/files/cbdb/files/sentence_segmentation_for_classical_chinese_based_on_lstm_with_radical_embedding.pdf).”


We found that there is no project has opened their pre-trained sentence segmentation models to the public yet. Although this is an old model, we think that it can still help some projects. 雖然模型已很老舊，我們發現當前並沒有項目在 GitHub 上公開用於漢語古文斷句的預訓練模型，因此我們認為它仍能幫到一些項目。

This repository is not a competitor of any current sentence segmentation or punctuation model. If you have the fund or resources, please DO pay for current commercial sentence segmentation, punctuation model or create the "modern" model on yourself. 此倉庫並不是任何當下斷句或者標點系統的競爭者。如果您有資金支持或者有其他選擇，請選擇那些當下的商業化斷句、標點模型，或利用自己的資源訓練合適的「現代」模型。

This repository is only for those projects, scholars and amateurs who 1) want to analysis millions records of historical Chinese texts, so that a high correction rate of punctuation is not an essential condition for your argument; And 2) can't create their own model; And 3) can't afford a commercial model. 此倉庫僅希望為以下項目、學者、愛好者提供幫助：1）希望標記成千上萬條語料記錄，研究結論對標點正確率容忍度高。2）無法建立自己的古漢語斷句、標點模型。3）無力支付付費模型。

We opened our training data here(training-data/). If you also want to help these projects, scholars and amateurs mentioned above, you can create your own model by these training data. Or add more training data. Any pull requests are welcomed. We are looking forward to see more open pre-trained models in China historical research. 在本倉庫的 training-data/ 目錄下，您可以找到我們用於訓練此模型的語料。如果希望幫助上述項目、學者、愛好者，您亦可基於這些訓練集訓練自己的模型，或豐富訓練集的內容。我們歡迎任何人向本倉庫提交代碼或無版權問題的語料。我們期待在中國歷史研究中，未來會有更多的預訓練模型開放給公眾。

We losed the source codes which we used to train the model. Once we find them back, we will update them to this repository immediately. 我們丟失了用於訓練模型的源代碼，但未來如果找到，第一時間更新在此倉庫中。

# Requirements

Python2.7, flask, tqdm, numpy, scipy, theano

Notes: We highly suggest you deploy it in a virtual environment by conda or other tools. 強烈建議您使用 conda 或其他工具將本模型部署在虛擬環境中。

# Directories

break-sent-api: The model to segment sentences. 用於斷句的模型

training-data: The training data. 訓練集

# Usage

1. Run break-sent-api/app.py 運行 break-sent-api/app.py

2. After you see something like this in your own command-line/terminal 在您的命令行或終端中看到類似如下提示後
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
You can use these URLs to upload your texts: 您可以使用以下鏈接上傳需標點的文本：

For middle period China: 中國中古時代文本：

http://127.0.0.1:5000/upload/tang

For late imperial China: 晚期中國文本：

http://127.0.0.1:5000/upload/qing

For Tang Dynasty Epitaphs: 唐墓誌類型文本：

http://127.0.0.1:5000/upload/muzhi

Notes: The difference of correction between the first two URLs is not big enough. You can use either of them for general purposed segmentation. 中古時代和晚期時代的模型差別並不大，您如要對通用文本進行斷句，使用任一即可。

3. Please put the text which you want to segment to a text file(txt), and then use the "Choose File" button to upload your file. After you click "Submit", it will start segmentation. After it finishes, it will download the result for you automatically. 請將您需要斷句的文本保存為文本文檔（txt），之後使用 Choose File 按鈕上傳此文本文檔。點擊 Submit 之後，系統將開始自動斷句。完成後，斷句的結果將被自動下載。

Notes: Please remove the lines which include less than 3 characters and blank lines in your upload text file. 請保持需要斷句的文本中每一行內容多於兩個字。


# Licence

 [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International license](https://creativecommons.org/licenses/by-nc-sa/4.0/)

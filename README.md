# bankruptcy

Code related to capstone project in Machine Learning Zoomcamp.

The dataset is about bankruptcy prediction of Polish companies. The data was collected from Emerging Markets Information Service (EMIS), which is a database containing information on emerging markets around the world. The bankrupt companies were analyzed in the period 2000-2012, while the still operating companies were evaluated from 2007 to 2013.
https://archive.ics.uci.edu/ml/datasets/Polish+companies+bankruptcy+data

The dataset contains five classification cases. I choose:
- 3rdYear â€“ the data contains financial rates from 3rd year of the forecasting period and corresponding class label that indicates bankruptcy status after 3 years. The data contains 10503 instances (financial statements), 495 represents bankrupted companies, 10008 firms that did not bankrupt in the forecasting period.


Attribute Information:

     X1 net profit / total assets
     X2 total liabilities / total assets
     X3 working capital / total assets
     X4 current assets / short-term liabilities
     X5 [(cash + short-term securities + receivables - short-term liabilities) / (operating expenses - depreciation)] * 365
     X6 retained earnings / total assets
     X7 EBIT / total assets
     X8 book value of equity / total liabilities
     X9 sales / total assets
     X10 equity / total assets
     X11 (gross profit + extraordinary items + financial expenses) / total assets
     X12 gross profit / short-term liabilities
     X13 (gross profit + depreciation) / sales
     X14 (gross profit + interest) / total assets
     X15 (total liabilities * 365) / (gross profit + depreciation)
     X16 (gross profit + depreciation) / total liabilities
     X17 total assets / total liabilities
     X18 gross profit / total assets
     X19 gross profit / sales
     X20 (inventory * 365) / sales
     X21 sales (n) / sales (n-1)
     X22 profit on operating activities / total assets
     X23 net profit / sales
     X24 gross profit (in 3 years) / total assets
     X25 (equity - share capital) / total assets
     X26 (net profit + depreciation) / total liabilities
     X27 profit on operating activities / financial expenses
     X28 working capital / fixed assets
     X29 logarithm of total assets
     X30 (total liabilities - cash) / sales
     X31 (gross profit + interest) / sales
     X32 (current liabilities * 365) / cost of products sold
     X33 operating expenses / short-term liabilities
     X34 operating expenses / total liabilities
     X35 profit on sales / total assets
     X36 total sales / total assets
     X37 (current assets - inventories) / long-term liabilities
     X38 constant capital / total assets
     X39 profit on sales / sales
     X40 (current assets - inventory - receivables) / short-term liabilities
     X41 total liabilities / ((profit on operating activities + depreciation) * (12/365))
     X42 profit on operating activities / sales
     X43 rotation receivables + inventory turnover in days
     X44 (receivables * 365) / sales
     X45 net profit / inventory
     X46 (current assets - inventory) / short-term liabilities
     X47 (inventory * 365) / cost of products sold
     X48 EBITDA (profit on operating activities - depreciation) / total assets
     X49 EBITDA (profit on operating activities - depreciation) / sales
     X50 current assets / total liabilities
     X51 short-term liabilities / total assets
     X52 (short-term liabilities * 365) / cost of products sold)
     X53 equity / fixed assets
     X54 constant capital / fixed assets
     X55 working capital
     X56 (sales - cost of products sold) / sales
     X57 (current assets - inventory - short-term liabilities) / (sales - gross profit - depreciation)
     X58 total costs /total sales
     X59 long-term liabilities / equity
     X60 sales / inventory
     X61 sales / receivables
     X62 (short-term liabilities *365) / sales
     X63 sales / short-term liabilities
     X64 sales / fixed assets

### The classification goal is to predict if there is the increased default risk.


Repo contains:

   *  readme.md
   *  notebook.ipynb
   *  script train.py
   *  script predict.py
   *  pipenv, pipenv.lock



Instructions (if you have pipenv, docker, awsb installed (as you are in progress in zoomcamp-course I think you have :) ) please skip installation procedure. At first copy all files to your directory. Next steps:

install pipenv

     pip install pipenv
Within the directory which contains files: pipenv, pipenv.lock

     pipenv install 
Run virtual environment shell

     pipenv shell 
Then you can deploy the model with flask, using gunicorn

     gunicorn --bind 0.0.0.0:9696 predict:app
Dockerfile

Instalation - debian (I didn't test it in Windows):

Install docker

    sudo apt-get install docker.io
If service is not running:

    sudo service docker start
Build docker file:

    sudo docker build -t mterm_project .
Run the file:

     sudo docker run -it --rm -p 9696:9696 mterm_project:latest
You can test if it works using described below file

depo_client_score.py

Test the model using depo_client_score.py:

        python depo_client_score.py
depo_client_score_ebs.py

As the model is also availablea on AWS Elastic Beanstalk you can test it using depo_client_score_ebs.py. The file contains url address. I deployed model according to below listed code:

        eb init -p docker -r eu-central-1 mterm_project
Deploy model it locally (for testeng):

        eb local run --port 9696
Deploy in AWS Elasticbeanstalk:

        eb create mterm-project-env
csv file with data - bank-additional-full.csv

Attribute Information:


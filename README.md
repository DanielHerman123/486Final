# **Reddit Partisanship Identification**

## Description
Our classifier program consists of three scripts, trainScraper.py, trainModel.py, and selectCommunities.py. The program uses Reddit's API to scrape multiple subreddits and creates a CSV file containing the contents of the last 300 posts for each subreddit. The CSV file is labeled with the posts from r/Liberal and r/Democrats as 0 for left, while the posts from r/Conservative and r/Republican are labeled as 2 for right. The CSV file, called training_data.csv, is stored in the trainingData/ directory.

The selectCommunities.py script is used to get the last 600 posts from a specified subreddit, such as r/PoliticalDiscussion, for classification with our model. The results of this script are put into the testingData/ directory. This process is repeated for multiple subreddits.

The trainModel.py script uses the data collected by trainScraper.py to fine tune a Hugging Face pretrained classifier called politicalBiasBERT by bucketresearch. It then attempts to classify any files gathered from selectCommunities.py.

The trainScraper script gets data collected from different specified subreddits using the reddit API. In addition, it is necessary to  specify the amount of content needed from each community using the command line when running this file. It will condense the data and output the data to a csv file in trainingData/ called traning_data.csv

## How to Run the Program

### trainScraper.py

To start the trainScraper.py script and scrape the specified subreddits, run the following command in your terminal:

Copy code
```bash

python3 trainscraper.py 300

```

This will start the script and scrape the specified subreddits. The resulting CSV file will be stored in the trainingData/ directory.

### selectCommunities.py
To run the selectCommunities.py script, open a command line terminal and type:

Copy code
```bash

Python3 selectcommunities.py 600 PoliticalDiscussion

```
This will get the last 600 posts from the r/PoliticalDiscussion subreddit and store the results in the testingData/ directory under the name PoliticalDiscussion.txt.

### trainModel.py
To run the trainModel.py script, open a command line terminal and type:

Copy code
```bash

Python3 trainModel.py

```
This will train a machine learning model using the data collected by trainScraper.py and selectCommunities.py. The resulting model will be used to classify files from the /testingdata directory and return percentages of idenitified posts.

## Dependencies
The program requires the following Python libraries to be installed:

Copy code
```bash

pip3 install praw
pip3 install pandas
pip3 install transformers
pip3 install torch

```

These libraries can be installed using pip as above.

## References
@misc {bucket_research_2023,
	author       = { {Bucket Research} },
	title        = { politicalBiasBERT (Revision c1ba41f) },
	year         = 2023,
	url          = { https://huggingface.co/bucketresearch/politicalBiasBERT },
	doi          = { 10.57967/hf/0315 },
	publisher    = { Hugging Face }
}
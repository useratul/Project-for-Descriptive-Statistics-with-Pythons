{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "fbae266a-1f2c-41f7-af6a-6ab0048b3ef8",
   "metadata": {},
   "source": [
    "# <font color = 'darkred'> **Descriptive Statistics with Python**"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "19e7c408-cd89-4c7e-b2be-1432760a62dc",
   "metadata": {},
   "source": [
    "## <font color = 'blue'> **Section 1**\n",
    "\n",
    "## <font color = \"red\"> **1)**. \n",
    "#### A statistics test was conducted for 10 learners in a class. The mean of their score is 85 and the variance of the score is zero. What can you interpret about the score obtained by all learners?\n",
    "\n",
    "#### **Ans:-**\n",
    "- **Mean Score = 85**\n",
    "- **Variance = 0**\n",
    "\n",
    "##### -- *When the mean score is 85 and the variance is zero, it indicates that all learners scored exactly the same on the test. Variance measures how much the scores differ from the mean; a variance of zero means there is no deviation from the mean. Therefore, each of the 10 learners scored exactly 85.*"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "66d2eaca-b82c-45fc-8039-7d98441cae8b",
   "metadata": {},
   "source": [
    "## <font color = \"red\"> **2).** \n",
    "#### In a residential locality, the mean size of the house is 2224 square feet and the median value of the house is 1500 square feet. What can you interpret about the skewness in the distribution of house size? Are there bigger or smaller houses in the residential locality?\n",
    "#### **Ans:-**\n",
    "- **Mean house size:**  *2224 square feet*\n",
    "- **Median house size:**  *1500 square feet*\n",
    "##### Since the mean is higher than the median, it means there are some very large houses pulling the average up. \n",
    "#### This tells us:\n",
    "***The distribution of house sizes is skewed to the right (positively skewed).***\n",
    "\n",
    "***There are bigger houses in the residential locality.***"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c61e2fcc-cfcd-4f60-ab52-ca8d103802ee",
   "metadata": {},
   "source": [
    "## <font color = \"red\"> **3).** \n",
    "#### The following table shows the mean and variance of the expenditure for two groups of people.You want to compare the variability in expenditure for both groups with respect to their mean. Which statistical measure would you use to evaluate the variability in expenditure? Please provide an explanation for your answer.\r",
    "                            Expenditure    Group I    Group II\n",
    "                          0    mean        $500,000    $40,000\n",
    "                          1   std.dev.     $125,000    $10,000\n",
    "#### **Ans:-**                          \n",
    "**For find the Coefficient of Variation (CV):**\n",
    "#### Formula:- **CV =  (Standard deviation / mean) * 100%**\n",
    "- **For Group I =** ($125,000 / $500,000) * 100% = 25%\n",
    "- **For Group II =** ($10,000 / $40,000) * 100% = 25%\n",
    "\n",
    "***Both groups have a variability percentage of 25%. it means the variability relative to the average amount spent is the same for both groups.*** \r\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4eecd705-67ee-462d-b085-5a0efa27bb01",
   "metadata": {},
   "source": [
    "## <font color = \"red\"> **4).**\n",
    "#### During the survey, the ages of 80 patients infected by COVID and admitted to one of the city hospitals were recorded and the collected data is represented in the less than cumulative frequency distribution table.\n",
    "                                Age(in years)     No. of Patients\n",
    "                                   5 - 15               6\n",
    "                                  15 - 25               11\n",
    "                                  25 - 35               21\n",
    "                                  35 - 45               23\n",
    "                                  45 - 55               14\n",
    "                                  55 - 65               5\n",
    "\n",
    "##### **Q1).** Which class interval has the highest frequency?\n",
    "##### **Ans:-** *(Highest Frequency  =  Highest No. of Patients)*\n",
    "\n",
    "##### ***** The highest frequency is ***23***, which corresponds to the class interval ***35 - 45*** years.*****\n",
    "\n",
    "##### **Q2).** Which age was affected the least?\n",
    "##### **Ans:-** The lowest frequency is ***5***.\n",
    "##### *** Therefore, the age group affected the least is ***55 - 65*** years. ***\n",
    "\n",
    "##### **Q3).** How many patients aged 45 years and above were admitted? \n",
    "##### **Ans:-** Age group 45 - 55 years: **14 patients** And 55 - 65 years: **5 patients**. Toal = **19 patients** was admitted.\n",
    "\n",
    "##### **Q4).** Which is the modal class interval in the above dataset?\n",
    "##### **Ans:-** The modal class interval is the one with the highest frequency. the highest frequency is **23**, which corresponds to the class interval ***35 - 45*** years.\n",
    "\n",
    "##### **Q5).** What is the median class interval of age?\n",
    "##### **Ans:-** \n",
    "                                Age(in years)     No. of Patients   *Cumulative Frequency*\n",
    "                                   5 - 15               6                6\n",
    "                                  15 - 25               11             6 + 11  = 17\n",
    "                                  25 - 35               21             17 + 21 = 38 \n",
    "                                  35 - 45               23             38 + 23 = 61\n",
    "                                  45 - 55               14             61 + 14 = 75\n",
    "                                  55 - 65               5              75 + 5  = 80\n",
    "- Total No. of patients **N** = 80 And ***Median = (N + 1) / 2 = 81/2 = 40.5.***\n",
    "- The cumulative frequency just before *40.5* is ***38.*** So the median class interval of age is **25 - 35 years.**                                 "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "089217c3-dd71-49d7-be39-e88dbfe0fd4c",
   "metadata": {},
   "source": [
    "## <font color = \"red\"> **5).**\n",
    "#### Assume you are the trader and you have invested over the years, and you are worried about the average return on investment. What average method would you use to compute the average return for the data given below?\n",
    "                            Year         Return         Asset Price\n",
    "                            2015          36%              5000\n",
    "                            2016          23%              6400\n",
    "                            2017          48%              7890\n",
    "                            2018          30%              9023\n",
    "                            2019          15%              4567\n",
    "                            2020          31%              3890\n",
    "                                                           *Total = 36770* \n",
    "##### **Ans:-** Used Formula:\n",
    "- **Weighted Return = Return × Asset Price**\n",
    "- **Weighted Average Return = Total Weighted Return / Total Asset Price**\n",
    "\n",
    "                            Year         **Weighted Return**\n",
    "                            2015        5000 * 36%   =  1800\n",
    "                            2016        6400 * 23%   =  1472\n",
    "                            2017        7890 * 48%   =  3787.2\n",
    "                            2018        9023 * 30%   =  2706.9\n",
    "                            2019        4567 * 15%   =  685.05\n",
    "                            2020        3890 * 31%   =  1205.9\n",
    "                                                        *Total = 4597.85*\n",
    "- **Weighted Average Return(%) = (4597.85 / 36770) * 100%  =  12.5%.**\n",
    "- So, the weighted average return on investment is ***12.5%.***  "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "86264a53-759b-4592-8f99-384b8222100b",
   "metadata": {},
   "source": [
    "\n",
    "\n",
    "## <font color = \"red\"> **6).** \n",
    "#### Suppose you have been told to measure the average height of all the males on the earth. What would be your strategy for the same? Would the average height be a parameter or a statistic? Justify your answer.\n",
    "\n",
    "### **Ans:-** Calculating the Avg Height = Sum of Height / No. of individuals\n",
    "- Collecting some sample heights as data and calculate the sample avg heights. By using this statement getting a quick estimate of the avg heights of all males on the earth.\n",
    "- This Avg sample is best estimate to calulate the global avg height of all the males on the earth."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "f73da46c-733b-4f1b-bbd5-1ac6d4107d1f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Average height: 173.2 cm\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "# Sample data\n",
    "data = {'Height': [170, 175, 180, 165, 172, 178, 169, 177]}\n",
    "\n",
    "df = pd.DataFrame(data)\n",
    "\n",
    "# Calculating the average height\n",
    "average_height = df['Height'].mean()\n",
    "\n",
    "print(f\"Average height: {average_height:.1f} cm\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8804b5e9-40e2-49e6-9f21-181dc5513b9c",
   "metadata": {
    "jp-MarkdownHeadingCollapsed": true
   },
   "source": [
    "## <font color = \"red\"> **7).**\n",
    "#### Calculate the z score of the following numbers:\n",
    "- **X = [4.5,6.2,7.3,9.1,10.4,11]**\n",
    "\n",
    "#### **Ans:-** Mean of ***X = (4.5+6.2+7.3+9.1+10.4+11) / 6 = 8.08***\n",
    "- Calculate Squared Deviation from the mean:\n",
    "\n",
    "                    (4.5 - 8.08) * (4.5 - 8.08) = {(-3.58) * (-3.58)} = 12.82\n",
    "                    (6.2 - 8.08) * (6.2 - 8.08) = {(-2.06) * (-2.06)} = 4.24\n",
    "                    (7.3 - 8.08) * (7.3 - 8.08) = {(-0.78) * (-0.78)} = 0.61\n",
    "                    (9.1 - 8.08) * (9.1 - 8.08) = {(1.02) * (1.02)}   = 1.04\n",
    "                    (10.4 -8.08) * (10.4 -8.08) = {(2.32) * (2.32)    = 5.38\n",
    "                    (11  - 8.08) * (11  - 8.08) = {(2.92) * (2.92)    = 8.53\n",
    "- *Sum of squared deviation* ***:*** ***(12.82 + 4.24 + 0.61 + 1.04 + 5.38 + 8.53) = 32.62***\n",
    "- **Variance = 32.62 / 6 = 5.44**\n",
    "- **Standard Deviation** : *square root of variance* **:**  **2.3**\n",
    "- **Calculate Z-Score :**\n",
    "\n",
    "                      (4.5 - 8.08) / 2.3 = -1.55\n",
    "                      (6.2 - 8.08) / 2.3 = -0.81\n",
    "                      (7.3 - 8.08) / 2.3 = -0.33\n",
    "                      (9.1 - 8.08) / 2.3 =  0.44\n",
    "                      (10.4- 8.08) / 2.3 =  1.01\n",
    "                      (11  - 8.08) / 2.3 =  1.26\n",
    "- So the *Z-Scores* for the given numbers are approximately : ***(-1.55, -0.81, -0.33, 0.44, 1.01, 1.26)***"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ffb049e6-7353-4f59-b3b0-9a63b94172b0",
   "metadata": {},
   "source": [
    "# <font color = 'blue'> **Section 2**\n",
    "\n",
    "##### *You are expected to perform statistical analysis for the Bank Personal Loan Modelling dataset. Below is the data dictionary. For questions, 8 to 20 use the Bank Personal Loan Modelling dataset and answer the given questions.*\n",
    "\n",
    "##        <font color = 'purple'>     **Performing with Bank Personal Loan Data**\n",
    "- Question 8 to 20 retrieving from loan data."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "5ab7f35c-0b0d-48d0-b0af-26847a7e0e9f",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import seaborn as sns\n",
    "import matplotlib.pyplot as plt"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2388b914-e69b-4bab-9437-cf0e1ba363cf",
   "metadata": {},
   "source": [
    "### **Data Loading in python** "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "bc47cf4d-06ec-4a05-85ac-5aac04c681a0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>ID</th>\n",
       "      <th>Age</th>\n",
       "      <th>Experience</th>\n",
       "      <th>Income</th>\n",
       "      <th>ZIP Code</th>\n",
       "      <th>Family</th>\n",
       "      <th>CCAvg</th>\n",
       "      <th>Education</th>\n",
       "      <th>Mortgage</th>\n",
       "      <th>Personal Loan</th>\n",
       "      <th>Securities Account</th>\n",
       "      <th>CD Account</th>\n",
       "      <th>Online</th>\n",
       "      <th>CreditCard</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>25</td>\n",
       "      <td>1</td>\n",
       "      <td>49</td>\n",
       "      <td>91107</td>\n",
       "      <td>4</td>\n",
       "      <td>1.6</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>45</td>\n",
       "      <td>19</td>\n",
       "      <td>34</td>\n",
       "      <td>90089</td>\n",
       "      <td>3</td>\n",
       "      <td>1.5</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>39</td>\n",
       "      <td>15</td>\n",
       "      <td>11</td>\n",
       "      <td>94720</td>\n",
       "      <td>1</td>\n",
       "      <td>1.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>35</td>\n",
       "      <td>9</td>\n",
       "      <td>100</td>\n",
       "      <td>94112</td>\n",
       "      <td>1</td>\n",
       "      <td>2.7</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>35</td>\n",
       "      <td>8</td>\n",
       "      <td>45</td>\n",
       "      <td>91330</td>\n",
       "      <td>4</td>\n",
       "      <td>1.0</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4995</th>\n",
       "      <td>4996</td>\n",
       "      <td>29</td>\n",
       "      <td>3</td>\n",
       "      <td>40</td>\n",
       "      <td>92697</td>\n",
       "      <td>1</td>\n",
       "      <td>1.9</td>\n",
       "      <td>3</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4996</th>\n",
       "      <td>4997</td>\n",
       "      <td>30</td>\n",
       "      <td>4</td>\n",
       "      <td>15</td>\n",
       "      <td>92037</td>\n",
       "      <td>4</td>\n",
       "      <td>0.4</td>\n",
       "      <td>1</td>\n",
       "      <td>85</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4997</th>\n",
       "      <td>4998</td>\n",
       "      <td>63</td>\n",
       "      <td>39</td>\n",
       "      <td>24</td>\n",
       "      <td>93023</td>\n",
       "      <td>2</td>\n",
       "      <td>0.3</td>\n",
       "      <td>3</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4998</th>\n",
       "      <td>4999</td>\n",
       "      <td>65</td>\n",
       "      <td>40</td>\n",
       "      <td>49</td>\n",
       "      <td>90034</td>\n",
       "      <td>3</td>\n",
       "      <td>0.5</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4999</th>\n",
       "      <td>5000</td>\n",
       "      <td>28</td>\n",
       "      <td>4</td>\n",
       "      <td>83</td>\n",
       "      <td>92612</td>\n",
       "      <td>3</td>\n",
       "      <td>0.8</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>5000 rows × 14 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "        ID  Age  Experience  Income  ZIP Code  Family  CCAvg  Education  \\\n",
       "0        1   25           1      49     91107       4    1.6          1   \n",
       "1        2   45          19      34     90089       3    1.5          1   \n",
       "2        3   39          15      11     94720       1    1.0          1   \n",
       "3        4   35           9     100     94112       1    2.7          2   \n",
       "4        5   35           8      45     91330       4    1.0          2   \n",
       "...    ...  ...         ...     ...       ...     ...    ...        ...   \n",
       "4995  4996   29           3      40     92697       1    1.9          3   \n",
       "4996  4997   30           4      15     92037       4    0.4          1   \n",
       "4997  4998   63          39      24     93023       2    0.3          3   \n",
       "4998  4999   65          40      49     90034       3    0.5          2   \n",
       "4999  5000   28           4      83     92612       3    0.8          1   \n",
       "\n",
       "      Mortgage  Personal Loan  Securities Account  CD Account  Online  \\\n",
       "0            0              0                   1           0       0   \n",
       "1            0              0                   1           0       0   \n",
       "2            0              0                   0           0       0   \n",
       "3            0              0                   0           0       0   \n",
       "4            0              0                   0           0       0   \n",
       "...        ...            ...                 ...         ...     ...   \n",
       "4995         0              0                   0           0       1   \n",
       "4996        85              0                   0           0       1   \n",
       "4997         0              0                   0           0       0   \n",
       "4998         0              0                   0           0       1   \n",
       "4999         0              0                   0           0       1   \n",
       "\n",
       "      CreditCard  \n",
       "0              0  \n",
       "1              0  \n",
       "2              0  \n",
       "3              0  \n",
       "4              1  \n",
       "...          ...  \n",
       "4995           0  \n",
       "4996           0  \n",
       "4997           0  \n",
       "4998           0  \n",
       "4999           1  \n",
       "\n",
       "[5000 rows x 14 columns]"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "loan_data = pd.read_csv(r\"C:\\Users\\DeLL\\Downloads\\Bank Personal Loan Modelling.csv\")\n",
    "loan_data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "1af72135-3131-4c54-b8d2-8b365e88f7a9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 5000 entries, 0 to 4999\n",
      "Data columns (total 14 columns):\n",
      " #   Column              Non-Null Count  Dtype  \n",
      "---  ------              --------------  -----  \n",
      " 0   ID                  5000 non-null   int64  \n",
      " 1   Age                 5000 non-null   int64  \n",
      " 2   Experience          5000 non-null   int64  \n",
      " 3   Income              5000 non-null   int64  \n",
      " 4   ZIP Code            5000 non-null   int64  \n",
      " 5   Family              5000 non-null   int64  \n",
      " 6   CCAvg               5000 non-null   float64\n",
      " 7   Education           5000 non-null   int64  \n",
      " 8   Mortgage            5000 non-null   int64  \n",
      " 9   Personal Loan       5000 non-null   int64  \n",
      " 10  Securities Account  5000 non-null   int64  \n",
      " 11  CD Account          5000 non-null   int64  \n",
      " 12  Online              5000 non-null   int64  \n",
      " 13  CreditCard          5000 non-null   int64  \n",
      "dtypes: float64(1), int64(13)\n",
      "memory usage: 547.0 KB\n"
     ]
    }
   ],
   "source": [
    "loan_data.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "68d39921-8d6a-4087-a776-bff0fd5d8264",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>ID</th>\n",
       "      <th>Age</th>\n",
       "      <th>Experience</th>\n",
       "      <th>Income</th>\n",
       "      <th>ZIP Code</th>\n",
       "      <th>Family</th>\n",
       "      <th>CCAvg</th>\n",
       "      <th>Education</th>\n",
       "      <th>Mortgage</th>\n",
       "      <th>Personal Loan</th>\n",
       "      <th>Securities Account</th>\n",
       "      <th>CD Account</th>\n",
       "      <th>Online</th>\n",
       "      <th>CreditCard</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>25</td>\n",
       "      <td>1</td>\n",
       "      <td>49</td>\n",
       "      <td>91107</td>\n",
       "      <td>4</td>\n",
       "      <td>1.6</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>45</td>\n",
       "      <td>19</td>\n",
       "      <td>34</td>\n",
       "      <td>90089</td>\n",
       "      <td>3</td>\n",
       "      <td>1.5</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>39</td>\n",
       "      <td>15</td>\n",
       "      <td>11</td>\n",
       "      <td>94720</td>\n",
       "      <td>1</td>\n",
       "      <td>1.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>35</td>\n",
       "      <td>9</td>\n",
       "      <td>100</td>\n",
       "      <td>94112</td>\n",
       "      <td>1</td>\n",
       "      <td>2.7</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>35</td>\n",
       "      <td>8</td>\n",
       "      <td>45</td>\n",
       "      <td>91330</td>\n",
       "      <td>4</td>\n",
       "      <td>1.0</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4995</th>\n",
       "      <td>4996</td>\n",
       "      <td>29</td>\n",
       "      <td>3</td>\n",
       "      <td>40</td>\n",
       "      <td>92697</td>\n",
       "      <td>1</td>\n",
       "      <td>1.9</td>\n",
       "      <td>3</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4996</th>\n",
       "      <td>4997</td>\n",
       "      <td>30</td>\n",
       "      <td>4</td>\n",
       "      <td>15</td>\n",
       "      <td>92037</td>\n",
       "      <td>4</td>\n",
       "      <td>0.4</td>\n",
       "      <td>1</td>\n",
       "      <td>85</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4997</th>\n",
       "      <td>4998</td>\n",
       "      <td>63</td>\n",
       "      <td>39</td>\n",
       "      <td>24</td>\n",
       "      <td>93023</td>\n",
       "      <td>2</td>\n",
       "      <td>0.3</td>\n",
       "      <td>3</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4998</th>\n",
       "      <td>4999</td>\n",
       "      <td>65</td>\n",
       "      <td>40</td>\n",
       "      <td>49</td>\n",
       "      <td>90034</td>\n",
       "      <td>3</td>\n",
       "      <td>0.5</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4999</th>\n",
       "      <td>5000</td>\n",
       "      <td>28</td>\n",
       "      <td>4</td>\n",
       "      <td>83</td>\n",
       "      <td>92612</td>\n",
       "      <td>3</td>\n",
       "      <td>0.8</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>5000 rows × 14 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "        ID  Age  Experience  Income  ZIP Code  Family  CCAvg  Education  \\\n",
       "0        1   25           1      49     91107       4    1.6          1   \n",
       "1        2   45          19      34     90089       3    1.5          1   \n",
       "2        3   39          15      11     94720       1    1.0          1   \n",
       "3        4   35           9     100     94112       1    2.7          2   \n",
       "4        5   35           8      45     91330       4    1.0          2   \n",
       "...    ...  ...         ...     ...       ...     ...    ...        ...   \n",
       "4995  4996   29           3      40     92697       1    1.9          3   \n",
       "4996  4997   30           4      15     92037       4    0.4          1   \n",
       "4997  4998   63          39      24     93023       2    0.3          3   \n",
       "4998  4999   65          40      49     90034       3    0.5          2   \n",
       "4999  5000   28           4      83     92612       3    0.8          1   \n",
       "\n",
       "      Mortgage  Personal Loan  Securities Account  CD Account  Online  \\\n",
       "0            0              0                   1           0       0   \n",
       "1            0              0                   1           0       0   \n",
       "2            0              0                   0           0       0   \n",
       "3            0              0                   0           0       0   \n",
       "4            0              0                   0           0       0   \n",
       "...        ...            ...                 ...         ...     ...   \n",
       "4995         0              0                   0           0       1   \n",
       "4996        85              0                   0           0       1   \n",
       "4997         0              0                   0           0       0   \n",
       "4998         0              0                   0           0       1   \n",
       "4999         0              0                   0           0       1   \n",
       "\n",
       "      CreditCard  \n",
       "0              0  \n",
       "1              0  \n",
       "2              0  \n",
       "3              0  \n",
       "4              1  \n",
       "...          ...  \n",
       "4995           0  \n",
       "4996           0  \n",
       "4997           0  \n",
       "4998           0  \n",
       "4999           1  \n",
       "\n",
       "[5000 rows x 14 columns]"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "## Handling duplicate data\n",
    "loan_data1 = loan_data.drop_duplicates()\n",
    "loan_data1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "b8d1e4d1-61ea-4a6f-b19d-23e0dfffaaf7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAACA4AAAPTCAYAAAA6w9n4AAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjguNCwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8fJSN1AAAACXBIWXMAAA9hAAAPYQGoP6dpAADxPklEQVR4nOzddXhUR9sG8Ht2N04SkgABQgjuxa0tTkuxlra4Q5Hi7l6gaJHixT1AcYp7cAvuUggeLJCE6O7z/cG3p7tJoNAXsgncv+viKuw5u+/MO3vOnjNznxklIgIiIiIiIiIiIiIiIiIiIiL6JOlsXQAiIiIiIiIiIiIiIiIiIiKyHQYHiIiIiIiIiIiIiIiIiIiIPmEMDhAREREREREREREREREREX3CGBwgIiIiIiIiIiIiIiIiIiL6hDE4QERERERERERERERERERE9AljcICIiIiIiIiIiIiIiIiIiOgTxuAAERERERERERERERERERHRJ4zBASIiIiIiIiIiIiIiIiIiok8YgwNERERERERERERERERERESfMAYHiIiIiIiIiIiIiIiIiIiIPmEMDhAREREREREREREREREREX3CGBwgIiIiIiIiIiIiIiIiIiL6hDE4QERERERERERERET0iRCRt3qNiIiIPi0MDhARERERERERERERfSKUUoiKisKjR48AADExMVpwYMeOHbh27Zoti0dEREQ2wuAAEREREREREREREdEnIjY2FpMnT0a1atVw4MAB2NnZQafTYcWKFahUqRLatGmD8PBwWxeTiIiIEpnB1gUgIiIiIiIiIiIiIqLEYTAY8PLlSxw/fhwVKlTApUuXcP36ddSrVw+pU6dGgwYN4OLiYutiEhERUSJTwsWLiIiIiIiIiIiIiIg+KS1btsTcuXNhMBgQGxuLVKlSYfz48WjUqBEAQESglLJxKYmIiCixcKkCIiIiIiIiIiIiIqJPRGxsLABg9uzZKFu2LJRSUEqhQ4cOWmjAaDQyNEBERPSJ4YwDRERERERERERERESfmDNnzqBgwYLav+3t7bF//34ULVoUJpMJOh2fOyQiIvqU8JefiIiIiIiIiIiIiOgTExsbiw4dOmD16tVo164doqOjUapUKRw5cgQ6nQ4mk8nWRSQiIqJExBkHiIiIiIiIiIiIiIg+ESKiLUPw6NEjpE6dGgDQsmVLzJ07F/b29ti7dy9KlCihzTxgNBqh1+ttWWwiIiL6wDjjABERERERERERERHRRyrus4OWMwmkTp0aUVFRAIDZs2ejZcuWiI6ORtmyZbWZB6Kjo7XQwLx583Djxo3EKzwRERElGgYHiIiIiIiIiIiIiIg+QpazC+zevRudOnVC2bJl0bdvXyxfvhwA4ODggMjISADAzJkzrcIDhw4dgr29PQBg9OjRaNGiBVq0aIGYmBjbVIiIiIg+GC5VQERERERERERERET0EVuzZg1q1aqlzT6glIJer0f79u0xYcIEAEBERAScnJwAAK1atcKcOXPg4OCAYcOG4fTp01iyZAm8vLywY8cOFChQwGZ1ISIiog+DwQEiIiIiIiIiIiIioo9UYGAgKlasiIiICPTv3x9+fn64cuUKxo8fj8jISDRt2hTz5s0DYB0e6Ny5MyZPnqx9TrZs2bB27VrkyZPHJvUgIiKiD8tg6wIQEREREREREREREdH7Ybk8AQAcOXIEz58/x+zZs/HTTz9pr1esWBHVq1fHggULAADz5s2Dk5MTIiMj4ejoiN9//x2ff/45bt26Bb1ej7p168LX1zfR60NERESJgzMOEBERERERERERERF9ZFavXg07OzucPXsWu3btwo4dOwAAJpMJSikopXDixAmUKVMGERERVjMPmMMDRERE9OlgcICIiIiIiIiIiIiI6CNy9uxZFChQAPb29siWLRv8/PywceNGq31MJhN0Ot1rwwMxMTGws7MDEH8WAyIiIvr46GxdACIiIiIiIiIiIiIien/y5MmDjh07Ijo6GhcuXEB0dDSio6MBvAoBAIBOp4PJZEKRIkUQEBAAJycnLFiwAC1btgQALTQAgKEBIiKiTwCDA0REREREREREREREyVTcSYVjY2Oh1+sxfvx49OjRAwCwc+dOLFu2DMCrEMDrwgNubm6YO3cu2rdvn7iVICIiIptjcICIiIiIiIiIiIiIKJkyzwZw6NAhREZGwmAwaOGBkSNHok+fPgCA5s2bY+3atdp7EgoPbN26FenSpUOLFi1sUhciIiKyHSVx44hERERERERERERERJRsbN68GdWqVUPVqlWxatUqODg4IDY2FgaDAUajEQMGDMDo0aORIkUKLFq0CDVq1ADwarYCc/DAaDRCr9cjKioKDg4OtqwOERER2QBnHCAiIiIiIiIiIiIiSsZSp04Nb29vbNq0CQ0bNkRUVJTVzAPDhw9Hz549ERYWhkaNGmHdunUArGce0Ov1AAB7e3ub1YOIiIhsh8EBIiIiIiIiIiIiIqJkrGjRoti0aROyZMmC1atXJxgeGDFiBHr27Inw8PDXhgfM/yYiIqJPD4MDRERERERERERERETJXKFChbBixYq3Dg80b94cK1asAMCwABEREQFKLKOERERERERERERERESU5IhIvAF+k8kEnc76+cDAwEDUqVMHN27cwI8//oglS5bAwcEBsbGxMBgMMBqNGDhwIEaNGoX06dPj0qVLcHFxYXiAiIjoE8fgABERERERERERERFRMrFhwwY8evQIP/30E4DXhwdq166Nv//+Gz/++CMWL14MR0dHq/DAsGHD8OOPPyJ//vy2qAYRERElMQwOEBERERERERERERElAxcuXEC+fPng4uKCadOmoXHjxgASDg/s3bsXjRo1wt27d1GjRg34+/vD0dERMTExsLOzs0XxiYiIKAnT/fsuRERERERERERERERka97e3ujduzciIiLQs2dPLFiwAACg0+lgMpms9i1WrBhq1qwJpRTWrVuHJk2aIDIykqEBIiIiShCDA0REREREREREREREyYCXlxd69uyJAQMGIDg4GL169cL8+fMBxA8PODs7o0SJEhARpE2bFitXrkTr1q1tVHIiIiJK6hgcICIiIiIiIiIiIiJKgiyDAEajEQDg6emJTp06YdCgQXj06BF69+4dLzwQExMD4NUMBQUKFMCsWbNQqFAhdO/ePdHrQERERMmDEhGxdSGIiIiIiIiIiIiIiAgQESil4r0eGxsLg8Gg/fvx48eYMmUKhg4dijRp0mDkyJFo3ry51XsaNmyIXbt24ebNm1BKwd7e/oOXn4iIiJInw7/vQkREREREREREREREH5plaODIkSNYs2YN9u7dC0dHR7i5uaFz587Inz8/UqVKhVSpUqFDhw4AgKFDh6Jt27Z48OABfvrpJ7i4uGD48OHw9/dHrVq1GBogIiKif8UZB4iIiIiIiIiIiIiIkpA1a9agWbNmCA0NBQDY2dkhJiYGDg4OaNKkCZo2bYovvvgCAPDkyRPMmjUL/fr1AwBkzJgRABAUFARvb2/s3bsXOXLksE1FiIiIKNlgcICIiIiIiIiIiIiIKInYtm0bqlSpAhcXFwwYMACVKlVCWFgYli5dipUrV+Lp06coX748BgwYgLJly2rvW7duHQYNGoRbt27B2dkZOXLkwMyZMxkaICIiorfCpQqIiIiIiIiIiIiIiJKABw8eYMSIERARTJgwAS1atNC2lSpVCiVLlsTMmTOxc+dOuLu7I02aNMidOzdEBDVq1ECpUqUQHh4OnU4Hd3d3uLq62rA2RERElJxwxgEiIiIiIiIiIiIioiTg6tWrKFOmDHLkyIG9e/cCAIxGIwBAr9cDANauXYs+ffrg1q1bmDhxIn7++WcYjUZtOxEREdF/obN1AYiIiIiIiIiIiIiICDh37hwePnyIyMhIhIWFwWQyQa/XQ6/Xw/wM4Pfff4+mTZsiKioKI0aMwP379xkaICIiov8ZgwNERERERERERERERDZkDgVkyZIFHh4eCAsLg9FohE6ng8lkAgAopbS/d+vWDXnz5sWLFy/w6NEjm5WbiIiIPh4MDhARERERERERERERJRLL1YNjYmIAvAoFAICPjw9SpUqFixcvYsiQIQBgFR7Q6XSIjY2FUgrOzs54/vw5bt++nbgVICIioo8SgwNERERERERERERERIlARLSQwMmTJzFq1CgMGjRI254qVSqMHDkSrq6umD9/PqZNmwbgn8BAbGwsDAYD7O3tERkZiSxZsqBQoUI2qQsRERF9XBgcICIiIiIiIiIiIkpklk+d06fBMjSwYcMG/PDDDxg8eDA2bNiAPXv2aPt9/vnn+Omnn/Dy5UuMGjUKQ4cOBQAYDAYYDAYAwMCBA3H27Fl89tlnSJEiRaLXhYiIiD4+SniFSkRERERERERERJRoLAeQr169ivDwcDx8+BDFihVDypQpodPxea+P2YYNG1CjRg3Y2dlh4MCB6NWrF/R6PfR6vbbP+fPnMWnSJCxevBgRERGoVq0aypcvj/Tp02PDhg3w9/eHt7c39u3bh2zZstmwNkRERPSxYHCAiIiIiIiIiIiIyAY2bNiAzp07IyQkBCEhIfjyyy9RqVIl9OnTB3Z2drYuHn0AZ86cQfXq1XHnzh3MmzcPTZs21bZZBkoA4Pr161i3bh2GDx+OkJAQq8/57LPPsGzZMuTOnTuxik5EREQfOQYHiIiIiIiIiIiIiBLZpk2bUL16dQBAqVKlcPv2bTx+/Bjh4eFo2LAh5syZA3t7exuXkt4Xk8kEnU6HSZMmoUuXLujTpw9GjBhhte11rl27hqVLl+LOnTvQ6/UoXrw4KleujHTp0iVW8YmIiOgTwOAAERERERERERER0QdmfprcZDIhLCwMNWrUQGBgIH777Te0atUKN2/exOHDh9G7d2/cvn0btWrVwuLFixke+EiY2/+bb77B9u3bsWXLFlSqVOm1oQHz/nFnISAiIiL6UAy2LgARERERERERERHRx848+BscHAxPT0+cO3cOHTp0QKtWrQAAmTJlQqZMmZAlSxbUq1cPK1euBACGBz4S5vY3GAwwGAzw8vL61/1DQ0Ph6uoKAIiJidGWr2CYgIiIiD6E189/RERERERERERERETvzYoVK5AzZ070798f7u7uqFevHgAgNjZW26d48eJYsWIFMmXKhJUrV6JRo0aIjo62VZHpPYmJiYHJZIKdnR1iY2OxbNkyAEhwtgGj0QgAWLlyJbp37w4AWmgAAEMDRERE9EEwOEBERERERERERET0gcXExCAwMBChoaHw9/fH3bt3cffu3QT3LVq0KMMDyZTlysAhISFaG9vZ2UGn0+Hnn3+Go6Mjtm3bhj179sR7n9FohF6vBwAsWLAAK1aswM2bNxOt/ERERPTpYnCAiIiIiIiIiIiI6AOzs7NDjx49MHDgQNy7dw9RUVHYuXMngFfT15tMJqv944YHvvvuO4YHkjjLJQT279+P1q1bo3bt2liwYIG2T758+VCpUiWcPXsWU6ZMwdGjRwG8mkUgNjZWCw10794dAQEBqFSpEtKkSZP4lSEiIqJPDoMDRERERERERERERIkgVapU6NixIwYPHgwAGDduHGbPng3g1ZT1CYUH/vzzT7i5uWHbtm0IDg5O9DLT2zOHBtasWYOqVati5cqVSJ8+PXx8fLTlB3x9fdGxY0fkyZMHq1evRv/+/TFr1iwAr2aliIiIQJcuXTBhwgRkzZoVAwcOhLOzs83qRERERJ8OJZZzJxERERERERERERHRe2cymbT17B8/fowpU6Zg6NChSJMmDcaOHYvGjRvH28/s1KlTcHFxQfbs2RO93PRutm3bhqpVqyJFihQYMWIE2rVrp22zbNvNmzdj+PDhOH78OGJiYpAvXz6YTCa8fPkSN2/ehK+vL7Zs2YLcuXPbqipERET0iWFwgIiIiIiIiIiIiOg9sJyq/uXLl3j58iWePXuW4ID/kydPMHHiRPz666/w9vbGmDFj3hge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lCtX7q3DA4MGDUr8itB78/jxY8mXL5+4uLjIokWLXnufHRwcLH5+flK6dGmt7UNCQtjXSpSMMThARMmOyWSSmJgYadq0qSil4s0qcODAASlYsKAopaRfv342KiW9L5YXmkuWLNEGgM1/ypUrJ0OGDNH2u3TpkvTu3Vtb87h06dIydOhQ6dGjhzalcbZs2bS125h8Th6mTZsW75i2bLv79+9rT5599dVXVk+mxcbGyvDhwyVnzpxy6dKlRC03/cPcXsHBwdrAkbOzs9XxXL9+fW3WCN5kftwSat8xY8ZInjx5tH9bDgRv2LDhX8MDbdq0kRs3bnzgktP/wtxpfPbsWcmdO7d4eHjI/v37te3m88SNGze06VDN5wpfX1+ZNm0az+PJ3P3796VChQraE22W4YGIiAgZM2aMZM+eXXsauVGjRvLDDz9IsWLFRCkl6dKl4xI0ycCsWbPE0dFRfv75Z/H29taeRLa8dntdeKB27draoISfn99rz+vBwcEMCSYBmzdvFqWUODk5yalTpyQkJER69OghOp3O6hqvbt26cvjwYe13+/z585IhQwaxs7PjUjPJzOHDh8XT01NcXFxk7ty5/7r/rl27xMvLS5RS4ujoqAUJ0qVLx9lCkrh3vR8zn9f79u0rBoNBGjduHG/mIEraLly4IC1atHiv4YHhw4cnfkXofxYbGyuhoaHStWtXbYmKo0ePase55bH9+PFjSZMmjWzfvl3mzZsnJ0+etGHJieh9YHCAiJKlx48fi4+PjxQqVMjqJuTgwYPa2tZ9+/a1eo/lQCIlP/7+/tqNx3fffSd169aVtGnTipOTkyilpEaNGlZTqC1evFhy5sxp1WGVIUMGadiwody7d09EGBpILkwmk9SqVUuUUrJixQoREauks7kdT506JZkzZxallPbUk7lzMjY2Vp48eZLIJSczcxs9fPhQsmbNqh3Hp06dkm3btsnkyZO147RJkyb/6X+DT7EkH5adkH///bccP35cLl68KP369ZOKFSu+dt/169cnGB6I++QDnzxPOsyDenGPT5PJJD/99JP2tGHc2UYmTJigDTA0btxY65xUSombm5v88ssviVYHen/MvwUPHjyQMmXKJBgeiIyMlPXr12uziBgMBu0a7ocffrBakoiSpqioKOnTp48opcTb21scHR1l586dIhL//Gx5bpgzZ47kzp1bO9ZLlCihBX0t38dgoW1Z/v//5MkT+fLLLyVVqlQyZcoU7fUHDx7IokWLpEyZMtKpUyeZM2dOvPdHR0dLhgwZpGjRomzTZMJ8vJoHkUaNGqVt+7f76suXL0uzZs2kYMGCki9fPqlZs6ZcuXLlg5aX/rvY2NgEr93e1saNG7Vz+caNG9938egDe1/hgVWrVomjo6MEBgYmfiXoX1ke03fv3pULFy7Itm3bZO/evSLyz7XXhQsXpGjRotp928aNG+XFixdWn9WjRw9RSsnu3bsTrfxE9GExOEBEydLly5fFxcVFvvjiC62z+dChQ68NDTx48EBmz57Np9SSEcuL2MePH0vRokXFy8tLWx9V5NX34I8//pC0adOKUkoqV65sdYMbGhoqmzdvliVLlsjSpUvl5s2b2iAGQwPJh9FolHr16olSSkaPHp3gPiaTSaKjo7U1Fdu3b2/1frIdy5kGsmXLJkop6dKlS7zBA/M09UopmTp1qi2KSokg7iwyfn5+opSS1KlTi4+Pj3h6esq+ffte+x7L8ECvXr0YEkiCnj9/Lvv375du3bpJ/fr1rQaFRf45J9+6dUuyZs0qqVKlks2bN2vbR40aJUopsbOz0zqbQ0JCZMKECZI/f37JkiULn05N4szHrPm/ltdcbxMeMNuzZ49s2rRJ5s+fL1euXOF01snIkydP5JdfftF+17t06aJti3tdZvnv06dPy19//SVr167V1j3nNXvSFB4eLrdu3RKllAwbNkx73fI3O+5vtGWQ3zxVfZcuXawGmihpi4qKkly5ckmKFCm03+J/u9cyb4+JiZGoqCgJDw/nQx1JTHR0tNy8eVPGjBkjzZs3l+rVq0vt2rVl6dKl//nJ4Xbt2olSSr799lt59OjR+y0wfXDvKzxgubQoJR2Wv7mbN2+WwoULW80GWa5cOZk0aZK2lNDx48clT548opSSXLlySePGjWXnzp2ye/du+fnnn7Xl5SyXDSWi5I3BASJKVswXN8+ePZPs2bNrUxqfOnUqwdBARESEiLxaW8/Dw0OWLFmS+IWm/8mDBw+0TqkRI0Zor5u/CzExMbJnzx5Jnz69KKWkQ4cO//qZ7JhKfsxT2FatWlWbMSIh5sHnr776itPXJiEPHjywCg1ERUWJyD9PipuPyRYtWohOp5OePXvarKyUOFasWKF1TBQvXlzriNDpdNKvX794HYyW5+0NGzZoU94OHTo0sYtOb3Dnzh2pXbu2uLu7i1JK3N3dpUuXLvE6DU0mk7x48UKaNGkiSilp3bq1iIj89ttvWmhg9erV8T7/2rVrEhISIiKcWSI5sJyC+nXhgbJly2rrnJvDAwz8fRweP34sw4cP1871M2bM0La97ZOs/C4kTQsWLJDMmTPLvHnzJGfOnHLu3DkRef2MEnHbt3///qKUkty5c2sDTZQ8hIaGiq+vr2TMmPGtwlyW92MMASVNz58/l0GDBkm+fPmsZms0LxWVPn16Wbx48Vt/nvm437FjhyilJE+ePNq1GyUv/yU8cOvWLRH55/eAfW9J25o1a7TjvVatWtKpUyepWLGipEqVStzd3aVFixZaGODcuXPy448/ire3tzYznOXsrlxKjOjjwuAAESVZlheY5pSjyKsbkcjISKlWrZoopaROnTpaaKB3797afuYUu8lkkrJly0qKFCnk6NGjiVZ++t+Zpy8fP3685MqVS/bs2SMi8aelFhFZtmyZeHh4SObMmeXw4cMiwpuU5MSyre7cuSMnT56Uu3fvaq8FBARIxowZxc7OTqZPnx7v/ebvxO7du7WbHko6zFMW6/V6+eOPP0Qk4XWOzTNG1KtXzyblpA/H8hiPjIyU0qVLS+rUqWXlypUi8s/U1g4ODmIwGOS3336LNwWi5WesXLlScuXK9dq1rynx/f3331pAqEyZMvLnn3/K33//HW8ZAksBAQGilBJ7e3upU+f/2LvzcKvKuuHjex1mQZnFCTERMC0RQ8WecChLTQ3LTIXEEWckITE0EXFCSx+nBqeEcgg1zXLK6VWjQnFC1CBnQFFARGYZzu/9w2ev9j7ngFjC2XB/PtfF9dje++x3nXedtfbaa33Xff+gzmigurr6vxoulzXnlltuWemQpLfeemtkWRbnnntu/lhd8cCMGTOiR48e+dypxXjAOq58q7OOZs2aFeeff34+ssxNN92UPycKWDctX7489t1338iyLI/4HnnkkU/9uQ8++CDGjx8f3/ve9yLLsth8881dZFgHffTRR7HFFlvkU8h9WvRz6623unmjgs2ePTv23nvvyLIsOnfuHIMGDYqbb745fv/738exxx4bu+66a35h8OKLL/5MU//Nnz8/+vTpEy+88MIa/A34vJRuy6XHa581HujSpUs+zRCVbcKECdG2bdto1KhR2ZRCERGXXnppNG7cOLIsKzt2mzFjRvzlL3+Jvn37xje+8Y3Ya6+94owzzqhz5DBg3SYcACre9ddfH4cddlh+J0PRU089FS1atMi/yJSONFA6p25xiLRjjz02Fi5cuFaXnf/OcccdF1mWRfPmzSPLsjovGBe999578a1vfSsPDVh3lH5Jffjhh+NrX/tatGzZMi655JKyu46HDx8eWZZFkyZN4pZbbql1UTEi8jmzr7jiilrvTf1ZsGBBPoRdlmVx3XXX5c+Vnpj4/ve/H40aNYrRo0fXx2KyFkyePDkmT54cLVu2jEsvvbTW81dccUVstNFG0ahRo7jssstq3c1Wuk0XRxVy53n9e+edd6Jbt26RZVkMHDiw7Lmaw9bXdOKJJ0aDBg3yO1f+8Ic/1PpZKs8TTzwRWZZFq1atak0vEhFx22235fv8Cy+8MH+8rnjgtddey+9e2nnnnQVB64DSbfPtt9+OiRMnxi233BLjx4+PGTNmlL121qxZMWLECPHAemTBggXRp0+fPPwaPnx4/plcl8WLF8fVV18d7du3jyzL4pvf/Ga8+uqra3GJ+TwUt9czzjgjnxqurhHeivv2pUuXxo477hjf+973TDVTgWbOnJmP+NWnT598ephSkydPjtNPPz3/PP+0bb2o+LdiH1/ZVvc4e3XjgWII6jiushW3y+KoUBdccEHZ85MmTYrddtstsiyLk08+eZXv47sarL+EA0DFKT3BPGvWrPzLzIABA2LSpEn565YvXx6XX355flH54osvrvVep556amRZFj169Ij33nuv7P2pLCv7Ullch8W7kIvrsS5XXHFFZFkWxxxzjC+p66A777wzH+6sf//+8de//rXWkJbHH398fpLyrLPOioceeig+/vjjmD9/fgwdOjSyLItu3bqp3OtRzW2vuA4XLlxYFg/ccMMNZa8rDlG+3XbbOZm8nhozZkxsuOGGMWrUqNhyyy3jySefjIhP/kZK/26uvPLK1YoHfJ5Xhnnz5sUPf/jDyLIsTjrppPzx1R2SeMyYMfl+4X//93/zx63fyte3b9/Isiw22WSTfHuuOTLI6sQDK1asiD59+kSjRo3yu9UMX165aq7jXXbZJVq3bh1ZlsWGG24YnTp1ittuuy2mTZuWv640Hth4443FA+uw4ihfCxYsiAMOOCCyLIutttoq/v73v6/y58aPHx8XXHBBXH/99eZArmCr89l733335TdwlH5uR/x71MeIf3+PHzZsWJ0jBlJ/Zs6cGZ07d86Dz+I0csUYt+Yx3MiRI/PP8yuvvHKtLy+fv9Jt/a9//Wv8+Mc/jv79+8fQoUNj8uTJtW66Wp144J133ok333xzrSw//53ly5fHXnvtFS1atCg7Xps4ceJKo4HFixc7ZoOECAeAilJ6EDJ16tR46623YtCgQdG1a9f8hHRpPDB16tQ4//zz83jg61//egwdOjQGDx4cPXv2rDVUlnn1Kt/tt99e66JvcdSI5s2bx29+85taP1P8ovvb3/42H12Cdctjjz0WjRs3jtatW+dD2Zcq3XaLw9k3bNgwsiyLL33pS9GpU6d82NPSOZVZu4onID744IO47bbb8sdL44Fi/JFlWYwZMyYiPpmWpFmzZtGkSZP4xz/+UfZerB+WL18eZ555ZjRs2DBatmwZWZbF3XffXfaa0mOAq666KjbaaKNo2LBhXHbZZXWOMEJleO6552KTTTaJnXfeOV+Hn/V46zvf+U5kWRZHH310zJ8/3/FahSsd5eOoo46qFQ+Urr/bb7+9znig5t/KqaeeGt/85jfjy1/+srvV1hE33XRTvm7322+/6N27dz59XPPmzePUU08tG6J69uzZZfFA8RiAyrSq47DicwsWLMj33926dYuJEyeu8j2XLl3qokMFK13nkyZNijvuuCNOO+20uOiii+Khhx6K+fPn589ffvnl+fY/YsSIsnM0Ef+epmz77bcXdFeY999/Px8l6owzzshHjajr2Kv0b+KnP/1pvs4ffPDBtba8rFl33XVXfl6l+O+LX/xiXHjhhWWjP0asOh6wb69cpdtx8Rh+3rx50bNnz2jbtm0e8z3//PN1RgPLly+PDz/8MK644or8XA2w/hMOABWj9GDm5ptvjq5du0ajRo2iVatWseGGG+YHsTVHHpgzZ07cc889sfXWW5cd7G655Zbxwx/+MN59992IEA2sC+64447Isiwf8rb0zoSBAwfmdzLdfvvtZScuiopzZl511VVrbZn571RXV8e8efPiwAMPrDUdRc1ttvR/jx49Oo4++uho2rRpNG7cOLbddtvo37+/udUqwNy5c6Nr167RqlWrsghkZSMP9OvXL5/X/vHHH48IJx7WV/Pnz48RI0bEF77whXxY1OnTp5e9pq54oFmzZjFy5Mg69/vUv3PPPTeyLIuRI0dGxGebOqK4Xxg7dmy0aNEitt9++/xvwn6gspV+JhfjgQ4dOsQTTzwREeXrr3h8V3M41NLXdO/ePX784x/H/PnzjTawDnjssceiSZMm0a5duxg7dmxEfPL5vmDBgjjzzDOjTZs20ahRozj22GPjX//6V/5zH3zwQZx33nn5RYrf//739fUrsAql38vffPPNeOKJJ+I3v/lN3HXXXfH222+XbbsLFy7Mpy3o2rWr+czXUaXr/J577omOHTtGVVVV2fmVvn37xn333Ze/7tJLL82f69y5cxxyyCFx6KGH5jdwbLbZZoLuCrNw4cLYYYcd8lE5i5/lpSNF1FTc3hctWhRHHnlkZFkWBx54YMybN0/ovY77xz/+ES1btoyqqqo488wz47e//W0cfPDB0a5du2jRokX86Ec/qjVCzD//+c98StFdd9017rzzznpaej6r++67r2ydHnzwwZFlWTz77LPx9ttv1xkNFKcmmTx5cjRs2DDOPPPMell2YO0TDlBRVnbQ6WA0LcU5UTfZZJO46qqrYurUqfHCCy/EueeeGxtttFF+R1rNqn3WrFnx97//PcaOHRt33XVXvPPOO6usp6ksy5Yti1NOOSWyLIsbb7wxf7x03Z122mmRZVm0aNEizj333Ph//+//xfLly2PevHn5UIjbbbfdKqczoPJMnz492rRpE1/5ylfyx1Z2wajmtjx16tR4/fXXY/78+as84cHa8/TTT8dOO+0UTZo0ia5du9YZg9SMBxo3bpwHQ+bKWz8Vt+n58+fHOeecE5tsskm0adMmrrjiivjwww/rfG1ExDXXXBNZlkWnTp2MOlChBgwY8F9fAHzvvffyqamOP/74z3HpWFOqq6vLIpHi38HGG29cZzxQOm3BT37yk7IpSM4+++zIsix+/vOfr71fgNVWup6L67Q4+tMvfvGLWs9FRFx33XWx5ZZbRtOmTeOyyy6LiH9/p58zZ06cccYZsdlmm5UNj0tlKD0Gu/fee2Pbbbctu3jcuXPnOOWUU8oCb/HA+uPee+/N1/WPf/zjuPXWW+Pyyy+Pb3zjG9G4cePYdddd45e//GX++ltuuSX23nvv2GCDDfKf22KLLeKAAw4w9VgFmjFjRgwdOjTatGkTWZbFiSeeuNqjRa1YsSKfWrBNmzZGklgH1fyOfeWVV9Y6/zZnzpy47rrrYptttokmTZrEoEGD6owHit/l99xzT3H3OuCBBx6ILMuiXbt28cADD0TEv6eK7N69e+y00061pp0rPb/2/e9/Pxo0aFBrxEBg/SUcoCJNnDgxxo0bFw8//HBMnTo1FixYkD/nYsL67bXXXsuHTavrBPQdd9yRH9Ace+yxteKBuvibWXcUo5Hhw4dHxL/XXemX2OLIA8V5cHfcccdo0qRJZFkWO+20k2kp1kHjxo2LLMti7733Xq3XF6emoDLUta09+eSTsffee0dVVVV06dJlpfFAcajDLMvyuxXss9dtxfVX13osXnxasGBBnHvuudGqVavYZJNN4tprr11lPHDjjTfmF5f8fVSeH/7wh5FlWdx6660R8dk+f8ePH58PSX/33XdHlmXRu3fvWvOqUllqDmf9//7f/4urr746ttxyy1rTFqwsHth9992jb9++se++++ZzpBtpoHK8+uqrMWDAgPx/F/ff1dXVsXTp0vyO1RdffDEi/r2eS9f3BRdckI8WNnny5LL3nzt3bh6POGavTH/84x/z7fX444+PUaNGxWmnnZZv53vuuWfZRYWa8cCnTVtA5ZkyZUpss802kWVZ3HDDDWXP3XHHHbHxxhtHlmUxatSosudmzJgRzz//fIwdOzbGjBkTr776aq3jOirH1KlTY+TIkflNOaXTPK5OPPCVr3wlsizLLz6y7nn44YfjnnvuiYMOOij23Xff/PFiELZw4cL4/e9/H126dFlpPDBp0qQ47bTT4qWXXlqry87qKT1WX7BgQeyxxx7RsmXLsqlfP/roo9hnn33KRpUpKv18Lwa+Bx54YMyePXvt/AJAvRMOUDEWLlwYt9xySz5UTvFf69ato0+fPmVzJ7H+mjhxYrRu3Tr22muv/LEVK1aUfYG55557YquttsoL6dJ4wLC2657Si0wPP/xwZFkWX/3qV2P58uVldziV/g0URybIsiwOPfTQ+PWvfx0PPvhgfPDBB7VeS+V79tlnI8uy2GGHHeL9999f5fpbtGhRPPTQQ6YkqBDFdTVz5sxac10+8cQTqxUPHH/88fn2fN111629hedzV3qC4oMPPog333wz/vnPf8bbb79d6zXFeKBly5ax6aabxrXXXhtz584te79VTVdC5SjecdSvX7/PvI6uueaa6N27d7zzzjvx0ksvxQEHHJD/vYhEKt/dd98dW2yxRf4Z3qJFi2jXrl0+RHVd8cD9998fO+ywQ7Rs2TKyLIsGDRpEt27dDGddQV5//fXYbLPNIsuyOOyww/LHS7fvr33ta9GsWbN4+umnaz1Xur6/853vlF1orLmPsJ1Xpueeey423XTTqKqqKrsTNeKT+bCbN29eNkpI8TtbaTzQvn371Yr8qX/F7fD222/PRxoo9eKLL8ZXv/rVWnejOveybik9t/KfxAPFeH+//faLLMvi4YcfXrMLzBoxYcKEyLIs9thjj9h1112jf//+EVE+TWjE6sUDbuioDHXti4v79WnTpsW0adOiTZs2+Q1axZ9ZsWJF/OEPf8hjoEMPPbQsCF2xYkWcfvrpkWVZfOELX4jXXntt7fxCQEUQDlAR5syZE3379o2mTZtGs2bNokuXLrHXXntFjx498ruKi19Mi0PPs37685//HFmWxS677BKLFy8u+9JSemKpOKRWlmUxYMCAeOWVV+pjcfkUdR3AruoEw5w5c2KLLbaIbt261fm60r+Hk046KbIsi4022igeeeSR1Xp/KtN7770X22+/fTRo0CCfN7PmieTiup86dWp069atbGhc6kdpNLD55ptHlmXx+OOPl71mdeOB0mkLrr/++rX3S/C5qTk37u67754PW7vxxhvHpZdeGrNmzSr7mdWJB6gcixYtimnTpsXVV18dDz30UD4s6UMPPRStWrWKHXfcMb9I9GkXA1esWBGLFy+OAw88MLIsi8ceeyz/fyNCJLIueOihh/LI+5prronFixfH5MmT44EHHog999xzlSMPTJkyJR599NEYOXJk/OEPfzBcfQVZsmRJfPe7340sy6JZs2b5ieTS55cuXRr7779/HnEXlW73xQtUF110Ua3XUfl+9atflY0CV/Tcc8/F7rvvHlmWxWmnnVb2XHEbX7hwYey1116RZZmh6itEXZ/Jpfvk4vPF4/E//elP+XMTJ06sc97riE/uVnXhsLItXrw4nnvuuRg+fHicc845+ShPEZ9cUPys8cCCBQtixx13jCzL4qmnnlrjy89nszox3vPPPx+HHnpoHoDtvvvuK/35mvHA4MGDTQtaQWqur/fee69s337XXXdFp06d4uyzz44NNtigbGrIoiVLlsRvf/vb6NmzZz4tbL9+/eKggw7Kt/VOnTrFyy+/vHZ+KaBiCAeodzNnzoydd945v8t43Lhx+YnlZcuWxe233x7HHHNMfkFh2LBhtU48s+5Z2QHtiy++GG3bto0tttgiZsyYERHlBzWl/73LLrvkfxfHHXeck44Vpriu3nnnnXjwwQdrzT8/duzYGD58eNx7770xZcqUfLSAL37xi9GsWbOyIc9K13tpCV2ctmCjjTbKLzhTeVa2vZeu1zPPPDOyLIu2bdvGM888U/Z86Qmpo48+OrIsi2uvvdZdavWoeDLp/fffz4c0Lb0rrfRk038SD9S8u43KUdd2Wbot33TTTfl6/Pa3vx3HHHNMfkfyMcccE88991zZ+9WMB66//vqYM2fO2vllWG3vvvtunHrqqfn2vsUWW8S9994bixcvjldffTWfA3t17kQsjY622mqr+J//+R8XHipMcR19/PHHtdZNdXV1LF68OL9wXFfIt2LFijjssMNWOfIAlWnZsmUxbNiwqKqqiu233z6PBw4//PCy1z322GPRvHnz2HjjjeOmm27KHy+u42I48Lvf/S6yLIshQ4astd+BlVudY+cVK1bEQQcdFFmWlU03UHoBuXRfH/HJBeTS9160aJH5zytEcZtcsmRJ/P3vf4/7779/pa8tfh8r7rOfe+65OqOB4mfDj370o3zUCSrPnDlz4rjjjotNN900Pza/9tpr4913381fs7rxQPG/J06cGC1btoyvf/3ra+8XYbWUfkf76KOP4k9/+lPccsstceedd8aTTz5ZFmc///zzcdxxx0WLFi2iQYMGZaP+rSwe2G677SLLsvjJT37ieK4CFNfBggULYuzYsfHDH/4wOnXqFLfeemvMnj07li5dmo8WsMUWW0TDhg3jb3/7W9nPFtf10qVLY8KECTFgwIBo2rRpNGjQIJ92aMCAAWXBEZAO4QD16v33348uXbrkB6ilFwSLJxuKdySNHDkyP9g977zz8te5cLRuePPNN+PRRx+NBQsW5I/Vte6WLl2a38VwxBFH5K8vPTBdvnx5LF++PHr16hW77bZbfkfDRRddtOZ/EVZLcX298cYb0aJFi+jRo0fZELTFYRCL/xo0aBDt2rWLPn365EOj/uY3v4np06fHsmXLyobVq+m0007L44FVnQihfpRu56+//nq8+OKL8dhjj9Vap8uXL8+nqunUqVP+pabUT3/608iyLHr16pWHRax9pRf9OnfunK+z0jsKq6ury9b9fxIP/Pa3v12LvxWro7hvf/311+PUU0/Nh6guuvvuu6Nhw4bRvn37sgtJJ598cr5eDznkkDwOKirGA+3atYuGDRvGzTff7Piugrz55pux/fbbR5Zl8eUvfznOO++8uOuuu8ruOLrrrrvydXzWWWet9L2K23t1dXUccsgh+fGbE5CVo7iO3nvvvfje974Xd911V607Dz/66KPYfPPNo127dvmwtcXXlH6+77vvvpFlWWy66ab5hSgq3/vvvx8dO3aMnj17xujRo/NpJUrnvn333Xfj+OOPjwYNGkSvXr3i9ttvz58r/RsoTlVwyy23RITv7vWpuJ+dN29e3HXXXTF48OAYOHBgXHnllfHuu+/m62bJkiV5GDR+/PiIiHjhhRfqvIC8bNmyWLhwYYwaNSo/tjNiTOUorvO5c+fG4MGD8+P10aNHl72uuO4vueSSyLIsTjnllBg/fnz8z//8T611vnjx4oj45Nhts802i549exoVtALNnDkzunfvHlmWxY477hg33nhjjBs3rs6RvT4tHijdpotTkVx77bURIQisFMV19OGHH8bAgQPzO8VL/33jG98oG0Vm4sSJceyxx0ajRo2iR48ecc899+TP1RUPjBkzJr7yla8Y7bUCFLe72bNnx0EHHRQNGjSI5s2bR5s2bWLkyJH5lAJvvfVWDBs2LDp06JB/D1+4cGFElE8ZW+qll16Kp59+Oh555JH44IMPat0ABqRDOEC9Kb3gcNppp+XRwKouEBa/yGRZFjfccMPaWlT+S2+99VZ+wunggw+Oq666KiL+fYBSPOgpHuw+8cQT0bFjx9hwww1j5MiReTxQ+qVl+fLlsc0228TZZ58d999/f7Ro0aLOYbJZ+0qjgWIEMHjw4LLXPProo3H33XfHJZdcEkceeWT07t07mjdvng9rXfy38cYbx2677Rbf/e534/LLL48xY8bEa6+9VmturWI80LZt2/jjH/+41n5XVt+f/vSn2HbbbaNVq1aRZVn07t07Ro8eHbNnz85f88orr8QBBxwQWZZFw4YNY+DAgXHFFVfENddcE9/+9rfziw//+te/6vE3SVtpNFC883jIkCFx6623RlVVVdlcyBHxmeOBRYsWRb9+/SLLMvPiVpjSfXubNm0iy7K488478+f/9a9/xVe+8pVo3Lhx3HzzzfnjxWGqN9xww9hpp53yYa8nTJhQ9v4LFiyIIUOGxLbbbhvTp09fO78Un2ratGn58fpxxx2XXzAoVdzOL7vssvzz+8c//nHMmzcv37Zrzps6ePDgfLSx0s8B6ldd+/jLLrus1usWLFgQnTp1ik033TQPB2pGvhER06dPz6OTDh06iAfWAcX1ePHFF+cjSowfPz6/oFQ68sC4ceNin332iaqqqthmm21ixIgRMX/+/Fi0aFEsW7YsBg0aFFmWxW677ZaPLEb9KG6Ts2fPjn333TcfSaL478ADDyyLhIYOHRpZlsVDDz0UU6dOrTMaKH4eTJ8+PTbeeOMYMGCAMKSCFLflWbNm5TdabLvttjFq1Kh49tln6/yZGTNmxJZbbhmtWrXKb/AZOHBg/nzpMcARRxwRWZbFlVdeab1XmDlz5uTH3EcffXSdx241rSoeKCqOSLHffvsZBbaCFLf1mTNn5qOybrHFFvH1r389vve978W3vvWt/PxKlmVxwAEHxJtvvhkRn1wkPuqoo6Jhw4ax2267xZ///Of8fWtu14sWLYqPPvporf1e1K10314cBWKPPfaIcePG1XlzzVtvvRU/+clPol27dtG2bdv4xS9+kY8mVrqORUBATcIB6sWsWbPyC4qDBg3KH19ZnV7XcNbt27c3p9Y6oLq6Or8IVFVVFVVVVZFlWXzrW9+Kyy+/vNb8WNXV1TFnzpy44IILolWrVtG2bds4/fTTY968eWWvKw65NGbMmIiIOOuss8rudnXQUz9KLywVh8Q7++yz8+dXto0vX7483njjjXjllVfi0EMPzb/sFAOSmrV0z549Y/HixWWhUfFvomPHjmUjW1D//vznP+frbtddd43NN988348PGTIkHy5xxYoVMWPGjBgwYECtdd6kSZPYbbfdYsqUKfX826SrrukJBg0aFCtWrIhnnnkmPyG5ePHism39P4kHSofQpP7VtW8fOnRo2Wuuu+66yLIsfvazn+WPXXLJJVFVVRUbbrhhTJkyJZ555pn85/v161crHli4cGF+Qsodi/Vvzpw5+R3jp59+ev74ytZN8fitdHSJ3/zmN7FgwYJYsWJFzJs3LyZPnpzPn77VVlvlQ1k7bqt/K9vH14w+qqurY+HChfnJylGjRpU9V/rfS5YsycO/4knrukYUovI89dRT0bRp0+jWrVtMnTo1/vKXv+Shdmkk+Pjjj8ehhx6ax79dunSJL33pS/nfUOfOnW3n9ax02y5OK7PrrrvGoEGD4rTTTssvJn3ta1+LBx98MCIiRo8eHVmWRatWrfILkMXv2RFRdgfi4YcfHlmWxe9+97u1+4uxUsV98ezZs/N99aGHHlrrnEqpFStWxLJly+LCCy/Mb/r4xje+kT9fOm3Nueeem1+sMgpcZVm8eHEcddRRkWVZHHnkkfl6W53j6prxwDHHHJM/N2LEiHyf/vrrr6+x5eezKW7rc+bMiR49euTfsT788MOy1913330xaNCg/LN6r732yqeimThx4mrHA9Sv4vqYO3duPiLMiSeeWOcNmKXr7u23346hQ4dGixYtomvXrjF69Og64wGAUsIB1rrq6ur45S9/mZ9AOuKII/LnVnUwW/wwe/3112P33XePpk2b5vMw+aCrbM8++2y0adMmGjduHCeccEJ+0TDLsth6663j2muvrTVs8VtvvRXnnHNObLzxxpFlWey0005x4YUXxpVXXpnfkfzlL385v7j0yCOPRJZlsfvuu9fHr0jUfWGpdLji4vZdetKweIBbug0/9thjUVVVFQMGDIh58+bFG2+8Ebfddltcc801cfjhh8f+++8fr776aq33jfgkLCqdi5P6UTrs2Ycffhi77rprtG7dOq6//vqI+GT7vuCCC2LrrbeOxo0bxymnnFLrQvF9990XV1xxRZxyyikxdOjQeOCBB2qFRqw9K7ugVPzC+dJLL0XTpk2jdevWdd6B8lnjASrH6u7bb7vttujZs2c+/OGtt94abdu2jRYtWuRDHUdEXHvttfkxwGGHHVbnXW+O6+pX8f//77777mjcuHHZhYNP20aXLFkS119/fT43ZjEo+trXvhbbb799tG7dOh91Ztq0aav1nqx5nxYNlK6j4j7hhhtuyE8yl474VTpfakTE2WefHb169coDgsmTJ6+V34lPV3P0t5qKYfZtt90WERH33ntvHvQeeuih+eteeeWVGD16dHTp0iXatWsXWZbF9ttvH/369Yt33nknImzn9aWuUUROPPHEsvVx//33x1ZbbVXr3ExxCrGaI02UxkTnnHNOZFkW++yzT8ycOXMt/Easrvnz5+f73QEDBqz2BeRXX301+vfvH82bN49u3brFyJEj4/333485c+bEjBkz4rjjjossy2KzzTYzClwFeuGFF2LzzTePHXbYIR9p4LPsf2vGAwMGDMinjW3Tpo1h6ivQxx9/nI/AWRqLLF26tOzzffbs2XHzzTfnEeA3v/nNfOqK559/Xjywjli2bFmcffbZkWVZfPe7381Dvk/bzqdOnRpDhw6N5s2bR9euXeOmm24SDwCrJBygXrz11lsxatSo/OTh6sYDRcWDom9961urnNqA+lddXR0fffRR9O3bN7Isi1//+tfx0UcfxdVXXx1f/epXI8uyaNy4cbRr1y5GjhwZL7zwQn4yYsaMGXHLLbfklXzpv+7du+d3r0R8MvR9lmVx0EEH1devmrS6LiwNGzYsf75mNPDGG2+s9L2ef/75qKqqih133LHWyAErVqzI36N023cysjLU/MIxc+bMmDFjRrRs2TIuvPDCsufmzZsXY8eOjW233TaPB9yxUplKTzoXhy2teRfqxx9/HF/60peiRYsWKx0VYmXxwHbbbRf/+7//u0Z/B/4zq7Nvr66uzl/37rvvxvLly2PZsmVx+OGHR9OmTeOOO+6IiH/fqTZ79uzYfvvto3HjxtG4cePYa6+94sUXX1zLvxmro3jH2v333x8Rq55OrKa//vWvcdJJJ+XTHBT/7b333nHJJZfk0xP4/K5/dV1YrCsaqLn+X3zxxXz465ojiJTejbzrrrvGd7/73YgIn/MVZNq0afHzn/+8LMaN+GS/X/y8HjduXGy00UbxxS9+MY8CH3jggTweqDk90axZs2Ly5Mnx2GOPxezZs/OQzHZeP4rrcebMmdG1a9d89Ji6ppC5++678/10cUqR119/PfbYY488AHvhhRdi7ty5sWLFili0aFEMHDgwH+2t5t8R9e/OO++MJk2aRK9evWpFA592kWjSpElxyimn5CFQ+/btY7PNNsunnNtuu+1cQK5Q559/fmRZFhdffHFErP6xW+nfRM14IMuyaN26dbz88strZJn570ybNi2222676NatW8yfPz8iVv25e/fdd+fxQN++ffPHX3zxxTwe6N27d9mUdFSOuXPnxi677BKdOnXKb6xZ3eMs8QDwWQgHWGvmzZtXdqA5bdq0uOiii/IvH0ceeWT+3KdNWfDggw9GVVVV7L777mUnpqhcd955Z2RZFs2aNcsvEFRXV8fPf/7z6NOnT/6FpFu3btG3b9947bXX8pNNH330Ufzyl7+MYcOGxemnnx7XXXddrTtai9MhFL8gOehZ+9544418CpK6pico/t/ikOalwVCpBQsWRJcu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fCc+/vjjz7SNz5o1K+67776I+CQgO+WUU2LzzTevdUwAECEcYC0qDlv7n8YDpXOk77zzztGpU6d46aWXIsKXl3XFsmXLolevXpFlWZx11lllJXvxYLdx48Zxyy23xKOPPprf4VqcV690uOOHH344GjZsGFmWxa677rrSObVZu55++umyC8nFC0zPPfdcHg0Uh0uMWPkX2eI8myNHjlwry81/rua+/dlnn82fmzhxYpx44omxwQYbxBe+8IWyYfDqigf+8Ic/RIcOHWLjjTc2D3IFq3kCqbgur7766siyLA444IBV/sy5554bw4YNi/fff3/NLiifm8+6b6+uro6f/vSn+QnpYcOGxXXXXRcHH3xwPnpBcY57Kk91dXUsWbIkvv/979e6m3h1jrk/+OCD2HTTTaNjx47x7rvvrslF5XPy9NNP55/l/fv3j+eeey4/RnvllVfyaKB0tKjly5fXij+nTJkSd911V/zyl7+McePGiQAr2FNPPZWv86uuuirGjx8fY8eOzb+rbbTRRtGnT5944okn4q9//WtUVVXFcccdFxH/Ht4+IuIvf/lL/vlgv155Sr9rDR06NI8HhgwZkt9BfvXVV0eDBg2iZcuWZedoila233cOpjIV18vzzz8fO+64Y2RZFltvvXWceeaZceCBB+bn3L785S/HOeeck0cFr732WowaNSpat24dnTp1KvtOx7rjF7/4RWRZFhtvvHH861//iohP31aLo1EccMABkWXZSqeuoTI99NBD0aRJk9hll13yc6yruphcfG78+PHRvHnz6NixY1ksQmV75JFH8vVdnGJgdeOB+++/P7bccst8ZN/p06c7JwOslHCAtarmiefVjQdK59spDrU3cOBA8y2tQ4oXjcaMGRMbbLBB9O7dO7/L9OKLL85PYvzhD38o+7k///nPMXz48DqHxrv++utj1KhRTkpXmNLt/KSTToqbb745v7B0ySWX5K8rPbgtvai4dOnSeOCBB6JZs2aGv1xH1Ny3l55oevHFF2PAgAHRqFGj2HnnneOPf/xj/lzNkxgLFy6Me+65R/G8jnryySdjgw02iD333HOl2/cFF1wQWZZF8+bNVzqMOZVpdfftxTuUIz65261x48Zlw+B269Yt/0x3N3pl++tf/xrNmzePRo0axXXXXZc/vrIT0MVt/fnnn4+WLVvGIYccslaWk89H6Tbev3//mD59ekyZMmWl0UBR8a5UFxHXPaXrfPjw4bFgwYJYtmxZ3HDDDXk4lGVZ7LffftGkSZPIsiz+/ve/13qfxx9/3H69gq0sHhg2bFicc8450aRJk2jYsGE8+eSTtV7PumvBggVx9dVXx5e//OWy47Asy+Lb3/52PPfcc/n5tOL+e9q0afmUFLfeemt9Lj7/oY8//jifruDoo4/+1Bi/+Hk+e/bs6Ny5c/Tq1WttLCafo2nTpsWmm25aa9qBTzsumzRpUrRs2TK22WYb4d86ZPr06bHZZpvlN+QVrWp9F7fzn/3sZ5FlWa3pgwHqIhxgrfus8UDpEGkjRoyILMuiR48e+ckJ1i1TpkzJ59W88cYb48orr8xHGrj77rvz15VeeKhr1Imaz1FZSrfzxo0bR4MGDcqmm6hrHVZXV8dFF10UI0aMiDlz5uTzYhsGc92wqnhg0qRJcdxxx0WjRo1il112WWU8wLqr+DfQvn37eOONNyKifB89cuTI/PlJkybV12LyX1jdfXvpev/d734XQ4YMicMOOywuuOCC/A5kn9+Vb+HChXH00UdHgwYNYtddd40///nP+XOrmopkv/32iyzL8vkyXYRad5Ru4wcddFC0bt06siyL8847L39N6bou/e8nn3wyP3Zj3VG6zocOHRoLFy7Mn7vzzjvj0EMPzf8OWrduHb/5zW9W+l7265WrrnigYcOG0ahRo2jUqFEehPjetX6ZN29ePPnkk3HkkUfGXnvtFQMHDoybbrqp1uuKd5xHROy///6RZVmdr6OyVVdXx/Lly+Pqq6+Otm3bRrt27WLkyJExa9as/PlSpfvso48+OrIsiwsuuKDWiEJUvquvvjqaNm0anTt3jrFjx+aP17Uei+u9OGLQgQceuNaWk89HcX1vs802cfvtt+ePr2p9V1dXxy677BKdOnWKt99+e60tK7DuEg5QLz5LPHDMMcdExL+Hsu/QoYNh6ddxN954Y2RZFi1btszveCiNBnxJWT88/fTT+d1JO++8c7z88su1XlN6EFucj2+XXXaJjz76KH+cdceq4oGXXnpJPLCe+/DDD2ObbbaJ9u3b1xo1ohgNtG7dus59AeuO1dm3R6z6ApKLS+uON954I3r06BFZlsWee+5ZdnKqeGK5eLFhxYoVcfrpp+fzZM+dO7e+Fpv/Qum0BVmWxQknnJA/V1fYGxExfPjw6NixY1x66aU+09dBpcdvw4YNKxsRaO7cuTFp0qQ48sgj3aG2jiuNB84444zIsiyqqqri8MMPjwULFtTjkrE21FzHdUVgixYtiu222y623HLLePXVV9fq8vH5mTlzZhxzzDGRZVlsttlmMWzYsFojeJZ+Vp9zzjn5DVrvvPNOvSwz/5333nsv9t577/x4vTT2rWuUqIjIRxb61a9+FRHOyaxL/pP1PWjQoMiyLAYMGOAzH1gtwgHqzWeJB4rDpbngsH54+eWX8yHzNthgg3j44Yfz5xysrl+eeuqpaNiwYR4BFefFjvj3yefSaGCLLbbIpyfwt7Bu+izxwD333FOPS8rnrbq6OnbaaafIsqzsy6toYP2zqn0765+XX345unbtGlmWRZcuXeKnP/1pLF26NP8c//jjj2Pu3LnRr1+/fC7l4olnow2sm5566qlo2rRpZFkWRx11VEyePLnsuKz0pOT5558fWZZFs2bN8vmUWfeUHr+dddZZeTxQXO/FeZMjbNfrstJ1N2TIkHwEoR//+McuFK+nPu07den+/IQTTogsy+Lwww83Leg6bvr06fGDH/wgmjRpEi1atIg99tgj/vGPf8ScOXMi4pPRKN5555044ogj8hu0Jk+eXM9LzX9jypQp0a1bt8iyLHr16lU2zVhNP/3pT/Obdkz9um6qub6vv/76lb72rLPOiizLonPnzqaDBVabcIB6tTrxQPv27fOhjV1wWH8U70jr2rVrXjs6CbV+qrmdP//88/kJjOXLl5dFA8US3jCZ67bViQc22GCD6NKlS9x33331uKR8XoonHffZZ5/IsixGjx4dEaKB9Vld+3bWX1OmTIlvfOMb+cXkXr16xcEHHxznnntu9OnTJ7p06RJZlsVOO+0U06ZNiwgjS6zrnnrqqXwb79+/f53beHEf37ZtW/v49UDNeKCuOY+Fveu+0u/cxe9hjRo1ijPOOKPWiFGko3ghceutt44333yzvheHz8G7774bp59+emyzzTZ54Ne9e/c46KCDokePHvk86d27dxcNrCdefvnl6NGjR1RVVUWjRo2iX79+8cQTT8TUqVNjxowZMXHixOjbt29kWRabbLKJ0XzXcaXru0mTJnHEEUfEk08+GW+//Xa8/fbb8eijj8aBBx6Yjz7yyiuv1PciA+sQ4QD17tPigbPPPjs6deoUL730Uj0uJZ+X4smmadOmxQ477BAtWrSIW2+9NSKcYF6flW7n/fv3z7+g/OQnP8mjgeI8W/4O1g+rigdefvnlOPTQQ6N9+/bxxhtv1ONS8nkrDnU5atSouOiii0QD67lVxQMuLq1/ZsyYEVdeeWV06NAhH3Gi+K979+4xePDg/C5ln+Xrh5rbeOnoIuedd559/HpodeIB1n2l8cDQoUPL4oHXX3+9HpeMtWnhwoXx7rvvxiGHHOLC0npq7ty58dhjj8Vhhx0W7dq1y6coybIsdttttxgxYkRMnz69vheTz9Hrr78eRx55ZDRv3jyyLIvmzZtHixYtok2bNvnxe8+ePcUi64ma67tZs2bRrFmzaNGiRb6977HHHkYVAj6zLCKiAPVswoQJhV133bVQKBQK/fv3LwwaNKjQo0ePQqFQKLzzzjuFpk2bFtq2bVufi8jnbNGiRYVTTz21MHr06MI+++xTeOCBB+p7kVjDam7nVVVVhdGjRxc233zzwt/+9rfClltuWVixYkWhQYMG9bykfF5qrvPTTjutsNNOOxUKhUJh8uTJhZYtWxY23XTT+lxEPmdXXHFFYfDgwYU2bdoU5syZU2jVqlVh3Lhxhe22266+F401pOZ2fvrppxe6d+9ez0vFmjR9+vTCpEmTChMnTiy0bdu20LRp08J+++1X2GijjQqNGzf2Wb6eKd3GjznmmMKgQYMK99xzT2H48OH28eup0nU+bNiwwuDBg30XXw9VV1cXqqqqCoVCoXDmmWcWfvaznxU22GCDwpFHHlk444wzCltttVX9LiBrTEQUJk6cWDjrrLMKkydPLrz11luF3r17F2688cbCNttsU9+Lxxry8ssvF2bPnl1YtmxZoaqqqvA///M/hYYNGzpmWw8tWrSoMGHChMLPf/7zwsyZMwuvvPJKYcMNNyz07NmzsO+++xa++93vOg+zHimu78svv7wwa9aswuTJkwvt2rUr7LTTToWDDjqo8PWvf72w8cYb1/diAusY4QAVo+ZJqRNOOKGw88471/NSsSZNnjy5sMceexRmzZpVuPnmmwt9+/at70ViDZswYUKhV69ehULhkxMWW2yxRWHcuHGigfVYzX378ccfX9hll13qean4vEVEIcuywuOPP1749re/XViyZEmhdevWhSeffLKw/fbb1/fisYYV9+0RUTjooIMK559/vvWeqOK+gPVL6Wd5z549C88884xoYD1Xus4HDhxYGDFiRKF169b1vFR83krjgbPOOqswatSoQvv27QuTJk1ykWE9tmzZssLNN99cOOOMMwodOnQo9O3bt3DMMce4kLieWtWxmeO29dvixYsLzZo1K7z77ruFxo0bF9q1a1ffi8QatGTJkkLTpk0L77//fqFp06aFli1b1vciAesw4QAVZcKECYXevXsXli5dWjjppJMKl19+eaFJkyb1vVisQYceemjhH//4R2HChAmFDh061PfisBYUT0Ruvvnmhb///e+Fjh07igbWc/bt6Zg2bVqhU6dOhULhk7tavvjFL9bzErG2PPPMM4Vddtml0L59+8I///nPQps2bep7kYDP0YQJEwp77rlnYfHixYU2bdoUnnzySdHAeu7ZZ58t7LzzzoV27doVXn31VSeg11Ol8cCIESMKhxxyiPgvAfPmzSu8+OKLhc6dOxfatWtXaNSoUX0vEvA5K4Yh1dXVhUKhUKiqqhKLrMdK13eWZYUsy6xv4D8mHKDi/OMf/ygccMAB7lJMxJtvvllo1qxZYZNNNnHxOCEvvPBCoV27doUtttjCek+EfXs6Jk+eXKiqqip07dq1vheFtWzixImFNm3aFDp27Fh2IQJYP/ztb38rfP/73y88+uijooFElO7XnXxef/nMBgAAioQDVKTi8Dqkw8mKNIkG0mLfDmmwb4f1V3HYW9KyfPnyQsOGDet7MQAAAFjDhAMAAAAAAAAAkDC39wIAAAAAAABAwoQD/2fmzJmFe++9tzB8+PDCfvvtV2jXrl0hy7JClmWFo446qr4XDwAAAAAAAADWCJPU/Z8OHTrU9yIAAAAAAAAAwFpnxIE6dOzYsfCtb32rvhcDAAAAAAAAANY4Iw78n+HDhxd23nnnws4771zo0KFD4a233ip84QtfqO/FAgAAAAAAAIA1Sjjwf84777z6XgQAAAAAAAAAWOtMVQAAAAAAAAAACRMOAAAAAAAAAEDChAMAAAAAAAAAkDDhAAAAAAAAAAAkTDgAAAAAAAAAAAlrWN8LkIo999yzvheBtaRp06aFBx98sFAoFAr77rtvYcmSJfW8RKxp1nlarO/0WOfpsc7TY52nxfpOj3WeHus8PdZ5eqzztFjf6bHO0/X444/X9yJQIX79618Xxo4dW/jBD35QOOmkk+p7cZJhxAEAAAAAAAAASJhwAAAAAAAAAAASJhwAAAAAAAAAgIQJBwAAAAAAAAAgYcIBAAAAAAAAAEiYcAAAAAAAAAAAEiYcAAAAAAAAAICENazvBagU48aNK7z22mv5/549e3b+36+99lph9OjRZa8/6qij1tKSAQAAAAAAAMCaIxz4PzfccENhzJgxdT73t7/9rfC3v/2t7DHhAAAAAAAAAADrA1MVAAAAAAAAAEDChAP/Z/To0YWIWO1/AAAAAAAAALA+EA4AAAAAAAAAQMKEAwAAAAAAAACQMOEAAAAAAAAAACRMOAAAAAAAAAAACRMOAAAAAAAAAEDChAMAAAAAAAAAkDDhAAAAAAAAAAAkTDgAAAAAAAAAAAkTDgAAAAAAAABAwoQDAAAAAAAAAJAw4QAAAAAAAAAAJEw4AAAAAAAAAAAJEw4AAAAAAAAAQMKEAwAAAAAAAACQMOEAAAAAAAAAACRMOAAAAAAAAAAACRMOAAAAAAAAAEDChAMAAAAAAAAAkDDhAAAAAAAAAAAkTDgAAAAAAAAAAAkTDgAAAAAAAABAwoQDAAAAAAAAAJAw4QAAAAAAAAAAJEw4AAAAAAAAAAAJEw4AAAAAAAAAQMKEAwAAAAAAAACQMOEAAAAAAAAAACRMOAAAAAAAAAAACRMOAAAAAAAAAEDChAMAAAAAAAAAkDDhAAAAAAAAAAAkTDgAAAAAAAAAAAkTDgAAAAAAAABAwoQDAAAAAAAAAJAw4QAAAAAAAAAAJEw4AAAAAAAAAAAJEw4AAAAAAAAAQMKEAwAAAAAAAACQMOEAAAAAAAAAACRMOAAAAAAAAAAACRMOAAAAAAAAAEDChAMAAAAAAAAAkDDhAAAAAAAAAAAkTDgAAAAAAAAAAAkTDgAAAAAAAABAwoQDAAAAAAAAAJAw4QAAAAAAAAAAJEw4AAAAAAAAAAAJEw4AAAAAAAAAQMKEAwAAAAAAAACQMOEAAAAAAAAAACRMOAAAAAAAAAAACRMOAAAAAAAAAEDChAMAAAAAAAAAkDDhAAAAAAAAAAAkTDgAAAAAAAAAAAkTDgAAAAAAAABAwoQDAAAAAAAAAJAw4QAAAAAAAAAAJEw4AAAAAAAAAAAJEw4AAAAAAAAAQMKEAwAAAAAAAACQMOEAAAAAAAAAACRMOAAAAAAAAAAACRMOAAAAAAAAAEDChAMAAAAAAAAAkDDhAAAAAAAAAAAkTDgAAAAAAAAAAAkTDgAAAAAAAABAwoQDAAAAAAAAAJAw4QAAAAAAAAAAJEw4AAAAAAAAAAAJEw4AAAAAAAAAQMKEAwAAAAAAAACQMOEAAAAAAAAAACRMOAAAAAAAAAAACRMOAAAAAAAAAEDChAMAAAAAAAAAkDDhAAAAAAAAAAAkTDgAAAAAAAAAAAkTDgAAAAAAAABAwoQDAAAAAAAAAJAw4QAAAAAAAAAAJEw4AAAAAAAAAAAJEw4AAAAAAAAAQMKEAwAAAAAAAACQMOEAAAAAAAAAACRMOAAAAAAAAAAACRMOAAAAAAAAAEDChAMAAAAAAAAAkDDhAAAAAAAAAAAkTDgAAAAAAAAAAAkTDgAAAAAAAABAwoQDAAAAAAAAAJAw4QAAAAAAAAAAJEw4AAAAAAAAAAAJEw4AAAAAAAAAQMKEAwAAAAAAAACQMOEAAAAAAAAAACRMOAAAAAAAAAAACRMOAAAAAAAAAEDChAMAAAAAAAAAkDDhAAAAAAAAAAAkTDgAAAAAAAAAAAkTDgAAAAAAAABAwoQDAAAAAAAAAJAw4QAAAAAAAAAAJEw4AAAAAAAAAAAJEw4AAAAAAAAAQMKEAwAAAAAAAACQMOEAAAAAAAAAACRMOAAAAAAAAAAACRMOAAAAAAAAAEDChAMAAAAAAAAAkDDhAAAAAAAAAAAkTDgAAAAAAAAAAAkTDgAAAAAAAABAwoQDAAAAAAAAAJAw4QAAAAAAAAAAJEw4AAAAAAAAAAAJEw4AAAAAAAAAQMKEAwAAAAAAAACQMOEAAAAAAAAAACRMOAAAAAAAAAAACRMOAAAAAAAAAEDChAMAAAAAAAAAkDDhAAAAAAAAAAAkTDgAAAAAAAAAAAkTDgAAAAAAAABAwoQDAAAAAAAAAJAw4QAAAAAAAAAAJEw4AAAAAAAAAAAJEw4AAAAAAAAAQMKEAwAAAAAAAACQMOEAAAAAAAAAACRMOAAAAAAAAAAACRMOAAAAAAAAAEDChAMAAAAAAAAAkDDhAAAAAAAAAAAkTDgAAAAAAAAAAAkTDgAAAAAAAABAwoQDAAAAAAAAAJAw4QAAAAAAAAAAJEw4AAAAAAAAAAAJEw4AAAAAAAAAQMKEAwAAAAAAAACQMOEAAAAAAAAAACRMOAAAAAAAAAAACRMOAAAAAAAAAEDChAMAAAAAAAAAkDDhAAAAAAAAAAAkTDgAAAAAAAAAAAkTDgAAAAAAAABAwoQDAAAAAAAAAJAw4QAAAAAAAAAAJEw4AAAAAAAAAAAJEw4AAAAAAAAAQMKEAwAAAAAAAACQMOEAAAAAAAAAACRMOAAAAAAAAAAACRMOAAAAAAAAAEDChAMAAAAAAAAAkDDhAAAAAAAAAAAkTDgAAAAAAAAAAAkTDgAAAAAAAABAwoQDAAAAAAAAAJAw4QAAAAAAAAAAJEw4AAAAAAAAAAAJEw4AAAAAAAAAQMKEAwAAAAAAAACQMOEAAAAAAAAAACRMOAAAAAAAAAAACRMOAAAAAAAAAEDChAMAAAAAAAAAkDDhAAAAAAAAAAAkTDgAAAAAAAAAAAkTDgAAAAAAAABAwoQDAAAAAAAAAJAw4QAAAAAAAAAAJEw4AAAAAAAAAAAJEw4AAAAAAAAAQMKEAwAAAAAAAACQMOEAAAAAAAAAACRMOAAAAAAAAAAACRMOAAAAAAAAAEDChAMAAAAAAAAAkDDhAAAAAAAAAAAkTDgAAAAAAAAAAAkTDgAAAAAAAABAwoQDAAAAAAAAAJAw4QAAAAAAAAAAJEw4AAAAAAAAAAAJEw4AAAAAAAAAQMKEAwAAAAAAAACQMOEAAAAAAAAAACRMOAAAAAAAAAAACRMOAAAAAAAAAEDChAMAAAAAAAAAkDDhAAAAAAAAAAAkTDgAAAAAAAAAAAkTDgAAAAAAAABAwoQDAAAAAAAAAJAw4QAAAAAAAAAAJEw4AAAAAAAAAAAJEw4AAAAAAAAAQMKEAwAAAAAAAACQMOEAAAAAAAAAACRMOAAAAAAAAAAACRMOAAAAAAAAAEDChAMAAAAAAAAAkDDhAAAAAAAAAAAkTDgAAAAAAAAAAAkTDgAAAAAAAABAwoQDAAAAAAAAAJAw4QAAAAAAAAAAJEw4AAAAAAAAAAAJEw4AAAAAAAAAQMKEAwAAAAAAAACQMOEAAAAAAAAAACRMOAAAAAAAAAAACRMOAAAAAAAAAEDChAMAAAAAAAAAkDDhAAAAAAAAAAAkTDgAAAAAAAAAAAkTDgAAAAAAAABAwoQDAAAAAAAAAJAw4QAAAAAAAAAAJEw4AAAAAAAAAAAJEw4AAAAAAAAAQMKEAwAAAAAAAACQMOEAAAAAAAAAACRMOAAAAAAAAAAACRMOAAAAAAAAAEDChAMAAAAAAAAAkDDhAAAAAAAAAAAkTDgAAAAAAAAAAAkTDgAAAAAAAABAwoQDAAAAAAAAAJAw4QAAAAAAAAAAJEw4AAAAAAAAAAAJEw4AAAAAAAAAQMKEAwAAAAAAAACQMOEAAAAAAAAAACRMOAAAAAAAAAAACRMOAAAAAAAAAEDChAMAAAAAAAAAkDDhAAAAAAAAAAAkTDgAAAAAAAAAAAkTDgAAAAAAAABAwoQDAAAAAAAAAJAw4QAAAAAAAAAAJEw4AAAAAAAAAAAJEw4AAAAAAAAAQMKEAwAAAAAAAACQMOEAAAAAAAAAACRMOAAAAAAAAAAACRMOAAAAAAAAAEDChAMAAAAAAAAAkDDhAAAAAAAAAAAkTDgAAAAAAAAAAAkTDgAAAAAAAABAwoQDAAAAAAAAAJAw4QAAAAAAAAAAJEw4AAAAAAAAAAAJEw4AAAAAAAAAQMKEAwAAAAAAAACQMOEAAAAAAAAAACRMOAAAAAAAAAAACRMOAAAAAAAAAEDChAMAAAAAAAAAkDDhAAAAAAAAAAAkTDgAAAAAAAAAAAkTDgAAAAAAAABAwoQDAAAAAAAAAJAw4QAAAAAAAAAAJEw4AAAAAAAAAAAJEw4AAAAAAAAAQMKEAwAAAAAAAACQMOEAAAAAAAAAACRMOAAAAAAAAAAACRMOAAAAAAAAAEDChAMAAAAAAAAAkDDhAAAAAAAAAAAkTDgAAAAAAAAAAAkTDgAAAAAAAABAwoQDAAAAAAAAAJAw4QAAAAAAAAAAJEw4AAAAAAAAAAAJEw4AAAAAAAAAQMKEAwAAAAAAAACQMOEAAAAAAAAAACRMOAAAAAAAAAAACRMOAAAAAAAAAEDChAMAAAAAAAAAkDDhAAAAAAAAAAAkTDgAAAAAAAAAAAkTDgAAAAAAAABAwoQDAAAAAAAAAJAw4QAAAAAAAAAAJEw4AAAAAAAAAAAJEw4AAAAAAAAAQMKEAwAAAAAAAACQMOEAAAAAAAAAACRMOAAAAAAAAAAACRMOAAAAAAAAAEDChAMAAAAAAAAAkDDhAAAAAAAAAAAkTDgAAAAAAAAAAAkTDgAAAAAAAABAwoQDAAAAAAAAAJAw4QAAAAAAAAAAJEw4AAAAAAAAAAAJEw4AAAAAAAAAQMKEAwAAAAAAAACQMOEAAAAAAAAAACRMOAAAAAAAAAAACRMOAAAAAAAAAEDChAMAAAAAAAAAkDDhAAAAAAAAAAAkTDgAAAAAAAAAAAkTDgAAAAAAAABAwoQDAAAAAAAAAJAw4QAAAAAAAAAAJEw4AAAAAAAAAAAJEw4AAAAAAAAAQMKEAwAAAAAAAACQMOEAAAAAAAAAACRMOAAAAAAAAAAACRMOAAAAAAAAAEDChAMAAAAAAAAAkDDhAAAAAAAAAAAkTDgAAAAAAAAAAAkTDgAAAAAAAABAwoQDAAAAAAAAAJAw4QAAAAAAAAAAJEw4AAAAAAAAAAAJEw4AAAAAAAAAQMKEAwAAAAAAAACQMOEAAAAAAAAAACRMOAAAAAAAAAAACRMOAAAAAAAAAEDChAMAAAAAAAAAkDDhAAAAAAAAAAAkTDgAAAAAAAAAAAkTDgAAAAAAAABAwoQDAAAAAAAAAJAw4QAAAAAAAAAAJEw4AAAAAAAAAAAJEw4AAAAAAAAAQMKEAwAAAAAAAACQMOEAAAAAAAAAACRMOAAAAAAAAAAACRMOAAAAAAAAAEDChAMAAAAAAAAAkDDhAAAAAAAAAAAkTDgAAAAAAAAAAAkTDgAAAAAAAABAwoQDAAAAAAAAAJAw4QAAAAAAAAAAJEw4AAAAAAAAAAAJEw4AAAAAAAAAQMKEAwAAAAAAAACQMOEAAAAAAAAAACRMOAAAAAAAAAAACRMOAAAAAAAAAEDChAMAAAAAAAAAkDDhAAAAAAAAAAAkTDgAAAAAAAAAAAkTDgAAAAAAAABAwoQDAAAAAAAAAJAw4QAAAAAAAAAAJEw4AAAAAAAAAAAJEw4AAAAAAAAAQMKEAwAAAAAAAACQMOEAAAAAAAAAACRMOAAAAAAAAAAACRMOAAAAAAAAAEDChAMAAAAAAAAAkDDhAAAAAAAAAAAkTDgAAAAAAAAAAAkTDgAAAAAAAABAwoQDAAAAAAAAAJAw4QAAAAAAAAAAJEw4AAAAAAAAAAAJEw4AAAAAAAAAQMKEAwAAAAAAAACQMOEAAAAAAAAAACRMOAAAAAAAAAAACRMOAAAAAAAAAEDChAMAAAAAAAAAkDDhAAAAAAAAAAAkTDgAAAAAAAAAAAkTDgAAAAAAAABAwoQDAAAAAAAAAJAw4QAAAAAAAAAAJEw4AAAAAAAAAAAJEw4AAAAAAAAAQMKEAwAAAAAAAACQMOEAAAAAAAAAACRMOAAAAAAAAAAACRMOAAAAAAAAAEDChAMAAAAAAAAAkDDhAAAAAAAAAAAkTDgAAAAAAAAAAAkTDgAAAAAAAABAwoQDAAAAAAAAAJAw4QAAAAAAAAAAJEw4AAAAAAAAAAAJEw4AAAAAAAAAQMKEAwAAAAAAAACQMOEAAAAAAAAAACRMOAAAAAAAAAAACRMOAAAAAAAAAEDChAMAAAAAAAAAkDDhAAAAAAAAAAAkTDgAAAAAAAAAAAkTDgAAAAAAAABAwoQDAAAAAAAAAJAw4QAAAAAAAAAAJEw4AAAAAAAAAAAJEw4AAAAAAAAAQMKEAwAAAAAAAACQMOEAAAAAAAAAACRMOAAAAAAAAAAACRMOAAAAAAAAAEDChAMAAAAAAAAAkDDhAAAAAAAAAAAkTDgAAAAAAAAAAAkTDgAAAAAAAABAwoQDAAAAAAAAAJAw4QAAAAAAAAAAJEw4AAAAAAAAAAAJEw4AAAAAAAAAQMKEAwAAAAAAAACQMOEAAAAAAAAAACRMOAAAAAAAAAAACRMOAAAAAAAAAEDChAMAAAAAAAAAkDDhAAAAAAAAAAAkTDgAAAAAAAAAAAkTDgAAAAAAAABAwoQDAAAAAAAAAJAw4QAAAAAAAAAAJEw4AAAAAAAAAAAJEw4AAAAAAAAAQMKEAwAAAAAAAACQMOEAAAAAAAAAACRMOAAAAAAAAAAACRMOAAAAAAAAAEDChAMAAAAAAAAAkDDhAAAAAAAAAAAkTDgAAAAAAAAAAAkTDgAAAAAAAABAwoQDAAAAAAAAAJAw4QAAAAAAAAAAJEw4AAAAAAAAAAAJEw4AAAAAAAAAQMKEAwAAAAAAAACQMOEAAAAAAAAAACRMOAAAAAAAAAAACRMOAAAAAAAAAEDChAMAAAAAAAAAkDDhAAAAAAAAAAAkTDgAAAAAAAAAAAkTDgAAAAAAAABAwoQDAAAAAAAAAJAw4QAAAAAAAAAAJEw4AAAAAAAAAAAJEw4AAAAAAAAAQMKEAwAAAAAAAACQMOEAAAAAAAAAACRMOAAAAAAAAAAACRMOAAAAAAAAAEDChAMAAAAAAAAAkDDhAAAAAAAAAAAkTDgAAAAAAAAAAAkTDgAAAAAAAABAwoQDAAAAAAAAAJAw4QAAAAAAAAAAJEw4AAAAAAAAAAAJEw4AAAAAAAAAQMKEAwAAAAAAAACQMOEAAAAAAAAAACRMOAAAAAAAAAAACRMOAAAAAAAAAEDChAMAAAAAAAAAkDDhAAAAAAAAAAAkTDgAAAAAAAAAAAkTDgAAAAAAAABAwoQDAAAAAAAAAJAw4QAAAAAAAAAAJEw4AAAAAAAAAAAJEw4AAAAAAAAAQMKEAwAAAAAAAACQMOEAAAAAAAAAACRMOAAAAAAAAAAACRMOAAAAAAAAAEDChAMAAAAAAAAAkDDhAAAAAAAAAAAkTDgAAAAAAAAAAAkTDgAAAAAAAABAwoQDAAAAAAAAAJAw4QAAAAAAAAAAJEw4AAAAAAAAAAAJEw4AAAAAAAAAQMKEAwAAAAAAAACQMOEAAAAAAAAAACRMOAAAAAAAAAAACRMOAAAAAAAAAEDChAMAAAAAAAAAkDDhAAAAAAAAAAAkTDgAAAAAAAAAAAkTDgAAAAAAAABAwoQDAAAAAAAAAJAw4QAAAAAAAAAAJEw4AAAAAAAAAAAJEw4AAAAAAAAAQMKEAwAAAAAAAACQMOEAAAAAAAAAACRMOAAAAAAAAAAACRMOAAAAAAAAAEDChAMAAAAAAAAAkDDhAAAAAAAAAAAkTDgAAAAAAAAAAAkTDgAAAAAAAABAwoQDAAAAAAAAAJAw4QAAAAAAAAAAJEw4AAAAAAAAAAAJEw4AAAAAAAAAQMKEAwAAAAAAAACQMOEAAAAAAAAAACRMOAAAAAAAAAAACRMOAAAAAAAAAEDChAMAAAAAAAAAkDDhAAAAAAAAAAAkTDgAAAAAAAAAAAkTDgAAAAAAAABAwoQDAAAAAAAAAJAw4QAAAAAAAAAAJEw4AAAAAAAAAAAJEw4AAAAAAAAAQMKEAwAAAAAAAACQMOEAAAAAAAAAACRMOAAAAAAAAAAACRMOAAAAAAAAAEDChAMAAAAAAAAAkDDhAAAAAAAAAAAkTDgAAAAAAAAAAAkTDgAAAAAAAABAwoQDAAAAAAAAAJAw4QAAAAAAAAAAJEw4AAAAAAAAAAAJEw4AAAAAAAAAQMKEAwAAAAAAAACQMOEAAAAAAAAAACRMOAAAAAAAAAAACRMOAAAAAAAAAEDChAMAAAAAAAAAkDDhAAAAAAAAAAAkTDgAAAAAAAAAAAkTDgAAAAAAAABAwoQDAAAAAAAAAJAw4QAAAAAAAAAAJEw4AAAAAAAAAAAJEw4AAAAAAAAAQMKEAwAAAAAAAACQMOEAAAAAAAAAACRMOAAAAAAAAAAACRMOAAAAAAAAAEDChAMAAAAAAAAAkDDhAAAAAAAAAAAkTDgAAAAAAAAAAAkTDgAAAAAAAABAwoQDAAAAAAAAAJAw4QAAAAAAAAAAJEw4AAAAAAAAAAAJEw4AAAAAAAAAQMKEAwAAAAAAAACQMOEAAAAAAAAAACRMOAAAAAAAAAAACRMOAAAAAAAAAEDChAMAAAAAAAAAkDDhAAAAAAAAAAAkTDgAAAAAAAAAAAkTDgAAAAAAAABAwoQDAAAAAAAAAJAw4QAAAAAAAAAAJEw4AAAAAAAAAAAJEw4AAAAAAAAAQMKEAwAAAAAAAACQMOEAAAAAAAAAACRMOAAAAAAAAAAACRMOAAAAAAAAAEDChAMAAAAAAAAAkDDhAAAAAAAAAAAkTDgAAAAAAAAAAAkTDgAAAAAAAABAwoQDAAAAAAAAAJAw4QAAAAAAAAAAJEw4AAAAAAAAAAAJEw4AAAAAAAAAQMKEAwAAAAAAAACQMOEAAAAAAAAAACRMOAAAAAAAAAAACRMOAAAAAAAAAEDChAMAAAAAAAAAkDDhAAAAAAAAAAAkTDgAAAAAAAAAAAkTDgAAAAAAAABAwoQDAAAAAAAAAJAw4QAAAAAAAAAAJEw4AAAAAAAAAAAJEw4AAAAAAAAAQMKEAwAAAAAAAACQMOEAAAAAAAAAACRMOAAAAAAAAAAACRMOAAAAAAAAAEDChAMAAAAAAAAAkDDhAAAAAAAAAAAkTDgAAAAAAAAAAAkTDgAAAAAAAABAwoQDAAAAAAAAAJAw4QAAAAAAAAAAJEw4AAAAAAAAAAAJEw4AAAAAAAAAQMKEAwAAAAAAAACQMOEAAAAAAAAAACRMOAAAAAAAAAAACRMOAAAAAAAAAEDChAMAAAAAAAAAkDDhAAAAAAAAAAAkTDgAAAAAAAD8//buPdbruo7j+OsYkw4cnSWK0WGQ1OCw/ogNGCedZMstybxgF7e2kJlIIcpWVCzqn8oS3TKYyVWtWazMoCVILeUc7hqOloKIB5W4ZJOGJHfYOf3h+I3TORw4IB7083hsbF9+n+/3fT7n/L7/nef5fQGAggkHAAAAAAAAAKBgwgEAAAAAAAAAKJhwAAAAAAAAAAAKJhwAAAAAAAAAgIIJBwAAAAAAAACgYMIBAAAAAAAAACiYcAAAAAAAAAAACiYcAAAAAAAAAICCCQcAAAAAAAAAoGDCAQAAAAAAAAAomHAAAAAAAAAAAAomHAAAAAAAAACAggkHAAAAAAAAAKBgwgEAAAAAAAAAKJhwAAAAAAAAAAAKJhwAAAAAAAAAgIIJBwAAAAAAAACgYMIBAAAAAAAAACiYcAAAAAAAAAAACiYcAAAAAAAAAICCCQcAAAAAAAAAoGDCAQAAAAAAAAAomHAAAAAAAAAAAAomHAAAAAAAAACAggkHAAAAAAAAAKBgwgEAAAAAAAAAKJhwAAAAAAAAAAAKJhwAAAAAAAAAgIIJBwAAAAAAAACgYMIBAAAAAAAAACiYcAAAAAAAAAAACiYcAAAAAAAAAICCCQcAAAAAAAAAoGDCAQAAAAAAAAAomHAAAAAAAAAAAAomHAAAAAAAAACAggkHAAAAAAAAAKBgwgEAAAAAAAAAKJhwAAAAAAAAAAAKJhwAAAAAAAAAgIIJBwAAAAAAAACgYMIBAAAAAAAAACiYcAAAAAAAAAAACiYcAAAAAAAAAICCCQcAAAAAAAAAoGDCAQAAAAAAAAAomHAAAAAAAAAAAAomHAAAAAAAAACAggkHAAAAAAAAAKBgwgEAAAAAAAAAKJhwAAAAAAAAAAAKJhwAAAAAAAAAgIIJBwAAAAAAAACgYMIBAAAAAAAAACiYcAAAAAAAAAAACiYcAAAAAAAAAICCCQcAAAAAAAAAoGDCAQAAAAAAAAAomHAAAAAAAAAAAAomHAAAAAAAAACAggkHAAAAAAAAAKBgwgEAAAAAAAAAKJhwAAAAAAAAAAAKJhwAAAAAAAAAgIIJBwAAAAAAAACgYMIBAAAAAAAAACiYcAAAAAAAAAAACiYcAAAAAAAAAICCCQcAAAAAAAAAoGDCAQAAAAAAAAAomHAAAAAAAAAAAAomHAAAAAAAAACAggkHAAAAAAAAAKBgwgEAAAAAAAAAKJhwAAAAAAAAAAAKJhwAAAAAAAAAgIIJBwAAAAAAAACgYMIBAAAAAAAAACiYcAAAAAAAAAAACiYcAAAAAAAAAICCCQcAAAAAAAAAoGDCAQAAAAAAAAAomHAAAAAAAAAAAAomHAAAAAAAAACAggkHAAAAAAAAAKBgwgEAAAAAAAAAKJhwAAAAAAAAAAAKJhwAAAAAAAAAgIIJBwAAAAAAAACgYMIBAAAAAAAAACiYcAAAAAAAAAAACiYcAAAAAAAAAICCCQcAAAAAAAAAoGDCAQAAAAAA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97s83vPyeM/L4z0vj/e8LN7v8njPKcH06dOzZs2aPPXUU+nRo0dXb6dL7dy587TWS3Gm7plTCgc6ejRA79698/vf/z51dXU5dOhQZsyY0SoceP/73185PnToUIdf59jHClRXV7daOzrnRDM6mvN27QUAAAAAAACgs/7+97+npaUlV155Zbvrs2bNyqxZs3Lddddl4cKF7+zm3mG//e1vu3oL7wpn6p45pXDgRC699NJcddVVWbRoUZqamrJjx4706dMnSXLeeedVzjvRR/7v3bu3cvz/jxI4OudkHhtwvDlv114AAAAAAAAAOmvkyJHp1q3tr2z/9a9/ZfHixRk0aFAuu+yyDBkypAt2x9noTN0zZyQcSJLBgwdn0aJFSd56tMHRcKC2trZyzrZt2zqcsXXr1spx3759W63V1tbm6aefzt69e/PGG290+CkIR+dcdNFFrR458HbtBQAAAAAAAKCzxo4dm7Fjx7Z5vaGhIYsXL87IkSMzc+bMLtgZZ6szdc+csXCgpaWl3dcHDx5cOd64cWOHM45dr6urazPnscceq5w3YsSIdmccOXIkmzdvbndGTU1N+vbtm61bt57WXgAAAAAAAACOmjt3blasWJEkee655yqvNTQ0JEmuv/76XH/99V20O85GXX3PnLFwYMOGDZXjo582kCQf+chH0qdPn+zYsSONjY0dzli2bFmS5MMf/nD69+/fau3yyy+vHDc2Nh43HFi7dm3lMQOXXXZZm/XLL7888+fPz4svvpjXXnstl1xySbtzjt1re3MAAAAAAAAAkmTFihX55S9/2eq1lStXZuXKlUmS/v37CwdopavvmaqW4300wGl4+eWXM2jQoBw+fDiXXnpp5S/+j/rGN76RBx54IEmyevXqdn/pv2bNmtTX11fOv//++1utHzp0KBdffHF2796durq6rF+/PlVVVW3mjB8/PrNmzUqSPPPMMxk2bFir9d/97nf58pe/nCT5yU9+ku9+97ttZuzbty+1tbXZtWtXBg8enPXr15/sjwIAAAAAAAAAzmrndPaCP/3pTzly5Mhx1//973/nC1/4Qg4fPpwkmTBhQptzJk2alG7d3vqwg4kTJ2b//v2t1vfv35+JEycmSbp165ZJkya1mXHuuefmjjvuSJK88MILuffee9ucs3r16sybNy9JMnLkyDbRQJLccMMNGTBgQJK3woH/jxySZPLkydm1a1flGAAAAAAAAADeKzr9iQP9+/fP4cOHc+ONN6a+vj79+/dPdXV1du7cmYaGhsycOTP/+c9/krz1GIC//vWv6d69e5s5U6ZMyU9/+tMkyZAhQ/Kd73wnAwYMyObNm3P33Xdn3bp1lfPuuuuudvfy5ptvZujQodm0aVOSZNy4cbnppptSXV2dpUuX5q677sqePXtSXV2dVatW5ROf+ES7cxYvXpzPf/7zaW5uTu/evTN16tQMHz48u3btypw5c/LYY49Vvp+Ghoa8733v68yPDAAAAAAAAADOWqcUDmzZsuWE5914442ZO3duLrjggnbXm5ubc+utt+bBBx887oxbbrkls2fPzjnnHP+DEZqamjJq1Ki89NJL7a6ff/75+fWvf51rrrmmw/3OmTMnt99+ew4dOtTu+vDhw7No0aL06tWrwzkAAAAAAAAA8G7S6XCgsbExjY2NWb16dV5++eXs3Lkz//3vf1NTU5O+ffvmk5/8ZMaMGZP6+vqTmrd48eLMnj07f/vb37Jz58706tUrw4YNy2233Zarr776pGbs3bs3999/fx599NE0NTXl0KFD6du3b0aNGpU777wz/fr1O6k5zz//fKZPn54nn3wyO3bsSM+ePVNXV5evfOUr+drXvlZ5vAIAAAAAAAAAvFd0OhwAAAAAAAAAAN47jv8MAAAAAAAAAADgPU84AAAAAAAAAAAFEw4AAAAAAAAAQMGEAwAAAAAAAABQMOEAAAAAAAAAABRMOAAAAAAAAAAABRMOAAAAAAAAAEDBhAMAAAAAAAAAUDDhAAAAAAAAAAAUTDgAAAAAAAAAAAUTDgAAAAAAAABAwYQDAAAAAAAAAFAw4QAAAAAAAAAAFEw4AAAAAAAAAAAFEw4AAAAAAAAAQMH+B1RrE2eWR2TQAAAAAElFTkSuQmCC",
      "text/plain": [
       "<Figure size 2500x1000 with 2 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Ans: \n",
      "There are no missing value\n"
     ]
    }
   ],
   "source": [
    "## Handling missing value\n",
    "import missingno as msno\n",
    "msno.matrix(loan_data)\n",
    "plt.show()\n",
    "print(\"Ans: \\nThere are no missing value\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "cdfc5b32-daab-4df6-9219-d2708ebdec82",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 5000 entries, 0 to 4999\n",
      "Data columns (total 8 columns):\n",
      " #   Column              Non-Null Count  Dtype\n",
      "---  ------              --------------  -----\n",
      " 0   ID                  5000 non-null   int64\n",
      " 1   ZIP Code            5000 non-null   int64\n",
      " 2   Education           5000 non-null   int64\n",
      " 3   Personal Loan       5000 non-null   int64\n",
      " 4   Securities Account  5000 non-null   int64\n",
      " 5   CD Account          5000 non-null   int64\n",
      " 6   Online              5000 non-null   int64\n",
      " 7   CreditCard          5000 non-null   int64\n",
      "dtypes: int64(8)\n",
      "memory usage: 312.6 KB\n"
     ]
    }
   ],
   "source": [
    "x = loan_data[['ID', 'ZIP Code', 'Education', 'Personal Loan', 'Securities Account', 'CD Account', 'Online', 'CreditCard']]\n",
    "x.info()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "2df3a822-5682-4281-b9c5-f31f4bc8dd84",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 5000 entries, 0 to 4999\n",
      "Data columns (total 6 columns):\n",
      " #   Column      Non-Null Count  Dtype  \n",
      "---  ------      --------------  -----  \n",
      " 0   Age         5000 non-null   int64  \n",
      " 1   Experience  5000 non-null   int64  \n",
      " 2   Income      5000 non-null   int64  \n",
      " 3   Family      5000 non-null   int64  \n",
      " 4   CCAvg       5000 non-null   float64\n",
      " 5   Mortgage    5000 non-null   int64  \n",
      "dtypes: float64(1), int64(5)\n",
      "memory usage: 234.5 KB\n"
     ]
    }
   ],
   "source": [
    "y = loan_data[['Age', 'Experience', 'Income', 'Family', 'CCAvg', 'Mortgage']]\n",
    "y.info()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "c51eb97f-e4ba-4a20-b5ad-c403cfc69170",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "73.7742"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.mean(y['Income'])"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "86d10732-e709-45c8-8247-6ed87d4d93d1",
   "metadata": {},
   "source": [
    "## <font color = \"red\"> **8).** \n",
    "#### Give us the statistical summary for all the variables in the dataset.\n",
    "**Ans:-** We have the 2 types of data **1.** ***Quantitative,*** **2.** ***Qualitative***\n",
    "##### We can use describe function for both of data types."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "a13731b1-4dc9-44d0-97ed-86a89743e653",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>count</th>\n",
       "      <th>mean</th>\n",
       "      <th>std</th>\n",
       "      <th>min</th>\n",
       "      <th>25%</th>\n",
       "      <th>50%</th>\n",
       "      <th>75%</th>\n",
       "      <th>max</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Age</th>\n",
       "      <td>5000.0</td>\n",
       "      <td>45.338400</td>\n",
       "      <td>11.463166</td>\n",
       "      <td>23.0</td>\n",
       "      <td>35.0</td>\n",
       "      <td>45.0</td>\n",
       "      <td>55.0</td>\n",
       "      <td>67.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Experience</th>\n",
       "      <td>5000.0</td>\n",
       "      <td>20.104600</td>\n",
       "      <td>11.467954</td>\n",
       "      <td>-3.0</td>\n",
       "      <td>10.0</td>\n",
       "      <td>20.0</td>\n",
       "      <td>30.0</td>\n",
       "      <td>43.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Income</th>\n",
       "      <td>5000.0</td>\n",
       "      <td>73.774200</td>\n",
       "      <td>46.033729</td>\n",
       "      <td>8.0</td>\n",
       "      <td>39.0</td>\n",
       "      <td>64.0</td>\n",
       "      <td>98.0</td>\n",
       "      <td>224.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Family</th>\n",
       "      <td>5000.0</td>\n",
       "      <td>2.396400</td>\n",
       "      <td>1.147663</td>\n",
       "      <td>1.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>4.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>CCAvg</th>\n",
       "      <td>5000.0</td>\n",
       "      <td>1.937938</td>\n",
       "      <td>1.747659</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.7</td>\n",
       "      <td>1.5</td>\n",
       "      <td>2.5</td>\n",
       "      <td>10.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Mortgage</th>\n",
       "      <td>5000.0</td>\n",
       "      <td>56.498800</td>\n",
       "      <td>101.713802</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>101.0</td>\n",
       "      <td>635.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "             count       mean         std   min   25%   50%    75%    max\n",
       "Age         5000.0  45.338400   11.463166  23.0  35.0  45.0   55.0   67.0\n",
       "Experience  5000.0  20.104600   11.467954  -3.0  10.0  20.0   30.0   43.0\n",
       "Income      5000.0  73.774200   46.033729   8.0  39.0  64.0   98.0  224.0\n",
       "Family      5000.0   2.396400    1.147663   1.0   1.0   2.0    3.0    4.0\n",
       "CCAvg       5000.0   1.937938    1.747659   0.0   0.7   1.5    2.5   10.0\n",
       "Mortgage    5000.0  56.498800  101.713802   0.0   0.0   0.0  101.0  635.0"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# For Quantitative type\n",
    "y.describe().T"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "8484ec22-c3e7-4fa6-b588-3b78b90891c1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>count</th>\n",
       "      <th>mean</th>\n",
       "      <th>std</th>\n",
       "      <th>min</th>\n",
       "      <th>25%</th>\n",
       "      <th>50%</th>\n",
       "      <th>75%</th>\n",
       "      <th>max</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>ID</th>\n",
       "      <td>5000.0</td>\n",
       "      <td>2500.5000</td>\n",
       "      <td>1443.520003</td>\n",
       "      <td>1.0</td>\n",
       "      <td>1250.75</td>\n",
       "      <td>2500.5</td>\n",
       "      <td>3750.25</td>\n",
       "      <td>5000.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>ZIP Code</th>\n",
       "      <td>5000.0</td>\n",
       "      <td>93152.5030</td>\n",
       "      <td>2121.852197</td>\n",
       "      <td>9307.0</td>\n",
       "      <td>91911.00</td>\n",
       "      <td>93437.0</td>\n",
       "      <td>94608.00</td>\n",
       "      <td>96651.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Education</th>\n",
       "      <td>5000.0</td>\n",
       "      <td>1.8810</td>\n",
       "      <td>0.839869</td>\n",
       "      <td>1.0</td>\n",
       "      <td>1.00</td>\n",
       "      <td>2.0</td>\n",
       "      <td>3.00</td>\n",
       "      <td>3.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Personal Loan</th>\n",
       "      <td>5000.0</td>\n",
       "      <td>0.0960</td>\n",
       "      <td>0.294621</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.00</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.00</td>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Securities Account</th>\n",
       "      <td>5000.0</td>\n",
       "      <td>0.1044</td>\n",
       "      <td>0.305809</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.00</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.00</td>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>CD Account</th>\n",
       "      <td>5000.0</td>\n",
       "      <td>0.0604</td>\n",
       "      <td>0.238250</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.00</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.00</td>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Online</th>\n",
       "      <td>5000.0</td>\n",
       "      <td>0.5968</td>\n",
       "      <td>0.490589</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.00</td>\n",
       "      <td>1.0</td>\n",
       "      <td>1.00</td>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>CreditCard</th>\n",
       "      <td>5000.0</td>\n",
       "      <td>0.2940</td>\n",
       "      <td>0.455637</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.00</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1.00</td>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                     count        mean          std     min       25%  \\\n",
       "ID                  5000.0   2500.5000  1443.520003     1.0   1250.75   \n",
       "ZIP Code            5000.0  93152.5030  2121.852197  9307.0  91911.00   \n",
       "Education           5000.0      1.8810     0.839869     1.0      1.00   \n",
       "Personal Loan       5000.0      0.0960     0.294621     0.0      0.00   \n",
       "Securities Account  5000.0      0.1044     0.305809     0.0      0.00   \n",
       "CD Account          5000.0      0.0604     0.238250     0.0      0.00   \n",
       "Online              5000.0      0.5968     0.490589     0.0      0.00   \n",
       "CreditCard          5000.0      0.2940     0.455637     0.0      0.00   \n",
       "\n",
       "                        50%       75%      max  \n",
       "ID                   2500.5   3750.25   5000.0  \n",
       "ZIP Code            93437.0  94608.00  96651.0  \n",
       "Education               2.0      3.00      3.0  \n",
       "Personal Loan           0.0      0.00      1.0  \n",
       "Securities Account      0.0      0.00      1.0  \n",
       "CD Account              0.0      0.00      1.0  \n",
       "Online                  1.0      1.00      1.0  \n",
       "CreditCard              0.0      1.00      1.0  "
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# For Qualitative type\n",
    "x.describe().T"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3894af1a-bccf-4202-a466-e528a672cde1",
   "metadata": {},
   "source": [
    "## <font color = \"red\"> **9).** \n",
    "#### Evaluate the measures of central tendency and measures of dispersion for all the quantitative variables in the dataset.\n",
    "**Ans:-** \n",
    "- For calculate measures of central tendency **:** Compute ***Mean,*** ***Median*** and ***Mode.***\n",
    "- For calculate measures of dispersion **:** Compute ***Range,*** ***Variance*** and ***Standard Deviation.***"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "f7ebc42b-2f35-4031-ac2c-df0ff55ec47c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Mean for the Quantitative types :\n",
      " Age           45.338400\n",
      "Experience    20.104600\n",
      "Income        73.774200\n",
      "Family         2.396400\n",
      "CCAvg          1.937938\n",
      "Mortgage      56.498800\n",
      "dtype: float64\n",
      "\n",
      "Median for the Quantitative types :\n",
      " Age           45.0\n",
      "Experience    20.0\n",
      "Income        64.0\n",
      "Family         2.0\n",
      "CCAvg          1.5\n",
      "Mortgage       0.0\n",
      "dtype: float64\n",
      "\n",
      "Mode for the Quantitative types : \n",
      " Age           35.0\n",
      "Experience    32.0\n",
      "Income        44.0\n",
      "Family         1.0\n",
      "CCAvg          0.3\n",
      "Mortgage       0.0\n",
      "Name: 0, dtype: float64\n",
      "\n",
      "Mode for the Qualitative types : \n",
      " ID                        1.0\n",
      "ZIP Code              94720.0\n",
      "Education                 1.0\n",
      "Personal Loan             0.0\n",
      "Securities Account        0.0\n",
      "CD Account                0.0\n",
      "Online                    1.0\n",
      "CreditCard                0.0\n",
      "Name: 0, dtype: float64\n"
     ]
    }
   ],
   "source": [
    "# Calculate measures of central tendency\n",
    "print(\"\\nMean for the Quantitative types :\\n\", y.mean())\n",
    "print(\"\\nMedian for the Quantitative types :\\n\", y.median())\n",
    "print(\"\\nMode for the Quantitative types : \\n\", y.mode().iloc[0])\n",
    "print(\"\\nMode for the Qualitative types : \\n\", x.mode().iloc[0])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "d2adf535-8668-49d2-9f41-91657e0988c9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Calculating Range for Quantitative : \n",
      " Age            44.0\n",
      "Experience     46.0\n",
      "Income        216.0\n",
      "Family          3.0\n",
      "CCAvg          10.0\n",
      "Mortgage      635.0\n",
      "dtype: float64\n",
      "\n",
      "Calculating Range for Qualitative : \n",
      " ID                     4999\n",
      "ZIP Code              87344\n",
      "Education                 2\n",
      "Personal Loan             1\n",
      "Securities Account        1\n",
      "CD Account                1\n",
      "Online                    1\n",
      "CreditCard                1\n",
      "dtype: int64\n",
      "\n",
      "Calculating Variance for Quantitative : \n",
      " Age             131.404166\n",
      "Experience      131.513962\n",
      "Income         2119.104235\n",
      "Family            1.317130\n",
      "CCAvg             3.054312\n",
      "Mortgage      10345.697538\n",
      "dtype: float64\n",
      "\n",
      "Calculating Variance for Qualitative : \n",
      " ID                    2.083750e+06\n",
      "ZIP Code              4.502257e+06\n",
      "Education             7.053801e-01\n",
      "Personal Loan         8.680136e-02\n",
      "Securities Account    9.351934e-02\n",
      "CD Account            5.676319e-02\n",
      "Online                2.406779e-01\n",
      "CreditCard            2.076055e-01\n",
      "dtype: float64\n",
      "\n",
      "Calculating Standard Deviation for Quantitative : \n",
      " Age            11.463166\n",
      "Experience     11.467954\n",
      "Income         46.033729\n",
      "Family          1.147663\n",
      "CCAvg           1.747659\n",
      "Mortgage      101.713802\n",
      "dtype: float64\n",
      "\n",
      "Calculating Standard Deviation for Qualitative : \n",
      " ID                    1443.520003\n",
      "ZIP Code              2121.852197\n",
      "Education                0.839869\n",
      "Personal Loan            0.294621\n",
      "Securities Account       0.305809\n",
      "CD Account               0.238250\n",
      "Online                   0.490589\n",
      "CreditCard               0.455637\n",
      "dtype: float64\n"
     ]
    }
   ],
   "source": [
    "# Calculate measure of dispersion\n",
    "print(\"\\nCalculating Range for Quantitative : \\n\", y.max() - y.min())\n",
    "print(\"\\nCalculating Range for Qualitative : \\n\", x.max() - x.min())\n",
    "print(\"\\nCalculating Variance for Quantitative : \\n\", y.var())\n",
    "print(\"\\nCalculating Variance for Qualitative : \\n\", x.var())\n",
    "print(\"\\nCalculating Standard Deviation for Quantitative : \\n\", y.std())\n",
    "print(\"\\nCalculating Standard Deviation for Qualitative : \\n\", x.std())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3b052742-5350-4f55-a023-f260cebe9e3a",
   "metadata": {},
   "source": [
    "## <font color = \"red\"> **10).** \n",
    "#### What statistical method will you use to examine the presence of a linear relationship between age and experience variables? Also, create a plot to illustrate this relationship."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "7e884e26-113f-40f2-8e2d-6e62c48f2b61",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAA0oAAAIhCAYAAABwnkrAAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjguNCwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8fJSN1AAAACXBIWXMAAA9hAAAPYQGoP6dpAACSUklEQVR4nOzdeVyUVfs/8M8wLIJsLiguuCFZ5laplbuWWlqBhpaaS6aZ4IIo5lKPmIoKibigJWaauZTmUmkKmZpmJWWWaU9f4XFXFFNABFnP7w9/TA7MPXNghlmYz/v14vU0576uuc8MNzxc3mfOpRJCCBAREREREZGGg6UnQEREREREZG1YKBEREREREZXCQomIiIiIiKgUFkpERERERESlsFAiIiIiIiIqhYUSERERERFRKSyUiIiIiIiISmGhREREREREVAoLJSIiIiIiolJYKBHZuPXr10OlUuGXX35RjDl//jxUKhXWr19vvomZ0KFDh6BSqTRfarUaPj4+ePHFF/W+bn2MeU+uXr2KyMhInDx5ssyxyMhIqFSqCs3JlErmcfPmTYOxTZo0wahRo0x2bplrsryOHTuGyMhIZGRkmOw5rVVBQQF8fX2hUqmwfft2S0/HbGSvwwd/F5T+MuV1XFlM/fNGRJXH0dITIKLKV69ePfz444/w9/e39FSMEhUVhZ49e6KgoAC//fYb5s6di+7du+PkyZMICAgw2zyuXr2KuXPnokmTJmjXrp3WsTFjxuC5554z21xMYefOnfD09LT0NPQ6duwY5s6di1GjRsHb29vS06lUX3/9Na5fvw4A+OijjxAcHGzhGVmf4OBgTJ06tcy4j4+PBWZTPrbw80ZE97FQIrIDLi4ueOqppyw9Db1ycnLg5uamNyYgIEDzOrp27Qpvb2+MHDkSn376KebOnWuOaRrUsGFDNGzY0NLTKJfHHnvM0lOgB3z00UdwdnZG9+7dkZiYiMuXL9vcNVXZ6tata/W/00rLzc2Fq6srf96IbAiX3hHZAV3LzEqWZp0+fRpDhgyBl5cX6tati9GjRyMzM1MrXwiBVatWoV27dnB1dUWNGjUQHByM//3vf1pxSUlJCAwMRMOGDVGtWjU0b94c48aNK7P8q+TcJ06cQHBwMGrUqFGhu13t27cHAM2/vpc4e/Yshg4dijp16sDFxQWPPPII4uPjDT5fSkoKXn/9dQQEBMDNzQ0NGjTAiy++iFOnTmliDh06hA4dOgAAXn/9dc2Sn8jISK3X9qDi4mJER0fj4YcfhouLC+rUqYMRI0bg8uXLWnE9evRAq1atkJycjK5du8LNzQ3NmjXDokWLUFxcrPV88+fPR4sWLeDq6gpvb2+0adMGy5YtK/Oarl+/bvD7W3opUMlSx08//RTh4eHw9fWFq6srunfvjt9++83g+1ji9u3beP3111GzZk1Ur14dL774YplrBgC+/fZbPPPMM/D09ISbmxs6d+6MAwcOaI5HRkYiIiICANC0aVPNe37o0CFERETAy8sLRUVFmviJEydCpVIhJiZGM/bPP//AwcEBK1as0IxlZWVh2rRpaNq0KZydndGgQQOEhYXh7t27WvOTvf5lv3/6XL16Ffv27cOLL76IiIgIFBcXKy4PTUhIwEMPPQQXFxe0bNkSmzdvxqhRo9CkSROtuPz8fMyfP19z/fn4+OD1119Henq6wfn88ssvePXVV9GkSRO4urqiSZMmGDJkCC5cuKAVV7Lc8uDBgxg/fjxq166NWrVqYeDAgbh69apWbEFBAaZPnw5fX1+4ubmhS5cuOH78uNT7I+vmzZvw8/NDp06dUFBQoBk/c+YMqlevjuHDh2vGSr5vR44cwVNPPQVXV1c0aNAA7777rtZ1Bci/l02aNMELL7yAHTt24LHHHkO1atU0/5ija+md7LWoUqkwYcIEbNy4EY888gjc3NzQtm1bfP3112Xeg//+978YMmQI6tatCxcXFzRq1AgjRoxAXl6eJiYtLQ3jxo1Dw4YN4ezsjKZNm2Lu3LkoLCws3xtOVFUJIrJpH3/8sQAgkpOTFWPOnTsnAIiPP/5YMzZnzhwBQLRo0UL85z//EUlJSSI2Nla4uLiI119/XSt/7NixwsnJSUydOlXs27dPbN68WTz88MOibt26Ii0tTRO3evVqsXDhQvHll1+Kw4cPiw0bNoi2bduKFi1aiPz8/DLnbty4sXj77bdFUlKS2LVrl+L8Dx48KACIbdu2aY1//fXXAoBYsmSJZuz06dPCy8tLtG7dWnzyySciMTFRTJ06VTg4OIjIyEi978nhw4fF1KlTxfbt28Xhw4fFzp07RVBQkHB1dRX//e9/hRBCZGZmat7zd955R/z444/ixx9/FJcuXdJ6bQ968803BQAxYcIEsW/fPvHBBx8IHx8f4efnJ9LT0zVx3bt3F7Vq1RIBAQHigw8+EElJSSIkJEQAEBs2bNDELVy4UKjVajFnzhxx4MABsW/fPhEXF6f1+srz/W3cuLEYOXJkmffbz89PBAYGiq+++kp8+umnonnz5sLT01OkpqYqfq+E+Pea9PPzE6NHjxbffPONWLNmjahTp47w8/MTt2/f1sRu3LhRqFQqERQUJHbs2CG++uor8cILLwi1Wi2+/fZbIYQQly5dEhMnThQAxI4dOzTveWZmpti3b58AII4dO6Z5zocffli4urqK3r17a8Y+++wzAUCcOXNGCCHE3bt3Rbt27UTt2rVFbGys+Pbbb8WyZcuEl5eX6NWrlyguLtbkyl7/st8/fRYsWCAAiD179oji4mLRuHFj0bRpU635CCHEhx9+KACIl19+WXz99ddi06ZN4qGHHhKNGzcWjRs31sQVFRWJ5557TlSvXl3MnTtXJCUlibVr14oGDRqIli1bipycHL3z2bZtm/jPf/4jdu7cKQ4fPiy2bt0qunfvLnx8fLSu3ZLvebNmzcTEiRPF/v37xdq1a0WNGjVEz549tZ5z5MiRQqVSiYiICJGYmChiY2NFgwYNhKenp9Z1qASACAkJEQUFBWW+Hnyfjh49KhwdHcWUKVOEEPe/5y1bthQPP/ywyM7O1sSVfN/q168vli9fLvbv3y8mTZokAIjQ0NAKvZeNGzcW9erVE82aNRPr1q0TBw8eFMePH9cce/B1ludaBCCaNGkiOnbsKD7//HOxd+9e0aNHD+Ho6Kj1c3ny5Enh7u4umjRpIj744ANx4MAB8emnn4rBgweLrKwsIYQQ165dE35+fqJx48biww8/FN9++62YN2+ecHFxEaNGjTL4fSCyByyUiGycsYVSdHS0VmxISIioVq2a5v+cf/zxxzLFiBD3/3h1dXUV06dP13nO4uJiUVBQIC5cuCAAiN27d5c593/+8x+p11jyh/tnn30mCgoKRE5Ojvjhhx9EixYtRMuWLbX+8O7bt69o2LChyMzM1HqOCRMmiGrVqolbt24pvielFRYWivz8fBEQEKD5Y0sIIZKTkxVzSxdKf/31l+YPuwf9/PPPAoCYNWuWZqx79+4CgPj555+1Ylu2bCn69u2refzCCy+Idu3aKc77wXkY+v4KoVwoPf7441px58+fF05OTmLMmDF6z11yTQ4YMEBr/IcffhAAxPz584UQ9/9ArFmzpnjxxRe14oqKikTbtm1Fx44dNWMxMTECgDh37pxW7N27d4Wzs7N47733hBBCXL58WQAQb7/9tnB1dRX37t0TQtwvdurXr6/JW7hwoXBwcCjzc7N9+3YBQOzdu1cIUb7rX/b7p6S4uFg0b95cNGjQQBQWFgoh/v0+HjhwQOv98fX1FU8++aRW/oULF4STk5NWobRlyxYBQHzxxRdasSXX8KpVqwzO60GFhYUiOztbVK9eXSxbtkwzXvI9L32dR0dHCwDi2rVrQoh/fx4e/HkSQohNmzYJANKFktLXxo0btWIXL14sAIidO3eKkSNHCldXV/HHH39oxZR83x78HSXE/WvGwcFBXLhwQQhRvveycePGQq1Wi7///rvM/Ev/vMleiyWvvW7duppiRwgh0tLShIODg1i4cKFmrFevXsLb21vcuHFD53sohBDjxo0T7u7umtdX4v333xcAxOnTpxVziewFl94R2bmXXnpJ63GbNm1w79493LhxA8D9D5arVCq89tprKCws1Hz5+vqibdu2OHTokCb3xo0beOutt+Dn5wdHR0c4OTmhcePGAIC//vqrzLlffvnlcs31lVdegZOTk2Z5VlZWFvbs2aP5cP+9e/dw4MABDBgwAG5ublrz7devH+7du4effvpJ8fkLCwsRFRWFli1bwtnZGY6OjnB2dsbZs2d1zl/GwYMHAaDMUpuOHTvikUce0VpiBgC+vr7o2LGj1libNm20ljp17NgRv//+O0JCQrB//35kZWUpnt/Q91efoUOHai0jbNy4MTp16qR5TYYMGzZM63GnTp3QuHFjTf6xY8dw69YtjBw5Uut7VVxcjOeeew7Jyclllh6V5ubmhqeffhrffvstgPvLP729vREREYH8/HwcPXoUwP3lfc8++6wm7+uvv0arVq3Qrl07rXP37dtXs6yvJE72+gfkvn9KDh8+jJSUFIwcORJqtRrAv8s7161bp4n7+++/kZaWhsGDB2vlN2rUCJ07d9Ya+/rrr+Ht7Y0XX3xRa/7t2rWDr69vmfmXlp2djbfffhvNmzeHo6MjHB0d4e7ujrt37+r8mdB1vQHQvP6S733pa2Pw4MFwdJT/2PTgwYORnJxc5qtfv35acREREejfvz+GDBmCDRs2YMWKFWjdunWZ5/Pw8Cgz96FDh6K4uBjff/89gPK/l23atMFDDz1k8LXIXoslevbsCQ8PD83junXrok6dOpr3OCcnB4cPH8bgwYP1bm7x9ddfo2fPnqhfv77WeZ9//nkA969HInvHzRyI7FytWrW0Hru4uAC4/8Fj4P5nXIQQqFu3rs78Zs2aAbj/uZk+ffrg6tWrePfdd9G6dWtUr14dxcXFeOqppzTP96B69eqVa66LFy9Gr169kJOTg8TERCxcuBBBQUH4+eef4eLign/++QeFhYVYsWKF1mdRHqRvu+zw8HDEx8fj7bffRvfu3VGjRg04ODhgzJgxOucv459//gGg+7XWr1+/zB/Qpb8fwP3vyYPnnzlzJqpXr45PP/0UH3zwAdRqNbp164bFixdrPrel9Hylv7/6+Pr66hz7/fffDebqyy95T0o+W6ZvV7dbt26hevXqes/z7LPPYt68ebh79y6+/fZb9OrVC7Vq1cITTzyBb7/9Fs2aNcO5c+e0Nvy4fv06UlJS4OTkpPM5S64T2eu/hMz3T8lHH30EABgwYIBmG3QvLy906dIFX3zxBVauXAlvb2/N+6drTnXr1sW5c+c0j69fv46MjAw4OzvrPKeh7eOHDh2KAwcO4N1330WHDh3g6ekJlUqFfv366XxNhq63krmXvjYcHR11vndKfHx8ylzrupRsGb5nzx74+vpqfTbpQbrey5I5Pni9lue9lP39JnstljB0jd2+fRtFRUUGNwC5fv06vvrqK+nzEtkjFkpEpFft2rWhUqlw5MgRzR89DyoZ+/PPP/H7779j/fr1GDlypOZ4SkqK4nOXt99Qs2bNNH8cdevWDa6urnjnnXewYsUKTJs2DTVq1IBarcbw4cMRGhqq8zmaNm2q+PyffvopRowYgaioKK3xmzdvVnhL6pI/aq5du1bmD5erV6+idu3a5X5OR0dHhIeHIzw8HBkZGfj2228xa9Ys9O3bF5cuXTK4e6CstLQ0nWOyf9Aq5Tdv3hwANK99xYoVijuYKRUoD3rmmWfw7rvv4vvvv8eBAwcwZ84czXhiYqLme/7MM89ocmrXrg1XV1etOzUPKpmb7PVvrMzMTHzxxRcAoNkspLTNmzcjJCRE8/6X3sQEKPuel2yqsG/fPp3P+eCdCV1z+vrrrzFnzhzMmDFDM56Xl4dbt27pf0EKSuaelpaGBg0aaMYLCws1BYkpXbt2DaGhoWjXrh1Onz6NadOmYfny5WXi9L2XJXMu73sp+/tN9lqUVbNmTajV6jKbxeh63jZt2mDBggU6j9evX79c5yWqilgoEZFeL7zwAhYtWoQrV66UWerzoJI/Ckr/4fjhhx9W2tymT5+O9evXY9GiRRg3bhw8PDzQs2dP/Pbbb2jTpo3iv/wqUalUZea/Z88eXLlyRfPHPVC+uzK9evUCcL8Ie/AP4OTkZPz111+YPXt2ueZYmre3N4KDg3HlyhWEhYXh/PnzaNmypVHPWWLLli0IDw/XfG8vXLiAY8eOYcSIEVL5mzZt0lpeeezYMVy4cAFjxowBAHTu3Bne3t44c+YMJkyYoPe59L3nHTt2hKenJ+Li4pCWlobevXsDuH+nafHixfj888/RsmVLrT/8XnjhBURFRaFWrVp6i2fZ699YmzdvRm5uLubNm4cuXbqUOT5o0CCsW7cOISEhaNGiBXx9ffH5558jPDxcE3Px4kUcO3aszOvcunUrioqK8OSTT5ZrTiqVCkKIMj8Ta9euLbMbnKwePXoAuH9tPPHEE5rxzz//3OQ7rRUVFWHIkCFQqVT45ptvsGnTJkybNg09evTAwIEDtWLv3LmDL7/8Umv53ebNm+Hg4IBu3boBMO691Ef2WpRVskPltm3bsGDBAsVC64UXXsDevXvh7++PGjVqGH1eoqqIhRJRFfHdd9/h/PnzZcZLr9kvr86dO+PNN9/E66+/jl9++QXdunVD9erVce3aNRw9ehStW7fG+PHj8fDDD8Pf3x8zZsyAEAI1a9bEV199haSkJKPOr4+TkxOioqIwePBgLFu2DO+88w6WLVuGLl26oGvXrhg/fjyaNGmCO3fuICUlBV999RW+++47xed74YUXsH79ejz88MNo06YNfv31V8TExJS5E+Tv7w9XV1ds2rQJjzzyCNzd3VG/fn2d/wLbokULvPnmm1ixYgUcHBzw/PPP4/z583j33Xfh5+eHKVOmlPt1v/jii2jVqhXat28PHx8fXLhwAXFxcWjcuLFJG+/euHEDAwYMwNixY5GZmYk5c+agWrVqmDlzplT+L7/8gjFjxmDQoEG4dOkSZs+ejQYNGiAkJAQA4O7ujhUrVmDkyJG4desWgoODUadOHaSnp+P3339Heno6Vq9eDQCaz5UsW7YMI0eOhJOTE1q0aAEPDw+o1Wp0794dX331FZo2barZar5z585wcXHBgQMHMGnSJK25hYWF4YsvvkC3bt0wZcoUtGnTBsXFxbh48SISExMxdepUPPnkk9LXv7E++ugj1KhRA9OmTUO1atXKHB8xYgRiY2Px+++/o23btpg7dy7GjRuH4OBgjB49GhkZGZg7dy7q1asHB4d/P3786quvYtOmTejXrx8mT56Mjh07wsnJCZcvX8bBgwcRGBiIAQMG6JyTp6cnunXrhpiYGNSuXRtNmjTB4cOH8dFHH1X4DusjjzyC1157DXFxcXBycsKzzz6LP//8E++//365mrBev35d5+cNPT09Nf9QMGfOHBw5cgSJiYnw9fXF1KlTcfjwYbzxxht47LHHtIqSWrVqYfz48bh48SIeeugh7N27FwkJCRg/fjwaNWoEwLj3Uh/Za7E8YmNj0aVLFzz55JOYMWMGmjdvjuvXr+PLL7/Ehx9+CA8PD7z33ntISkpCp06dMGnSJLRo0QL37t3D+fPnsXfvXnzwwQfs30Vk2b0kiMhYJbtNKX2dO3dO7653D27x++Dzld5dbN26deLJJ58U1atXF66ursLf31+MGDFC/PLLL5qYM2fOiN69ewsPDw9Ro0YNMWjQIHHx4kUBQMyZM8fguZUobQ9e4sknnxQ1atQQGRkZQoj7O9qNHj1aNGjQQDg5OQkfHx/RqVMnzW5rJTGl35Pbt2+LN954Q9SpU0e4ubmJLl26iCNHjoju3buL7t27a51zy5Yt4uGHHxZOTk5ar0/X9uBFRUVi8eLF4qGHHhJOTk6idu3a4rXXXtNsKV6ie/fu4tFHHy3z+kaOHKm1k9mSJUtEp06dRO3atYWzs7No1KiReOONN8T58+c1MeX5/irterdx40YxadIk4ePjI1xcXETXrl21vt9KSs6RmJgohg8fLry9vYWrq6vo16+fOHv2bJn4w4cPi/79+4uaNWsKJycn0aBBA9G/f/8y3++ZM2eK+vXrCwcHBwFAHDx4UHNs2bJlAoAYO3asVk7v3r0FAPHll1+WOW92drZ45513RIsWLYSzs7NmW/kpU6ZobfsthNz1L/v9K+33338XAERYWJhizH//+18BQEycOFEztmbNGtG8eXPh7OwsHnroIbFu3ToRGBgoHnvsMa3cgoIC8f7774u2bduKatWqCXd3d/Hwww+LcePG6fx+POjy5cvi5ZdfFjVq1BAeHh7iueeeE3/++WeZa0Zp982Sa+nB71VeXp6YOnWqqFOnjqhWrZp46qmnxI8//ljmOZXo+33XuXNnIYQQiYmJwsHBQev3jhBC/PPPP6JRo0aiQ4cOIi8vTwjx7/ft0KFDon379sLFxUXUq1dPzJo1SxQUFFTovWzcuLHo37+/zvnrep2y1yJKbVmu7znPnDkjBg0aJGrVqqX5PTFq1CjNTpBCCJGeni4mTZokmjZtKpycnETNmjXFE088IWbPnq21hTqRvVIJIUQl12JERGRDDh06hJ49e2Lbtm16N1og65KRkYGHHnoIQUFBWLNmjaWnYzN69OiBmzdv4s8//7T0VIjIynDpHRERkY1JS0vDggUL0LNnT9SqVQsXLlzA0qVLcefOHUyePNnS0yMiqhJYKBEREdkYFxcXnD9/HiEhIbh16xbc3Nzw1FNP4YMPPsCjjz5q6ekREVUJXHpHRERERERUioPhECIiIiIiIvvCQomIiIiIiKgUFkpERERERESlVPnNHIqLi3H16lV4eHhoussTEREREZH9EULgzp07qF+/vlaDbl2qfKF09epV+Pn5WXoaRERERERkJS5duoSGDRvqjanyhZKHhweA+2+Gp6enhWdDtqygoACJiYno06cPnJycLD0dsjO8/sjSeA2SJfH6I1PJysqCn5+fpkbQp8oXSiXL7Tw9PVkokVEKCgrg5uYGT09P/pIms+P1R5bGa5AsidcfmZrMR3K4mQMREREREVEpLJSIiIiIiIhKYaFERERERERUSpX/jJIMIQQKCwtRVFRk6amQBTg5OUGtVlt6GkRERERkRey+UMrPz8e1a9eQk5Nj6amQhahUKjRs2BDu7u6WngoRERERWQm7LpSKi4tx7tw5qNVq1K9fH87OzmxKa2eEEEhPT8fly5cREBDAO0tEREREBMDOC6X8/HwUFxfDz88Pbm5ulp4OWYiPjw/Onz+PgoICFkpEREREBICbOQAAHBz4Ntgz3kUkIiIiotJYIRAREREREZXCQomIiIiIiKgUFkpkVSIjI9GuXTtLT4OIiIiI7BwLJRs0atQoqFQqqFQqODk5oW7duujduzfWrVuH4uLicj3X+vXr4e3tXTkTrYBp06bhwIED5cpp0qQJ4uLiKmdCRERERGSXWCiZQFFxEQ79fQhbft6CQ38fQlFx5Teufe6553Dt2jWcP38e33zzDXr27InJkyfjhRdeQGFhYaWfv7K4u7ujVq1alp4GEREREdk5FkpG2nFiB5rMaIKe7/fE0LVD0fP9nmgyowl2nNhRqed1cXGBr68vGjRogMcffxyzZs3C7t278c0332D9+vWauNjYWLRu3RrVq1eHn58fQkJCkJ2dDQA4dOgQXn/9dWRmZmruUEVGRgIAPv30U7Rv3x4eHh7w9fXF0KFDcePGDb1zatKkCebNm4ehQ4fC3d0d9evXx4oVK7RiLl68iMDAQLi7u8PT0xODBw/G9evXNcdLL70bNWoUgoKC8P7776NevXqoVasWQkNDUVBQAADo0aMHLly4gClTpmheAwBcuHABL774ImrUqIHq1avj0Ucfxd69eyv6dhMRERFRBeTm52LCpgnou7QvJmyagNz8XEtPSRoLJSPsOLEDwauDcfn2Za3xK7evIHh1cKUXS6X16tULbdu2xY4d/57XwcEBy5cvx59//okNGzbgu+++w/Tp0wEAnTp1QlxcHDw9PXHt2jVcu3YN06ZNA3C/x9S8efPw+++/Y9euXTh37hxGjRplcA4xMTFo06YNTpw4gZkzZ2LKlClISkoCcL+5a1BQEG7duoXDhw8jKSkJqampeOWVV/Q+58GDB5GamoqDBw9iw4YNWL9+vaYY3LFjBxo2bIj33ntP8xoAIDQ0FHl5efj+++9x6tQpLF68GO7u7uV9S4mIiIiogoLig+AW6ob4Q/FIPJOI+EPxcAt1Q1B8kKWnJsWuG84ao6i4CJO3ToaAKHNMQEAFFcK2hiGwXSDUDuZrYvrwww/jjz/+0DwOCwvT/HfTpk0xb948jB8/HqtWrYKzszO8vLygUqng6+ur9TyjR4/W/HezZs2wfPlydOzYEdnZ2XoLjs6dO2PGjBkAgIceegg//PADli5dit69e+Pbb7/FH3/8gXPnzsHPzw8AsHHjRjz66KNITk5Ghw4ddD5njRo1sHLlSqjVajz88MPo378/Dhw4gLFjx6JmzZpQq9WaO18lLl68iJdffhmtW7fWvAYiIiIiMo+g+CDsPrlb57HdJ3cjKD4Iu0J3mXdS5cQ7ShV05OyRMneSHiQgcOn2JRw5e8SMs7p/1+bBBqoHDx5E79690aBBA3h4eGDEiBH4559/cPfuXb3P89tvvyEwMBCNGzeGh4cHevToAeB+AaLP008/XebxX3/9BQD466+/4OfnpymSAKBly5bw9vbWxOjy6KOPQq3+t9isV6+ewWWAkyZNwvz589G5c2fMmTNHq3gkIiIiosqTm5+rWCSV2H1yt9Uvw2OhVEHXMq6ZNM5U/vrrLzRt2hTA/c/p9OvXD61atcIXX3yBX3/9FfHx8QCg+YyPLnfv3kWfPn3g7u6OTz/9FMnJydi5cyeA+0vyyqukcCtdxJVQGi/h5ORU5vkM7e43ZswY/O9//8Pw4cNx6tQptG/fvsznpYiIiIjI9CK2RZg0zlJYKFVQPe96Jo0zhe+++w6nTp3Cyy+/DAD45ZdfUFhYiCVLluCpp57CQw89hKtXr2rlODs7o6hIe5e+//73v7h58yYWLVqErl274uGHHzZ4B6fETz/9VObxww8/DOD+3aOLFy/i0qVLmuNnzpxBZmYmHnnkkXK/Xn2vAQD8/Pzw1ltvYceOHZg6dSoSEhIqfA4iIiIiknP2xlmTxlkKC6UK6hrQFQ1rNIQKuu+EqKCCXw0/dA3oWinnz8vLQ1paGq5cuYITJ04gKioKgYGBeOGFFzBixAgAgL+/PwoLC7FixQr873//w8aNG/HBBx9oPU+TJk2QnZ2NAwcO4ObNm8jJyUGjRo3g7Oysyfvyyy8xb948qXn98MMPiI6Oxv/93/8hPj4e27Ztw+TJkwEAzz77LNq0aYNhw4bhxIkTOH78OEaMGIHu3bujffv2FX4vmjRpgu+//x5XrlzBzZs3Adz/bNb+/ftx7tw5nDhxAt99951RxRgRERERyQmoE2DSOEthoVRBagc1lr26DADKFEslj+Nejau0jRz27duHevXqoUmTJnjuuedw8OBBLF++HLt379Z8nqddu3aIjY3F4sWL0apVK2zatAkLFy7Uep5OnTrhrbfewiuvvAIfHx9ER0fDx8cH69evx7Zt29CyZUssWrQI77//vtS8pk6dil9//RWPPfYY5s2bhyVLlqBv374A7i+Z27VrF2rUqIFu3brh2WefRbNmzfDZZ58Z9V689957OH/+PPz9/eHj4wMAKCoqQmhoKB555BE899xzaNGiBVatWmXUeYiIiIjIsJhBMSaNsxSVEKLstm1VSFZWFry8vJCZmQlPT0+tY/fu3cO5c+fQtGlTVKtWrULPv+PEDkzeOllrYwe/Gn6IezUOAx8faNTcbU2TJk0QFhamtdOeLZC9DgoKCrB3717069evzOemiCobrz+yNF6DZEm8/myPvl3vACCwXaBFdr3TVxuUxu3BjTTw8YEIbBeII2eP4FrGNdTzroeuAV3NuiU4EREREVFlyL6XjeFrhyP1Zir8a/tj45iNcK9muDflrtBdisWSpYqk8mKhZAJqBzV6tOhh6WkQEREREZlMxwUdkXw+WfP41JVT8JjogQ5NOuD47OMG869mXC3XuLXhZ5TIZM6fP29zy+6IiIiIqKzSRdKDks8no+OCjpWabw1YKBERERERkUb2vWzFIqdE8vlkZN/LrpR8a8FCCfcbnpL94vefiIiI6F/D1w43Ks7YfGth14VSya4pOTk5Fp4JWVJ+fj4AaLZVJyIiIrJnqTdTjYozNt9a2PVmDmq1Gt7e3rhx4wYAwM3NDSqV7gayVDUVFxcjPT0dbm5ucHS06x8HIiIiIgCAf21/nLpySiquMvKthd3/Zejr6wsAmmKJ7I+DgwMaNWrEIpmIiIgIwMYxG+Ex0UMqrjLyrYXdF0oqlQr16tVDnTp1UFBQYOnpkAU4OzvDwcGuV6ESERERabhXc0eHJh30bsjQoUkHxX5KxuZbC7svlEqo1Wp+RoWIiIiIqpTDZw6jx9IemseHphxC95bdDeYdn31ccYtvmT5KxuZbAxZKRERERERVkGps2Y8VlBRNIsHwrr/6+iDJuHX3VrnGrQ3XGxERERERVTG6iiRzHm8+qzlS0xV2xUtPRfNZzfXmWwMWSkREREREVcjhM4eNivv1f79K5SvFZeZkKhZJJVLTU5GZkyl1HkthoUREREREVIU8+JmkisS1X9heKl8prv/y/lL5snGWwkKJiIiIiIhM5uKtiyaNsxQWSkREREREZDKNajYyaZylsFAiIiIiIqpCDk05ZFTcLzN/kcpXitszaY9UvmycpbBQIiIiIiKqQmT6JOmLe6LZE1L5SnFebl7w9/HXm+vv4w8vNy+p81gKCyUiIiIiIiu17+Q+qMaqNF/7Tu6TyjPUJ6myj6dEpSgWS/4+/kiJStGbbw2splBauHAhVCoVwsLCNGNCCERGRqJ+/fpwdXVFjx49cPr0actNkoiIiIjITFRjVXg+/nmtsefjnzfYw8hUIvpGlGu8tJSoFGQsy0Bn/87wq+GHzv6dkbEswyaKJMBKCqXk5GSsWbMGbdq00RqPjo5GbGwsVq5cieTkZPj6+qJ37964c+eOhWZKRERERFT5LN0wdvr26YjZH6PzWMz+GEzfPl1vfgkvNy8cnXEUF6Mv4uiMo1a/3O5BFi+UsrOzMWzYMCQkJKBGjRqacSEE4uLiMHv2bAwcOBCtWrXChg0bkJOTg82bN1twxkRERERElUd2eZ1S3KbvN0nlK8XlF+YjNjFWb25sYizyC/OlzmOrHC09gdDQUPTv3x/PPvss5s+frxk/d+4c0tLS0KdPH82Yi4sLunfvjmPHjmHcuHE6ny8vLw95eXmax1lZWQCAgoICFBQUVNKrIHtQcv3wOiJL4PVHlsZrkCzJ3q6/gR8OhKujq1Rc5vLMMuNjt4yVyh+7ZSwGPz24zPjqg6vhrHY2mL/6u9UI6RliMM6alOcaUgkh9H8SqxJt3boVCxYsQHJyMqpVq4YePXqgXbt2iIuLw7Fjx9C5c2dcuXIF9evX1+S8+eabuHDhAvbv36/zOSMjIzF37twy45s3b4abm1ulvRYiIiIiIrJuOTk5GDp0KDIzM+Hp6ak31mJ3lC5duoTJkycjMTER1apVU4xTqbTXTwohyow9aObMmQgPD9c8zsrKgp+fH/r06WPwzSDSp6CgAElJSejduzecnJwsPR2yM7z+yNJ4DZIl2dv15zVJ/nM8uu4oGZu/6uAqzNw502DuwgELbe6OUslqMxkWK5R+/fVX3LhxA0888e/+60VFRfj++++xcuVK/P333wCAtLQ01KtXTxNz48YN1K1bV/F5XVxc4OLiUmbcycnJLn6wqPLxWiJL4vVHlsZrkCzJXq6/HeN2lNntTpdvQr/R+X4kDEnAaxtfM5j/6fBPdeaP7zUeU7dPRZEoUsxVq9QY32s8nBxt6/tRnuvHYps5PPPMMzh16hROnjyp+Wrfvj2GDRuGkydPolmzZvD19UVSUpImJz8/H4cPH0anTp0sNW0iIiIiokr1XLvnjIob1m2YVL5SnLOjM8L7hOs8ViK8TzicHQ1/jsmWWeyOkoeHB1q1aqU1Vr16ddSqVUszHhYWhqioKAQEBCAgIABRUVFwc3PD0KFDLTFlIiIiIqJy2f7Tdgz6aJDm8bY3tiH4qWCDeSJB6N3CW6YhrDH50cHRAO7vbvfgnSW1So3wPuGa41WZxXe902f69OnIzc1FSEgIbt++jSeffBKJiYnw8PCw9NSIiIiIiPTSVagM+mgQ8JHhQsUaRAdHY37QfKw6uAqp6anw9/FHSM+QKn8nqYRVFUqHDh3SeqxSqRAZGYnIyEiLzIeIiIiIqCJkGr7qK5YsnV/C2dEZYb3DDMZVRRZvOEtEREREVJVs/2m7UXHGNoz98pcvpfJl4+wVCyUiIiIiIhN68DNJFYmT2bFOX1zgh4FS+bJx9oqFEhERERERUSkslIiIiIiIiEphoUREREREZELb3thmVNynwz+VyleK2z1ut1S+bJy9YqFERERERGRCMn2S9MUZ2zD2pfYvSeXLxtkrFkpERERERAoS9idANVal+UrYnyCVJ9MQ1pqPEwslIiIiIiKdVGNVeHP7m1pjb25/02CPImshEkSZ5XW7x+1mkSTJqhrOEhERERFZA0s3fDVVw9iX2r8E0Z6FUUXwjhIRERER0QNkl9cpxW34boNUvlLcj//3o1S+bBxVDAslIiIiIqIHlF5uV964UVtGSeUrxXWK6SSVLxtHFcNCiYiIiIiIqBQWSkRERERERKWwUCIiIiIiesCa4DVGxa0fsl4qXynuWMQxqXzZOKoYFkpERERERA8Y23esUXEje42UyleKe/qhp6XyZeOoYlgoERERERGVYumGr2wYa3kslIiIiIioytp5fCdUY1War53Hd0rnigSB5x96Xmvs+Yeely5SRIJAUOsgrbGg1kHlyj8y9YjW2JGpR1gkmQkbzhIRERFRlaSraevAhIFAgtwdGV353/zfN9LNXnXl7zq1Szp/x4kdmLx1stbYkHVDsOzVZRj4+ECD+WQc3lEiIiIioipHV5FiS8d3nNiB4NXBuHz7stb4ldtXELw6GDtO7NCbT8ZjoUREREREVYrs8jqluIU7F0rlK8Ut/WqpVL5SXFFxESZvnQyBsnedSsbCtoahqLhI6jxUMSyUiIiIiKhKGZggtyxNKW7W3llS+Upx4V+GS+UrxR05e6TMnaQHCQhcun0JR84eUYwh47FQIiIiIiKyItcyrpk0jiqGhRIRERERkRWp513PpHFUMSyUiIiIiKhK2TFWbqMDpbioflFS+UpxsS/FSuUrxXUN6IqGNRpCBd0bPqiggl8NP3QN6Cp1HqoYFkpEREREVKUM6DjAqLiZA2ZK5SvFTXlxilS+UpzaQY1lry4DgDLFUsnjuFfjoHZQS52HKoaFEhERERFZrZ3Hd8JrkhcAwGuSl/SOdob6FFn78YGPD8T28dvRoEYDrfGGNRpi+/jtZuujVFRchEN/H8KWn7fg0N+H7GqnPTacJSIiIiKrVNJryNXRVTNWnoaxliYSBJZ+tVRrd7vYl2Kl7zgNfHwgAtsF4sjZI7iWcQ31vOuha0BXs91JKml4++AOfA1rNLSbhrcslIiIiIjI6sg0bNVXLFk6v8SUF6dIF0a6qB3U6NGiR4XzK6qk4W3pXk4lDW/NeVfLUrj0joiIiIisirENY+dunyuVrxT34b4PpfJl42wNG97ex0KJiIiIiKyKsQ1jI/dHSuUrxb31xVtS+bJxtoYNb+9joURERERERBpseHsfCyUiIiIiItJgw9v7WCgRERERkVUxtmFsZN9IqXyluA9e/kAqXzbO1rDh7X0slIiIiIjIqhjbMHZO8BypfKW4cc+Nk8qXjbM1bHh7HwslIiIiIqo0kzdOhmqsSvM1eeNkqTxLN3w19ri1yC/MR1xSHCZunoi4pDjkF+ZL5VlLw1tLYh8lIiIiIqoUunoRLf9+OZZ/v9wmCg2RIPDhvg+1drf74OUPbOZO0vTt0xGbGIsi8e823tO2TUN4n3BEB0cbzLd0w1tLY6FERERERCZn6YavpmoYO+65cTZTGD1o+vbpiNkfU2a8SBRpxmWKJUs1vLUGXHpHRERERCYlu7xOKW7Jl0uk8pXiVuxZIZUvG2dr8gvzEZsYqzcmNjFWehmevWKhREREREQmtfz75UbFTftqmlS+UtykXZOk8mXjbM2qg6u0ltvpUiSKsOrgKjPNyDaxUCIiIiIiqkJS01NNGmevWCgREREREVUh/j7+Jo2zVyyUiIiIiMikJnWTXPqmEPf+i+9L5SvFLQ+SXPonGWdrQnqGQK3SvzOdWqVGSM8QM83INrFQIiIiIiKTWjZ8mVFxU1+aKpWvFDex/0SpfNk4W+Ps6IzwPuF6Y8L7hMPZ0dlMM7JNLJSIiIiISNGKPSu0GsbK7hRn6YavVaVhbG5+LiZsmoC+S/tiwqYJyM3PlcqLDo5GRN+IMneW1Co1IvpGSG0Nbu/YR4mIiIiIdNLVi2jSrkmYtGuSTRQaX4z/AqM+GoU7+Xc0Yx7OHlj/xnrLTaocguKDsPvkbs3jxDOJiD8Uj8B2gdgVustgfnRwNOYHzceqg6uQmp4Kfx9/hPQM4Z0kSbyjRERERERlyDRstebjO07sQPDqYK0iCQCy87MRvDoYO07s0JtvaaWLpAftPrkbQfFBUs/j7OiMsN5hWDF0BcJ6h7FIKgcWSkRERESkxdiGrVuObpHKV4p79/N3pfKV4oqKizB562QIlL3rVTIWtjUMRcX6ew1ZSm5+rmKRVGL3yd3Sy/CoYlgoEREREZEWYxu2Dt0wVCpfKW5+0nypfKW4I2eP4PLty4p5AgKXbl/CkbNHpM5jbhHbIkwaRxXDQomIiIiIqpRrGddMGmduZ2+cNWkcVQwLJSIiIiKqUup51zNpnLkF1AkwaRxVDAslIiIiItJibMPWzSM3S+Urxb3T+x2pfKW4rgFd0bBGQ6ige8MHFVTwq+GHrgFdpc5jbjGDYkwaRxXDQomIiIiItBjbsHVIlyFS+Upx8wbPk8pXilM7qLHs1fvNbEsXSyWP416Ng9pBXSbXGrg6uyKwXaDemMB2gXB1djXTjOwTCyUiIiKiKmzjoY1aDWM3HtoolWfphq/GHh/4+EBsH78dDWo00BpvWKMhto/fjoGPD9SbbyqZOZnosqgLGk1vhC6LuiAzJ1Mqb1foLsViSbaPEhmHDWeJiIiIqihdvYZGbBqBEZtG2ETD2MB2gTq3yTZ0t6XEwMcHIrBdII6cPYJrGddQz7seugZ0NdudpOazmiM1PVXz+NLtS/Ce7A1/H3+kRKUYzN8Vugu5+bmI2BaBszfOIqBOAGIGxfBOkpmwUCIiIiKqgmQatuorliydL9NwVeauitpBjR4tehiMM7XSRdKDUtNT0XxWc6liydXZFSuHrTT19EgCl94RERERVTGyy+uU4lZ/s1oqXykufm+8VL5SnK03XM3MyVQskkqkpqdKL8Mjy2ChRERERFTFjNg0wqi4kB0hUvlKcRN2TpDKV4qz9Yar/Zf3N2kcWQYLJSIiIiKyKrbecPXirYsmjSPLYKFERERERFbF1huuNqrZyKRxZBkslIiIiIiqmE+GfWJU3KqBq6TyleJWDpDbfEApztYbru6ZtMekcWQZLJSIiIiIqpjhPYYbFTf++fFS+Upxof1CpfKV4my94aqXmxf8ffz1xvj7+MPLzctMM6KKYKFEREREZMVW7Fmh1TB2xZ4VUnmWbvhq7HFrabiafS8bA1YOQJvINhiwcgCy72VL5aVEpSgWS7J9lMiy2EeJiIiIyErp6kU0adckTNo1ySYaxkb0jUDM/rLL4yL6yu1WV9Jwdca2GQCAsV3GYtGgRWa7k9RxQUckn0/WPD515RQ8JnqgQ5MOOD77uMH8lKgUZOZkov/y/rh46yIa1WyEPZP28E6SjeAdJSIiIiIrJNOw1ZqPT98+XWeRBAAx+2Mwfft0vfklXJ1d8f7g9wEA7w9+32JF0oOSzyej44KOUs/j5eaFozOO4mL0RRydcZRFkg1hoURERERkZWSX1ynFvb3lbal8pThj8/ML8xGbGKs3NzYxFvmF+VLnMbfse9mKRVKJ5PPJ0svwyDaxUCIiIiKyMpN2TTIqLvq7aKl8pThj81cdXIUiUaQ3t0gUYdVBud31zG34WsnNMCTjyDaxUCIiIiIik0pNTzVpnLml3pScv2Qc2SYWSkRERERkUoa2xi5vnLn515acv2Qc2SYWSkRERERWZnnQcqPipveS2yhBKc7Y/JCeIVCr1Hpz1So1QnqGSJ3H3DaO2WjSOLJNLJSIiIiIrMzE/hONils8ZLFUvlKcsfnOjs4I7xOuNze8TzicHZ2lzmNu7tXc0aFJB70xHZp0gHs1dzPNiCyBhRIRERFRJdp5fKdWw9idx3dK5Vm64auxx6ODoxHRN6LMnSW1So2IvhGIDpbbMMJYmTmZ6LKoCxpNb4Qui7ogMydTKu/47OOKxZJsHyWybWw4S0RERFRJdPUaGpgwEEgwXGhYA2MbxkYHR2N+0HysOrgKqemp8PfxR0jPELPdSWo+q7nWhhGXbl+C92Rv+Pv4IyUqxWD+8dnHkX0vG8PXDkfqzVT41/bHxjEbeSfJTrBQIiIiIqoEMg1b9RVLls431DAWgNRdIWdHZ4T1DjMYZ2qli6QHpaanovms5lLFkns1d+ycIHcXkKoWLr0jIiIiMjHZ5XVKcR9/+7FUvlJcwv4EqXylOFtvGJuZk2lw6/HU9FTpZXhkn1goEREREZnYwISBRsWN/my0VL5S3Jvb35TKV4qz9Yax/Zf3N2kc2ScWSkRERESkxdYbxl68ddGkcWSfWCgRERERkRZbbxjbqGYjk8aRfWKhRERERGRiO8buMCpu3SvrpPKV4tYEr5HKV4qz9YaxeybtMWkc2ScWSkREREQmNqDjAKPiXn/2dal8pbixfcdK5SvF2XrDWC83L4N3u/x9/OHl5mWmGZEtYqFEREREpMeKPSu0Gsau2LNCKs/SDV+rSsPY3PxcTPt8GgBg2ufTkJufK5WXEpWiWCzJ9lEi+8ZCiYiIiEiBaqwKk3ZN0hqbtGuSwR5F1kIkiDLL69YEr5FudhsdHI2cVTlYOngpJvScgKWDlyJnVY7ZiqSg+CC4hboh4ej9bcwTjibALdQNQfFBUvkpUSnIWJaBzv6d4VfDD539OyNjWQaLJJJi0UJp9erVaNOmDTw9PeHp6Ymnn34a33zzjea4EAKRkZGoX78+XF1d0aNHD5w+fdqCMyYiIiJ7IdOw1ZqPlxjbdyxEgtB8yS7LK1HSMHbF0BUI6x1mtuV2QfFB2H1yt85ju0/uli6WvNy8cHTGUVyMvoijM45yuR1Js2ih1LBhQyxatAi//PILfvnlF/Tq1QuBgYGaYig6OhqxsbFYuXIlkpOT4evri969e+POnTuWnDYRERFVcbLL65TiPtz3oVS+UtzCnQul8mXjbE1ufq5ikVRi98nd0svwiCpCJYSQu/dqJjVr1kRMTAxGjx6N+vXrIywsDG+//TYAIC8vD3Xr1sXixYsxbtw4nfl5eXnIy8vTPM7KyoKfnx9u3rwJT09Ps7wGqpoKCgqQlJSE3r17w8nJydLTITvD648szd6uQa9J8ncdMpdnWl2+rZv2+TTNcjsAcFW7Yl3vdRidNBq5Rf8WR2O7jMX7g9+3xBTJRmVlZaF27drIzMw0WBtYTaFUVFSEbdu2YeTIkfjtt99QrVo1+Pv748SJE3jsscc0cYGBgfD29saGDRt0Pk9kZCTmzp1bZnzz5s1wc3OrtPkTEREREZF1y8nJwdChQ6UKJUczzUnRqVOn8PTTT+PevXtwd3fHzp070bJlSxw7dgwAULduXa34unXr4sKFC4rPN3PmTISH/7udZckdpT59+vCOEhnF3v41lawLrz+yNHu7Bi19R4h3lHhHiSpHVlaWdKzFC6UWLVrg5MmTyMjIwBdffIGRI0fi8OHDmuMqlfYHFYUQZcYe5OLiAhcXlzLjTk5OdvGLnSofryWyJF5/ZGn2cg0ufmFxmd3udFketFzn+7E0cCne+uItg/kfvPyBzvx3+7yLWXtnGcyP6hdVJb8fiwYtwvJDy8uM5xblIrcwVyuuKr5+qjzluV4svj24s7Mzmjdvjvbt22PhwoVo27Ytli1bBl9fXwBAWlqaVvyNGzfK3GUiIiIiMqWJ/ScaFTfuOd2fpZaNmzlgplS+bJytcXV2RWC7QL0xge0C4ersaqYZkT2yeKFUmhACeXl5aNq0KXx9fZGUlKQ5lp+fj8OHD6NTp04WnCERERHZA0s3fDX2uK3bFbpLsVgKbBeIXaG7zDshsjsWLZRmzZqFI0eO4Pz58zh16hRmz56NQ4cOYdiwYVCpVAgLC0NUVBR27tyJP//8E6NGjYKbmxuGDh1qyWkTERGRDdnw3Qaoxqo0Xxu+070hlC4iQeCFR17QGnvhkRekixSRIPD8Q89rjT3/0PPlyv9Pn/9ojf2nz39sqkjKzc/FhE0T0HdpX0zYNKFcW3rvCt2FnPgcjO1yv/fT2C5jkROfwyKJzMKiu9698cYbOHDgAK5duwYvLy+0adMGb7/9Nnr37g3g/t2luXPn4sMPP8Tt27fx5JNPIj4+Hq1atZI+R1ZWFry8vKR2tiDSp6CgAHv37kW/fv24HprMjtcfWZqtXoP6mrLKFBuWzu+4oCOSzyeXGe/QpAOOzz5uMN/SlJrGlveOkK1ef2R9ylMbWPSO0kcffYTz588jLy8PN27cwLfffqspkoD7GzlERkbi2rVruHfvHg4fPlyuIomIiIjsl74ixRaOKxVJAJB8PhkdF3TUm29pSkUScL9ZbFB8kHknRFROVvcZJSIiIiJjyS6vU4qL3xsvla8Ut3jXYql8pbjse9mKRVKJ5PPJyL6XLXUec8vNz1UskkrsPrm7XMvwiMyNhRIRERFVOaO2jDIqbsLOCVL5SnEz9syQyleKG752uFS+bJy5RWyLMGkckSWwUCIiIiKyMqk3U00aZ25nb5w1aRyRJbBQIiIiIrIy/rX9TRpnbgF1AkwaR2QJLJSIiIioylk/ZL1RcSsHrJTKV4pb1H+RVL5S3MYxG6XyZePMLWZQjEnjiCyBhRIRERFVOSN7jTQqLrRfqFS+UtzbQW9L5SvFuVdzR4cmHfTmdmjSAe7V3KXOY26uzq6KzWJLBLYLhKuzq5lmRFR+LJSIiIjIqr37+btaDWPf/fxdqTxDfYqs/fjx2ccViyVz9lG6cusKak6uCadxTqg5uSau3LoilbcrdJdisVTePkpEluBo6QkQERERKdHVa2h+0nzMT5ov1bDV0jo06aDYMFbG8dnHkX0vG8PXDkfqzVT41/bHxjEbzXYnyWW8C/IL8zWPb+fcRsO3G8LZ0Rl5q/MM5u8K3YXc/FxEbIvA2RtnEVAnADGDYngniWwCCyUiIiKySjINW/UVS5bOl2kYK3NXyL2aO3ZO2GkwztRKF0kPyi/Mh8t4F6liydXZFSuHyX3mi8iacOkdERERWR3Z5XVKcdt/2i6VrxS3cOdCqXylOFtvGHvl1hXFIqlEfmG+9DI8IlvEQomIiIiszvyk+UbFDfpokFS+UtysvbOk8pXibL1hbOu5rU0aR2SLWCgRERERmZitN4y9c++OSeOIbBELJSIiIiITs/WGsR7VPEwaR2SLWCgRERGR1Xmn9ztGxW17Y5tUvlJcVL8oqXylOFtvGHtqzimTxhHZIhZKREREZHXmDZ5nVFzwU8FS+UpxMwfMlMpXirP1hrENajaAs6Oz3hhnR2c0qNnATDMiMj8WSkRERFSp4vfGazWMjd8bL5Vn6YavVaVh7MWbF+ExwQPqN9XwmOCBizcvSuXlrc5TLJZk+ygR2TL2USIiIqJKo6sX0YSdEzBh5wQ2jDUDp3FOKCwu1DzOzstG45mN4ejgiIIPCwzm563Ow5VbV9B6bmvcuXcHHtU8cGrOKd5JIrvAQomIiIgqhaUbvtp7w9jSRdKDCosL4TTOSapYalCzAW4tu2Xq6RFZPS69IyIiIpOTXV6nFJewP0EqXynO2Hxbbxh78eZFxSKpRGFxofQyPCJ7xEKJiIiITG7CzglGxb25/U2pfKU4Y/NtvWHso5GPmjSOyB6xUCIiIiIqxdYbxubk55g0jsgesVAiIiIiKsXWG8a6ObuZNI7IHrFQIiIiIpNbOWClUXFrgtdI5SvFGZtv6w1jT0eeNmkckT1ioUREREQmF9ov1Ki4sX3HSuUrxRmbb+sNYxvVbgRHB/2bGzs6OKJR7UZmmhGR7WGhRERERHp9lPgRvCZ5AQC8Jnnho8SPpPIs3fC1qjSMPXfjHFxDXOEw1gGuIa44d+OcVF7BhwWKxZJsHyUie8Y+SkRERKSopBeRq6OrZmzMtjEYs22MTTSMretZF9ezruscl2HphrHqN9UoFsWax/cK7qHZ7GZwUDmgaE2RwfyCDwtw8eZFPBr5KHLyc+Dm7IbTkad5J4lIAgslIiIi0snSDV+Nzfed6quzSAKA61nX4TvVF2lL0vSeA7Bcw9jSRdKDikUx1G+qpYqlRrUb4c7KO6aeHlGVx6V3REREVIbs8jqluI2HJDdDUIibs22OVL5S3K3sW4pFUonrWddxK/uW1HnM7dyNc4pFUoliUSy9DI+Iyo+FEhEREZUxZtsYo+JGbBohla8U917ie1L5SnHdY7pL5cvGmVvLyJYmjSOi8mOhRERERFXO1cyrJo0zt7yCPJPGEVH5sVAiIiKiKqe+V32Txpmbi5OLSeOIqPxYKBEREVEZawetNSruk2GfSOUrxf2nz3+k8pXiDkcclsqXjTO3M5FnTBpHROXHQomIiIjKeKPPG0bFDe8xXCpfKW7uoLlS+UpxNd1rGtwCvK5nXdR0ryl1HnNrWqcpHFT6/0xzUDmgaZ2mZpoRkf1hoURERFTFbfhuA1RjVZqvDd9tkMqzdMNXY4+nLUlTLJbqetaV2hrcFFLSUuD8ljNUY1VwfssZKWkpUnlFa4oUiyXZPkpEVHEslIiIiKow1VgVRm0ZpTU2assogz2KrEWHJh3KNV5a2pI0/LP0H7Sq3wo1q9dEq/qt8M/Sf8xWJDmMdUDAuwEoKCoAABQUFSDg3QA4jJX7E6xoTRH+t+B/qOZUDSqoUM2pGv634H8skojMgA1niYiIqihLN3w1Nr/jgo5IPp+s81jy+WR0XNARx2cf13sO4P4yvFNzTxmMMzWHsQ4Q0P36BAQcxjqgOEF/ryTg/jK83FW5pp4eERnAO0pERERVkOzyOqW4ZV8vk8pXipv92WypfKW47HvZikVSieTzyci+ly11HnNLSUtRLJJKCAjpZXhEZH4slIiIiKqg0svtyhsXtjtMKl8pLurbKKl8pbjhayU3g5CMMzc2jCWyfSyUiIiIyOqk3kw1aZy5lXwmyVRxRGR+LJSIiIjI6vjX9jdpnLk5qZ1MGkdE5sdCiYiIqApaP2S9UXFxgXFS+Upxs56dJZWvFLdxzEapfNk4c2PDWCLbx0KJiIioChrZa6RRcZNfmCyVrxS34JUFUvlKce7V3A1uAd6hSQe4V3OXOo+5NfdtDhUM7PoHFZr7NjfTjIiovFgoERERWbmPv/1Yq2Hsx99+LJVn6Yavxh4/Pvu43j5KMluDm8KZy2egflMN1VgV1G+qceay3F2g4oRixWJJBZXU1uBEZDnso0RERGTFdPUiGv3ZaIz+bLTBQsMa1PWsi+tZ13WOyzg++ziy72Vj+NrhSL2ZCv/a/tg4ZqPZ7iSVfv+LRTEenfsoAMOFHnC/WEpJS0HLyJYoKCqAk9oJZyLP8E4SkQ1goURERGSlLN3w1dh836m+OoskALiedR2+U32RtiRN7zmA+8vwdk7YaTDO1Ix9/SWa+zZH/gf5ppoWEZkJl94RERFZIdnldUpxW45ukcpXiluwQ/IzRgpxt7JvKRZJJa5nXcet7FtS5zE32eV1snFEZHtYKBEREVmh0Z+NNipu6IahUvlKce98845UvlJc95juUvmycebW+r3WJo0jItvDQomIiIhM7mrmVZPGmVuxkNtoQTaOiGwPCyUiIiIyufpe9U0aZ24OKrk/kWTjiMj2VPinOzU1Fe+88w6GDBmCGzduAAD27duH06dPm2xyRERE9mrdK+uMits8crNUvlLc/OfnS+UrxR2OOCyVLxtnbqf+c8qkcURkeypUKB0+fBitW7fGzz//jB07diA7OxsA8Mcff2DOnDkmnSAREZE9ev3Z142KG9JliFS+UtzsgbOl8pXiarrXNLgFeF3PuqjpXlPqPObWsmFLk8YRke2pUKE0Y8YMzJ8/H0lJSXB2dtaM9+zZEz/++KPJJkdERFQVrP5mtVbD2NXfrJbKs3TDV2OPpy1JUyyW6nrWldoa3BSu3LqCmpNrwmmcE2pOrokrt65I5Rn7+onItlWoj9KpU6eweXPZW/U+Pj74559/jJ4UERFRVaGrF0/IjhCE7Aixiz+005ak4Vb2LXSP6Y6rmVdR36s+DkccNtudJJfxLsgv/LeH0e2c22j4dkM4Ozojb3WewXyRIHDm8hm0fq81ikUxHFQOOPWfU7yTRGQHKlQoeXt749q1a2jatKnW+G+//YYGDRqYZGJERES2ztINXy2dX6Kme02cmmv+z/KULpIelF+YD5fxLlLFUsuGLVG0psjU0yMiK1ehpXdDhw7F22+/jbS0NKhUKhQXF+OHH37AtGnTMGLECFPPkYiIyObILq9TijM2f+HOhVL5SnF/X/1bKl82ztyu3LqiWCSVyC/Ml16GR0T2p0KF0oIFC9CoUSM0aNAA2dnZaNmyJbp164ZOnTrhnXfkGtQRERFVZSE7QoyKMzZ/1t5ZUvlKcY/OfVQqXzbO3FrPlWwYKxlHRPanQkvvnJycsGnTJsybNw8nTpxAcXExHnvsMQQEBJh6fkRERGQBRcVyS81k48ztzr07Jo0jIvtToUKpRLNmzdCsWTNTzYWIiIishNpBLVUEqR3UZphN+XlU88DtnNtScUREulRo6V1wcDAWLVpUZjwmJgaDBg0yelJERES2btXAVUbFGZsf1S9KKl8p7vQcuQbysnHmdmqOZMNYyTgisj8Vbjjbv3//MuPPPfccvv/+e6MnRUREZOvGPz/eqDhj82cOmCmVrxTXon4LqXzZOHNrULMBnB2d9cY4OzqjQU3u1ktEulWoUMrOztZqNFvCyckJWVlZRk+KiIjImsTvjddqGBu/N14qz9INXy193FSy72VjwMoBaBPZBgNWDkD2vWypvLzVeYrFkmwfJSKyXxUqlFq1aoXPPvuszPjWrVvRsiUbsBERUdWhGqvChJ0TtMYm7JxgsMeQtfD38S/XeGkiQeC/c/+r+SyS2kGN/879r9mKpI4LOsJjogd2/b4Lp66cwq7fd8Fjogc6LugolZ+3Og+XF19GDbcacHRwRA23Gri8+DKLJCIyqEKbObz77rt4+eWXkZqail69egEADhw4gC1btmDbtm0mnSAREZGlWLphq7H5zWc1R2p6qs5jqempaD6rOVKiUvSeA7i/vO5W3C3s3bsXt+JuwcnJyWCOKXRc0BHJ55N1Hks+n4yOCzri+OzjBp+nQc0GuLXslqmnR0RVXIXuKL300kvYtWsXUlJSEBISgqlTp+Ly5cv49ttvERQUZOIpEhERmZ/s8jqluI+//VgqXylu6VdLpfKV4jJzMhWLpBKp6anIzMmUOo+5Zd/LViySSiSfT5ZehkdEVF4VKpQAoH///vjhhx9w9+5d3Lx5E9999x26d+9uyrkRERFZTOnlduWNG/3ZaKl8pbjwL8Ol8pXi+i8vu+mSMXHmNnztcJPGERGVl1F9lPLz83Hjxg0UFxdrjTdq1MioSREREZFxLt66aNI4c0u9qf9uWHnjiIjKq0KF0tmzZzF69GgcO3ZMa1wIAZVKhaIi6+zSTUREZC8a1WyES7cvScVZI//a/jh1xXCPI//acptSEBGVV4WW3o0aNQoODg74+uuv8euvv+LEiRM4ceIEfvvtN5w4ccLUcyQiIjK7lQNWGhW37pV1UvlKcbEvxUrlK8XtmbRHKl82ztw2jtlo0jgiovKqUKF08uRJfPjhh3j++efRrl07tG3bVuuLiIjI1oX2CzUq7vVnX5fKV4qb8uIUqXylOC83L4NbgPv7+MPLzUvqPObmXs0dHZp00BvToUkHuFdzN9OMiMjeVKhQatmyJW7evGnquRAREVkVSzdsNfZ4SlSK3j5KMluDW9Lx2ccVi6UOTTpIbQ1ORFRRFSqUFi9ejOnTp+PQoUP4559/kJWVpfVFRERkTZZ8uQSqsSrN15Ivl0jnigSBAW0GaI0NaDNAuuGqSBAY0XGE1tiIjiPKlb+o/yKtsUX9F0nnp0SlIGNZBjr7d4ZfDT909u+MjGUZVl8klTg++zjurLiDoLZBaN2gNYLaBuHOijsskoio0qmEEOVure3gcL++Uqm0G+FZ42YOWVlZ8PLyQmZmJjw9PS09HbJhBQUF2Lt3L/r162e2ZotEJXj9VZy+pq0yxYal84Pig7D75O4y44HtArErdJfBfFPhNUiWxOuPTKU8tUGFdr07ePBghSZGRERkTvqKlJLj+ooVS+crFUkAsPvkbgTFB5m1WCIisicVKpTYWJaIiKyd7PK6JV8uwdSXppYZ/yjxI6n8jxI/wht93igzvvGQ5K5thzZieI+yTVNz83MVi6QSu0/uRm5+LlydXaXORURE8ir0GSUAOHLkCF577TV06tQJV65cAQBs3LgRR48eNdnkiIiIKmraV9OMihuzbYxUvlLciE0jdI7LxkVsi5DKl40jIqLyqVCh9MUXX6Bv375wdXXFiRMnkJeXBwC4c+cOoqKiTDpBIiIie3T2xlmTxhERUflUqFCaP38+PvjgAyQkJGh9oK5Tp05sOEtERGQCAXUCTBpHRETlU6FC6e+//0a3bt3KjHt6eiIjI8PYORERERnt/RffNypu7aC1UvlKcZ8M+0QqXykuZlCMVL5sHBERlU+FCqV69eohJaVs/4WjR4+iWbNmRk+KiIjIWLo2aChPnK4NGsoTp2uDhvLEuTq7IrBdoN7cwHaB3MiBiKiSVKhQGjduHCZPnoyff/4ZKpUKV69exaZNmzBt2jSEhISYeo5ERGTnpnw6Rath7JRPp0jlGepTZO3Hd4XuUiyWzNlHKb8wH6sOrgIArDq4CvmF+WY5LxGRJVWoUJo+fTqCgoLQs2dPZGdno1u3bhgzZgzGjRuHCRMmSD/PwoUL0aFDB3h4eKBOnToICgrC33//rRUjhEBkZCTq168PV1dX9OjRA6dPn67ItImIyAapxqoQdzhOayzucJzBHkXWwtnRuVzjpe0K3YWc+ByE9ghFn5Z9ENojFDnxOWYrkqZvnw63EDfM3DkTADBz50y4hbhh+vbpZjk/EZGlVHh78AULFuDmzZs4fvw4fvrpJ6Snp2PevHnleo7Dhw8jNDQUP/30E5KSklBYWIg+ffrg7t27mpjo6GjExsZi5cqVSE5Ohq+vL3r37o07d+5UdOpERGQjZBq2WvNxl/Euindf8gvz4TLeRW9+CVdnV6wcthL7p+zHymErzbbcbvr26YjZH4MiUaQ1XiSKELM/hsUSEVVpFS6UAMDNzQ3t27dHx44d4e7uXu78ffv2YdSoUXj00UfRtm1bfPzxx7h48SJ+/fVXAPfvJsXFxWH27NkYOHAgWrVqhQ0bNiAnJwebN282ZupERGTlZJfXKcV9/O3HUvlKcQt3LpTKV4q7cuuKwSVq+YX5uHLritR5zC2/MB+xibF6Y2ITY7kMj4iqLEfZwIEDB2L9+vXw9PTEwIED9cbu2LGjQpPJzMwEANSsWRMAcO7cOaSlpaFPnz6aGBcXF3Tv3h3Hjh3DuHHjyjxHXl6epq8TAGRlZQEACgoKUFBQUKF5EQHQXD+8jsgS7PH6+/CHD+HqaPjOyYc/fIjoV6LLjId+ESqVH/pFKF7r/lqZ8XmJ86Ty5yXOw7QXyjat7TC/g1R+h/kdcGHxBYNx5rb64Go4q/9dHuiqdtX6X03cd6sR0pOfT6bKZY+/A6lylOcaUgkh9H+S9P97/fXXsXz5cnh4eOD111/XG/vxx3L/ivcgIQQCAwNx+/ZtHDlyBABw7NgxdO7cGVeuXEH9+vU1sW+++SYuXLiA/fv3l3meyMhIzJ07t8z45s2b4ebmVu55ERERERFR1ZCTk4OhQ4ciMzMTnp6eemOl7yiVFD8lmyv4+PiYtPCYMGEC/vjjDxw9erTMMZVKew24EKLMWImZM2ciPDxc8zgrKwt+fn7o06ePwTeDSJ+CggIkJSWhd+/eWo2WiczBHq8/r0le0rGZyzOtLr/x242RkZthMNfb1dsq7yitOrhKs4EDcP9O0rre6zA6aTRyi3I14wsHLOQdJap09vg7kCpHyWozGdKFUgkhBAICAnD69GkEBJimG/jEiRPx5Zdf4vvvv0fDhg01476+vgCAtLQ01KtXTzN+48YN1K1bV+dzubi4wMWl7IdjnZyc+INFJsFriSzJnq6/cZ3HldntTpew7mE635P4l+Mx+rPRBvPXvbJOZ/67fd7FrL2zDOZH9YvSmZ/8TjIavt1QR4a2s++ctcrv6fhe4zF1+9QyGznkFuUit/B+oaRWqTG+13g4OVrf/KlqsqffgVQ5ynP9lHszBwcHBwQEBOCff/4pb2oZQghMmDABO3bswHfffYemTZtqHW/atCl8fX2RlJSkGcvPz8fhw4fRqVMno89PRETWa+lrS42Ke/1Z/cvEDcXNHDBT57hsXIOaDQxuAe7s6IwGNRtIncfcnB2dEd4nXG9MeJ9w6W3OiYhsTYV2vYuOjkZERAT+/PNPo04eGhqKTz/9FJs3b4aHhwfS0tKQlpaG3Nz7/1KlUqkQFhaGqKgo7Ny5E3/++SdGjRoFNzc3DB061KhzExGR+YRuCNVqGBu6IVQqz9INX409nrc6T28fpbzVeTqPmVpRcREO/X0IW37egkN/H0JRcZHhJADRwdGI6BsBtUqtNa5WqRHRNwLRwWU30SAiqirKvfQOAF577TXk5OSgbdu2cHZ2hqur9g44t27dknqe1atXAwB69OihNf7xxx9j1KhRAO43t83NzUVISAhu376NJ598EomJifDw8KjI1ImIyMx09RpadXQVVh1dZbDQsAZerl7IzNXxGSZXuc8w5a3Ow5VbV9B6bmvcuXcHHtU8cGrOKbPdSdpxYgcmb52My7cva8Ya1miIZa8uw8DH9e9iC9wvluYHzcfq71YDufc/kzS+13jeSSKiKk9617sHbdiwQe/xkSNHVnhCppaVlQUvLy+pnS2I9CkoKMDevXvRr18/ro8ms7PV689QQ1ZA/10ZS+d7T/LWWSSV8HL1QsbyDIPnsJQdJ3YgeHUwBLRfowr335ft47dLFUuA7V6DVDXw+iNTKU9tUKE7StZUCBERkXWSXV4XuiEU8SPjy4xv+E7/P8o9GDeyV9n/XypPw1ldn1NKz0rXWyQBQGZuJtKz0uHj6SN1LnMqKi7C5K2TyxRJACAgoIIKYVvDENguEGoHtY5nICKybxX6jBIApKam4p133sGQIUNw48YNAMC+fftw+vRpk02OiIhs16qjq4yKG7VllFS+UpzMjnf64jpGdZTKl40ztyNnj2gttytNQODS7Us4cvaIGWdFRGQ7KlQoHT58GK1bt8bPP/+MHTt2IDs7GwDwxx9/YM6cOSadIBERkSWkZ6ebNM7crmVcM2kcEZG9qVChNGPGDMyfPx9JSUlwdv73w5w9e/bEjz/+aLLJERERWYqPu9xyOtk4c6vnXc9wUDniiIjsTYUKpVOnTmHAgAFlxn18fEzSX4mIiGxfSJcQo+LWD1kvla8Ut+6VdVL5SnHHZx2XypeNM7euAV3RsEZDzcYNpamggl8NP3QN6GrmmRER2YYKFUre3t64dq3srfrffvsNDRpYZ+M8IiIyL10bNJQnTtcGDeWJM7bhrI+nj8EtwL1cvaxyIwcAUDuosezVZQBQplgqeRz3ahw3ciAiUlChQmno0KF4++23kZaWBpVKheLiYvzwww+YNm0aRowYYeo5EhGRBc3cOlOrWezMrTOlcy3d8NXY4xnLMxSLJXNuDV7RhrEDHx+I7eO3o0EN7X/EbFijYbm2BiciskcV2h58wYIFGDVqFBo0aAAhBFq2bImioiIMHToU77zzjqnnSEREFqKrD9GiA4uw6MAim2gWC9y/e6Jri2ylJWmlZSzPQHpWOjpGdUR6djp83H1wfNZxs91JMrZh7MDHByKwXSCOnD2CaxnXUM+7HroGdOWdJCIiAypUKDk5OWHTpk1477338Ntvv6G4uBiPPfYYAgICTD0/IiKyEEPNWlVjVQaLJWOfw9h8h7EOOosk4P722A5jHVCcUKz3HMD9ZXjnFp0zGGdqSg1jr9y+guDVwdJ3hdQOavRo0aOSZklEVDVVuI8SAPj7++Pll1/GoEGDWCQREVUhssvr9MXN2SbXLkIp7vCZw1L5SnEpaSmKRVIJAYGUtBSp85iboYaxABC2NUx6GR4REZVPhQuljz76CK1atUK1atVQrVo1tGrVCmvXrjXl3IiIyEIWHVhkdNx7ie9JPYdSXI+lPaTyleJaRraUypeNMzc2jCUisqwKLb179913sXTpUkycOBFPP/00AODHH3/ElClTcP78ecyfP9+kkyQiIiqvgqICk8aZGxvGEhFZVoUKpdWrVyMhIQFDhgzRjL300kto06YNJk6cyEKJiIgszkntJFUEOamdzDCb8mPDWCIiy6rQ0ruioiK0b9++zPgTTzyBwsJCoydFRESWNeOZGUbH/afPf6SeQynu0JRDUvlKcWciz0jly8aZGxvGEhFZVoUKpddeew2rV68uM75mzRoMGzbM6EkREZFlLXx1odFxcwfNlXoOpbjuLbtL5SvFNfdtbnALcBVUaO7bXOo85saGsURElmX0Zg5jxozBmDFj0KpVKyQkJMDBwQHh4eGaLyIisqw52+ZoNYyV3Y3O2GatpngOY48XJxTrvSMjszW4JbFhLBGR5VToM0p//vknHn/8cQBAamoqAMDHxwc+Pj74888/NXEqlVwzPyIiqhy6+hC9l/ge3kt8z2Yaxnq5eiEzN1PnuIzihGKkpKWgZWRLFBQVwEnthDORZ6z2TlJpbBhLRGQZFSqUDh48aOp5EBGRiVm62aspnsN7krfOIgkAMnMz4T3JGxnLM/SeA7i/DC//g3yDcdaKDWOJiMyvQkvvrl+/rnjsjz/+qPBkiIjINIxt9hq/N14qX1/cZ8c+k3oOpbj0rHTFIqlEZm4m0rPSpc5DRERUHhUqlFq3bo0vv/yyzPj777+PJ5980uhJERGRcYxt9jph5wSpfH1xr378qtRzKMV1jOoolS8bR0REVB4VKpTefvttvPLKK3jrrbeQm5uLK1euoFevXoiJicFnn8n9CyIREZE+6dlyd4pk44iIiMqjQoXS1KlT8dNPP+GHH35AmzZt0KZNG7i6uuKPP/7ASy+9ZOo5EhGRHfJx9zFpHBERUXlUeHvwZs2a4dFHH8X58+eRlZWFwYMHo27duqacGxERVZCxzV5XDlgpla8vbuvrW6WeQynu+KzjUvmycUREROVRoUKp5E5SSkoK/vjjD6xevRoTJ07E4MGDcfv2bVPPkYiIysnYZq+h/UKl8vXFvdLpFannUIrz8fQxuAW4l6sXfDx5R4mIiEyvQoVSr1698Morr+DHH3/EI488gjFjxuC3337D5cuX0bp1a1PPkYjIri3cuRBek+4XDF6TvLBw50KpPEs3ezXFc2Qsz1AslrxcvaS2BiciIqqICvVRSkxMRPfu3bXG/P39cfToUSxYsMAkEyMion/7ELk6umrGZu2dhVl7Z9lMw1g3Zzfk5OfoHJeRsTwD6Vnp6BjVEenZ6fBx98HxWcd5J4mIiCpVue4o9evXD5mZmZoiacGCBcjIyNAcv337NrZs2WLSCRIR2SuZZq3WfBwAqodW11kkAUBOfg6qh1Y3+BzA/WV45xadQ/bKbJxbdI5FEhERVbpyFUr79+9HXl6e5vHixYtx69YtzePCwkL8/fffppsdEZGdkl1epxQ3d7vkZ5QU4vad3CeVry8uLSNNsUgqkZOfg7SMNKlzERERmVO5CiUhhN7HRERkGrP2zjIqLnJ/pFS+Utzz8c9L5euLazevndRzyMYRERGZU4W3ByciItInIyfDpHFERETmVK5CSaVSQaVSlRkjIiIqzdvN26RxRERE5lSuXe+EEBg1ahRcXFwAAPfu3cNbb72F6tXvfxj3wc8vERFRxUX1i5JafhfVL0rneGTfSKnld5F9dcd8E/qN1PK7b0K/UTx28t2TqBdRz+BznHz3pMEYIiIicyvXHaWRI0eiTp068PLygpeXF1577TXUr19f87hOnToYMWJEZc2ViMhuzBww06i4OcFzpPKV4p5r95xUvr44X29fg1uAuzm7wdfbV+pcRERE5lSuO0off/xxZc2DiKjKWvrVUoR/Ga55HPtSLKa8OMVgnkgQerfglmnmasl8ALgbf1dxi3A3Zzfcjb9r8DlMIfteNoavHY7Um6nwr+2PjWM2wr2au1nOTUREtqlCDWeJiEiOrkIj/MtwhH8ZbhMNY71cvZCZm6lzXNbd+LtIy0hDu3ntkJGTAW83b5x896TZ7iR1XNARyeeTNY9PXTkFj4ke6NCkA47PPm6WORARke3hrndERJXE0g1fjT3uPclbZ5EEAJm5mfCe5K03/0G+3r5IW5KGe6vvIW1JmsWKpAcln09GxwUdzTIPIiKyPSyUiIgqwdKvlhoV91HiR1L5SnGbvt8kla8Ul56VrlgklcjMzUR6VrrUeSwh+162YpFUIvl8MrLvZZtpRkREZEtYKBERVYIHP5NUkbgx28ZI5SvFvbbxNal8pbiOUXJ3WmTjLGH42uEmjSMiIvvCQomIiMpIz5a7UyQbZwmpN1NNGkdERPaFhRIREZXh4+5j0jhL8K/tb9I4IiKyLyyUiIgqQexLsUbFrR20VipfKe7T4Z9K5SvFHZ8ltxucbJwlbByz0aRxRERkX1goERFVApk+Sfri3ujzhlS+UtywbsOk8pXifDx9DG4B7uXqBR9P672j5F7NHR2adNAb06FJB/ZTIiIinVgoERFVEpmGrtZ8PGN5hmKx5OXqhYzlGXrzrcHx2ccViyX2USIiIn1YKBERGbDs62VQjVVpvpZ9vUw6VyQI9GvRT2usX4t+0s1mRYLAgDYDtMYGtBlQrvw1wWu0xtYEr5HOz1iegRtLbqBJrSao7lIdTWo1wY0lN8xeJOXm52LCpgnou7QvJmyagNz8XOnc47OP486KOwhqG4TWDVojqG0Q7qy4wyKJiIj0UgkhrL81vBGysrLg5eWFzMxMeHp6Wno6ZMMKCgqwd+9e9OvXD05OTpaeDpmJvqasMsWGqfJdHV2x5bktGLJvCHILc6Xzm89qjtT0sru6+fv4IyUqxWC+NQiKD8Luk7vLjAe2C8Su0F3mn5Cd4u9AsiRef2Qq5akNeEeJiEiBviLHFo4rFUkAkJqeiuazmuvNtwZKRRIA7D65G0HxQeadEBER2Q0WSkREOsgur1OKi98bL5WvFGdsfmZOpmKRVCI1PRWZOZlS57GE3PxcxSKpxO6Tu8u1DI+IiEgWCyUiIh3CdocZFTdh5wSpfKU4Y/P7L+8vlS8bZwkR2yJMGkdERFQeLJSIiKqgi7cumjTOEs7eOGvSOCIiovJgoUREVAU1qtnIpHGWEFAnwKRxRERE5cFCiYhIh7jAOKPiVg5YKZWvFGds/p5Je6TyZeMsIWZQjEnjiIiIyoOFEhGRDpNfmGxUXGi/UKl8pThj873cvODv468319/HH15uuhvKWgNXZ1cEtgvUGxPYLhCuzq5mmhEREdkTFkpEVOV9/O3HWg1jP/72Y6k8Q32KrP14SlSKYrFk7j5K+YX5iEuKw8TNExGXFIf8wnypvF2huxSLJfZRIiKiyuRo6QkQEVUmXb2GRn82GqM/Gy3VsNXSIvpGIGZ/2aVlEX3ldnpLiUpBZk4m+i/vj4u3LqJRzUbYM2mPWe8kTd8+HbGJsSgSRZqxadumIbxPOKKDow3m7wrdhdz8XERsi8DZG2cRUCcAMYNieCeJiIgqFQslIqqyZBq26iuWLJ0/fft0nUUSAM24TKHh5eaFozOOGoyrDEqvoUgUles1uDq7YuUwuc9tERERmQKX3hFRlSS7vE4pLmF/glS+UtySL5dI5SvF5RfmIzYxVm9ubGKs9BI2S6gKr4GIiOwXCyUiqpJGfzbaqLg3t78pla8UN+2raVL5SnGrDq7SWqqmS5EowqqDq6TOYwlV4TUQEZH9YqFERGSFUtNTTRpnCVXhNRARkf1ioUREZIUMbe1d3jhLqAqvgYiI7BcLJSKqkta9ss6ouDXBa6TyleLef/F9qXyluJCeIVCr1Hpz1So1QnqGSJ3HEqrCayAiIvvFQomIqqTXn33dqLixfcdK5SvFTX1pqlS+UpyzozPC+4TrzQ3vEw5nR2ep81hCVXgNRERkv1goEZHV+yjxI62GsR8lfiSVZ+mGr8Yejw6ORkTfiDJ3ZdQqNSL6Rkhtq20Kufm5mLBpAvou7YsJmyYgNz9XOtdaXgMREVF5sY8SEVk1Xb2IxmwbgzHbxthEw1h/H3+dmxXIfi4nOjga84PmY/V3q4FcYOGAhRjfa7zZ7sIExQdh98ndmseJZxIRfygege0CsSt0l9RzlLyGVQdXITU9Ff4+/gjpGcI7SUREZNV4R4mIrJZMw1ZrPt58VnPFHd1S01PRfFZzvfklnB2dNZ/jMWeBUbpIetDuk7sRFB8k/VzOjs4I6x2GFUNXIKx3GIskIiKyeiyUiMgqyS6vU4rb/tN2qXyluE3fb5LKV4rLzMk0uO11anoqMnMypc5jbrn5uYpFUondJ3eXaxkeERGRLWGhRERWacy2MUbFDfpokFS+UtxrG1+TyleK67+8v1S+bJy5RWyLMGkcERGRrWGhRERUCS7eumjSOHM7e+OsSeOIiIhsDQslIqJK0KhmI5PGmVtAnQCTxhEREdkaFkpEZJXWDlprVNy2N7ZJ5SvFfTr8U6l8pbg9k/ZI5cvGmVvMoBiTxhEREdkaFkpEZJXe6POGUXHBTwVL5SvFDes2TCpfKc7LzcvgFuD+Pv7wcvOSOo+5uTq7IrBdoN6YwHaBcHV2NdOMiIiIzIuFEhFVuvi98VoNY+P3xkvlWbrhq7HHU6JSFIslfx9/pESl6M03laLiIhz6+xC2/LwFh/4+hKLiIqm8XaG7FIul8vRRIiIiskVsOEtElUpXr6EJOydgws4JNtEwNrBdoM5tsg3dbSmREpWCzJxM9F/eHxdvXUSjmo2wZ9Ies91J2nFiByZvnYzLty9rxhrWaIhlry7DwMcHGszfFboLufm5iNgWgbM3ziKgTgBiBsXwThIREVV5LJSIqNLINGzVVyxZOl+m4arMXRUvNy8cnXHUYJyp7TixA8GrgyGg/Rqv3L6C4NXB2D5+u1Sx5OrsipXDVlbWNImIiKwSl94RUaWQXV6nFLfx0EapfKW4ZV8vk8pXirP1hqtFxUWYvHVymSIJgGYsbGuY9DI8IiIie8NCiYgqxYSdE4yKG7FphFS+UlzY7jCpfKU4W2+4euTsEa3ldqUJCFy6fQlHzh4x46yIiIhsBwslIiIdbL3h6rWMayaNIyIisjcslIiIdLD1hqv1vOuZNI6IiMjesFAiokqxcoDch/+V4j4Z9olUvlJcXGCcVL5SnK03XO0a0BUNazSECro3tFBBBb8afuga0NXMMyMiIrINLJSIqFKE9gs1Km54j+FS+Upxk1+YLJWvFGfrDVfVDmose/X+RhWli6WSx3GvxkHtoDb73IiIiGwBCyUiMmjZ18u0GsbK7ihn6Yavxh63loarufm5mPb5NADAtM+nSe+0N/Dxgdg+fjsa1GigNd6wRkPprcGJiIjslUULpe+//x4vvvgi6tevD5VKhV27dmkdF0IgMjIS9evXh6urK3r06IHTp09bZrJEdko1VlVmZ7iw3WEGexRZiy/Gf1Gu8dJ2he5CTnwOQnuEok/LPgjtEYqc+ByzFUlB8UFwC3VDwtEEAEDC0QS4hbohKD5IKn/g4wNxftF5HJx2EJvHbMbBaQdxbtE5FklEREQGWLRQunv3Ltq2bYuVK3V/RiE6OhqxsbFYuXIlkpOT4evri969e+POnTtmnimRfZJp2GrNx0sarpbJgwrBq4Ox48QOvfklShqu7p+yHyuHrTTbcjuZhrcy1A5q9GjRA0OeHIIeLXpwuR0REZEEixZKzz//PObPn4+BA8v+y6YQAnFxcZg9ezYGDhyIVq1aYcOGDcjJycHmzZstMFsi+2Jsw9aFOxdK5SvF7Ty+UypfKc7WG67aesNbIiIiW+do6QkoOXfuHNLS0tCnTx/NmIuLC7p3745jx45h3LhxOvPy8vKQl5eneZyVlQUAKCgoQEFBQeVOmqq0kuvHXq6jmXtmwtXR8J2TmXtmIqRvSJnxeYnzpPLnJc7DtBemlRkf9vEwqfxhHw9D5mOZZcaPnj2Kf+78o/c5bt65ie//+z26BHQxeB5zm7FthtbcXdWuWv/7YNz7g98369zIPtnb70CyLrz+yFTKcw2phBD6P81sJiqVCjt37kRQUBAA4NixY+jcuTOuXLmC+vXra+LefPNNXLhwAfv379f5PJGRkZg7d26Z8c2bN8PNza1S5k5ERERERNYvJycHQ4cORWZmJjw9PfXGWu0dpRIqlfZnEIQQZcYeNHPmTISHh2seZ2Vlwc/PD3369DH4ZhDpU1BQgKSkJPTu3RtOTk6Wnk6l85rkJR2bubzsHR1L5x89exT9V/Q3mLtn4h6rvKM07fNpmg0cgPt3ktb1XofRSaORW/TvcruxXcbyjhKZhb39DiTrwuuPTKVktZkMqy2UfH19AQBpaWmoV+/fzvE3btxA3bp1FfNcXFzg4uJSZtzJyYk/WGQS9nItLey/sMxud7rEBcbpfD/e7fMuZu2dZTA/ql+UzvxNr2/CwATDO7PtGLtDZ363h7uhlkctXLl9RefnlFRQoWGNhuj2cDer3Nxg0aBFWH5oeZnx3KJc5BbmasXZw/VI1sNefgeSdeL1R8Yqz/VjtX2UmjZtCl9fXyQlJWnG8vPzcfjwYXTq1MmCMyOyD8Y2bJ05YKZUvlLcgI4DpPKV4my94aqtN7wlIiKydRYtlLKzs3Hy5EmcPHkSwP0NHE6ePImLFy9CpVIhLCwMUVFR2LlzJ/7880+MGjUKbm5uGDp0qCWnTWRzPtz3oVbD2A/3fSiVZ+mGr8Yet5aGq9n3sjFg5QC0iWyDASsHIPtetlSetTS8JSIiskcWXXr3yy+/oGfPnprHJZ8tGjlyJNavX4/p06cjNzcXISEhuH37Np588kkkJibCw8PDUlMmsjm6eg299cVbeOuLtwwWGtagrmddXM+6rnNcxsDHByKwXSCOnD2CaxnXUM+7HroGdDXbnaSOCzoi+Xyy5vGpK6fgMdEDHZp0wPHZxw3m7wrdhdz8XMzYNgPA/c8kLRq0iHeSiIiIKpnV7HpXWbKysuDl5SW1swWRPgUFBdi7dy/69etnM+ujDTVkBfTflbF0vu9UX51FUom6nnWRtiTN4DkspXSRVJpssQTY5vVHVQuvQbIkXn9kKuWpDaz2M0pEZBzZ5XVKcTO3Sn7GSCFuwY4FUvlKcbeyb+ktkgDgetZ13Mq+JXUec8u+l623SAKA5PPJ0svwiIiIyLxYKBFVUW998ZZRcYsOLJLKV4p755t3pPKV4rrHdJfKl40zt+Frh5s0joiIiMyLhRIRWaWrmVdNGmduqTdTTRpHRERE5sVCiYisUn2v+iaNMzf/2v4mjSMiIiLzYqFEVEV98PIHRsXNeGaGVL5S3Pzn50vlK8UdjjgslS8bZ24bx2w0aRwRERGZFwsloipq3HPjjIpb+OpCqXyluNkDZ0vlK8XVdK9pcAvwup51UdO9ptR5zM29mjs6NOmgN6ZDkw5wr+ZuphkRERFRebBQIrIB9towNm1JmmKxZM6twSvaMPb47OOKxVJ5tgYnIiIi87Now1kiMszWG8aqoIJA2XmqYLjHEnC/WLqVfQvdY7rjauZV1Peqj8MRh812J8nYhrHHZx9H9r1sDF87HKk3U+Ff2x8bx2zknSQiIiIrx0KJyIoZatiqGqsyquFrZec7jHXQWSQBgICAw1gHFCcU6z0HcH8Z3qm5pwzGmZq+hrHJ55PRcUFHqWLJvZo7dk7YaerpERERUSXi0jsiK2Vsw9gtR7dI5SvFJexPkMpXiktJS1EskkoICKSkpUidx9zYMJaIiMi+sVAislLGNowdumGoVL5S3Jvb35TKV4prGdlSKl82ztzYMJaIiMi+sVAiokpRUFRg0jhzY8NYIiIi+8ZCiYgqhZPayaRx5saGsURERPaNhRKRlTK2YezmkZul8pXi1gSvkcpXijsTeUYqXzbO3NgwloiIyL6xUCKyUsY2jB3SZYhUvlLc2L5jpfKV4pr7Nje4BbgKKjT3bS51HnNjw1giIiL7xkKJyAzstWFscUKxYrGkgkpqa3BTyC/MR1xSHCZunoi4pDjkF+ZL5bFhLBERkf1iHyWiSmbrDWMj+kYgZn+MznEZxQnFSElLQcvIligoKoCT2glnIs+Y7U7S9O3TEZsYiyJRpBmbtm0awvuEIzo42mA+G8YSERHZJxZKRJXI0g1fjc2fvn26ziIJgGZcptho7tsc+R/I3cUxJaX5F4mics2fDWOJiIjsD5feEVUSYxvGxu+Nl8pXilv29TKpfKW4/MJ8xCbG6s2NTYyVXsZmbrY+fyIiIrIsFkpElcTYhrETdk6QyleKC9sdJpWvFLfq4Cqt5Wq6FIkirDq4Suo85mbr8yciIiLLYqFERDqlpks2XJWMMzdbnz8RERFZFgslItLJ30ey4apknLnZ+vyJiIjIslgoEVUSYxvGrhywUipfKS4uME4qXykupGcI1Cq13ly1So2QniFS5zE3W58/ERERWRYLJaJKYmzD2NB+oVL5SnGTX5gsla8U5+zojPA+4Xpzw/uEw9nRWeo85mbr8yciIiLLYqFEVIks3fDV2OPRwdGI6BtR5s6MWqVGRN8Iqa21LcnW509ERESWw0KJSELM7hh4TfICAHhN8kLMbt29hXQRCQITumrvTDeh6wTpZrMiQeDFli9qjb3Y8sVy5b/33HtaY+899550fnRwNHJW5WDp4KWY0HMClg5eipxVOWYtMtKz0tF0RlO4T3BH0xlNkZ6VLp1rDfMnIiIi26MSQsj9tWSjsrKy4OXlhczMTHh6elp6OmSDSpq2ujq6YstzWzBk3xDkFuYCMHxH5sF8XcyR7z3JG5m5mWXGvVy9kLE8w2C+pdn6/E2loKAAe/fuRb9+/eDk5GTp6ZAd4jVIlsTrj0ylPLUB7ygR6aGvSLGF40pFBgBk5mbCe5K33nxLs/X5ExERke1ioUSkQHZ5nVLcd39+J5WvFBe/N14qXykuPStdscgokZmbWa5lbOZk6/MnIiIi28ZCiUjB9K+nGxX3zLJnpPKV4ibsnKBzXDauY1RHqXzZOHOz9fkTERGRbWOhRFRFpWfL3WmRjTM3W58/ERER2TYWSkRVlI+7j0njzM3W509ERES2jYUSkYLoF+S2j1aKOzD5gFS+UtzKASul8pXijs86LpUvG2dutj5/IiIism0slIgURARGGBXXq1UvqXyluNB+oVL5SnE+nj7wcvXSm+vl6gUfT+u8I2Pr8yciIiLbxkKJ7MLSr5ZCNVal+Vr61VKpPEN9iqz9eMbyDMViw5x9iCraMNZa5k9ERET2h4USVXmqsSqEfxmuNRb+ZbjBHkTWIrBdYLnGS8tYnoEbS26gSa0mqO5SHU1qNcGNJTfMVmR4T/JGnal1cP6f87ibdxfn/zmPOlPrSPdAsvT8iYiIyD45WnoCRJVJpmGrvrsyls4Pig/C7pO7dR7bfXI3guKDsCt0l95zAPeXsZ1bdM5gnKnJNIyVKXgsNX8iIiKyX7yjRFWW7PI6pbgVe1ZI5SvFvb3lbal8pbjc/FzFIqnE7pO7kZufK3Uec2PDWCIiIrJlLJSoyiq93K68cZN2TZLKV4qL/k5y1zyFuIhtkptJSMaZGxvGEhERkS1joURkpc7eOGvSOHNjw1giIiKyZSyUiKxUQJ0Ak8aZGxvGEhERkS1joURVVuxLsUbFLQ9aLpWvFDe913SpfKW4mEExUvmycebGhrFERERky1goUZU15cUpRsVN7D9RKl8pbvGQxVL5SnGuzq4GtwAPbBcIV2dXqfOYGxvGEhERkS1joUQ24eNvP9ZqGPvxtx9L5Vm64auxx3eF7tLbR0lma3BTyC/MR1xSHCZunoi4pDjkF+ZL5bFhLBEREdkq9lEiq6erF9Hoz0Zj9GejDRYa1sDL1UvnNtmG7raU2BW6C7n5uYjYFoGzN84ioE4AYgbFmO1O0vTt0xGbGIsiUaQZm7ZtGsL7hCM62PDOfhnLM5CelY6OUR2Rnp0OH3cfHJ91nHeSiIiIyKqxUCKrZumGr8bmm6rhqquzK1YOW2kwztSmb5+OmP1lPwNVJIo04zLFEhvGEhERka3h0juyWrLL65TivvzlS6l8pbiY3ZKbKSjE2XrD1fzCfMQm6t8QIzYxVnoZHhEREZEtYaFEVmv0Z6ONigv8UP9GCIbipn8tuWudQpytN1xddXCV1nI7XYpEEVYdXGWmGRERERGZDwslokpi6w1XU9NTTRpHREREZEtYKBFVEltvuOrv42/SOCIiIiJbwkKJrNa6V9YZFbd73G6pfKW46BcMb1KgL87WG66G9AyBWqXWG6NWqRHSM8RMMyIiIiIyHxZKZLVef/Z1o+Jeav+SVL5SXERghFS+UpytN1x1dnRGeJ9wvTHhfcLh7OhsphkRERERmQ8LJTKLhP0JWg1jE/YnSOVZuuGrscetpeFqZk4muizqgkbTG6HLoi7IzNG/G1+J6OBoRPSNKHNnSa1SI6JvhNTW4ERERES2iH2UqNLp6kX05vY38eb2N+2iYaylG642n9Vca8OFS7cvwXuyN/x9/JESlWIwPzo4GvOD5mPVwVVITU+Fv48/QnqG8E4SERERVWkslKhSWbrhq7U0jLVUw9XSRdKDUtNT0XxWc6liydnRGWG9w0w8OyIiIiLrxaV3VGlkl9cpxX2470OpfKU4e28Ym5mTaXDr7tT0VOlleERERET2hIUSVZo3t79pVNxbX7wlla8UZ+8NY/sv72/SOCIiIiJ7wkKJSIGtN4y9eOuiSeOIiIiI7AkLJSIFtt4wtlHNRiaNIyIiIrInLJSo0qwJXmNU3AcvfyCVrxRn7w1j90zaY9I4IiIiInvCQokqzdi+Y42KG/fcOKl8pTh7bxjr5eYFfx9/vTH+Pv7wcpPb5pyIiIjInrBQIik7j+/Uahi78/hOqTxLN3ytKg1j8wvzEZcUh4mbJyIuKQ75hflSeSlRKYrFkmwfJSIiIiJ7xD5KZJCuXkQDEwYCCYYLDWtgqoaxXRd3BXD/Mz1H3j5itjtJ07dPR2xiLIpEkWZs2rZpCO8Tjuhgw8sLU6JSkJmTif7L++PirYtoVLMR9kzawztJRERERHrwjhLpJdOw1ZqPyzSMleHj6YNTkacAAKciT5m1SIrZH6NVJAFAkShCzP4YTN8utwW6l5sXjs44iovRF3F0xlEWSUREREQGsFAiRbLL65Tijv73qFS+Utxnxz6TyleKs/WGsfmF+YhNjNUbE5sYK70Mj4iIiIjksVAiRQMTBhoV13VJV6l8pbhXP35VKl8pztYbxq46uKrMnaTSikQRVh1cZaYZEREREdkPFkpUZdl6w9jU9FSTxhERERGRPBZKVGXZesNYQ1t7lzeOiIiIiOSxUCJFO8buMCruyNQjUvlKcVtf3yqVrxRn6w1jQ3qGQK1S641Rq9QI6RliphkRERER2Q8WSqRoQMcBRsV1ebiLVL5S3CudXpHKV4qz9Yaxzo7OCO8TrjcmvE84nB2dzTQjIiIiIvvBQslOHE85rtUw9niK3F0USzd8rSoNYzNzMtFlURc0mt4IXRZ1QWaO/t34SkQHRyOib0SZO0tqlRoRfSOk+igRERERUfmx4awd0NVr6MnFTwKwjYaxEX0jELM/Rue4jJKGsR2jOiI9Ox0+7j44Puu42e4kNZ/VXGvDhUu3L8F7sjf8ffyREpViMD86OBrzg+Zj1cFVSE1Phb+PP0J6hvBOEhEREVElYqFUxck0bNVXLFk6v6Thqi4l4zJ3VXw8fXBu0TmDcaZWukh6UGp6KprPai5VLDk7OiOsd5iJZ0dERERESrj0rgqTXV6nFPfdn99J5SvFGduw1tYbrmbmZBrcujs1PVV6GR4RERERmQ8LpSqsZHldReOeWfaMVL5SnLENa2294Wr/5f1NGkdERERE5sNCiayWrTdcvXjroknjiIiIiMh8WCiR1bL1hquNajYyaRwRERERmQ8LpSrs57d/NiruwOQDUvlKccY2rLX1hqt7Ju0xaRwRERERmQ8LpSqsY/OORsX1atVLKl8pztiGtbbecNXLzcvg3S5/H394uelviktERERE5sdCyUacu3EOriGucBjrANcQV5y7IbfVtaUbvhp73FQNV4uKi3Do70PY8vMWHPr7EIqK9W8SoSv/6NmjAICjZ49K56dEpSgWS7J9lIiIiIjI/Gyij9KqVasQExODa9eu4dFHH0VcXBy6du1q6WmZjfpNNYpFsebxvYJ7aDa7GRxUDihaU74/+C3BzdkNOfk5OsdlGNtwdceJHZi8dTIu376sGWtYoyGWvboMAx83vDNfSf4/d/7Blue2oP+K/qjlUUs6PyUqBZk5mei/vD8u3rqIRjUbYc+kPbyTRERERGTFrP6O0meffYawsDDMnj0bv/32G7p27Yrnn38eFy/ax05hpYukBxWLYqjf1P8ZHpmGr5V5vHpodZ1FEgDk5Oegemh1vfklShqurhi6AmG9w8pVJAWvDtYqkgDgyu0rCF4djB0n9H+Oytj8El5uXjg64yguRl/E0RlHWSQRERERWTmrL5RiY2PxxhtvYMyYMXjkkUcQFxcHPz8/rF692tJTq3TnbpxTLJJKFItixWV4v/7vV6nzKMVt/2m7VL5SXFpGmmKRVCInPwdpGWlS5ymvouIiTN46GQJll/eVjIVtDVNcRmdsPhERERHZLqteepefn49ff/0VM2bM0Brv06cPjh07pjMnLy8PeXl5msdZWVkAgIKCAhQUFFTeZCvBE/OegKujq1Tc9djrZca7xnSVyu8a0xWZyzPLjI/YMEIqf8SGEQh8IrDM+FNRT0nlPxX1FM4uOGswrryOnj2Kf+78o3cON+/cxPf//R5dAroYzHdVa/+voXwiUyr5/WVrv8eo6uA1SJbE649MpTzXkEoIof/T9BZ09epVNGjQAD/88AM6deqkGY+KisKGDRvw999/l8mJjIzE3Llzy4xv3rwZbm5yn4khIiIiIqKqJycnB0OHDkVmZiY8PT31xlr1HaUSKpX252CEEGXGSsycORPh4f9uKZ2VlQU/Pz/06dPH4JthbeqG18W9wnsG46o5VtN5R8lrkvznYHTdUTI2P2B2AG7cuWEwt45HnUq7o9R/RX+DcXsm7lG8o/RgvqvaFet6r8PopNHILco1mE9kSgUFBUhKSkLv3r3h5ORk6emQHeI1SJbE649MpWS1mQyrLpRq164NtVqNtDTtz7DcuHEDdevW1Znj4uICFxeXMuNOTk4294P167u/otnsZgbjTs89rfO1HYk4gvYL2xvM/2XmLzrzPxn5CQZ9NMhg/rY3tunM/2nWT6gXUc9g/k+zfqqU7023h7uhlkctXLl9RefnjFRQoWGNhuj2cDeoHcpuiqGUn1uUi9zCXIP5RJXBFn+XUdXCa5AsidcfGas8149Vb+bg7OyMJ554AklJSVrjSUlJWkvxqqqmdZrCQaX/W+SgckDTOk11Hnui2RNS51GKC34qWCpfKc7X29fgFuBuzm7w9faVOk95qR3UWPbqMgD3i6IHlTyOezVOscgxNp+IiIiIbJdVF0oAEB4ejrVr12LdunX466+/MGXKFFy8eBFvvfWWpadWLreyb6H1nNaoFVYLree0xq3sW1J5RWuKFIslmT5Klm4Yezf+rmKx5Obshrvxd/XmG2vg4wOxffx2+HpqF2P1POth+/jtBvsgleQ3qNFAa7xhjYZS+URERERkm6x66R0AvPLKK/jnn3/w3nvv4dq1a2jVqhX27t2Lxo0bW3pq0nyn+uJ61r+fIbp19xZqTamFup51kbbE8NbYPh4+WvkPjpvDF+O/wNDVQ5GHf3cTdIELNo/fLJV/N/4u0jLS0G5eO2TkZMDbzRsn3z1ZaXeSSvvkx09wLeua1tjVrKv45MdPpAqdgY8PRGC7QHz/3++RdTYLeybu4XI7IiIioirO6u8oAUBISAjOnz+PvLw8/Prrr+jWrZulpyStdJH0oOtZ1+E7VX+xYGy+sQ1jSxquPlgkAUA+8svVcNXX2xdpS9Jwb/U9pC1JM1uRFBQfhN0nd+s8tvvkbgTFB0k9j9pBrdmwoUtAFxZJRERERFWcTRRKtupW9i3FIqfE9azrisvwjM03tuGsrTdczc3PVSySSuw+uRu5+bl6Y4iIiIjI/rBQqkTdY7obFWdsvsyOd/rijpw9gsu3LyvmCQhcun0JR84ekTqPuUVsizBpHBERERHZDxZKlehq5lWj4ozNN9a1jGuGg8oRZ25nb8j1ZpKNIyIiIiL7wUKpEtX3qm9UnLH5xqrnbbgHUnnizC2gToBJ44iIiIjIfrBQqkSHIw4bFWds/i8zf5HKV4rrGtAVDWs0LNNDqIQKKvjV8EPXgK5S5zG3mEExJo0jIiIiIvvBQqkS1XSvibqedfXG1PWsi5ruNSsl39iGs7becNXV2RWB7QL1xgS2C4Srs6uZZkREREREtoKFUiVLW5KmWOzI9FEyNt/YhrG23nB1V+guxWIpsF0gdoXuMu+EiIiIiMgmWH3D2aogbUkaLt68iEcjH0VOfg7cnN1wOvI0GtVuJJ1/6uIptJ3XFgICKqjw+7u/o3Wj1lL5IkHgeMpxPLn4Sc3Yz2//jI7NO0rllzRcPXL2CK5lXEM973roGtDVrHeSioqLKnz+XaG7kJufi4htETh74ywC6gQgZlAM7yQRERERkSIWSmbQcUFHJJ9P1jzOzstG45mN0aFJBxyffdxgvst4F+QX5mseCwi0mdcGzo7OyFudpyfzvh0ndmDy1slaYy+veRnLXl0mfUdI7aBGjxY9pGJNrWT+D25V3rBGw3LN39XZFSuHraysKRIRERFRFcOld5WsdJH0oOTzyei4QP9dndJF0oPyC/PhMt5Fb/6OEzsQvDq4TD+kK7evIHh1MHac2KE339Jsff5EREREZJtYKFWi7HvZikVSieTzyci+l63z2JVbVxSLpBL5hfm4cuuKzmNFxUWYvHUyBMp+DqlkLGxrGIqKi/Sew1Jsff5EREREZLtYKFWi4WuHGxXXeq7cZ5CU4o6cPVLmTsyDBAQu3b6EI2ePSJ3H3Gx9/kRERERku1goVaLUm6lGxd25d0cqXynuWsY1qXzZOHOz9fkTERERke1ioVSJ/Gv7GxXnUc1DKl8prp53Pal82Thzs/X5ExEREZHtYqFUiTaO2WhU3Kk5p6TyleK6BnRFwxoNyzSLLaGCCn41/NA1oKvUeczN1udPRERERLaLhVIlcq/mjg5NOuiN6dCkA9yrues81qBmAzg7OuvNd3Z0RoOaDXQeUzuosezVZQBQptgoeRz3apxZ+yGVh63Pn4iIiIhsFwulSnZ89nHFYkmmj1Le6jzFYkmmj9LAxwdi+/jtaFBDu5hqWKMhto/fLt2HyFJsff5EREREZJvYcNYMerTogV/O/6K1zbUKKukGrpOfmYwliUtQLIo1Yw4qB0x+ZrKerH8NfHwgAtsF4sjZI7iWcQ31vOuha0BXm7kTY+vzJyIiIiLbw0Kpkk3fPh0x+2PKjAsIzXh0cHS584tFsVR+CbWDWrows0a2Pn8iIiIisi1celeJ8gvzEZsYqzcmNjFWsamssflERERERFQxLJQq0aqDq1AkivTGFIkirDq4qlLyiYiIiIioYlgoVaLUdMmGswpxxuYTEREREVHFsFCqRP4+kg1nFeKMzSciIiIioophoVSJQnqGQK3SvzObWqVGSM+QSsknIiIiIqKKYaFUiZwdnRHeJ1xvTHifcL19kozJJyIiIiKiiuH24JWsZOvu2MRYrY0Z1Co1wvuEG9za29h8IiIiIiIqPxZKZhAdHI35QfOx6uAqpKanwt/HHyE9Q6TvBBmbT0RERERE5cNCyUycHZ0R1jvMYvlERERERCSPn1EiIiIiIiIqhYUSERERERFRKSyUiIiIiIiISmGhREREREREVAoLJSIiIiIiolJYKBEREREREZXCQomIiIiIiKgUFkpERERERESlsFAiIiIiIiIqhYUSERERERFRKSyUiIiIiIiISmGhREREREREVAoLJSIiIiIiolIcLT2ByiaEAABkZWVZeCZk6woKCpCTk4OsrCw4OTlZejpkZ3j9kaXxGiRL4vVHplJSE5TUCPpU+ULpzp07AAA/Pz8Lz4SIiIiIiKzBnTt34OXlpTdGJWTKKRtWXFyMq1evwsPDAyqVytLTIRuWlZUFPz8/XLp0CZ6enpaeDtkZXn9kabwGyZJ4/ZGpCCFw584d1K9fHw4O+j+FVOXvKDk4OKBhw4aWngZVIZ6envwlTRbD648sjdcgWRKvPzIFQ3eSSnAzByIiIiIiolJYKBEREREREZXCQolIkouLC+bMmQMXFxdLT4XsEK8/sjReg2RJvP7IEqr8Zg5ERERERETlxTtKREREREREpbBQIiIiIiIiKoWFEhERERERUSkslIiIiIiIiEphoURUyurVq9GmTRtNU7unn34a33zzjea4EAKRkZGoX78+XF1d0aNHD5w+fdqCM6aqauHChVCpVAgLC9OM8fqjyhQZGQmVSqX15evrqznO648q25UrV/Daa6+hVq1acHNzQ7t27fDrr79qjvMaJHNioURUSsOGDbFo0SL88ssv+OWXX9CrVy8EBgZqfhFHR0cjNjYWK1euRHJyMnx9fdG7d2/cuXPHwjOnqiQ5ORlr1qxBmzZttMZ5/VFle/TRR3Ht2jXN16lTpzTHeP1RZbp9+zY6d+4MJycnfPPNNzhz5gyWLFkCb29vTQyvQTIrQUQG1ahRQ6xdu1YUFxcLX19fsWjRIs2xe/fuCS8vL/HBBx9YcIZUldy5c0cEBASIpKQk0b17dzF58mQhhOD1R5Vuzpw5om3btjqP8fqjyvb222+LLl26KB7nNUjmxjtKRHoUFRVh69atuHv3Lp5++mmcO3cOaWlp6NOnjybGxcUF3bt3x7Fjxyw4U6pKQkND0b9/fzz77LNa47z+yBzOnj2L+vXro2nTpnj11Vfxv//9DwCvP6p8X375Jdq3b49BgwahTp06eOyxx5CQkKA5zmuQzI2FEpEOp06dgru7O1xcXPDWW29h586daNmyJdLS0gAAdevW1YqvW7eu5hiRMbZu3YoTJ05g4cKFZY7x+qPK9uSTT+KTTz7B/v37kZCQgLS0NHTq1An//PMPrz+qdP/73/+wevVqBAQEYP/+/XjrrbcwadIkfPLJJwD4O5DMz9HSEyCyRi1atMDJkyeRkZGBL774AiNHjsThw4c1x1UqlVa8EKLMGFF5Xbp0CZMnT0ZiYiKqVaumGMfrjyrL888/r/nv1q1b4+mnn4a/vz82bNiAp556CgCvP6o8xcXFaN++PaKiogAAjz32GE6fPo3Vq1djxIgRmjheg2QuvKNEpIOzszOaN2+O9u3bY+HChWjbti2WLVum2f2p9L9c3bhxo8y/cBGV16+//oobN27giSeegKOjIxwdHXH48GEsX74cjo6OmmuM1x+ZS/Xq1dG6dWucPXuWv/+o0tWrVw8tW7bUGnvkkUdw8eJFAOA1SGbHQolIghACeXl5aNq0KXx9fZGUlKQ5lp+fj8OHD6NTp04WnCFVBc888wxOnTqFkydPar7at2+PYcOG4eTJk2jWrBmvPzKrvLw8/PXXX6hXrx5//1Gl69y5M/7++2+tsf/7v/9D48aNAYDXIJkdl94RlTJr1iw8//zz8PPzw507d7B161YcOnQI+/bt0/S0iYqKQkBAAAICAhAVFQU3NzcMHTrU0lMnG+fh4YFWrVppjVWvXh21atXSjPP6o8o0bdo0vPjii2jUqBFu3LiB+fPnIysrCyNHjuTvP6p0U6ZMQadOnRAVFYXBgwfj+PHjWLNmDdasWQMAvAbJ7FgoEZVy/fp1DB8+HNeuXYOXlxfatGmDffv2oXfv3gCA6dOnIzc3FyEhIbh9+zaefPJJJCYmwsPDw8IzJ3vA648q0+XLlzFkyBDcvHkTPj4+eOqpp/DTTz9p/kWf1x9Vpg4dOmDnzp2YOXMm3nvvPTRt2hRxcXEYNmyYJobXIJmTSgghLD0JIiIiIiIia8LPKBEREREREZXCQomIiIiIiKgUFkpERERERESlsFAiIiIiIiIqhYUSERERERFRKSyUiIiIiIiISmGhREREREREVAoLJSIiIiIiolJYKBEREREREZXCQomIiGzasWPHoFar8dxzz1l6KkREVIWohBDC0pMgIiKqqDFjxsDd3R1r167FmTNn0KhRI0tPiYiIqgDeUSIiIpt19+5dfP755xg/fjxeeOEFrF+/Xuv4l19+iYCAALi6uqJnz57YsGEDVCoVMjIyNDHHjh1Dt27d4OrqCj8/P0yaNAl379417wshIiKrw0KJiIhs1meffYYWLVqgRYsWeO211/Dxxx+jZKHE+fPnERwcjKCgIJw8eRLjxo3D7NmztfJPnTqFvn37YuDAgfjjjz/w2Wef4ejRo5gwYYIlXg4REVkRLr0jIiKb1blzZwwePBiTJ09GYWEh6tWrhy1btuDZZ5/FjBkzsGfPHpw6dUoT/84772DBggW4ffs2vL29/1979++SThzHcfwVGBUKDk4ROAk5HRgYLeEi9Qc46CSEiJsgTiJtNYlTUDkoEbSFNN3iJOgiCiKIhEODTQ3a0iba8AXhruXLF76p9XzADZ/73B3vz/ji8+MUj8e1s7OjUqm0eKbRaCgUCunj40Pb29vLGBYAYAUwowQAWEvPz89qtVqKxWKSJIfDoWg0qkqlsugPBoOWdw4PDy3tTqeju7s7uVyuxXV6eqrZbKaXl5fvGQgAYCU5ll0AAAD/olwuazqdam9vb3FvPp9rc3NTk8lE8/lcGxsblnfsiyhms5lSqZTS6fSX73MoBAD8bgQlAMDamU6nur+/V7FY1MnJiaUvEono4eFBfr9fpmla+trttqV9cHCgfr8vn8/332sGAKwX9igBANbO09OTotGo3t7e5Ha7LX35fF6maaparWp/f1+ZTEaJRELdblfZbFavr696f3+X2+1Wr9fT0dGRzs7OlEwm5XQ6NRgMVKvVdHV1taTRAQBWAXuUAABrp1wuKxwOfwlJ0p8ZpW63q8lkosfHR1WrVRmGoZubm8Wpd1tbW5IkwzBUr9c1HA51fHysQCCg8/Nz7e7ufut4AACrhxklAMCvcXl5qdvbW41Go2WXAgBYcexRAgD8WNfX1woGg/J4PGo2myoUCvwjCQDwVwhKAIAfazgc6uLiQuPxWF6vV9lsVrlcbtllAQDWAEvvAAAAAMCGwxwAAAAAwIagBAAAAAA2BCUAAAAAsCEoAQAAAIANQQkAAAAAbAhKAAAAAGBDUAIAAAAAG4ISAAAAANh8Au1XyMDBK+iGAAAAAElFTkSuQmCC",
      "text/plain": [
       "<Figure size 1000x600 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Age</th>\n",
       "      <th>Experience</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Age</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.994215</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Experience</th>\n",
       "      <td>0.994215</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                 Age  Experience\n",
       "Age         1.000000    0.994215\n",
       "Experience  0.994215    1.000000"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "plt.figure(figsize=(10, 6))\n",
    "plt.scatter(loan_data['Age'], loan_data['Experience'], color='darkgreen', label='Data points')\n",
    "plt.xlabel('Age')\n",
    "plt.ylabel('Experience')\n",
    "plt.title('Linear Relationship between Age and Experience')\n",
    "plt.legend()\n",
    "plt.grid(True)\n",
    "plt.show()\n",
    "loan_data[['Age', 'Experience']].corr()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5a1c5a85-393b-459a-abcf-d0ff36f39c83",
   "metadata": {},
   "source": [
    "## <font color = \"red\"> **11).** \n",
    "#### What is the most frequent family size observed in this dataset?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "34c6f36a-49d5-4a1e-9155-d3654c1fa2b0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "The most frequent family size is :  1\n"
     ]
    }
   ],
   "source": [
    "## The most frequent family size in this data set using variable \"Family\" \n",
    "print(\"\\nThe most frequent family size is : \", loan_data[\"Family\"].mode()[0])"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "501ad686-bb76-4aec-8067-6e63a688b97c",
   "metadata": {},
   "source": [
    "## <font color = \"red\"> **12).** \n",
    "#### What is the percentage of variation you can observe in the ‘Income’ variable?\n",
    "**Ans:-**\n",
    "- Calculate the coefficient of variation of the Income variable = **(std.dev. of income / mean of income) * 100**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "b8de2262-1914-42fa-ac84-7b621e2fc23c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Percentage of variation in 'Income': 62.40%\n"
     ]
    }
   ],
   "source": [
    "mean_of_income = loan_data[\"Income\"].mean()\n",
    "std_dev_income = loan_data[\"Income\"].std()\n",
    "\n",
    "cv_of_income = (std_dev_income / mean_of_income) * 100\n",
    "\n",
    "print(f\"\\nPercentage of variation in 'Income': {cv_of_income:.2f}%\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b3e1e826-270b-4bbb-8308-70dc206e25b7",
   "metadata": {},
   "source": [
    "## <font color = \"red\"> **13).** \n",
    "#### The ‘Mortgage’ variable has a lot of zeroes. Impute with some business logical value that you feel fit for the data.\n",
    "**Ans:-**\n",
    "-  A common approach is to replace zeros with the median or mean for 'Mortgage' variable."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "b5f78036-cf4e-48e0-8d88-f2a52e4dc6e0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "count    5000.000000\n",
      "mean       56.498800\n",
      "std       101.713802\n",
      "min         0.000000\n",
      "25%         0.000000\n",
      "50%         0.000000\n",
      "75%       101.000000\n",
      "max       635.000000\n",
      "Name: Mortgage, dtype: float64\n",
      "count    5000.000000\n",
      "mean      162.436000\n",
      "std        57.959919\n",
      "min        75.000000\n",
      "25%       153.000000\n",
      "50%       153.000000\n",
      "75%       153.000000\n",
      "max       635.000000\n",
      "Name: Mortgage, dtype: float64\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "<Axes: >"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAjEAAAGfCAYAAACukYP3AAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjguNCwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8fJSN1AAAACXBIWXMAAA9hAAAPYQGoP6dpAAA2a0lEQVR4nO3dcVDU953/8dcqyyIWVtHCQiXEpp7VoDbFFrG5qlFAJ4SkdqJXe5y589RcooZBJ61mMsG7RLx0JtrDxjOeF43okekktrmJRXBS9RyCRgwTsZ5nJybVFsQmsGjEZYPf3x8dvr+s+EXW7KofeT5mdsbv9/vez/fzfbMJr/nsfheXZVmWAAAADDPgVk8AAADgRhBiAACAkQgxAADASIQYAABgJEIMAAAwEiEGAAAYiRADAACMRIgBAABGIsQAAAAjEWIAAICRYr7Mk8vKyrRq1So99dRTWr9+vSTJsiytXr1ar7zyilpbW5Wdna1f/OIXuvfee+3nBQIBrVixQv/1X/+ljo4OTZ8+XS+//LJGjBhh17S2tmrZsmV66623JEmFhYUqLy/XkCFD+jS3K1eu6E9/+pMSEhLkcrm+zGUCAICbxLIsXbhwQWlpaRow4DprLdYNOnz4sHX33Xdb48ePt5566il7/9q1a62EhATrjTfesI4dO2bNnTvXSk1Ntdrb2+2axx9/3Pra175m1dTUWEePHrWmTZtmTZgwwfr888/tmpkzZ1qZmZlWbW2tVVtba2VmZloFBQV9nt+ZM2csSTx48ODBgwcPAx9nzpy57u96l2WF/wcgL168qG9/+9t6+eWX9fzzz+tb3/qW1q9fL8uylJaWpuLiYv3kJz+R9JdVl5SUFP3rv/6rFi9eLL/fr69+9avavn275s6dK0n605/+pPT0dO3evVv5+fk6ceKExo4dq7q6OmVnZ0uS6urqlJOTo//93//V6NGjrztHv9+vIUOG6MyZM0pMTAz3EnsVDAZVXV2tvLw8ud3uiI5tOnrjjN44ozfO6I0zeuPM5N60t7crPT1dbW1t8nq9vdbe0NtJTz75pB588EHNmDFDzz//vL3/9OnTam5uVl5enr3P4/FoypQpqq2t1eLFi1VfX69gMBhSk5aWpszMTNXW1io/P1/vvvuuvF6vHWAkadKkSfJ6vaqtrb1miAkEAgoEAvb2hQsXJEmDBg3SoEGDbuQyHcXExCg+Pl6DBg0y7sURbfTGGb1xRm+c0Rtn9MaZyb0JBoOS1KePgoQdYiorK3X06FG99957PY41NzdLklJSUkL2p6Sk6OOPP7ZrYmNjNXTo0B413c9vbm5WcnJyj/GTk5PtmquVlZVp9erVPfZXV1crPj6+D1cWvpqamqiMeyegN87ojTN644zeOKM3zkzszaVLl/pcG1aIOXPmjJ566ilVV1crLi7Ose7q9GRZ1nUT1dU116rvbZyVK1eqpKTE3u5ejsrLy4vK20k1NTXKzc01LuFGG71xRm+c0Rtn9MYZvXFmcm/a29v7XBtWiKmvr1dLS4uysrLsfV1dXTpw4IA2bNigkydPSvrLSkpqaqpd09LSYq/O+Hw+dXZ2qrW1NWQ1pqWlRZMnT7Zrzp071+P858+f77HK083j8cjj8fTY73a7o/YDjObYpqM3zuiNM3rjjN44ozfOTOxNOPMN63tipk+frmPHjqmhocF+TJw4UT/+8Y/V0NCgr3/96/L5fCHLV52dndq/f78dULKysuR2u0Nqmpqa1NjYaNfk5OTI7/fr8OHDds2hQ4fk9/vtGgAA0L+FtRKTkJCgzMzMkH2DBw/WsGHD7P3FxcVas2aNRo0apVGjRmnNmjWKj4/XvHnzJEler1cLFizQ8uXLNWzYMCUlJWnFihUaN26cZsyYIUkaM2aMZs6cqYULF2rTpk2SpEWLFqmgoKBPdyYBAIA735f6srtrefrpp9XR0aEnnnjC/rK76upqJSQk2DXr1q1TTEyM5syZY3/Z3datWzVw4EC7ZseOHVq2bJl9F1NhYaE2bNgQ6ekCAABDfekQs2/fvpBtl8ul0tJSlZaWOj4nLi5O5eXlKi8vd6xJSkpSRUXFl50eAAC4Q/G3kwAAgJEIMQAAwEiEGAAAYCRCDAAAMBIhBgAAGIkQAwAAjESIAQAARor4l90BUVPqvdUz6F2p/1bPAAD6FVZiAACAkQgxAADASIQYAABgJEIMAAAwEiEGAAAYiRADAACMRIgBAABGIsQAAAAjEWIAAICRCDEAAMBIhBgAAGAkQgwAADASIQYAABiJEAMAAIxEiAEAAEYixAAAACMRYgAAgJEIMQAAwEiEGAAAYCRCDAAAMBIhBgAAGIkQAwAAjESIAQAARiLEAAAAIxFiAACAkQgxAADASIQYAABgpLBCzMaNGzV+/HglJiYqMTFROTk5+s1vfmMff+yxx+RyuUIekyZNChkjEAho6dKlGj58uAYPHqzCwkKdPXs2pKa1tVVFRUXyer3yer0qKipSW1vbjV8lAAC444QVYkaMGKG1a9fqyJEjOnLkiB544AE9/PDDOn78uF0zc+ZMNTU12Y/du3eHjFFcXKxdu3apsrJSBw8e1MWLF1VQUKCuri67Zt68eWpoaFBVVZWqqqrU0NCgoqKiL3mpAADgThITTvFDDz0Usv3CCy9o48aNqqur07333itJ8ng88vl813y+3+/Xli1btH37ds2YMUOSVFFRofT0dO3du1f5+fk6ceKEqqqqVFdXp+zsbEnS5s2blZOTo5MnT2r06NFhXyQAALjzhBVivqirq0u//OUv9dlnnyknJ8fev2/fPiUnJ2vIkCGaMmWKXnjhBSUnJ0uS6uvrFQwGlZeXZ9enpaUpMzNTtbW1ys/P17vvviuv12sHGEmaNGmSvF6vamtrHUNMIBBQIBCwt9vb2yVJwWBQwWDwRi/zmrrHi/S4d4Ko9mZAXOTHjKTrXDOvG2f0xhm9cUZvnJncm3DmHHaIOXbsmHJycnT58mV95Stf0a5duzR27FhJ0qxZs/Too48qIyNDp0+f1rPPPqsHHnhA9fX18ng8am5uVmxsrIYOHRoyZkpKipqbmyVJzc3Nduj5ouTkZLvmWsrKyrR69eoe+6urqxUfHx/uZfZJTU1NVMa9E0SlNxNeifyYkXTVW6dOeN04ozfO6I0zeuPMxN5cunSpz7Vhh5jRo0eroaFBbW1teuONNzR//nzt379fY8eO1dy5c+26zMxMTZw4URkZGXr77bc1e/ZsxzEty5LL5bK3v/hvp5qrrVy5UiUlJfZ2e3u70tPTlZeXp8TExHAvs1fBYFA1NTXKzc2V2+2O6Nimi2pvykZEdrxIW3m218O8bpzRG2f0xhm9cWZyb7rfSemLsENMbGysvvGNb0iSJk6cqPfee08///nPtWnTph61qampysjI0KlTpyRJPp9PnZ2dam1tDVmNaWlp0eTJk+2ac+fO9Rjr/PnzSklJcZyXx+ORx+Ppsd/tdkftBxjNsU0Xld5cuRzZ8SKtj9fL68YZvXFGb5zRG2cm9iac+d7wZ2K6WZYV8lmUL/rkk0905swZpaamSpKysrLkdrtVU1OjOXPmSJKamprU2NioF198UZKUk5Mjv9+vw4cP67vf/a4k6dChQ/L7/XbQuV1klu5RoMt5deh289HaB2/1FAAAiJiwQsyqVas0a9Yspaen68KFC6qsrNS+fftUVVWlixcvqrS0VD/84Q+Vmpqqjz76SKtWrdLw4cP1gx/8QJLk9Xq1YMECLV++XMOGDVNSUpJWrFihcePG2XcrjRkzRjNnztTChQvt1Z1FixapoKCAO5MAAIAtrBBz7tw5FRUVqampSV6vV+PHj1dVVZVyc3PV0dGhY8eO6bXXXlNbW5tSU1M1bdo0vf7660pISLDHWLdunWJiYjRnzhx1dHRo+vTp2rp1qwYOHGjX7NixQ8uWLbPvYiosLNSGDRsidMkAAOBOEFaI2bJli+OxQYMGac+ePdcdIy4uTuXl5SovL3esSUpKUkVFRThTAwAA/Qx/OwkAABiJEAMAAIxEiAEAAEYixAAAACMRYgAAgJEIMQAAwEiEGAAAYCRCDAAAMBIhBgAAGIkQAwAAjESIAQAARiLEAAAAIxFiAACAkQgxAADASIQYAABgJEIMAAAwEiEGAAAYiRADAACMRIgBAABGIsQAAAAjEWIAAICRCDEAAMBIhBgAAGAkQgwAADASIQYAABiJEAMAAIxEiAEAAEYixAAAACMRYgAAgJEIMQAAwEiEGAAAYCRCDAAAMBIhBgAAGIkQAwAAjESIAQAARgorxGzcuFHjx49XYmKiEhMTlZOTo9/85jf2ccuyVFpaqrS0NA0aNEhTp07V8ePHQ8YIBAJaunSphg8frsGDB6uwsFBnz54NqWltbVVRUZG8Xq+8Xq+KiorU1tZ241cJAADuOGGFmBEjRmjt2rU6cuSIjhw5ogceeEAPP/ywHVRefPFFvfTSS9qwYYPee+89+Xw+5ebm6sKFC/YYxcXF2rVrlyorK3Xw4EFdvHhRBQUF6urqsmvmzZunhoYGVVVVqaqqSg0NDSoqKorQJQMAgDtBTDjFDz30UMj2Cy+8oI0bN6qurk5jx47V+vXr9cwzz2j27NmSpG3btiklJUU7d+7U4sWL5ff7tWXLFm3fvl0zZsyQJFVUVCg9PV179+5Vfn6+Tpw4oaqqKtXV1Sk7O1uStHnzZuXk5OjkyZMaPXr0NecWCAQUCATs7fb2dklSMBhUMBgM5zKvq3s8zwArouNGW6T70Ns5onKuAXGRHzOSrnPNUe2N4eiNM3rjjN44M7k34czZZVnWDf0m7urq0i9/+UvNnz9f77//vuLi4nTPPffo6NGjuu++++y6hx9+WEOGDNG2bdv0zjvvaPr06fr00081dOhQu2bChAl65JFHtHr1av3nf/6nSkpKerx9NGTIEK1bt05///d/f835lJaWavXq1T3279y5U/Hx8TdyiQAA4Ca7dOmS5s2bJ7/fr8TExF5rw1qJkaRjx44pJydHly9f1le+8hXt2rVLY8eOVW1trSQpJSUlpD4lJUUff/yxJKm5uVmxsbEhAaa7prm52a5JTk7ucd7k5GS75lpWrlypkpISe7u9vV3p6enKy8u7bhPCFQwGVVNTo2ePDFDgiiuiY0dTY2l+1M/R3Zvc3Fy53e7IDl42IrLjRdrKs70ejmpvDEdvnNEbZ/TGmcm96X4npS/CDjGjR49WQ0OD2tra9MYbb2j+/Pnav3+/fdzlCv2lbllWj31Xu7rmWvXXG8fj8cjj8fTY73a7o/YDDFxxKdBlToi5mS/kqPT9yuXIjhdpfbzeaL4mTUdvnNEbZ/TGmYm9CWe+Yd9iHRsbq2984xuaOHGiysrKNGHCBP385z+Xz+eTpB6rJS0tLfbqjM/nU2dnp1pbW3utOXfuXI/znj9/vscqDwAA6L++9PfEWJalQCCgkSNHyufzqaamxj7W2dmp/fv3a/LkyZKkrKwsud3ukJqmpiY1NjbaNTk5OfL7/Tp8+LBdc+jQIfn9frsGAAAgrLeTVq1apVmzZik9PV0XLlxQZWWl9u3bp6qqKrlcLhUXF2vNmjUaNWqURo0apTVr1ig+Pl7z5s2TJHm9Xi1YsEDLly/XsGHDlJSUpBUrVmjcuHH23UpjxozRzJkztXDhQm3atEmStGjRIhUUFDjemQQAAPqfsELMuXPnVFRUpKamJnm9Xo0fP15VVVXKzc2VJD399NPq6OjQE088odbWVmVnZ6u6uloJCQn2GOvWrVNMTIzmzJmjjo4OTZ8+XVu3btXAgQPtmh07dmjZsmXKy8uTJBUWFmrDhg2RuF4AAHCHCCvEbNmypdfjLpdLpaWlKi0tdayJi4tTeXm5ysvLHWuSkpJUUVERztQAAEA/w99OAgAARiLEAAAAIxFiAACAkQgxAADASIQYAABgJEIMAAAwEiEGAAAYiRADAACMRIgBAABGIsQAAAAjEWIAAICRCDEAAMBIhBgAAGAkQgwAADASIQYAABiJEAMAAIxEiAEAAEYixAAAACMRYgAAgJEIMQAAwEiEGAAAYCRCDAAAMBIhBgAAGIkQAwAAjESIAQAARiLEAAAAIxFiAACAkQgxAADASIQYAABgJEIMAAAwEiEGAAAYiRADAACMRIgBAABGIsQAAAAjhRViysrK9J3vfEcJCQlKTk7WI488opMnT4bUPPbYY3K5XCGPSZMmhdQEAgEtXbpUw4cP1+DBg1VYWKizZ8+G1LS2tqqoqEher1der1dFRUVqa2u7sasEAAB3nLBCzP79+/Xkk0+qrq5ONTU1+vzzz5WXl6fPPvsspG7mzJlqamqyH7t37w45XlxcrF27dqmyslIHDx7UxYsXVVBQoK6uLrtm3rx5amhoUFVVlaqqqtTQ0KCioqIvcakAAOBOEhNOcVVVVcj2q6++quTkZNXX1+v73/++vd/j8cjn811zDL/fry1btmj79u2aMWOGJKmiokLp6enau3ev8vPzdeLECVVVVamurk7Z2dmSpM2bNysnJ0cnT57U6NGjw7pIAABw5wkrxFzN7/dLkpKSkkL279u3T8nJyRoyZIimTJmiF154QcnJyZKk+vp6BYNB5eXl2fVpaWnKzMxUbW2t8vPz9e6778rr9doBRpImTZokr9er2traa4aYQCCgQCBgb7e3t0uSgsGggsHgl7nMHrrH8wywIjputEW6D72dIyrnGhAX+TEj6TrXHNXeGI7eOKM3zuiNM5N7E86cbzjEWJalkpIS3X///crMzLT3z5o1S48++qgyMjJ0+vRpPfvss3rggQdUX18vj8ej5uZmxcbGaujQoSHjpaSkqLm5WZLU3Nxsh54vSk5OtmuuVlZWptWrV/fYX11drfj4+Bu9zF79y8QrURk3Wq5+Wy+aampqIj/ohFciP2Yk9bG/UenNHYLeOKM3zuiNMxN7c+nSpT7X3nCIWbJkiT744AMdPHgwZP/cuXPtf2dmZmrixInKyMjQ22+/rdmzZzuOZ1mWXC6Xvf3FfzvVfNHKlStVUlJib7e3tys9PV15eXlKTEzs83X1RTAYVE1NjZ49MkCBK9eez+2osTQ/6ufo7k1ubq7cbndkBy8bEdnxIm3l2V4PR7U3hqM3zuiNM3rjzOTedL+T0hc3FGKWLl2qt956SwcOHNCIEb3/YklNTVVGRoZOnTolSfL5fOrs7FRra2vIakxLS4smT55s15w7d67HWOfPn1dKSso1z+PxeOTxeHrsd7vdUfsBBq64FOgyJ8TczBdyVPp+5XJkx4u0Pl5vNF+TpqM3zuiNM3rjzMTehDPfsO5OsixLS5Ys0Ztvvql33nlHI0eOvO5zPvnkE505c0apqamSpKysLLnd7pAlrqamJjU2NtohJicnR36/X4cPH7ZrDh06JL/fb9cAAID+LayVmCeffFI7d+7Ur3/9ayUkJNifT/F6vRo0aJAuXryo0tJS/fCHP1Rqaqo++ugjrVq1SsOHD9cPfvADu3bBggVavny5hg0bpqSkJK1YsULjxo2z71YaM2aMZs6cqYULF2rTpk2SpEWLFqmgoIA7kwAAgKQwQ8zGjRslSVOnTg3Z/+qrr+qxxx7TwIEDdezYMb322mtqa2tTamqqpk2bptdff10JCQl2/bp16xQTE6M5c+aoo6ND06dP19atWzVw4EC7ZseOHVq2bJl9F1NhYaE2bNhwo9cJAADuMGGFGMvq/ZbiQYMGac+ePdcdJy4uTuXl5SovL3esSUpKUkVFRTjTAwAA/Qh/OwkAABiJEAMAAIxEiAEAAEYixAAAACMRYgAAgJEIMQAAwEiEGAAAYCRCDAAAMBIhBgAAGIkQAwAAjESIAQAARiLEAAAAIxFiAACAkQgxAADASIQYAABgJEIMAAAwEiEGAAAYiRADAACMRIgBAABGIsQAAAAjEWIAAICRCDEAAMBIhBgAAGAkQgwAADASIQYAABiJEAMAAIxEiAEAAEYixAAAACMRYgAAgJEIMQAAwEiEGAAAYCRCDAAAMBIhBgAAGIkQAwAAjESIAQAARgorxJSVlek73/mOEhISlJycrEceeUQnT54MqbEsS6WlpUpLS9OgQYM0depUHT9+PKQmEAho6dKlGj58uAYPHqzCwkKdPXs2pKa1tVVFRUXyer3yer0qKipSW1vbjV0lAAC444QVYvbv368nn3xSdXV1qqmp0eeff668vDx99tlnds2LL76ol156SRs2bNB7770nn8+n3NxcXbhwwa4pLi7Wrl27VFlZqYMHD+rixYsqKChQV1eXXTNv3jw1NDSoqqpKVVVVamhoUFFRUQQuGQAA3AliwimuqqoK2X711VeVnJys+vp6ff/735dlWVq/fr2eeeYZzZ49W5K0bds2paSkaOfOnVq8eLH8fr+2bNmi7du3a8aMGZKkiooKpaena+/evcrPz9eJEydUVVWluro6ZWdnS5I2b96snJwcnTx5UqNHj47EtQMAAIOFFWKu5vf7JUlJSUmSpNOnT6u5uVl5eXl2jcfj0ZQpU1RbW6vFixervr5ewWAwpCYtLU2ZmZmqra1Vfn6+3n33XXm9XjvASNKkSZPk9XpVW1t7zRATCAQUCATs7fb2dklSMBhUMBj8MpfZQ/d4ngFWRMeNtkj3obdzROVcA+IiP2YkXeeao9obw9EbZ/TGGb1xZnJvwpnzDYcYy7JUUlKi+++/X5mZmZKk5uZmSVJKSkpIbUpKij7++GO7JjY2VkOHDu1R0/385uZmJScn9zhncnKyXXO1srIyrV69usf+6upqxcfHh3l1ffMvE69EZdxo2b179007V01NTeQHnfBK5MeMpD72Nyq9uUPQG2f0xhm9cWZiby5dutTn2hsOMUuWLNEHH3yggwcP9jjmcrlCti3L6rHvalfXXKu+t3FWrlypkpISe7u9vV3p6enKy8tTYmJir+cOVzAYVE1NjZ49MkCBK71f1+2ksTQ/6ufo7k1ubq7cbndkBy8bEdnxIm3l2V4PR7U3hqM3zuiNM3rjzOTedL+T0hc3FGKWLl2qt956SwcOHNCIEf//F4vP55P0l5WU1NRUe39LS4u9OuPz+dTZ2anW1taQ1ZiWlhZNnjzZrjl37lyP854/f77HKk83j8cjj8fTY7/b7Y7aDzBwxaVAlzkh5ma+kKPS9yuXIztepPXxeqP5mjQdvXFGb5zRG2cm9iac+YZ1d5JlWVqyZInefPNNvfPOOxo5cmTI8ZEjR8rn84UsX3V2dmr//v12QMnKypLb7Q6paWpqUmNjo12Tk5Mjv9+vw4cP2zWHDh2S3++3awAAQP8W1krMk08+qZ07d+rXv/61EhIS7M+neL1eDRo0SC6XS8XFxVqzZo1GjRqlUaNGac2aNYqPj9e8efPs2gULFmj58uUaNmyYkpKStGLFCo0bN86+W2nMmDGaOXOmFi5cqE2bNkmSFi1apIKCAu5MAgAAksIMMRs3bpQkTZ06NWT/q6++qscee0yS9PTTT6ujo0NPPPGEWltblZ2drerqaiUkJNj169atU0xMjObMmaOOjg5Nnz5dW7du1cCBA+2aHTt2aNmyZfZdTIWFhdqwYcONXCMAALgDhRViLOv6txS7XC6VlpaqtLTUsSYuLk7l5eUqLy93rElKSlJFRUU40wMAAP0IfzsJAAAYiRADAACMRIgBAABGIsQAAAAjEWIAAICRCDEAAMBIhBgAAGAkQgwAADASIQYAABiJEAMAAIxEiAEAAEYixAAAACMRYgAAgJEIMQAAwEiEGAAAYCRCDAAAMBIhBgAAGIkQAwAAjESIAQAARiLEAAAAIxFiAACAkQgxAADASIQYAABgJEIMAAAwEiEGAAAYiRADAACMRIgBAABGIsQAAAAjEWIAAICRCDEAAMBIhBgAAGAkQgwAADASIQYAABiJEAMAAIxEiAEAAEYKO8QcOHBADz30kNLS0uRyufSrX/0q5Phjjz0ml8sV8pg0aVJITSAQ0NKlSzV8+HANHjxYhYWFOnv2bEhNa2urioqK5PV65fV6VVRUpLa2trAvEAAA3JnCDjGfffaZJkyYoA0bNjjWzJw5U01NTfZj9+7dIceLi4u1a9cuVVZW6uDBg7p48aIKCgrU1dVl18ybN08NDQ2qqqpSVVWVGhoaVFRUFO50AQDAHSom3CfMmjVLs2bN6rXG4/HI5/Nd85jf79eWLVu0fft2zZgxQ5JUUVGh9PR07d27V/n5+Tpx4oSqqqpUV1en7OxsSdLmzZuVk5OjkydPavTo0eFOGwAA3GHCDjF9sW/fPiUnJ2vIkCGaMmWKXnjhBSUnJ0uS6uvrFQwGlZeXZ9enpaUpMzNTtbW1ys/P17vvviuv12sHGEmaNGmSvF6vamtrrxliAoGAAoGAvd3e3i5JCgaDCgaDEb2+7vE8A6yIjhttke5Db+eIyrkGxEV+zEi6zjVHtTeGozfO6I0zeuPM5N6EM+eIh5hZs2bp0UcfVUZGhk6fPq1nn31WDzzwgOrr6+XxeNTc3KzY2FgNHTo05HkpKSlqbm6WJDU3N9uh54uSk5PtmquVlZVp9erVPfZXV1crPj4+AlfW079MvBKVcaPl6rf1oqmmpibyg054JfJjRlIf+xuV3twh6I0zeuOM3jgzsTeXLl3qc23EQ8zcuXPtf2dmZmrixInKyMjQ22+/rdmzZzs+z7IsuVwue/uL/3aq+aKVK1eqpKTE3m5vb1d6erry8vKUmJh4I5fiKBgMqqamRs8eGaDAlWvP53bUWJof9XN09yY3N1dutzuyg5eNiOx4kbbybK+Ho9obw9EbZ/TGGb1xZnJvut9J6YuovJ30RampqcrIyNCpU6ckST6fT52dnWptbQ1ZjWlpadHkyZPtmnPnzvUY6/z580pJSbnmeTwejzweT4/9brc7aj/AwBWXAl3mhJib+UKOSt+vXI7seJHWx+uN5mvSdPTGGb1xRm+cmdibcOYb9e+J+eSTT3TmzBmlpqZKkrKysuR2u0OWuJqamtTY2GiHmJycHPn9fh0+fNiuOXTokPx+v10DAAD6t7BXYi5evKjf//739vbp06fV0NCgpKQkJSUlqbS0VD/84Q+Vmpqqjz76SKtWrdLw4cP1gx/8QJLk9Xq1YMECLV++XMOGDVNSUpJWrFihcePG2XcrjRkzRjNnztTChQu1adMmSdKiRYtUUFDAnUkAAEDSDYSYI0eOaNq0afZ29+dQ5s+fr40bN+rYsWN67bXX1NbWptTUVE2bNk2vv/66EhIS7OesW7dOMTExmjNnjjo6OjR9+nRt3bpVAwcOtGt27NihZcuW2XcxFRYW9vrdNAAAoH8JO8RMnTpVluV8a/GePXuuO0ZcXJzKy8tVXl7uWJOUlKSKiopwpwcAAPoJ/nYSAAAwEiEGAAAYiRADAACMRIgBAABGIsQAAAAjEWIAAICRCDEAAMBIhBgAAGAkQgwAADASIQYAABiJEAMAAIxEiAEAAEYixAAAACMRYgAAgJEIMQAAwEiEGAAAYCRCDAAAMBIhBgAAGIkQAwAAjESIAQAARiLEAAAAIxFiAACAkQgxAADASIQYAABgJEIMAAAwEiEGAAAYiRADAACMRIgBAABGIsQAAAAjEWIAAICRCDEAAMBIhBgAAGAkQgwAADASIQYAABiJEAMAAIwUdog5cOCAHnroIaWlpcnlculXv/pVyHHLslRaWqq0tDQNGjRIU6dO1fHjx0NqAoGAli5dquHDh2vw4MEqLCzU2bNnQ2paW1tVVFQkr9crr9eroqIitbW1hX2BAADgzhR2iPnss880YcIEbdiw4ZrHX3zxRb300kvasGGD3nvvPfl8PuXm5urChQt2TXFxsXbt2qXKykodPHhQFy9eVEFBgbq6uuyaefPmqaGhQVVVVaqqqlJDQ4OKiopu4BIBAMCdKCbcJ8yaNUuzZs265jHLsrR+/Xo988wzmj17tiRp27ZtSklJ0c6dO7V48WL5/X5t2bJF27dv14wZMyRJFRUVSk9P1969e5Wfn68TJ06oqqpKdXV1ys7OliRt3rxZOTk5OnnypEaPHn2j1wsAAO4QYYeY3pw+fVrNzc3Ky8uz93k8Hk2ZMkW1tbVavHix6uvrFQwGQ2rS0tKUmZmp2tpa5efn691335XX67UDjCRNmjRJXq9XtbW11wwxgUBAgUDA3m5vb5ckBYNBBYPBSF6mPZ5ngBXRcaMt0n3o7RxROdeAuMiPGUnXueao9sZw9MYZvXFGb5yZ3Jtw5hzRENPc3CxJSklJCdmfkpKijz/+2K6JjY3V0KFDe9R0P7+5uVnJyck9xk9OTrZrrlZWVqbVq1f32F9dXa34+PjwL6YP/mXilaiMGy27d+++aeeqqamJ/KATXon8mJHUx/5GpTd3CHrjjN44ozfOTOzNpUuX+lwb0RDTzeVyhWxbltVj39WurrlWfW/jrFy5UiUlJfZ2e3u70tPTlZeXp8TExHCmf13BYFA1NTV69sgABa70fl23k8bS/Kifo7s3ubm5crvdkR28bERkx4u0lWd7PRzV3hiO3jijN87ojTOTe9P9TkpfRDTE+Hw+SX9ZSUlNTbX3t7S02KszPp9PnZ2dam1tDVmNaWlp0eTJk+2ac+fO9Rj//PnzPVZ5unk8Hnk8nh773W531H6AgSsuBbrMCTE384Uclb5fuRzZ8SKtj9cbzdek6eiNM3rjjN44M7E34cw3ot8TM3LkSPl8vpDlq87OTu3fv98OKFlZWXK73SE1TU1NamxstGtycnLk9/t1+PBhu+bQoUPy+/12DQAA6N/CXom5ePGifv/739vbp0+fVkNDg5KSknTXXXepuLhYa9as0ahRozRq1CitWbNG8fHxmjdvniTJ6/VqwYIFWr58uYYNG6akpCStWLFC48aNs+9WGjNmjGbOnKmFCxdq06ZNkqRFixapoKCAO5MAAICkGwgxR44c0bRp0+zt7s+hzJ8/X1u3btXTTz+tjo4OPfHEE2ptbVV2draqq6uVkJBgP2fdunWKiYnRnDlz1NHRoenTp2vr1q0aOHCgXbNjxw4tW7bMvoupsLDQ8btpAABA/xN2iJk6daosy/nWYpfLpdLSUpWWljrWxMXFqby8XOXl5Y41SUlJqqioCHd6AACgn+BvJwEAACMRYgAAgJEIMQAAwEiEGAAAYCRCDAAAMBIhBgAAGIkQAwAAjESIAQAARiLEAAAAIxFiAACAkQgxAADASIQYAABgJEIMAAAwEiEGAAAYiRADAACMRIgBAABGIsQAAAAjEWIAAICRCDEAAMBIhBgAAGAkQgwAADASIQYAABiJEAMAAIxEiAEAAEYixAAAACMRYgAAgJEIMQAAwEiEGAAAYCRCDAAAMBIhBgAAGCnmVk8At5FS75cfY0CcNOEVqWyEdOXylx8PAAAHrMQAAAAjsRLTj9z907d7Pf5R3E2aCAAAEcBKDAAAMBIhBgAAGCniIaa0tFQulyvk4fP57OOWZam0tFRpaWkaNGiQpk6dquPHj4eMEQgEtHTpUg0fPlyDBw9WYWGhzp49G+mpAgAAg0VlJebee+9VU1OT/Th27Jh97MUXX9RLL72kDRs26L333pPP51Nubq4uXLhg1xQXF2vXrl2qrKzUwYMHdfHiRRUUFKirqysa0wUAAAaKygd7Y2JiQlZfulmWpfXr1+uZZ57R7NmzJUnbtm1TSkqKdu7cqcWLF8vv92vLli3avn27ZsyYIUmqqKhQenq69u7dq/z8/GueMxAIKBAI2Nvt7e2SpGAwqGAwGNHr6x7PM8CK6Li3WnDAl/9kb/cYkRjLONd5nXW/biL9erwT0Btn9MYZvXFmcm/CmbPLsqyI/iYuLS3Vz372M3m9Xnk8HmVnZ2vNmjX6+te/rg8//FD33HOPjh49qvvuu89+zsMPP6whQ4Zo27ZteueddzR9+nR9+umnGjp0qF0zYcIEPfLII1q9erXjea91bOfOnYqPj4/kJQIAgCi5dOmS5s2bJ7/fr8TExF5rI74Sk52drddee01/9Vd/pXPnzun555/X5MmTdfz4cTU3N0uSUlJSQp6TkpKijz/+WJLU3Nys2NjYkADTXdP9/GtZuXKlSkpK7O329nalp6crLy/vuk0IVzAYVE1NjZ49MkCBK66Ijn0rNXoWfOkxggPiVDPu35R7bJnc/e3L7lb2/rmt7tdNbm6u3G73TZqUGeiNM3rjjN44M7k33e+k9EXEQ8ysWbPsf48bN045OTm65557tG3bNk2aNEmS5HKF/uK3LKvHvqtdr8bj8cjj8fTY73a7o/YDDFxxKdB154SYSIYO95XL/S/E9PF1Fs3XpOnojTN644zeODOxN+HMN+q3WA8ePFjjxo3TqVOn7M/JXL2i0tLSYq/O+Hw+dXZ2qrW11bEGAAAg6iEmEAjoxIkTSk1N1ciRI+Xz+VRTU2Mf7+zs1P79+zV58mRJUlZWltxud0hNU1OTGhsb7RoAAICIv520YsUKPfTQQ7rrrrvU0tKi559/Xu3t7Zo/f75cLpeKi4u1Zs0ajRo1SqNGjdKaNWsUHx+vefPmSZK8Xq8WLFig5cuXa9iwYUpKStKKFSs0btw4+24lAACAiIeYs2fP6kc/+pH+/Oc/66tf/aomTZqkuro6ZWRkSJKefvppdXR06IknnlBra6uys7NVXV2thIQEe4x169YpJiZGc+bMUUdHh6ZPn66tW7dq4MCBkZ4uAAAwVMRDTGVlZa/HXS6XSktLVVpa6lgTFxen8vJylZeXR3h2QPR0/4HNj9Y+eItnAgD9A387CQAAGIkQAwAAjESIAQAARiLEAAAAIxFiAACAkQgxAADASIQYAABgJEIMAAAwEiEGAAAYiRADAACMRIgBAABGIsQAAAAjEWIAAICRCDEAAMBIhBgAAGCkmFs9AeBOc/dP377mfs9ASy9+V8os3aNAl+smz6p3H6198FZPAQDCxkoMAAAwEisxQIR8FDev1+PBAXHarVfU6Fkg95XLN2lWf3H35Z039XwAcDOwEgMAAIxEiAEAAEYixAAAACMRYgAAgJEIMQAAwEiEGAAAYCRCDAAAMBIhBgAAGIkQAwAAjMQ39gL9wPW+TVilN2UajjKDO8L+u1L8vScArMQAAAAjEWIAAICReDsJwC3X6FkQ/h/HLI3qlK46l/8mngxAX7ESAwAAjMRKDABcx90/fTsi4/BhZCCyWIkBAABGuu1XYl5++WX97Gc/U1NTk+69916tX79ef/3Xf32rpwWgH7nuLep9VXoDzxkQJ014RSobITl8Xujuyzu/1LR6w+oRbme3dYh5/fXXVVxcrJdfflnf+973tGnTJs2aNUu/+93vdNddd93q6QHAbSFiIetaSr/s8/lQNKLntg4xL730khYsWKB//Md/lCStX79ee/bs0caNG1VWVnaLZwcAuJ5IfZ7oWjwDrWt+SSKrR/3HbRtiOjs7VV9fr5/+9Kch+/Py8lRbW9ujPhAIKBAI2Nt+/1/S/6effqpgMBjRuQWDQV26dEkxwQHqutK3bxc1wSedsV96jOCAWF26dEmfdMbKfeVKBGZ156A3zuiNM9N7Uz/gsaiNHXTF6beXXtR+19NyD/j/b7V9sipqpzRGcECcLt37oj5Z/fW+f23BjVj+vxEf8sKFC5Iky7KuW3vbhpg///nP6urqUkpKSsj+lJQUNTc396gvKyvT6tWre+wfOXJk1OZ4pxkesZGiuLRtPHrjjN44ozfO6I2zm9Cbssj95rjahQsX5PV6e625bUNMN5crdKXDsqwe+yRp5cqVKikpsbevXLmiTz/9VMOGDbtm/ZfR3t6u9PR0nTlzRomJiREd23T0xhm9cUZvnNEbZ/TGmcm9sSxLFy5cUFpa2nVrb9sQM3z4cA0cOLDHqktLS0uP1RlJ8ng88ng8IfuGDBkSzSkqMTHRuBfHzUJvnNEbZ/TGGb1xRm+cmdqb663AdLttvycmNjZWWVlZqqmpCdlfU1OjyZMn36JZAQCA28VtuxIjSSUlJSoqKtLEiROVk5OjV155RX/4wx/0+OOP3+qpAQCAW+y2DjFz587VJ598on/+539WU1OTMjMztXv3bmVkZNzSeXk8Hj333HM93r4CvekNvXFGb5zRG2f0xll/6Y3L6ss9TAAAALeZ2/YzMQAAAL0hxAAAACMRYgAAgJEIMQAAwEiEGAAAYCRCTJhefvlljRw5UnFxccrKytL//M//3OopRd2BAwf00EMPKS0tTS6XS7/61a9CjluWpdLSUqWlpWnQoEGaOnWqjh8/HlITCAS0dOlSDR8+XIMHD1ZhYaHOnj17E68i8srKyvSd73xHCQkJSk5O1iOPPKKTJ0+G1PTX3kjSxo0bNX78ePsbQ3NycvSb3/zGPt6fe/NFZWVlcrlcKi4utvf1596UlpbK5XKFPHw+n328P/dGkv74xz/qb//2bzVs2DDFx8frW9/6lurr6+3j/a4/FvqssrLScrvd1ubNm63f/e531lNPPWUNHjzY+vjjj2/11KJq9+7d1jPPPGO98cYbliRr165dIcfXrl1rJSQkWG+88YZ17Ngxa+7cuVZqaqrV3t5u1zz++OPW1772NaumpsY6evSoNW3aNGvChAnW559/fpOvJnLy8/OtV1991WpsbLQaGhqsBx980Lrrrrusixcv2jX9tTeWZVlvvfWW9fbbb1snT560Tp48aa1atcpyu91WY2OjZVn9uzfdDh8+bN19993W+PHjraeeesre359789xzz1n33nuv1dTUZD9aWlrs4/25N59++qmVkZFhPfbYY9ahQ4es06dPW3v37rV+//vf2zX9rT+EmDB897vftR5//PGQfd/85jetn/70p7doRjff1SHmypUrls/ns9auXWvvu3z5suX1eq1///d/tyzLstra2iy3221VVlbaNX/84x+tAQMGWFVVVTdt7tHW0tJiSbL2799vWRa9uZahQ4da//Ef/0FvLMu6cOGCNWrUKKumpsaaMmWKHWL6e2+ee+45a8KECdc81t9785Of/MS6//77HY/3x/7wdlIfdXZ2qr6+Xnl5eSH78/LyVFtbe4tmdeudPn1azc3NIX3xeDyaMmWK3Zf6+noFg8GQmrS0NGVmZt5RvfP7/ZKkpKQkSfTmi7q6ulRZWanPPvtMOTk59EbSk08+qQcffFAzZswI2U9vpFOnTiktLU0jR47U3/zN3+jDDz+URG/eeustTZw4UY8++qiSk5N13333afPmzfbx/tgfQkwf/fnPf1ZXV1ePv6CdkpLS4y9t9yfd195bX5qbmxUbG6uhQ4c61pjOsiyVlJTo/vvvV2ZmpiR6I0nHjh3TV77yFXk8Hj3++OPatWuXxo4d2+97U1lZqaNHj6qsrKzHsf7em+zsbL322mvas2ePNm/erObmZk2ePFmffPJJv+/Nhx9+qI0bN2rUqFHas2ePHn/8cS1btkyvvfaapP752rmt/3bS7cjlcoVsW5bVY19/dCN9uZN6t2TJEn3wwQc6ePBgj2P9uTejR49WQ0OD2tra9MYbb2j+/Pnav3+/fbw/9ubMmTN66qmnVF1drbi4OMe6/tgbSZo1a5b973HjxiknJ0f33HOPtm3bpkmTJknqv725cuWKJk6cqDVr1kiS7rvvPh0/flwbN27U3/3d39l1/ak/rMT00fDhwzVw4MAeSbWlpaVH6u1Puu8a6K0vPp9PnZ2dam1tdawx2dKlS/XWW2/pt7/9rUaMGGHvpzdSbGysvvGNb2jixIkqKyvThAkT9POf/7xf96a+vl4tLS3KyspSTEyMYmJitH//fv3bv/2bYmJi7Gvrj725lsGDB2vcuHE6depUv37dSFJqaqrGjh0bsm/MmDH6wx/+IKl//j+HENNHsbGxysrKUk1NTcj+mpoaTZ48+RbN6tYbOXKkfD5fSF86Ozu1f/9+uy9ZWVlyu90hNU1NTWpsbDS6d5ZlacmSJXrzzTf1zjvvaOTIkSHH+3NvnFiWpUAg0K97M336dB07dkwNDQ32Y+LEifrxj3+shoYGff3rX++3vbmWQCCgEydOKDU1tV+/biTpe9/7Xo+vcfi///s/ZWRkSOqn/8+5+Z8lNlf3LdZbtmyxfve731nFxcXW4MGDrY8++uhWTy2qLly4YL3//vvW+++/b0myXnrpJev999+3by1fu3at5fV6rTfffNM6duyY9aMf/eiat/SNGDHC2rt3r3X06FHrgQceMPaWvm7/9E//ZHm9Xmvfvn0ht4NeunTJrumvvbEsy1q5cqV14MAB6/Tp09YHH3xgrVq1yhowYIBVXV1tWVb/7s3Vvnh3kmX1794sX77c2rdvn/Xhhx9adXV1VkFBgZWQkGD/f7Y/9+bw4cNWTEyM9cILL1inTp2yduzYYcXHx1sVFRV2TX/rDyEmTL/4xS+sjIwMKzY21vr2t79t3057J/vtb39rSerxmD9/vmVZf7mt77nnnrN8Pp/l8Xis73//+9axY8dCxujo6LCWLFliJSUlWYMGDbIKCgqsP/zhD7fgaiLnWj2RZL366qt2TX/tjWVZ1j/8wz/Y/6189atftaZPn24HGMvq37252tUhpj/3pvt7Tdxut5WWlmbNnj3bOn78uH28P/fGsizrv//7v63MzEzL4/FY3/zmN61XXnkl5Hh/64/Lsizr1qwBAQAA3Dg+EwMAAIxEiAEAAEYixAAAACMRYgAAgJEIMQAAwEiEGAAAYCRCDAAAMBIhBgAAGIkQAwAAjESIAQAARiLEAAAAI/0/bU1exZFfxYIAAAAASUVORK5CYII=",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "print(loan_data[\"Mortgage\"].describe().T)\n",
    "loan_data['Mortgage'].hist()\n",
    "\n",
    "median_value = loan_data[loan_data['Mortgage'] > 0]['Mortgage'].median()\n",
    "# replace 0 with median_value\n",
    "loan_data['Mortgage'] = loan_data['Mortgage'].replace(0, median_value)\n",
    "\n",
    "print(loan_data['Mortgage'].describe())\n",
    "loan_data['Mortgage'].hist()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "53cf6ddc-fbe0-4e53-a4fc-0f875af43b49",
   "metadata": {},
   "source": [
    "## <font color = \"red\"> **14).** \n",
    "#### Plot a density curve of the CCAvg variable for the customers who possess credit cards and write an interpretation about its distribution.\n",
    "**Ans:-**\n",
    "- ***Interpretaion -***\n",
    "- The curve is skewed to right 'Positivily Right Skewed', it means there are more customers with lower average credit card usage\n",
    "- A taller and sharper peak suggests a leptokurtic distribution with more customers having 'CCAvg' values close to the mode, whereas a flatter peak indicates a platykurtic distribution with more variation around the mode.\n",
    "- There are long tails it's indicates presence of some ***'outliers'*** the customers who are using the avg credit card significantly higher or lower than the majority."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "b704c5e8-3fc1-4e5a-b734-aeea09d6a21b",
   "metadata": {},
   "outputs": [],
   "source": [
    "# For ignore Wanrings\n",
    "import warnings\n",
    "warnings.filterwarnings(\"ignore\", category=SyntaxWarning)\n",
    "warnings.filterwarnings(\"ignore\", category=FutureWarning)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "41d85f55-d00e-4451-97bc-84fac69d0b48",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "ID                    3.731723e+06\n",
      "Age                   6.684800e+04\n",
      "Experience            2.978800e+04\n",
      "Income                1.081980e+05\n",
      "ZIP Code              1.369714e+08\n",
      "Family                3.553000e+03\n",
      "CCAvg                 2.822140e+03\n",
      "Education             2.744000e+03\n",
      "Mortgage              2.378970e+05\n",
      "Personal Loan         1.430000e+02\n",
      "Securities Account    1.430000e+02\n",
      "CD Account            2.400000e+02\n",
      "Online                8.820000e+02\n",
      "CreditCard            1.470000e+03\n",
      "dtype: float64\n"
     ]
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAkAAAAHFCAYAAAAaD0bAAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjguNCwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8fJSN1AAAACXBIWXMAAA9hAAAPYQGoP6dpAABvUklEQVR4nO3dd3xT9f4/8FdGk3Ql3XtQoKWUTcsWkFWGIKJIRUFwc0EFUe+VixN/WidfFAHliiAqULwsBwplyCxDaAHZq7RAS/du05HP74/aXEIH3SdtXs/HIw/t6cnJ+4SMVz/nM2RCCAEiIiIiCyKXugAiIiKi5sYARERERBaHAYiIiIgsDgMQERERWRwGICIiIrI4DEBERERkcRiAiIiIyOIwABEREZHFYQAiIiIii8MAJIFVq1ZBJpMZbxqNBh4eHhgyZAgiIyORkpIidYlGMpkMb7/9tvHnM2fO4O2330Z8fHyjPs7bb79t8pyoVCoEBARg9uzZyMrKMu5X8dzV5/G3bt1qci6NafHixWjfvj1UKhVkMplJzVU5efIknnjiCQQEBECj0cDOzg49e/bERx99hIyMDJN9DQYDvvvuOwwfPhwuLi6wsrKCm5sbxo4di59//hkGg6HS8U+dOgWZTAYrKyskJSU15qnWSWxsLAYPHgydTgeZTIZFixY1+WPm5OTgvffeQ1hYGLRaLdRqNdq0aYMnn3wSx48fb5LHvHnzJt5++23ExcU1yfFbq6rez2vWrKnydRIfHw+ZTIZPPvmkQY955coVPP/88wgKCoK1tTVsbGzQqVMnvP7667hx40aDjl1bd36u1uV5qEl9PisaW0M+o5udoGa3cuVKAUCsXLlSxMTEiL1794r//ve/Ys6cOUKn0wknJycRHR0tdZlCCCFiYmJEYmKi8ecff/xRABC7d+9u1Md56623BADx+++/i5iYGLF9+3YxZ84cIZPJRN++fYXBYBBC/O+5u3r1ap0fY9asWaIpXvKxsbECgHj66afFvn37RExMjCgtLa12/+XLlwulUik6deoklixZInbv3i22b98u3n//fREQECAeeOAB476FhYVi5MiRQiaTicmTJ4v169eLvXv3ig0bNohnnnlGqNVqsXnz5kqP8eKLLwoAAoD44IMPGv2ca6t79+4iMDBQbN26VcTExIikpKQmfbxLly6Jtm3bCjs7O/HKK6+IX375Rfzxxx9i1apVYsyYMQKAyMrKavTHPXr0qPE9TbWXkpIiYmJiRFFRkXHbfffdJ/z9/Svte/XqVQFAfPzxx/V+vJ9//lnY2toKf39/8fHHH4sdO3aInTt3ikWLFomuXbuK7t271/vYdQFAvPXWW8af6/I8VKe+nxWNrSGf0c2NAUgCFS+Qo0ePVvrdtWvXhK+vr7C3txfJyckSVFezpg5AqampJtunTp0qAIj9+/cLIcwzAH3//fcCgDh8+PBd9z148KBQKBRi1KhRJh92FfR6vdiyZYvx53/84x8CgPj222+rPN6FCxfEiRMnTLYVFRUJZ2dn0a1bN+Ht7S2CgoLqeEaNR6lUin/84x+Ndrzi4mJRUlJS5e9KS0tFly5dhFarFadOnapyn61bt4r8/PxGq6dCSw9ABoNBFBQUSF2GEKLpAtCVK1eEra2t6NGjR5Uh2GAwiA0bNtR4jMZ67dwZgKpS1wBUn8+K+rjba4UBiGpUUwASQoj169cLAOKdd94x2X706FExbtw44ejoKNRqtejevbuIioqq8ti7du0SM2bMEM7OzsLJyUlMmDBB3Lhxw2TfnTt3isGDBwsnJyeh0WiEr6+vePDBB03e5Le/USuOfedt5cqVYsGCBUKhUIiEhIRK5/PEE08IJycnUVhYWO1zUl0AWrJkiQAgfvjhB5Ma7nxzrVixQnTt2lWo1Wrh6OgoHnjgAXHmzBnj76dNm1Zl7Xd7k97tuIMHD650zGnTplV7vLFjxwqlUlnl83SnpKQkYWVlJUaOHHnXfW+3bt06AUAsXrxY/Pvf/xYAxL59+4y/Hz9+vPDz8xNlZWWV7tu7d2/Ro0cP48+ZmZniySefFI6OjsLW1laMGTNGXL58+a4f4NW9ViqcOnVK3H///cLBwUGo1WrRrVs3sWrVKpNj7N69WwAQq1evFnPnzhVeXl5CJpOJs2fPVvmY//3vfwUAERkZWavnadq0aVV+wVS8Fm+3fv160bt3b6HVaoW1tbUICAgQTzzxhEmdd95uf362bNki+vbtK6ytrYWdnZ0YPny4OHjwYJWPe+LECTFx4kSh1WqFo6OjeOmll0RJSYk4d+6cGDlypLCzsxP+/v7iww8/rFR7dna2ePnll0WbNm2ElZWV8PLyErNnzxZ5eXkm+wEQs2bNEsuWLRPBwcHCyspKLFu2TAghxNKlS0XXrl2Fra2tsLOzEx06dBDz5s2r8bkMCwsTY8aMMdnWuXNnAUAcOXLEuG3Dhg0CgDh58qQQovL7uar3U8W/xe0B6NNPPxVt2rQRtra2om/fviImJqbG+oQQ4vnnnxcAarVvRS2dOnUSe/bsEf369RPW1tYiIiJCCFH75zk7O1s8/fTTwsnJSdja2oqRI0eK8+fPV3p91OV5qEpdPysKCwvF3LlzRbdu3Yyvs759+1bZQlTTayUmJkb0799fqNVq4enpKV577TWxfPnySp+ttfmukQIDkATuFoDy8vKEQqEQw4YNM27btWuXUKlUYuDAgSIqKkr8/vvvYvr06ZX+6qw4dtu2bcULL7wgtm3bJr7++mvh6OgohgwZYtzv6tWrQqPRiBEjRojNmzeLP/74Q/zwww9i6tSpIjMz07jf7W/UlJQU8f777wsAYsmSJSImJkbExMSIlJQUcevWLaFWq8X8+fNNziU9PV1YW1uLV199tcbnpLoA9NJLLwkAYvv27Sbnd/ubq6KmyZMni19//VWsXr1atG3bVuh0OnHhwgUhRPmlkYkTJxo/ACtuVbXC1OW4p0+fFq+//rrJJc1Lly5VebzS0lJhY2Mj+vTpU+NzUWHNmjUCgPHDprZGjBgh1Gq1yMjIEJcuXRIymUxMnz7d+PstW7YIAJUus549e1YAEJ9//rkQQoiysjJxzz33CI1GIz744AOxfft28c4774jAwMC7BqCKJn0AYuLEicbnWwghzp07J+zt7UW7du3E6tWrxa+//iomT54sAJh8qVcEC29vbzFx4kTx008/iV9++UWkp6dX+ZjPPvusAFBtQLpTbQPQwYMHhUwmE4888ojYunWr2LVrl1i5cqWYOnWqEKL8S67idfn6668bz7Xi0vEPP/wgAIjw8HCxefNmERUVJUJDQ4VKpTIJphWP26FDB/Huu++K6Oho8c9//lMAEM8//7wIDg4Wn3/+uYiOjhZPPPGEAGDSYpGfny+6d+8uXFxcxMKFC8WOHTvEZ599JnQ6nRg6dKjxMrIQwvi8du3aVaxZs0bs2rVL/PXXX2Lt2rUCgHjhhRfE9u3bxY4dO8SXX34pXnzxxRqfy9dee03Y2dmJ4uJiIYQQycnJAoCwtrYW7733nnG/f/zjH8Ld3d34853v59OnT4sBAwYIDw8Pk/epEP8LQG3atBGjRo0SmzdvFps3bxZdunQRjo6Od720GRQUZPLYd1Pxhe3r6ysWL14sdu/eLfbs2VPr59lgMIghQ4YItVot3nvvPbF9+3bx1ltvibZt2941ANX0PFSlrp8VWVlZYvr06eK7774Tu3btEr///rt45ZVXhFwur9SCVN1r5fTp08LGxkaEhISItWvXii1btoiRI0cKPz8/k3Op7XeNFBiAJHC3ACSEEO7u7qJjx47Gn4ODg0WPHj0qNf+PHTtWeHp6Gv+arzj2zJkzTfb76KOPBABjH4yKv5bj4uJqrPXON2pNl8CmTZsm3NzchF6vN2778MMPhVwuv2tLS8WHf3JysigpKRGZmZni+++/F9bW1sLX19fYenTnB0VmZqawtrau9NdnQkKCUKvV4tFHHzVuq8slsLoctzb/nkL870vhkUceqVUNH3zwgQDK+0XVVnx8vJDL5SaPMXjwYGFraytycnKEEEKUlJQId3d3k3MQQoh//vOfQqVSibS0NCGEEL/++muVH6qRkZG1asIX4n9/Pd7ukUceEWq1ulIr2OjRo4WNjY3xi6wiAA0aNKhW5z5q1CgBoMZQe7vaBqBPPvlEADX3HaruElhZWZnw8vISXbp0MWlxy83NFW5ubqJ///6VHvfTTz81OUb37t0FALFx40bjtpKSEuHq6ioefPBB47bIyEghl8srvQ4r3utbt241bgMgdDqdyMjIMNn3+eefFw4ODtWeZ3V27NghAIi9e/cKIcovC9vb24uZM2ea/OEVGBhY5Xvn9s+Hu10C69Kli0kfuyNHjggAYu3atTXWqNFoRN++fWt9ThWtMDt37jTZXtvn+bfffhMAxGeffWay33vvvXfXACRE3S6B1eez4nalpaWipKREPPXUUyYtwEJU/1qJiIgQ1tbWJl01SktLRXBwsMm51Pa7RgocBWamhBDG/7906RLOnTuHxx57DABQWlpqvI0ZMwZJSUk4f/68yf3vv/9+k5+7du0KALh27RoAoHv37lCpVHj22Wfx7bff4sqVKw2uefbs2UhJScGPP/4IoHxEwrJly3DfffehTZs2tTqGh4cHrKys4OjoiClTpqBnz574/fffodFoqtw/JiYGhYWFmD59usl2X19fDB06FDt37qzXuTTVcZvaypUrYTAY8OSTTxq3Pfnkk8jPz0dUVBQAQKlUYsqUKdi4cSOys7MBAGVlZfjuu+8w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pKRg3759WLlyJRQKBTZt2gRXV1fjvl999RVGjx6NkSNHYvr06fD29kZGRgbOnj2L48ePG/vd1NaXX36JXbt24b777oOfnx+KioqMX441fUh17twZALB8+XLY29tDo9EgICDA+BeOQqHArFmz8K9//Qu2traV+tA0NgcHB7zxxhv497//jccffxyTJ09Geno63nnnHWg0Grz11lvGfbt06QIA+PDDDzF69GgoFAp07doVKpWqQceti379+mHZsmWYOXMmQkND8Y9//AOdOnVCSUkJYmNjsXz5cnTu3Bnjxo0DACxcuBBXrlzB9OnTsW3bNkyYMAHu7u5IS0tDdHQ0Vq5ciXXr1sHb2xtbtmzByJEjMX78+Cof+//+7/+wevVqREZGwsrKCpMnT8bcuXMxefJk6PX6Sv9Wo0aNwoABA/Dyyy8jJycHoaGhiImJMX7A3t6npS7eeust/PLLLxgyZAjefPNNODk54YcffsCvv/6Kjz76CDqdrl7HrXjfhIeHo1+/fvjHP/6BIUOGwNbWFteuXcN///tf/Pzzz8ZLThEREXjzzTfxyCOP4NVXX0VRURE+//xzlJWVmRz3zTffxPXr1zFs2DD4+PggKysLn332GaysrIwhsV27drC2tsYPP/yAjh07ws7ODl5eXvDy8sJHH32Exx57DGPHjsVzzz0HvV6Pjz/+GFlZWfjggw/qda5VmTNnDjZs2IBBgwbhpZdeQteuXWEwGJCQkIDt27fj5ZdfRp8+fWo8xjPPPANra2sMGDAAnp6eSE5ORmRkJHQ6nbEvVHVCQ0Ph6OiI7du3m1xKHT58ON59913j/99Nly5dsHHjRixbtgyhoaGQy+UICwurxTNQs4CAAKxbtw4RERHo3r07nn/+efTo0QNA+Qz333zzDYQQmDBhQo3Hqe3zHB4ejkGDBuGf//wn8vPzERYWhgMHDhj/GGns56G2nxVdu3bF2LFjsXHjRsycORMTJ05EYmIi3n33XXh6euLixYu1qu/111/HTz/9hKFDh+LNN9+EjY0NlixZgvz8fJP96vtd0ywk7IBtse6cI0WlUgk3NzcxePBg8f7774uUlJQq73fixAkxadIk4ebmJqysrISHh4cYOnSo+PLLLysd+84RChUjaipGb8XExIgJEyYIf39/oVarhbOzsxg8eLD46aefTO6HKkb7LFq0SAQEBAiF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",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Skewness: CCAvg    1.598443\n",
      "dtype: float64\n",
      "Kurtosis: 2.646706374237909\n"
     ]
    }
   ],
   "source": [
    "#This data only for those customers who possess credit cards\n",
    "credit_card = loan_data[loan_data['CreditCard'] == 1]\n",
    "print(credit_card.sum())\n",
    "\n",
    "sns.kdeplot(credit_card['CCAvg'], shade=True)\n",
    "plt.title('Density Plot of CCAvg for Customers with Credit Cards')\n",
    "plt.xlabel('CCAvg')\n",
    "plt.ylabel('Density')\n",
    "plt.show()\n",
    "\n",
    "\n",
    "# Calculate skewness\n",
    "data_skewness = loan_data[['CCAvg']].skew()\n",
    "print(\"Skewness:\", data_skewness)\n",
    "\n",
    "# Calculate kurtosis\n",
    "data_kurtosis = loan_data['CCAvg'].kurt()\n",
    "print(\"Kurtosis:\", data_kurtosis)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "709e99f7-ed21-417f-9d61-eca6f7394879",
   "metadata": {},
   "source": [
    "- If skewness is greter than 1 then the data distribution is highly skewed.\n",
    "- Distribution has a flatter peak and lighter tails than a normal distribution. Kurtosis < 3. So the data is Platykurtic."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6b00d815-310f-457b-9ff8-91b95076fba8",
   "metadata": {},
   "source": [
    "## <font color = \"red\"> **15).** \n",
    "#### Do you see any outliers in the dataset? If yes, what plot you would think will be suitable to showcase to the stakeholders?\n",
    "**Ans:-**\n",
    "- ***Identify the Outliers***"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "25a27c6a-688f-40f4-b19e-1989b834dbaf",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "      Age  Experience  Income  Family  CCAvg  Mortgage\n",
      "18     46          21     193       2   8.10         0\n",
      "47     37          12     194       4   0.20       211\n",
      "53     50          26     190       3   2.10       240\n",
      "59     31           5     188       2   4.50       455\n",
      "303    49          25     195       4   3.00       617\n",
      "...   ...         ...     ...     ...    ...       ...\n",
      "4659   28           4     199       1   6.33         0\n",
      "4670   52          26     194       1   1.70         0\n",
      "4895   45          20     201       2   2.80         0\n",
      "4981   34           9     195       2   3.00       122\n",
      "4993   45          21     218       2   6.67         0\n",
      "\n",
      "[96 rows x 6 columns]\n"
     ]
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAz8AAAIOCAYAAACWBLP/AAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjguNCwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8fJSN1AAAACXBIWXMAAA9hAAAPYQGoP6dpAABe9ElEQVR4nO3deViU9f7/8dewDYICAsqiiEtmuZCm5XrCjluZ2nq0tPWYWZhLaZZWHlPCkx3NvplWtlguaaeyY5tpG51ESy0PYWqZhJrgFosrA8Pn94c/RkdwQQeGYZ6P6+KK+77fc9/vgWmcF5/7/twWY4wRAAAAANRwPu5uAAAAAACqAuEHAAAAgFcg/AAAAADwCoQfAAAAAF6B8AMAAADAKxB+AAAAAHgFwg8AAAAAr0D4AQAAAOAVCD8AAAAAvALhBwA81Pz582WxWLR+/fqz1t59991q3Lhxpfbz888/a/Lkyfr999/P6fh//vmnbr31VtWvX18Wi0U33HCDS/rYuXOnHnzwQTVr1kyBgYGqW7euunfvrkWLFskYc977Xbx4sWbNmlXuNovFosmTJzuWv/76a1ksFn399dfnfTwAgOv5ubsBAEDN8PPPP+upp55S9+7dywSdJ598UqNHj3ZaN3XqVC1btkyvv/66mjVrpvDw8AvuYfXq1erXr59q166tRx55RAkJCcrPz9c777yj22+/XR9++KEWL14sH5+K/+1v8eLFysjI0JgxY85ae/nll2vNmjVq2bLleTwLAEBlIfwAACpds2bNyqzLyMhQs2bNNGTIEJccIy8vTzfddJNCQ0P13XffKSoqyrHt+uuvV0JCgh577DG1bdtWjz32mEuOeTohISHq1KmTy/Z39OhRBQYGymKxuGyfAOCNOO0NAGqY+fPnq0WLFrJarbr00kv11ltvlVtns9mUnJysSy65RFarVfXq1dM999yjffv2OdU1btxY/fr104oVK3T55ZerVq1auuSSS/T66687HfNvf/ubJOnqq6+WxWKRxWLR/PnzJTmf9vb777/LYrHo888/1+bNm51q/fz8NG3atDK9fvPNN7JYLPr3v/992uf96quvau/evfrnP//pFHxKjR8/XpdccomeffZZFRUVOfq2WCxlTtU79bS17t276+OPP1ZWVpaj3zMFkdOd9rZ+/XoNGDBA4eHhCgwMVLt27fTOO+841ZT2tHLlSv39739XvXr1FBQUpMLCQu3bt0/33Xef4uLiHL+zrl276vPPPz9tLwCAEwg/AFCDzJ8/X/fcc48uvfRSvffee3riiSc0depUffnll051JSUluv766/XPf/5TgwcP1scff6x//vOfWrVqlbp3766jR4861f/vf//T2LFj9dBDD+k///mPEhISNHToUH3zzTeSpOuuu04pKSmSpBdffFFr1qzRmjVrdN1115XpMSYmRmvWrFG7du3UtGlTR+1NN92kAQMG6KWXXpLdbnd6zOzZsxUbG6sbb7zxtM991apV8vX1Vf/+/cvdbrFYNGDAAP3555/asGHD2X+YJ5kzZ466du2q6OhoR79r1qyp0D6++uorde3aVXl5eXrppZf0n//8R23bttWgQYMcIfFkf//73+Xv768FCxbo3Xfflb+/v+644w598MEHmjRpklauXKlXX31VPXv21IEDByrUCwB4K057A4AaoqSkRI8//rguv/xyLVu2zDEy0a1bNzVv3lyxsbGO2nfeeUcrVqzQe++9p5tuusmx/rLLLtMVV1yh+fPn64EHHnCs379/v1avXq1GjRpJkq666ip98cUXWrx4sa666irVq1dPzZs3lyS1bNnyjKd8Wa1WderUSSEhIbLZbE61o0aN0tVXX60PP/zQMQHC7t27tWzZMj355JPy8zv9P1s7duxQvXr1FBwcfNqaJk2aOGorclpay5YtFRYW5uj9fCQlJalVq1b68ssvHc+jT58+2r9/vyZOnKg777zT6VqkHj166OWXX3bax+rVq3Xvvfdq2LBhjnXXX3/9efUDAN6IkR8AqCG2bt2q3bt3a/DgwU6nZMXHx6tLly5OtR999JHCwsLUv39/FRcXO77atm2r6OjoMqdrtW3b1hF8JCkwMFAXX3yxsrKyXPocunfvrssuu0wvvviiY91LL70ki8Wi++6774L3XzrbW1VfO7Nt2zZt2bLFcX3TyT/zvn37Kjs7W1u3bnV6zM0331xmP1deeaXmz5+v5ORkrV271nH6HgDg3BB+AKCGKD31KTo6usy2U9ft2bNHeXl5CggIkL+/v9NXTk6O9u/f71QfERFRZp9Wq7XM6XGuMGrUKH3xxRfaunWrioqKNG/ePN1yyy3lPq+TNWrUSPv27dPhw4dPW1N6bU9cXJwrWz6rPXv2SJLGjRtX5uedlJQkSWV+5jExMWX2s3TpUt1111169dVX1blzZ4WHh+vOO+9UTk5O5T8JAKgBOO0NAGqI0oBS3gfhU9dFRkYqIiJCK1asKHdfderUcX2D52jw4MF69NFH9eKLL6pTp07KycnRiBEjzvq4Xr16aeXKlfrwww916623ltlujNHy5csVHh6u9u3bSzo+giVJhYWFTrWnBpELFRkZKUmaMGGC02mGJ2vRooXTcnmjU5GRkZo1a5ZmzZqlHTt2aPny5Xrssce0d+/e0/4uAQAnEH4AoIZo0aKFYmJi9Pbbb+vhhx92fHjOyspSWlqa0zU//fr105IlS2S329WxY0eXHN9qtUrSBY8GBQYG6r777tPs2bOVlpamtm3bqmvXrmd93L333qtnn31WEyZM0F//+lfVr1/fafv06dO1ZcsW/fOf/5S/v78kOWagS09Pdwofy5cvL7P/CxnpatGihZo3b67//e9/jokhLlSjRo304IMP6osvvtDq1atdsk8AqOkIPwBQQ/j4+Gjq1Km69957deONN2rYsGHKy8vT5MmTy5wyduutt2rRokXq27evRo8erSuvvFL+/v7atWuXvvrqK11//fVnnFmtPK1bt5YkvfLKK6pTp44CAwPVpEmTck+ZO5ukpCRNnz5dGzZs0KuvvnpOjwkLC9P777+vfv36qX379nrkkUd02WWXqaCgQEuXLtWiRYs0aNAgPfLII47HXHHFFWrRooXGjRun4uJi1a1bV8uWLdO3335bZv9t2rTR+++/r7lz56p9+/by8fFRhw4dzvk5vfzyy7r22mvVp08f3X333WrQoIH+/PNPbd68WT/88MMZp/GWpPz8fF199dUaPHiwLrnkEtWpU0fr1q3TihUrTjuaBABwRvgBgBpk6NChkqRnnnlGN910kxo3bqyJEycqNTXVaRIDX19fLV++XM8//7wWLFigadOmyc/PTw0bNlRiYqLatGlT4WM3adJEs2bN0vPPP6/u3bvLbrfrjTfe0N13313hfTVo0EDdunVTenq6Bg8efM6P69q1q9LT0/XMM8/o+eef165du1SrVi1ddtllWrhwYZnJIHx9ffXhhx/qwQcf1P333y+r1apbb71Vs2fPLjNN9+jRo7Vp0yZNnDhR+fn5MsY4JlA4F1dffbW+//57Pf300xozZoxyc3MVERGhli1bauDAgWd9fGBgoDp27KgF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fXt9+eWXmj59un766SetWLFCV199tUaMGCFJ+uijj9SpUycVFhZq0aJF2rx5sxYsWKDQ0FA9+eSTTvvbsWOH1qxZowcffFCvvfaaO54S/r+4uDgtWbJER48edaw7duyY3n77bTVq1Oi892uMUXFxsSta9HqEn2rm8OHDeuedd/TAAw+oX79+Zf6av3z5cjVv3ly1atXS1VdfrTfffFMWi0V5eXmOmrS0NF111VWqVauW4uLiNGrUKB0+fLhqn0gNZbVaFR0d7fRVt25dff311woICNB///tfR+2MGTMUGRmp7OxsSVL37t314IMP6sEHH1RYWJgiIiL0xBNP6OTZ5m02m8aPH68GDRooODhYHTt21Ndff+3YPn/+fIWFhemjjz5Sy5YtZbValZWVVWZ0wRij6dOnq2nTpqpVq5Yuu+wyvfvuu47tX3/9tSwWi7744gt16NBBQUFB6tKli7Zu3er0fJcvX64OHTooMDBQkZGRuummm865V5TVvXt3jRo1SuPHj1d4eLiio6M1efJkp5q8vDzdd999jr/0tm7dWh999JFj+3vvvadWrVrJarWqcePGmjFjhtPjGzdurOTkZN15552qXbu24uPj9Z///Ef79u3T9ddfr9q1a6tNmzZav3690+N436g65b2PPP/882rTpo2Cg4MVFxenpKQkHTp0yPGYk//fb9GihYKCgnTLLbfo8OHDevPNN9W4cWPVrVtXI0eOlN1udzzu1NPeTvbXv/5VDz74oNO6AwcOyGq16ssvv6yU547jSkcBvv/+e91yyy26+OKL1apVKz388MNau3atjhw5onvuuUd9+/bV8uXL1bNnTzVp0kQdO3bUv/71L7388stO+3vjjTfUr18/PfDAA1q6dKnj/93PPvtMgYGBTp8RJGnUqFFKTEx0LM+bN09xcXEKCgrSjTfeqJkzZ/IHtfN0+eWXq1GjRnr//fcd695//33FxcWpXbt2jnWFhYUaNWqU6tevr8DAQHXr1k3r1q1zbC/9d/qzzz5Thw4dZLVatWDBAj311FP63//+5xg1Lv2cuGXLFnXr1k2BgYFq2bKlPv/88zKnuT766KO6+OKLFRQUpKZNm+rJJ59UUVGRU//JycmqX7++6tSpo3vvvVePPfZYmZGmN954Q5deeqkCAwN1ySWXaM6cOa77AVYFg2rltddeMx06dDDGGPPhhx+axo0bm5KSEmOMMZmZmcbf39+MGzfObNmyxbz99tumQYMGRpLJzc01xhiTnp5uateubZ577jnzyy+/mNWrV5t27dqZu+++211Pqca46667zPXXX3/a7Y888oiJj483eXl5ZuPGjcZqtZr333/fsT0xMdHUrl3bjB492mzZssUsXLjQBAUFmVdeecVRM3jwYNOlSxfzzTffmG3btplnn33WWK1W88svvxhjjHnjjTeMv7+/6dKli1m9erXZsmWLOXToUJneJk6caC655BKzYsUK89tvv5k33njDWK1W8/XXXxtjjPnqq6+MJNOxY0fz9ddfm02bNpm//OUvpkuXLo59fPTRR8bX19dMmjTJ/Pzzz2bjxo3m6aefPudecdzJv5vExEQTEhJiJk+ebH755Rfz5ptvGovFYlauXGmMMcZut5tOnTqZVq1amZUrV5rffvvNfPjhh+aTTz4xxhizfv164+PjY6ZMmWK2bt1q3njjDVOrVi3zxhtvOI4XHx9vwsPDzUsvvWR++eUX88ADD5g6deqYa665xrzzzjtm69at5oYbbjCXXnqp472F942qc7r3keeee858+eWXZvv27eaLL74wLVq0MA888IBje+n/+7169TI//PCDSU1NNREREaZ3795m4MCBZtOmTebDDz80AQEBZsmSJY7HxcfHm+eee86xLMksW7bMGGPMokWLTN26dc2xY8cc259//nmnf3fgegcOHDAWi8WkpKSctub99983kkxaWtpZ91dSUmLi4+PNRx99ZIwxpn379ub11183xhhTXFxsoqKizKuvvuqoL1338ssvG2OM+fbbb42Pj4959tlnzdatW82LL75owsPDTWho6AU8S+9U+v/3zJkzTY8ePRzre/ToYZ577jlz/fXXm7vuussYY8yoUaNMbGys+eSTT8ymTZvMXXfdZerWrWsOHDhgjDnx73RCQoJZuXKl2bZtm9m1a5cZO3asadWqlcnOzjbZ2dnmyJEjxm63mxYtWphevXqZjRs3mv/+97/myiuvdPr/3Rhjpk6dalavXm0yMzPN8uXLTVRUlHnmmWcc2xcuXGgCAwPN66+/brZu3WqeeuopExISYi677DJHzSuvvGJiYmLMe++9Z7Zv327ee+89Ex4ebubPn1+pP1tXIvxUM126dDGzZs0yxhhTVFRkIiMjzapVq4wxxjz66KOmdevWTvWPP/64U/i54447zH333edU89///tf4+PiYo0ePVv4TqMHuuusu4+vra4KDg52+pkyZYowxprCw0LRr184MHDjQtGrVytx7771Oj09MTHT6wGnM8d/ppZdeaowxZtu2bcZisZg//vjD6XE9evQwEyZMMMYc/wAkyWzcuLFMb6UfqA4dOmQCAwPL/KM5dOhQc9tttxljTrypfv75547tH3/8sZHkeJ107tzZDBkypNyfxbn0iuNODT/dunVz2n7FFVeYRx991BhjzGeffWZ8fHzM1q1by93X4MGDTa9evZzWPfLII6Zly5aO5fj4eHP77bc7lrOzs40k8+STTzrWrVmzxkgy2dnZxhjeN6pSee8jt9xyS5m6d955x0RERDiWS//f37Ztm2Pd8OHDTVBQkDl48KBjXZ8+fczw4cMdy2cKP8eOHTPh4eFm6dKlju1t27Y1kydPdsVTxWl89913RpLTH8dO9cwzzxhJ5s8//zzr/lauXGnq1atnioqKjDHHg3TXrl0d20eNGmX++te/OpY/++wzExAQ4Nj3oEGDzHXXXee0zyFDhhB+zkPp+/2+ffuM1Wo1mZmZ5vfffzeBgYFm3759jvBz6NAh4+/vbxYtWuR4rM1mM7GxsWb69OnGmBP/Tn/wwQdOx/jHP/7hFEaMMebTTz81fn5+jvd0Y4xZtWpVmfBzqunTp5v27ds7ljt27GhGjBjhVNO1a1en48XFxZnFixc71UydOtV07tz5jD+b6sSvqkeacHpbt27V999/7xgq9fPz06BBg/T666+rZ8+e2rp1q6644gqnx1x55ZVOyxs2bNC2bdu0aNEixzpjjEpKSpSZmalLL7208p9IDXb11Vdr7ty5TuvCw8MlSQEBAVq4cKESEhIUHx9f7qkmnTp1ksVicSx37txZM2bMkN1u1w8//CBjjC6++GKnxxQWFioiIsKxHBAQoISEhNP2+PPPP+vYsWPq1auX03qbzeY05C7JaT8xMTGSpL1796pRo0bauHGjhg0bVu4xzrVXlHXq7y4mJkZ79+6VJG3cuFENGzYs83MttXnzZl1//fVO67p27apZs2bJbrfL19e3zDGioqIkSW3atCmzbu/evYqOjuZ9o4qd+j4SHBysr776SikpKfr5559VUFCg4uJiHTt2TIcPH1ZwcLAkKSgoSM2aNXM8LioqSo0bN1bt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702vXr1M7dq1TXBwsElISHCapQvn56677jKSyny1aNHCPPXUUyYmJsbs37/fUf/BBx+YgIAA8+OPPxpjjl/snpSUZO6//34TEhJi6tatax577DGnCRBsNpuZNGmSady4sfH39zfR0dHmxhtvNOnp6caY4xc9l3cR6qkzSJWUlJjnn3/etGjRwvj7+5t69eqZPn36mNTUVGPMiQspSyfKMMaYH3/80UgymZmZjnXvvfeeadu2rQkICDCRkZHmpptuOudecdypEx6MHj3aafvJs/8Yc3wmqHvuucdERESYwMBA07p1a8csTsYY8+6775qWLVsaf39/06hRI/Pss8867e/UC9yNMWUues3MzDSSHK9NY3jfqCqnm+1t5syZJiYmxtSqVcv06dPHvPXWW07/j5b3/355Fz6fuv8zTXhQ6uDBgyYoKMgkJSWd/xNDhe3evduMGDHCxMfHm4CAANOgQQMzYMAA89VXXzlq1q1bZ2666SZTr149Y7VazUUXXWTuu+8+8+uvv5r169cbSeb7778vd//9+/c3/fv3dyxfccUVRpL58ssvy9S+8sorpkGDBqZWrVrmhhtuMMnJySY6Otrlz7mmO9ussCe/3x89etSMHDnSREZGGqvVarp27er0uyzv32ljjk9UcvPNN5uwsDAjyTHb5+bNm03Xrl1NQECAueSSS8yHH35oJJkVK1Y4HvvII4+YiIgIU7t2bTNo0CDz3HPPlXlfmTJliomMjDS1a9c2f//7382oUaNMp06dnGoWLVrk+GxQt25dc9VVV51xAo/qxmIMJ3Z6sqefflovvfSSdu7c6e5WcBbdu3dX27ZtT3vPDQBwh507d6px48Zat26dLr/8cne3g2pg2LBh2rJli9O96+BZVq9erW7dumnbtm1OE6VUVK9evRQdHa0FCxa4sDv34rQ3DzNnzhxdccUVioiI0OrVq/Xss8+WuUkdAABnU1RUpOzsbD322GPq1KkTwceL/etf/1KvXr0UHBysTz/9VG+++abn3bjSyy1btky1a9dW8+bNtW3bNo0ePVpdu3atUPA5cuSIXnrpJfXp00e+vr56++239fnnn2vVqlWV2HnVI/x4mF9//VXJycn6888/1ahRI40dO1YTJkxwd1sAAA+zevVqXX311br44ov17rvvursduNH333/vuFakadOm+r//+z/de++97m4LFXDw4EGNHz9eO3fuVGRkpHr27FlmJrezsVgs+uSTT5ScnKzCwkK1aNFC7733nnr27FlJXbsHp70BAAAA8Ao+Zy8BAAAAAM9H+AEAAADgFQg/AAAAALwC4QcAAACAVyD8AAAAAPAKhB8AAAAAXoHwAwAAAMArEH4AAAAAeAXCDwAAAACv8P8AR3/eQCad0M0AAAAASUVORK5CYII=",
      "text/plain": [
       "<Figure size 1000x600 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "Q1 = y['Income'].quantile(0.25)\n",
    "Q3 = y['Income'].quantile(0.75)\n",
    "IQR = Q3 - Q1\n",
    "\n",
    "lower_bound = Q1 - 1.5 * IQR\n",
    "upper_bound = Q3 + 1.5 * IQR\n",
    "\n",
    "# Identify outliers\n",
    "outliers = y[(y['Income'] < lower_bound) | (y['Income'] > upper_bound)]\n",
    "print(outliers)\n",
    "\n",
    "## Identify the Outliers using boxplot\n",
    "plt.figure(figsize = (10, 6))\n",
    "sns.boxplot(data = y)\n",
    "plt.title(\"Identify Outliers\")\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8aebfa40-efef-4541-bba8-822971166039",
   "metadata": {},
   "source": [
    "- In the Quantitative data type we have three columns which have the *Outliers* the column name is: 'Income', 'CCAvg' and 'Mortgage'."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "df98643d-555e-4524-b77e-6403d2bfcce2",
   "metadata": {},
   "source": [
    "## <font color = \"red\"> **16).** \n",
    "#### Give us the decile values of the variable ‘Income’ in the dataset.\n",
    "**Ans:-**\n",
    "- Deciles divide the data into ten equal parts. The first decile (D1) represents the 10th percentile, the second decile (D2) represents the 20th percentile, and so on up to the ninth decile (D9) which represents the 90th percentile."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "3fcbb049-9e46-4284-a600-f4b387935b12",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.1     22.0\n",
      "0.2     33.0\n",
      "0.3     42.0\n",
      "0.4     52.0\n",
      "0.5     64.0\n",
      "0.6     78.0\n",
      "0.7     88.3\n",
      "0.8    113.0\n",
      "0.9    145.0\n",
      "Name: Income, dtype: float64\n"
     ]
    }
   ],
   "source": [
    "# Calculate deciles for Income\n",
    "deciles = y['Income'].quantile([0.1 * i for i in range(1, 10)])\n",
    "\n",
    "# Print the deciles\n",
    "print(deciles)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "56a9bcf7-d797-4730-baae-abe7236f262a",
   "metadata": {},
   "source": [
    "## <font color = \"red\"> **17).** \n",
    "#### Give the IQR of all the variables which are quantitative and continuous.\n",
    "- I have created in one DataFrame as **y** for all quantitative variables."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "4b9c9e2b-078a-43a1-b114-bb64aa504078",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Age            20.0\n",
       "Experience     20.0\n",
       "Income         59.0\n",
       "Family          2.0\n",
       "CCAvg           1.8\n",
       "Mortgage      101.0\n",
       "dtype: float64"
      ]
     },
     "execution_count": 44,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Calculate IQR for all quantitative variables \n",
    "Q1 = y.quantile(0.25)\n",
    "Q3 = y.quantile(0.75)\n",
    "IQR = Q3 - Q1\n",
    "IQR"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "645f715a-956f-4992-aaf8-a8de7279624b",
   "metadata": {},
   "source": [
    "## <font color = \"red\"> **18).** \n",
    "#### Do the higher-income holders spend more on credit cards?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "5ba18b6f-d717-487e-bb9a-9cc8f1b3bd99",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAA04AAAIhCAYAAAB5deq6AAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjguNCwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8fJSN1AAAACXBIWXMAAA9hAAAPYQGoP6dpAABocklEQVR4nO3deXwU9f3H8ffmvgNJJBA5TA0qEFAORQiHonIoWJRW1P5EBCmolCIeiFZQQVGs9ahFS/HCA2iLWFRQKAqCQCuIgogKFQUlIRIhCUk25/z+CLvMnjMbAgnwej4ePB7Z2fnO9zPf73e+sx9md8ZhGIYhAAAAAEBAYQ0dAAAAAAA0diROAAAAAGCBxAkAAAAALJA4AQAAAIAFEicAAAAAsEDiBAAAAAAWSJwAAAAAwAKJEwAAAABYIHECAAAAAAskTgBOCVu2bNFNN92kzMxMxcTEKCEhQV26dNGsWbP0888/H/P6v/vuOzkcDr388svuZQ888IAcDofHerNnz/ZYx47y8nI9++yz6tWrl5o2baqoqCidfvrpuuaaa7R69ep6iN6av33xxzAMLViwQL1791azZs0UExOjli1basCAAZo7d+5xiPToXHTRRbrooovcr/3168nO4XBo/PjxDR0GABx3JE4ATnp/+9vf1LVrV33yySe666679N5772nx4sX69a9/reeff16jR49ukLhuvvlmrV+/3mNZqInT/v37lZOTo0mTJik7O1svv/yyVq5cqSeeeELh4eG65JJL9Pnnn9dz5HU3ZcoUXXfddWrXrp3mzp2rZcuWacaMGUpPT9e//vWvhg4vZC1atND69et1xRVXNHQoAIBjLKKhAwCAY2n9+vW65ZZbdNlll+mtt95SdHS0+73LLrtMd9xxh957772g2ygrK1NsbGy9x9ayZUu1bNnyqLYxYsQIff7553r//ffVr18/j/euvfZaTZo0SU2bNj2qOiSpurpaVVVVHu0XqrKyMj311FMaMWKE5syZ4/HeyJEjVVNTc7RhHnfR0dG68MILGzoMAMBxwBUnACe1Rx55RA6HQ3PmzPH7oT8qKkpXXnml+/UZZ5yhwYMH680331Tnzp0VExOjBx98UJKUl5ensWPHqmXLloqKilJmZqYefPBBVVVVeWxz7969uuaaa5SYmKjk5GQNHz5ceXl5PnV7f73tjDPO0LZt27R6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npb1PPjgg8rNzdWYMWNUXFysNm3a6Lvvvgu4flpamtauXau//e1vmj9/vt544w2VlpaqWbNmuvDCC7VkyRKde+65kqT77rtPpaWleuGFFzRr1iy1b99ezz//vBYvXmz7h/CuBwn/4Q9/0PDhw9W8eXPdeuutKisr80hm/ElKStKDDz6olStX6t5779W+ffvkcDiUmZmpiRMnavLkyT5XE8aPHy+n06kJEyYoPz9fHTp00LvvvqucnBz3Ou3bt9enn36q6dOn6w9/+IPy8/PVpEkTtW3b1uNrf6F46KGHFB8fr9mzZ+vVV1/VOeeco+eff972M6vsCAsL09tvv6077rhDjz76qCoqKpSTk6PXXntNF154oZo0aWJrO9dee60mTpyoH374wefW65LUr18/LVmyRE8++aRKS0t1+umna8SIEbrvvvvc69TU1Ki6uvqYP4R49OjRysjI0GOPPaabb75ZhmHojDPO0I033uhe5/rrr1d8fLxmzpyp4cOHKzw8XBdeeKE+/PBDW8eQXfHx8VqzZo0effRRzZkzR7t27VJsbKxat26tSy+9lCtOAHw4jEDXywEAaCDfffedMjMz9fjjj+vOO+9s6HCOK9dzjD7++ON6TRQAAEeHK04AADSQ+fPn68cff1THjh0VFhamDRs26PHHH1efPn1ImgCgkSFxAgCggSQmJmrBggWaMWOGSkpK1KJFC40cOVIzZsxo6NAAAF74qh4AAAAAWOB25AAAAABggcQJAAAAACyQOAEAAACAhVPu5hA1NTXau3evEhMT5XA4GjocAAAAAA3EMAwVFxcrIyPD8sHjp1zitHfvXrVq1aqhwwAAAADQSOzZs0ctW7YMus4plzglJiZKqm2cpKSkBo4GAAAAQEMpKipSq1at3DlCMKdc4uT6el5SUhKJEwAAAABbP+Hh5hAAAAAAYIHECQAAAAAskDgBAAAAgAUSJwAAAACwQOIEAAAAABZInAAAAADAAokTAAAAAFggcQIAAAAACyROAAAAAGCBxAkAAAAALJA4AQAAAIAFEicAAAAAsEDiBAAAAAAWSJwAAAAAwEJEQ1b+0Ucf6fHHH9emTZuUm5urxYsXa+jQoUHLrF69WpMmTdK2bduUkZGhu+++W+PGjTs+AdezHw6UqthZpbLySqUlxqikolpFZZVKjo1UfFS4CsucSor1XJ4QE6GS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gcQJAAAAACyQOAEAAACABRInAAAAALBA4gQAAAAAFkicAAAAAMACiRMAAAAAWCBxAgAAAAALJE4AAAAAYIHECQAAAAAskDgBAAAAgAUSJwAAAACwQOIEAAAAABZInAAAAADAAokTAAAAAFggcQIAAAAACyROAAAAAGCBxAkAAAAALJA4AQAAAIAFEicAAAAAsEDiBAAAAAAWSJwAAAAAwAKJEwAAAABYIHECAAAAAAskTgAAAABggcQJAAAAACyQOAEAAACABRInAAAAALBA4gQAAAAAFkicAAAAAMACiRMAAAAAWCBxAgAAAAALJE4AAAAAYIHECQAAAAAskDgBAAAAgAUSJwAAAACwQOIEAAAAABYiQi3wzDPP+F3ucDgUExOjrKws9enTR+Hh4UcdHAAAAAA0BiEnTk8++aR++uknlZaWqmnTpjIMQwcPHlRcXJwSEhKUn5+vX/ziF/rwww/VqlWrYxEzAAAAABxXIX9V75FHHtH555+vHTt2qKCgQD///LO++eYbde/eXU8//bR2796t5s2b6/bbbz8W8QIAAADAcecwDMMIpcCZZ56pRYsW6bzzzvNYvnnzZg0bNkzffvut1q1bp2HDhik3N7c+Y60XRUVFSk5OVmFhoZKSkho6HAAAAAANJJTcIOQrTrm5uaqqqvJZXlVVpby8PElSRkaGiouLQ900AAAAADRKISdOF198scaOHavNmze7l23evFm33HKL+vXrJ0naunWrMjMz6y9KAAAAAGhAISdOL7zwglJSUtS1a1dFR0crOjpa3bp1U0pKil544QVJUkJCgp544ol6DxYAAAAAGkLIv3Fy+eqrr/TNN9/IMAydc845Ovvss+s7tmOC3zgBAAAAkELLDUK+HbnLOeeco3POOaeuxQEAAADghBFy4lRdXa2XX35ZK1euVH5+vmpqajze/+CDD+otOAAAAABoDEJOnH7/+9/r5Zdf1hVXXKHs7Gw5HI5jERcAAAAANBohJ04LFizQ3//+d11++eXHIh4AAAAAaHRCvqteVFSUsrKyjkUsAAAAANAohZw43XHHHXr66adVx5vxAQAAAMAJJ+Sv6q1du1Yffvihli1bpg4dOigyMtLj/TfffLPeggMAAACAxiDkxKlJkya66qqrjkUsAAAAANAohZw4vfTSS8ciDgAAAABotEL+jRMAAAAAnGpsXXHq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DockKT09Xbt375YkJScnu/8GAAAAgJNJyL9x6ty5szZu3KizzjpLF198saZOnar9+/fr1VdfVceOHY9FjAAAAADQoEK+4vTII4+oRYsWkqTp06crNTVVt9xyi/Lz8zVnzpx6DxAAAAAAGprDMAyjoYM4nkJ5OjAAAACAk1couYHtK05lZWVasmSJiouL/Va4ZMkSlZeXhx4tAAAAADRythOnOXPm6Omnn1ZiYqLPe0lJSXrmmWc0d+7ceg0OAAAAABoD24nT66+/rokTJwZ8f+LEiXrllVfqIyYAAAAAaFRsJ047duzQueeeG/D9Tp06aceOHfUSFAAAAAA0JrYTp6qqKv30008B3//pp59UVVVVL0EBAAAAQGNiO3Hq0KGD/v3vfwd8f8WKFerQoUO9BAUAAAAAjYntxGnUqFGaPn263nnnHZ/33n77bc2YMUOjRo2q1+AAAAAAoDGIsLvib3/7W3300Ue68sordc455+jss8+Ww+HQ9u3b9c033+iaa67Rb3/722MZKwAAAAA0CNtXnCTptdde04IFC3TWWWfpm2++0VdffaWzzz5b8+fP1/z5849VjAAAAADQoByGYRgNHcTxFMrTgQEAAACcvELJDUK64gQAAAAApyISJwAAAACwQOIEAAAAABZInAAAAADAQsiJ06hRo1RcXOyzvKSkhOc4AQAAADgphZw4vfLKKyorK/NZXlZWpnnz5tVLUAAAAADQmNh+AG5RUZEMw5BhGCouLlZMTIz7verqai1dulTNmjU7JkECAAAAQEOynTg1adJEDodDDodDZ511ls/7DodDDz74YL0GBwAAAACNge3E6cMPP5RhGOrXr58WLVqklJQU93tRUVFq06aNMjIyQg5g9uzZevzxx5Wbm6sOHTroqaeeUu/evS3Lffzxx+rbt6+ys7P12WefhVwvAAAAANhlO3Hq27evJGnXrl1q3bq1HA7HUVe+cOFCTZw4UbNnz1ZOTo7++te/atCgQfryyy/VunXrgOUKCws1YsQIXXLJJdq3b99RxwEAAAAAwTgMwzCsVtqyZYuys7MVFhamLVu2BF23U6dOtivv3r27unTpoueee869rF27dho6dKhmzpwZsNy1116rtm3bKjw8XG+99VZIV5yKioqUnJyswsJCJSUl2S4HAAAA4OQSSm5g64rTeeedp7y8PDVr1kznnXeeHA6H/OVbDodD1dXVtoKsqKjQpk2bdM8993gs79+/v9atWxew3EsvvaT//e9/eu211zRjxgzLesrLy1VeXu5+XVRUZCs+AAAAAHCxlTjt2rVLp512mvvv+rB//35VV1crPT3dY3l6erry8vL8ltmxY4fuuecerVmzRhER9r5lOHPmTG5aAQAAAOCo2Mo+2rRp4/fv+uD9WynDMPz+fqq6ulrXX3+9HnzwQb939QtkypQpmjRpkvt1UVGRWrVqVfeAAQAAAJxybCVOS5Yssb3BK6+80tZ6aWlpCg8P97m6lJ+f73MVSpKKi4u1ceNGbd68WePHj5ck1dTUyDAMRUREaPny5erXr59PuejoaEVHR9uOHwAAAAC82Uqchg4d6vHa+zdO5itEdn/jFBUVpa5du2rFihW66qqr3MtXrFihX/7ylz7rJyUlaevWrR7LZs+erQ8++ED//Oc/lZmZaateAAAAAAhVmJ2Vampq3P+WL1+u8847T8uWLdPBgwdVWFiopUuXqkuXLnrvvfdCqnzSpEmaO3euXnzxRW3fvl233367du/erXHjxkmq/ZrdiBEjagMNC1N2drbHv2bNmikmJkbZ2dmKj48PcdcBAAAAwB7bz3FymThxop5//nn16tXLvWzAgAGKi4vTb3/7W23fvt32toYPH66CggI99NBDys3NVXZ2tpYuXer+HVVubq52794daogAAAAAUK9sPcfJLDY2Vv/973/VsWNHj+VbtmxR9+7dVVZWVq8B1jee4wQAAABACi03sPVVPbPzzz9fEydOVG5urntZXl6e7rjjDl1wwQWhRwsAAAAAjVzIidOLL76o/Px8tWnTRllZWcrKylLr1q2Vm5urF1544VjECAAAAAANKuTfOGVlZWnLli1asWKFvvrqKxmGofbt2+vSSy/1+/wlAAAAADjRhfwbJzOn06no6OgTKmHiN04AAAAApGP8G6eamhpNnz5dp59+uhISErRr1y5J0v33389X9QAAAACclEJOnGbMmKGXX35Zs2bNUlRUlHt5x44dNXfu3HoNDgAAAAAag5ATp3nz5mnOnDn6zW9+o/DwcPfyTp066auvvqrX4AAAAACgMQg5cfrxxx+VlZXls7ympkaVlZX1EhQAAAAANCYhJ04dOnTQmjVrfJb/4x//UOfOneslKAAAAABoTEK+Hfm0adN0ww036Mcff1RNTY3efPNNff3115o3b57eeeedYxEjAAAAADSokK84DRkyRAsXLtTSpUvlcDg0depUbd++XW+//bYuu+yyYxEjAAAAADSokK44VVVV6eGHH9aoUaO0evXqYxUTAAAAADQqIV1xioiI0OOPP67q6upjFQ8AAAAANDohf1Xv0ksv1apVq45BKAAAAADQOIV8c4hBgwZpypQp+uKLL9S1a1fFx8d7vH/llVfWW3AAAAAA0Bg4DMMwQikQFhb4IpXD4Wj0X+MrKipScnKyCgsLlZSU1NDhAAAAAGggoeQGIV9xqqmpqXNgAAAAAHAiCvk3TgAAAABwqrGdOH3wwQdq3769ioqKfN4rLCxUhw4d9NFHH9VrcAAAAADQGNhOnJ566imNGTPG73f/kpOTNXbsWD355JP1GhwAAAAANAa2E6fPP/9cAwcODPh+//79tWnTpnoJCgAAAAAaE9uJ0759+xQZGRnw/YiICP3000/1EhQAAAAANCa2E6fTTz9dW7duDfj+li1b1KJFi3oJCgAAAAAaE9uJ0+WXX66pU6fK6XT6vFdWVqZp06Zp8ODB9RocAAAAADQGth+Au2/fPnXp0kXh4eEaP368zj77bDkcDm3fvl1/+ctfVF1drU8//VTp6enHOuajwgNwAQAAAEjH6AG46enpWrdunW655RZNmTJFrnzL4XBowIABmj17dqNPmgAAAACgLmwnTpLUpk0bLV26VAcOHNDOnTtlGIbatm2rpk2bHqv4AAAAAKDBhZQ4uTRt2lTnn39+fccCAAAAAI2S7ZtDAAAAAMCpisQJAAAAACyQOAEAAACABRInAAAAALBA4gQAAAAAFkicAAAAAMACiRMAAAAAWCBxAgAAAAALJE4AAAAAYIHECQAAAAAskDgBAAAAgAUSJwAAAACwQOIEAAAAABZInAAAAADAAokTAAAAAFggcQIAAAAACyROAAAAAGCBxAkAAAAALJA4AQAAAIAFEicAAAAAsEDiBAAAAAAWSJwAAAAAwAKJEwAAAABYIHECAAAAAAskTgAAAABggcQJAAAAACyQOAEAAACABRInAAAAALBA4gQAAAAAFkicAAAAAMACiRMAAAAAWCBxAgAAAAALJE4AAAAAYIHECQAAAAAskDgBAAAAgAUSJwAAAACwQOIEAAAAABZInAAAAADAAokTAAAAAFggcQIAAAAACyROAAAAAGCBxAkAAAAALJA4AQAAAIAFEicAAAAAsEDiBAAAAAAWGjxxmj17tjIzMxUTE6OuXbtqzZo1Add98803ddlll+m0005TUlKSevTooffff/84RgsAAADgVNSgidPChQs1ceJE3Xfffdq8ebN69+6tQYMGaffu3X7X/+ijj3TZZZdp6dKl2rRpky6++GINGTJEmzdvPs6RAwAAADiVOAzDMBqq8u7du6tLly567rnn3MvatWunoUOHaubMmba20aFDBw0fPlxTp061tX5RUZGSk5NVWFiopKSkOsUNAAAA4MQXSm7QYFecKioqtGnTJvXv399jef/+/bVu3Tpb26ipqVFxcbFSUlICrlNeXq6ioiKPfwAAAAAQigZLnPbv36/q6mqlp6d7LE9PT1deXp6tbTzxxBMqKSnRNddcE3CdmTNnKjk52f2vVatWRxU3AAAAgFNPg98cwuFweLw2DMNnmT/z58/XAw88oIULF6pZs2YB15syZYoKCwvd//bs2XPUMQMAAAA4tUQ0VMVpaWkKDw/3ubqUn5/vcxXK28KFCzV69Gj94x//0KWXXhp03ejoaEVHRx91vAAAAABOXQ12xSkqKkpdu3bVihUrPJavWLFCPXv2DFhu/vz5GjlypN544w1dccUVxzpMAAAAAGi4K06SNGnSJN1www3q1q2bevTooTlz5mj37t0aN26cpNqv2f3444+aN2+epNqkacSIEXr66ad14YUXuq9WxcbGKjk5ucH2AwAAAMDJrUETp+HDh6ugoEAPPfSQcnNzlZ2draVLl6pNmzaSpNzcXI9nOv31r39VVVWVbrvtNt12223u5TfeeKNefvnl4x0+AAAAgFNEgz7HqSHwHCcAAAAA0gnyHCcAAAAAOFGQOAEAAACABRInAAAAALBA4gQAAAAAFkicAAAAAMACiRMAAAAAWCBxAgAAAAALJE4AAAAAYIHECQAAAAAskDgBAAAAgAUSJwAAAACwQOIEAAAAABZInAAAAADAAokTAAAAAFggcQIAAAAACyROAAAAAGCBxAkAAAAALJA4AQAAAIAFEicAAAAAsEDiBAAAAAAWSJwAAAAAwAKJEwAAAABYIHECAAAAAAskTgAAAABggcQJAAAAACyQOAEAAACABRInAAAAALBA4gQAAAAAFkicAAAAAMACiRMAAAAAWCBxAgAAAAALJE4AAAAAYIHECQAAAAAskDgBAAAAgAUSJwAAAACwQOIEAAAAABZInAAAAADAAokTAAAAAFggcQIAAAAACyROAAAAAGCBxAkAAAAALJA4AQAAAIAFEicAAAAAsEDiBAAAAAAWSJwAAAAAwAKJEwAAAABYIHECAAAAAAskTgAAAABggcQJAAAAACyQOAEAAACABRInAAAAALBA4gQAAAAAFkicAAAAAMACiRMAAAAAWCBxAgAAAAALJE4AAAAAYIHECQAAAAAskDgBAAAAgAUSJwAAAACwQOIEAAAAABZInAAAAADAAokTAAAAAFggcQIAAAAACyROAAAAAGCBxAkAAAAALJA4AQAAAIAFEicAAAAAsEDiBAAAAAAWSJwAAAAAwAKJEwAAAABYIHECAAAAAAskTgAAAABggcQJAAAAACxENHQAs2fP1uOPP67c3Fx16NBBTz31lHr37h1w/dWrV2vSpEnatm2bMjIydPfdd2vcuHHHMeL688OBUhU7q3TIWam0hGhVVNeosKxSybGRigwP08GScjWNj1Z5dY2KyiqVHBep+KgIFTurVFJeqVTXe6WVSoqNVHxUuA6WOpUcF6OSiuraMrGRSoiJUMumcQHrLyqrVGpipGIiItyvkw9v7+cSp6IjIxUbFa79xU7FR9cuLyhxKjYqUvHRtWWcFZVKS4jRIVO95jJWMZjboNhZu2+u9kiKqS1fUlGlUueResxtcKisUqmmNkyKjVRCdIQOlVepsDRwO5jbIDnuSBnX9txtf7hPCg6V17Z1kPWiDq+XEBOpuKhw7T/kVFyUdRuUHW5D774rq6rSwUNH2qfo8P5FhoepuKxcKfFH2r1J3JE+KXZ6xp0YY28sJPsZS8WuNo2p3W9zmxwoKVdKvOf4jQoPU0FJbRscTT/4a9P4qHAdKncqIdo03vyU8XcMJdlog+LD24sKD9OB0nI1jTtynCXHHzkGXfWY+9g15pPiIhUbGfhYtXs8mOOOjQrXz4ecahLnf5wXlx0ZIyXlR8aSaxyY29CyDQKMnfKqKpWVVyo51vdYLzhUe6x7lympqNLBkiPjav+h2rnDKoYS55Fjy1lRqdR4zzpdY9G8397jLzHmyN/J8ZGK9ZrjrMaieV40z1HmY9C1r/GH2yAuJlJxh8eIeSwVlJQrITq0NvAunxgbePzFR9euV3h4TnDNI03jj8RjbtO6HA/e23b16YFSp2KiIxUX6Tn3eB+3JRVOxUf59qPVnJSWGKloP+enYqdTCTGe8biOwcRYUz84A4+LBBvnJ/MxXFruNU/H+T8GzWPRex5pYuoTu+1g7ociZ7mamuZmjzFmmnPLKyrd5wd/nzNCmRM8xluxU/ExR8413uPKvd+H51/XMZPo57zsGj9REaGdn34uLVdMZIT7GGwSf2TONa9XUuFUXFRtW3mfY5v4mc/9xVBYWqH9hypU5KxU09hIRUaEqcirngOl5UqMiar9POKsUmp81OG2rlKTuIjaesqr3O95t1WRs1IJMZFKi49SclyUTxs0BuZ2SIpt3LEeSw7DMIyGqnzhwoW64YYbNHv2bOXk5Oivf/2r5s6dqy+//FKtW7f2WX/Xrl3Kzs7WmDFjNHbsWH388ce69dZbNX/+fA0bNsxWnUVFRUpOTlZhYaGSkpLqe5ds+76gRPcu3qrNuw/qmes666WPd+njnQXu9/udc5omD2ynh97Zpo93FiguKty9XqAyl5xzmu4f3EF/eGur1pqW98pK1cNXdVSb1Hif+j/eWaCzmiVozohuuu+trR7b65WVqhlDO+q38zaqWVK07h/cQb+Zu0HnNE/UjKHZ2v1zmf760f+0u6BU80ZfoD+89YVPeXOZQDGY9yfQvvXKStW0IR0UGe7QfW99YbvMyJxMTZi/WaUV1T7tYG4Dc5nRvX4hQ4ZeWOu5vZysVI3ulSmHHJq79tuA9eZkpeqmw/V2ad3EVht8nVes12++0N3f3n3w44FSzV79P58xMtXU3+YxEiyeYGPBzlgyt6n3OA1UZ136wVzGvL0ev0g5qtisjgfzPkwd3EGPvbddH3z1U8D29R7ngcap3RiClZk+NFvT3/lSH3z1k8dy85gNNJbqMg68yzw6tKOqJL9zhasNzm6e6Hf87z9U4d6HES/8V21S42y1QbD5ZZTpeAwUd+fWTTS2z5lqnRKr+/xsI9BYNM+Ldo/1GUOzVVlt6IG3g7e9nTbwLn9zgHnJu+1nmMZIWkKUeyzUZSx6xzAjwPh7ZGhHlVfXBN3vYMdtsPo7nZ6kZ67rEvD8NP2dbVrpFc+0KztIhoLG07l1E1vHg7ndgs3TwcaieR4x90ld+qHfOafp/sHtdf9bX3i0o/cYu6XvmTq9aVxI49dO/b2yUjV1SAflHXTqr2v+Z/szjLm89/nA/DnDbgyuY6h1apzG9TlTLVNi/c4RrjHy+Q+FHu0ebD43x7D3YJkmL9qiNTv2q1XT2IBz0YyhHfXUv7/W8i/zPbZr57ObuR+6tWmqR4d1UkaTWDUm5nZw6dM2rVHGWheh5AYNmjh1795dXbp00XPPPede1q5dOw0dOlQzZ870WX/y5MlasmSJtm/f7l42btw4ff7551q/fr2tOhtD4vTDgVJNXrRFH+8s0Ph+Wdq8+4DHQSTJZ7n5td0yZr2yUvXosE5q2TTOo35JWjGpjx5Ysi1guWlXdtBlf/pIvQ4f3KNf2aiZV2Vr6dZcrdlZoCXjc/TYe18FLO8qEygGO/smSb3bpmlQdnPdu/gL22VyslLVuXVTPfvBTo92kOTRBmaPHN63tf5iyErVoI4tfGIIVq+dNnjhxm560WsyNbfh+H5ZunbOfzyWBxsjVvEEGguBth1oW3bXq0s/eJdxvZZ01LHZaQPXeufZ3J6rj3tnpWlQR99xajcGqzLnmdrExTxmg42lUMeBd5llv++lGe9ut2yDQOPftd7dA8/Rlc9+bKsNgs0v5uMxWNzmuSNQP0gKOC/aHefmedGq7a3awFuwecl7jnGNEfNYqO/jwWzBb7vrzx/sDNo+UuDjNlj9q+7s65PwWsVjtx/sHA/mdgt2bAUbi4H6JJR2cLE7Fs3Han2eG1xxus5Jdfk84u98YP6cYTcG1zE086qOWrp1r9/+drV951ZNPNrdzvGQGB2h8fM3u5MFq886dw88R8u/3BfyZzfvNunTNk1/vq5zo7maU1ha4dEOZo0t1roKJTdosN84VVRUaNOmTerfv7/H8v79+2vdunV+y6xfv95n/QEDBmjjxo2qrKz0W6a8vFxFRUUe/xpasbPKfeB0btXE70Hkvdz82m4Zs7U7C1TsrPKpX5Kqqo2g5aqqDfffzZKiJUnNkmLck1REeFjQ8q4ygWKws2+StGbHfqUnxYRU5uOdBercqolPO3i3gVl6UozfDyeStGZngd8YgtVrpw2aJUUHbcP4aN9v1QYbI1bxBBoLoW7L7np16QfvMq7X9RGbnTZwrWd3e64+XrPT/zi1G4NVGXObuJjHbLCxFOo48C5jyGGrDQKNf9friPCwoDGY2yDY/GI+HoPFbZ47/MXtbyya50W7Y848LwZbz04beAs2L3nPMUfiibY9rkI9HszioyMs26eu9ZdV1oQcj91+sHM8mOMOdmwFG4uB+sTfevU1N5uP1fo8N7jWc52T6vJ5xN/5wPw5w24MrmOoWVJ0wP52tb13u9sZj/sPVXgkC1afdSLCw+r02U3ybJOPduzX/kMVftdrCN7tYNbYYj0eGixx2r9/v6qrq5Wenu6xPD09XXl5eX7L5OXl+V2/qqpK+/f779SZM2cqOTnZ/a9Vq1b1swNHoajsSJJXXlXjdx3v5ebXdst4K3ZW+tTv77VPOdP7h5zVPnUVW5R3lQkUg519836/LmXMMQTb57rEYLUdqzYwv++Pv/eDjRGreAKNhVC3FUqdofaDvzLlVTX1FptVG4S6PXMfHU0MoY5n72VWYymUceBdJpRjPVhM5u1YtYFVncHay+484W8s1qVPQjoGLdogWFl//LV9oP7wJ9SxEKjuQGWO1fnJ6niwKmN1PNT12Ar0ntU26mtuLq7jnGJ3HPj7LFCXON31hng8mMvYqcu73e2MxyKnZ/1Wc1FxWWWdPrv5e7/YGbyu48m7Hbw1pliPhwa/q57D4fB4bRiGzzKr9f0td5kyZYoKCwvd//bs2XOUER+9pNhI99/REf67wHu5+bXdMt4SYyJ96vf32qec6f2EmHCfuhItyrvKBIrBzr55v1+XMuYYgu1zXWKw2o5VG5jf98ff+8HGiFU8gcZCqNsKpc5Q+8FfmeiIsHqLzaoNQt2euY+OJoZQx7P3MquxFMo48C4TyrEeLCbzdqzawKrOYO1ld57wNxbr0ichHYMWbRCsrD/+2j5Qf/gT6lgIVHegMsfq/GR1PFiVsToe6npsBXrPahv1NTcn1nFOsTsO/H0WqEuc7npDPB7MZezU5d3udsZjUoxn/VZzUWJsZJ0+u/l7PzEmeF3Hk3c7eGtMsR4PDZY4paWlKTw83OfqUn5+vs9VJZfmzZv7XT8iIkKpqal+y0RHRyspKcnjX0NLjIlQr6zaeDfvOaicLN/YN+856F7Hez27Zcx6ZaUqMSbCp35Jigh3BC0XEe5w/51fVC5Jyi9yqnfbNElSVXVN0PKuMoFisLNvUu1vnPKLnCGVyclK1eY9B33awbsNzPYVOdU7UAxZqdrnJ4Zg9dppg/yi8qBtWFLu+7+UwcaIVTyBxkKgbQfalt316tIP3mVcr+sjNjtt4FrPvL1A7Wvu495Z/sep3RisypjbxMU8ZoONpVDHgXcZhwxbx3qg8e96XVVdEzQGcxsEm1/Mx2OwuM1zh7+4/Y1F87xo99jKDzJ3eLeJVRt4CzYvec8xR+Iptz2uQj0ezErKqyzHT12Px9jIsJDjqe2HtKDxeP9tZywGO7aCjcVAfeJvvfqam83Han2eG1zrlZRXBd223Thd2zN/zrAbg+sYyi8qD3psbN5z0Kfd7RwPaQlR6tP2yDiy+qxTVV3js926fFbp0zZNaQmN5zdD3u1g1thiPR4aLHGKiopS165dtWLFCo/lK1asUM+ePf2W6dGjh8/6y5cvV7du3RQZeeJkvC2b1t5JqVdWql5cu0s35WT6HExf7i3U/YM7uJe71gtWZvveQs04vF2zXlm1d4lx3WLTXL8k3fbap5ox1H+5GVd11G2vfapeWbV30pm8aIt6ZaWqx5lpGtP7F+qVlarbXv9U04dm+y1vLhMoBvP+BNq3Xlmpmjq4vXqcmRpSmZtyMvXi2l0+7eDdBuYyLZJjdVMv3+3lZKXqpl6ZapEcG7Qfckz12m2DyYu26P7BHQL2XXV1jd8xYu438xgJFk+wseASbCyZ29R7nAaqsy79YC5j3t72vYW2ygSKzW4b5Bzuuy/3FgZtX+8+njrE/zi1G0OwMtOHdnTHY15uHrOBxlJdxoF3mcSoiIBzhasNAo1/8z7c9vqnttsg2PziOh6Djb+crFSN6f0Ld58E6odg86LdY73nmWmaOsS67e20gXd5Vx9btf30oR21/fAYMY+FuoxF7xjM2zaXz0iO1TSL/Q523Aarf8L8zQHH3MNX+Y+nW2aKpg5pHzQeu8eDud2CzdPBxqJ5HrGa66364cu9hX6PB+/9+flQRcjj1079rvFWUWmE9BnGo628zgfmzxl2Y3AdQzlZqWrZNFYPBZgjXGPEu92DzeeuGJLjovTosE7upCHYXDTjqo56ce23Pu1h57ObuR/6tE3TY8M6NaqbLXi3g0tjjPV4aBS3I3/++efVo0cPzZkzR3/729+0bds2tWnTRlOmTNGPP/6oefPmSTpyO/KxY8dqzJgxWr9+vcaNG3dC3o5c8nxGREp8tCq9ng9y0PzsB9MzW3yeDVNWWfvMlKhwFZY5lRgbo9LDz29JjIlUoo1ntjRNOPKME1e5hMPPV4iMqH12Q4Hr2SOHn+MUE3UknvLKI89ZcZU3l7GKwdwGxc4jfxeWHdmHkoraZ8i46vF4jlOAMq7n+gRqB3MbmJ+Jc8jp2b6uZ9r87PWcDO/1kmIjFX34eRrxXs9ssWoD8zMmzH1XVlWlwhL/Y+TQ4ed5uNrdPEZcr6MOxx0fbW8sWI0ln2cllZarSdyRtje3gbmt7PaDdz3ebZrg9RynQGWiTLFVmI4TO23gqvNAkGPQVa+5j11jPiH2yDNt/B2rdo8Hc9xxUeE6UOJUUqyprWOOPM/IfAyUlFcqNeFI33m3oZ02MI95Vxnv5zh5H+tx0b7jraSi9pktrnFVcPjZcHbawNVu5uc4efe397HvPf5cfyebnq0VbG4MNC96zNPO2rY3t49r32Kjjzwbxl/bh9IG3uVdx5O/8RcXXbue+VlLxc4gz/+rw/HgvW3zeSI6ynq/zc9xCuX8lJJw5Hla5nqLnU7Fx3jOUa6xGB8TOB7zuLBzPHg/x8nj2ApwDJrHovc8Yu6TUNrBtT2P5zh571v0kXgqKivd5wfvzxmJdZgTvMdboM8j5v12nRu8n+Nk/tzi+pwRyvnJ/Bynn0vKlRTn+Rwx13qBnuPk73wZqB9czy8qdlaqiek5Tp7HgP/nOBWVVSkpLkIJAZ7j5GqrYmel4qMjlZbQeJ+NZG6HxJjGHWuoTpjbkUu1D8CdNWuWcnNzlZ2drSeffFJ9+vSRJI0cOVLfffedVq1a5V5/9erVuv32290PwJ08eXJID8BtTIkTAAAAgIZzQiVOxxuJEwAAAADpBHmOEwAAAACcKEicAAAAAMACiRMAAAAAWCBxAgAAAAALJE4AAAAAYIHECQAAAAAskDgBAAAAgAUSJwAAAACwQOIEAAAAABZInAAAAADAAokTAAAAAFggcQIAAAAACyROAAAAAGAhoqEDON4Mw5AkFRUVNXAkAAAAABqSKydw5QjBnHKJU3FxsSSpVatWDRwJAAAAgMaguLhYycnJQddxGHbSq5NITU2N9u7dq8TERDkcjoDrFRUVqVWrVtqzZ4+SkpKOY4SAJ8YiGgvGIhoLxiIaC8biic8wDBUXFysjI0NhYcF/xXTKXXEKCwtTy5Ytba+flJTEgYBGgbGIxoKxiMaCsYjGgrF4YrO60uTCzSEAAAAAwAKJEwAAAABYIHEKIDo6WtOmTVN0dHRDh4JTHGMRjQVjEY0FYxGNBWPx1HLK3RwCAAAAAELFFScAAAAAsEDiBAAAAAAWSJwAAAAAwAKJEwAAAABYIHHyY/bs2crMzFRMTIy6du2qNWvWNHRIOMk98MADcjgcHv+aN2/uft8wDD3wwAPKyMhQbGysLrroIm3btq0BI8bJ4qOPPtKQIUOUkZEhh8Oht956y+N9O2OvvLxcv/vd75SWlqb4+HhdeeWV+uGHH47jXuBkYDUWR44c6TNPXnjhhR7rMBZRH2bOnKnzzz9fiYmJatasmYYOHaqvv/7aYx3mxlMTiZOXhQsXauLEibrvvvu0efNm9e7dW4MGDdLu3bsbOjSc5Dp06KDc3Fz3v61bt7rfmzVrlv70pz/p2Wef1SeffKLmzZvrsssuU3FxcQNGjJNBSUmJzj33XD377LN+37cz9iZOnKjFixdrwYIFWrt2rQ4dOqTBgwerurr6eO0GTgJWY1GSBg4c6DFPLl261ON9xiLqw+rVq3Xbbbdpw4YNWrFihaqqqtS/f3+VlJS412FuPEUZ8HDBBRcY48aN81h2zjnnGPfcc08DRYRTwbRp04xzzz3X73s1NTVG8+bNjUcffdS9zOl0GsnJycbzzz9/nCLEqUCSsXjxYvdrO2Pv4MGDRmRkpLFgwQL3Oj/++KMRFhZmvPfee8ctdpxcvMeiYRjGjTfeaPzyl78MWIaxiGMlPz/fkGSsXr3aMAzmxlMZV5xMKioqtGnTJvXv399jef/+/bVu3boGigqnih07digjI0OZmZm69tpr9e2330qSdu3apby8PI9xGR0drb59+zIucUzZGXubNm1SZWWlxzoZGRnKzs5mfKLerVq1Ss2aNdNZZ52lMWPGKD8/3/0eYxHHSmFhoSQpJSVFEnPjqYzEyWT//v2qrq5Wenq6x/L09HTl5eU1UFQ4FXTv3l3z5s3T+++/r7/97W/Ky8tTz549VVBQ4B57jEscb3bGXl5enqKiotS0adOA6wD1YdCgQXr99df1wQcf6IknntAnn3yifv36qby8XBJjEceGYRiaNGmSevXqpezsbEnMjaeyiIYOoDFyOBwerw3D8FkG1KdBgwa5/+7YsaN69OihM888U6+88or7x8+MSzSUuow9xifq2/Dhw91/Z2dnq1u3bmrTpo3effddXX311QHLMRZxNMaPH68tW7Zo7dq1Pu8xN556uOJkkpaWpvDwcJ//CcjPz/f5XwXgWIqPj1fHjh21Y8cO9931GJc43uyMvebNm6uiokIHDhwIuA5wLLRo0UJt2rTRjh07JDEWUf9+97vfacmSJfrwww/VsmVL93LmxlMXiZNJVFSUunbtqhUrVngsX7FihXr27NlAUeFUVF5eru3bt6tFixbKzMxU8+bNPcZlRUWFVq9ezbjEMWVn7HXt2lWRkZEe6+Tm5uqLL75gfOKYKigo0J49e9SiRQtJjEXUH8MwNH78eL355pv64IMPlJmZ6fE+c+Opi6/qeZk0aZJuuOEGdevWTT169NCcOXO0e/dujRs3rqFDw0nszjvv1JAhQ9S6dWvl5+drxowZKioq0o033iiHw6GJEyfqkUceUdu2bdW2bVs98sgjiouL0/XXX9/QoeMEd+jQIe3cudP9eteuXfrss8+UkpKi1q1bW4695ORkjR49WnfccYdSU1OVkpKiO++8Ux07dtSll17aULuFE1CwsZiSkqIHHnhAw4YNU4sWLfTdd9/p3nvvVVpamq666ipJjEXUn9tuu01vvPGG/vWvfykxMdF9ZSk5OVmxsbG2zsuMx5NUg93PrxH7y1/+YrRp08aIiooyunTp4r79JHCsDB8+3GjRooURGRlpZGRkGFdffbWxbds29/s1NTXGtGnTjObNmxvR0dFGnz59jK1btzZgxDhZfPjhh4Ykn3833nijYRj2xl5ZWZkxfvx4IyUlxYiNjTUGDx5s7N69uwH2BieyYGOxtLTU6N+/v3HaaacZkZGRRuvWrY0bb7zRZ5wxFlEf/I1DScZLL73kXoe58dTkMAzDOP7pGgAAAACcOPiNEwAAAABYIHECAAAAAAskTgAAAABggcQJAAAAACyQOAEAAACABRInAAAAALBA4gQAAAAAFkicAAAAAMACiRMAAAAAWCBxAgA0WiNHjtTQoUMbOgwAAEicAAAAAMAKiRMA4IRw0UUXacKECbr77ruVkpKi5s2b64EHHvBY5+DBg/rtb3+r9PR0xcTEKDs7W++88477/UWLFqlDhw6Kjo7WGWecoSeeeMKj/BlnnKEZM2ZoxIgRSkhIUJs2bfSvf/1LP/30k375y18qISFBHTt21MaNGz3KrVu3Tn369FFsbKxatWqlCRMmqKSk5Ji1BQDg+CNxAgCcMF555RXFx8frP//5j2bNmqWHHnpIK1askCTV1NRo0KBBWrdunV577TV9+eWXevTRRxUeHi5J2rRpk6655hpde+212rp1qx544AHdf//9evnllz3qePLJJ5WTk6PNmzfriiuu0A033KARI0bo//7v//Tpp58qKytLI0aMkGEYkqStW7dqwIABuvrqq7VlyxYtXLhQa9eu1fjx449r2wAAji2H4Zr5AQBoZEaOHKmDBw/qrbfe0kUXXaTq6mqtWbPG/f4FF1ygfv366dFHH9Xy5cs1aNAgbd++XWeddZbPtn7zm9/op59+0vLly93L7r77br377rvatm2bpNorTr1799arr74qScrLy1OLFi10//3366GHHpIkbdiwQT169FBubq6aN2+uESNGKDY2Vn/961/d2127dq369u2rkpISxcTEHJO2AQAcX1xxAgCcMDp16uTxukWLFsrPz5ckffbZZ2rZsqXfpEmStm/frpycHI9lOTk52rFjh6qrq/3WkZ6eLknq2LGjzzJXvZs2bdLLL7+shIQE978BAwaopqZGu3btquuuAgAamYiGDgAAALsiIyM9XjscDtXU1EiSYmNjg5Y1DEMOh8NnWbA6XOv7W+aqt6amRmPHjtWECRN8ttW6deugMQEAThwkTgCAk0KnTp30ww8/6JtvvvF71al9+/Zau3atx7J169bprLPOcv8Oqi66dOmibdu2KSsrq87bAAA0fnxVDwBwUujbt6/69OmjYcOGacWKFdq1a5eWLVum9957T5J0xx13aOXKlZo+fbq++eYbvfLKK3r22Wd15513HlW9kydP1vr163Xbbbfps88+044dO7RkyRL97ne/q4/dAgA0EiROAICTxqJFi3T++efruuuuU/v27XX33Xe7f7/UpUsX/f3vf9eCBQuUnZ2tqVOn6qGHHtLIkSOPqs5OnTpp9erV2rFjh3r37q3OnTvr/vvvV4sWLephjwAAjQV31QMAAAAAC1xxAgAAAAALJE4AAAAAYIHECQAAAAAskDgBAAAAgAUSJwAAAACwQOIEAAAAABZInAAAAADAAokTAAAAAFggcQIAAAAACyROAAAAAGCBxAkAAAAALPw/grzOYrfFsbYAAAAASUVORK5CYII=",
      "text/plain": [
       "<Figure size 1000x600 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Correlation between income and credit card spending: -0.0023850077511431513\n"
     ]
    }
   ],
   "source": [
    "# Visualize the relationship\n",
    "plt.figure(figsize=(10, 6))\n",
    "sns.scatterplot(x='Income', y='CreditCard', data=loan_data)\n",
    "plt.title('Credit Card Spending vs. Income')\n",
    "plt.xlabel('Income')\n",
    "plt.ylabel('Credit Card Spending')\n",
    "plt.show()\n",
    "\n",
    "# Correlation Analysis\n",
    "correlation = loan_data['Income'].corr(loan_data['CreditCard'])\n",
    "print(\"Correlation between income and credit card spending:\", correlation)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "120f7218-6775-4b44-a173-bce9a4b8ed1c",
   "metadata": {},
   "source": [
    "- Linear relationship lies among the some numbers, like if corr. is (0 - 0.2) then strongly weak correlation and (0.2 - 0.5) then moderate corr. and (0.5 - 0.7) then strong corr., is greater than (0.7) then very strong correlation.\n",
    "- Here, corr. between income and credit card have Strongly Weak Correlation. It mean higher-income holders not spend more on credit cards."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "fc9f5f23-b3ec-4486-b43f-b190ef2f0be1",
   "metadata": {},
   "source": [
    "## <font color = \"red\">**19).** \n",
    "#### How many customers use online banking? Do customers using bank internet facilities have higher incomes?\n",
    "- groupby function works for doing some aggregation fuction to find who is using online banking or not. The value retreive **1** is who is using online banking and **0** is who is not use online banking. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "f8c49095-4b2e-4b83-bd04-72179e1aadfb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Online\n",
      "0    72.978671\n",
      "1    74.311662\n",
      "Name: Income, dtype: float64\n",
      "Customer using Online Banking is:  2984\n"
     ]
    }
   ],
   "source": [
    "# Calculate avg income\n",
    "avg_income = loan_data.groupby('Online')['Income'].mean()\n",
    "print(avg_income)\n",
    "\n",
    "users_count = loan_data['Online'].sum()\n",
    "print(\"Customer using Online Banking is: \", users_count)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "eb6098db-4191-48bb-90ca-ab9e9a21dde7",
   "metadata": {},
   "source": [
    "- Total 2984 customers who is using the online banking.\n",
    "- Customers who are using bank internet facilities avg income is : 74.311662"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "603d5901-359f-4d94-ad7e-3d3b07a07c03",
   "metadata": {},
   "source": [
    "## <font color = \"red\">**20).** \n",
    "#### Using the z-score of the income variable, find out the number of observations outside the +-3σ."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "id": "b46ca33f-e966-4891-8204-c97de9ba5841",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Observation indicating as Outliers : \n",
      " ID                      8891.00\n",
      "Age                       93.00\n",
      "Experience                45.00\n",
      "Income                   442.00\n",
      "ZIP Code              185741.00\n",
      "Family                     4.00\n",
      "CCAvg                     13.34\n",
      "Education                  2.00\n",
      "Mortgage                 306.00\n",
      "Personal Loan              0.00\n",
      "Securities Account         0.00\n",
      "CD Account                 1.00\n",
      "Online                     2.00\n",
      "CreditCard                 1.00\n",
      "dtype: float64\n"
     ]
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAA1IAAAIOCAYAAACyHTw/AAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjguNCwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8fJSN1AAAACXBIWXMAAA9hAAAPYQGoP6dpAAA8aklEQVR4nO3de3RU5b3G8WfMZRJCEkhGMgwkGDXcTLAICoTWYCFQFCiNNlYuYksVG+EYLkWBqqGnhspRoAXFQlVQoGm7AOuRVggFUhHtiVEOt4hokUBNmgZjQiAXDPv8wWGWY7jkxYQ9Sb6ftfZazLt/e+a3p+9Jz9N37z0Oy7IsAQAAAAAa7Sq7GwAAAACAloYgBQAAAACGCFIAAAAAYIggBQAAAACGCFIAAAAAYIggBQAAAACGCFIAAAAAYIggBQAAAACGCFIAAAAAYIggBQBtyJ49e/TDH/5Q8fHxCgkJUfv27XXTTTdp4cKF+uyzz+xuT5K0bt06LVmyxJbP/uyzz/SDH/xAnTp1ksPh0NixYy9af/r0aS1fvlyDBg1SZGSkQkND1atXLz366KM6fvz4Zfdx4MABZWVl6ZNPPmmw77777tM111zjM3bNNdfovvvuu+zPAwCYC7S7AQDAlbFy5UplZGSoR48e+ulPf6revXvr9OnTevfdd/X888/r7bff1saNG+1uU+vWrdO+ffuUmZl5xT/7P//zP7Vx40a9+OKLuu666xQVFXXB2lOnTun222/Xzp079cADD+ixxx5TaGio3n77bT399NNat26dcnNz1aNHD+M+Dhw4oPnz52vIkCENQtP5bNy4UREREcafAwC4fAQpAGgD3n77bf3kJz9RamqqXn31VTmdTu++1NRUzZw5U2+88YaNHfqHffv26brrrtP48eMvWTt9+nTl5eUpJydHd999t3f8tttu01133aVbbrlFd955p/73f/9XAQEBzdm2+vbt22TvZVmWampqFBoa2mTvCQCtEZf2AUAbkJ2dLYfDoRUrVviEqHOCg4M1ZswY7+szZ85o4cKF6tmzp5xOpzp16qR7771Xx44d8znuQpeUDRkyREOGDPG+3rFjhxwOh373u99p3rx58ng8ioiI0LBhw3Tw4EGf4zZt2qQjR47I4XB4t3OWL1+uG2+8Ue3bt1d4eLh69uypuXPnXvL8P/vsM2VkZKhLly4KDg7Wtddeq3nz5qm2tlaS9Mknn8jhcGjr1q0qLCz0fu6OHTvO+34lJSV68cUXNWLECJ8QdU737t31yCOPaP/+/Xr11Ve94w6HQ1lZWQ3qv/w9rlq1St///vclnQ1l53pZtWrVBc/vfP85VFZWatasWYqPj1dwcLC6dOmizMxMnTx50qfO4XBo6tSpev7559WrVy85nU6tXr1a0uV/3wDQFrAiBQCtXH19vbZt26Z+/fopNja2Ucf85Cc/0YoVKzR16lSNGjVKn3zyiR577DHt2LFD7733nlwu12X1MnfuXA0ePFi//e1vVVlZqUceeUSjR49WYWGhAgIC9Nxzz+mBBx7Qxx9/3OAyw5ycHGVkZGjatGl6+umnddVVV+mjjz7SgQMHLvqZNTU1uu222/Txxx9r/vz56tOnj958800tWLBAu3fv1qZNm9S5c2e9/fbbysjIUEVFhdauXStJ6t2793nfc/v27friiy8ueg/V2LFjNXfuXOXm5urOO+9s9Hd0xx13KDs7W3PnztWzzz6rm266SZJ03XXXNfo9Tp06pZSUFB07dkxz585Vnz59tH//fj3++OPau3evtm7d6hNQX331Vb355pt6/PHH5Xa71alTp8v+vgGgrSBIAUArV1ZWplOnTik+Pr5R9R988IFWrFihjIwMLV261Dvet29fDRgwQIsXL9aTTz55Wb307t1ba9as8b4OCAhQenq68vPzNXDgQPXu3VsdOnSQ0+nUwIEDfY5966231KFDB/3617/2jg0dOvSSn7l69Wrt2bNHf/jDH7wrPampqWrfvr0eeeQR5ebmKjU1VQMHDlRERITq6uoafPZXFRUVSdJFv9Nz+87VNtbVV1+thIQESWe/r0v1cj6//vWvtWfPHv39739X//79JZ39rrp06aK77rpLb7zxhkaOHOmtr6qq0t69e9WxY0fv2PPPP39Z3zcAtBVc2gcA8LF9+3ZJanCp2C233KJevXrpr3/962W/95cvH5SkPn36SJKOHDlyyWNvueUWff7557rnnnv0pz/9SWVlZY36zG3btiksLEx33XWXz/i58/s659MYX175uVJef/11JSYm6hvf+Ia++OIL7zZixIjzXrL47W9/2ydESZf/fQNAW0GQAoBWzuVyqV27djp8+HCj6s89trtz584N9nk8nq/1WO/o6Gif1+fu16qurr7ksRMnTtSL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GanJkydr5syZio6OVlRUlGbNmqWkpCQNGzasyfoEAAAAgC8zukfq3BPyfvOb36h79+5f+8P/9a9/aeLEiSouLlZkZKT69OmjN954Q6mpqZKk2bNnq7q6WhkZGSovL9eAAQO0ZcsWhYeHe99j8eLFCgwMVHp6uqqrqzV06FCtWrVKAQEBX7s/AAAAADgfoyAVFBSkffv2XfJhD431wgsvXHS/w+FQVlaWsrKyLlgTEhKipUuXaunSpU3SEwAAAABcivHvSN17772XDEAAAAAA0JoZP/68rq5Ov/3tb5Wbm6v+/fsrLCzMZ/+iRYuarDkAAAAA8EfGQWrfvn266aabJEkffvihz76muuQPAAAAAPyZcZDavn17c/QBAAAAAC2G8T1SAAAAANDWGa9ISVJ+fr7++Mc/qqioSHV1dT77NmzY0CSNAQAAAIC/Ml6RysnJ0eDBg3XgwAFt3LhRp0+f1oEDB7Rt2zZFRkY2R48AAAAA4FeMg1R2drYWL16s119/XcHBwfrVr36lwsJCpaenKy4urjl6BAAAAAC/YhykPv74Y91xxx2SJKfTqZMnT8rhcGj69OlasWJFkzcIAAAAAP7G+B6pqKgonThxQpLUpUsX7du3T0lJSfr888916tSpJm+wLSoqksrK7O5CKiy0uwMAAADAPzU6SO3evVvf+MY39K1vfUu5ublKSkpSenq6Hn74YW3btk25ubkaOnRoc/baJhQVST161qumOsDuVgAAAABcQKOD1E033aS+fftq7NixuueeeyRJc+bMUVBQkHbu3Km0tDQ99thjzdZoW1FWprMhKm285LJ5SejQSGn7k/b2AAAAAPihRgept956Sy+++KKefvppLViwQGlpaZo8ebJmz56t2bNnN2ePbZOrUPK8b28PZT3t/XwAAADATzX6YRODBg3SypUrVVJSouXLl+vYsWMaNmyYrrvuOj355JM6duxYc/YJAAAAAH7D+Kl9oaGhmjRpknbs2KEPP/xQ99xzj37zm98oPj5et99+e3P0CAAAAAB+xThIfdl1112nRx99VPPmzVNERIQ2b97cVH0BAAAAgN8yfvz5OXl5eXrxxRe1fv16BQQEKD09XZMnT27K3gAAAADALxkFqaNHj2rVqlVatWqVDh8+rOTkZC1dulTp6ekKCwtrrh4BAAAAwK80OkilpqZq+/btuvrqq3Xv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",
      "text/plain": [
       "<Figure size 1000x600 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import scipy.stats as stats\n",
    "z = stats.zscore(loan_data['Income'])\n",
    "#z.head(10)\n",
    "\n",
    "abs_z = np.abs(z)\n",
    "observations = loan_data[(abs_z > 3)].sum()\n",
    "print(\"Observation indicating as Outliers : \\n\", observations)\n",
    "\n",
    "plt.figure(figsize = (10, 6))\n",
    "plt.hist(loan_data[\"Income\"], bins = 20, color = \"green\", edgecolor = \"blue\")\n",
    "plt.title(\"Counts of Outliers\")\n",
    "plt.ylabel(\"Variables\")\n",
    "plt.show()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

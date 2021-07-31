{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "265603db-afea-4d2e-bb1c-c411b56a8de6",
   "metadata": {},
   "outputs": [],
   "source": [
    "def load_and_process(Table):\n",
    "    #Import libraries\n",
    "    import pandas as pd\n",
    "    import numpy as np\n",
    "    import matplotlib.pyplot as plt\n",
    "    import seaborn as sns\n",
    "    %matplotlib inline\n",
    "\n",
    "    #Import data\n",
    "    data = pd.read_csv(Table)\n",
    "\n",
    "    #Clean, Process, and Wrangle Data\n",
    "    df = data[data.Year > 1799]\\\n",
    "              .drop(columns=['Date', 'Location', 'Name', 'Age', 'Injury', 'Time', 'Unnamed: 14'])\\\n",
    "              .dropna(subset=['Year','Country'])\\\n",
    "              .reset_index(drop=True)\n",
    "    return df"
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
   "version": "3.9.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

# Meta Ads Campaign Performance Analysis 📊

📌 Project Overview
Marketing teams spend heavily across multiple Meta ad campaigns but often lack clarity on which campaigns are profitable and which are wasting budget.

This project processes a dataset of global ad performance data, filters it specifically for Meta campaigns, cleans the raw metrics, engineers accurate marketing KPIs, and applies a custom Python classifier to automate budget optimization decisions.

🧰 Tech Stack
Tool                                        Purpose
Python	                                     Core programming & data pipeline
Pandas	                                     Data cleaning, filtering, and transformation
NumPy	                                      Vectorized, division-safe KPI calculations
Matplotlib & Seaborn	                       Custom data visualizations
Excel / CSV	                                Final reporting export


🧹 Data Cleaning & Preprocessing

Real-world ad data is rarely clean. To ensure mathematically accurate analysis, the pipeline performs the following steps:

Filtering: Safely isolates only Meta and Facebook platform rows, ignoring case-sensitivity and missing values.

Handling Dirty Numerics: Forces all financial/performance columns (impressions, clicks, ad_spend, conversions, revenue) into numeric types.

Error Coercion: Uses errors='coerce' to convert broken text strings, hidden characters, or invalid entries into NaN, which are then filled with 0 so formulas do not crash.

Preventing Division-by-Zero: Uses numpy.where() to safely calculate all ratios (CTR, CPC, CPA, ROAS). If a denominator is 0, the formula returns 0 instead of throwing an error.


🧠 Automated Campaign Classification
The Python script includes a custom rule-based classifier (classify_campaign) that automatically tags every campaign for the marketing team based on its ROAS:

## Status	Rule	Business Action:

✅ Continue	             ROAS ≥ 2.5        	   Strong performer                — scale budget and increase bids.
⚠️ Pause                	1.0 ≤ ROAS < 2.5	     Break-even / underperforming    — needs creative or audience optimization.
❌ Discontinue	          ROAS < 1.0	           Losing money                    — cut spend immediately to prevent further losses.
-  No Spend	             Spend = 0             Inactive campaign               — ignore during optimization.

🧮 Performance Metrics & Formulas:

-> Feature                    Metric	Calculation Formula	                            Why it was calculated (Business Value)

 1) CTR (%)                 	Clicks ÷ Impressions × 100                            	Measures ad attractiveness (how many people clicked after seeing it).
 2) CPC                      	Ad Spend ÷ Clicks	Cost per click;                       helps understand the efficiency of the ad budget.
 3) CPA                      	Ad Spend ÷ Conversions	Cost per acquisition;           shows exactly how much it costs to get a customer.
 4) Conversion Rate (%)      	Conversions ÷ Clicks × 100	                            Measures how effective the landing page/ad is at turning clicks into sales.
 5) ROAS	                    Revenue ÷ Ad Spend	Return on Ad Spend;                 the primary metric used to classify the campaigns (Continue/Pause/Discontinue).




## Set up a Virtual Environment 
  
                           python3 -m venv .venv
                           source .venv/bin/activate

##  Install dependencies
                           pip install -r requirements.txt                   

## Run the Analysis
from the deginated location :
nameofthefile:


                          In terminal    python3 index.py


      

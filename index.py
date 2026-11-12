import pandas as pd
import numpy as np

# ==========================================
# PHASE 1: LOAD & FILTER DATA
# ==========================================
print("Loading dataset...")
# Make sure 'meta_ads_raw.csv' is in your working folder (or update the filename)
df = pd.read_csv("global_ads_performance_dataset.csv")

# Convert the date column to proper datetime format
df['date'] = pd.to_datetime(df['date'])

# Filter for Meta/Facebook ads safely (if the 'platform' column exists)
if 'platform' in df.columns:
    df = df[df['platform'].str.contains('Meta|Facebook', case=False, na=False)].copy()

print(f"Data loaded successfully. Total rows to process: {len(df)}")


# ==========================================
# PHASE 2: CLEAN NUMERICAL COLUMNS
# ==========================================
# Force financial/performance columns into numbers and handle missing values / text errors
num_cols = ['impressions', 'clicks', 'ad_spend', 'conversions', 'revenue']
df[num_cols] = df[num_cols].apply(pd.to_numeric, errors='coerce').fillna(0)


# ==========================================
# PHASE 3: RECALCULATE & ENGINEER KPIS
# ==========================================
# Using np.where to prevent division by zero errors
df['CTR_%'] = np.where(df['impressions'] > 0, (df['clicks'] / df['impressions']) * 100, 0).round(2)
df['CPC'] = np.where(df['clicks'] > 0, df['ad_spend'] / df['clicks'], 0).round(2)
df['CPA'] = np.where(df['conversions'] > 0, df['ad_spend'] / df['conversions'], 0).round(2)
df['Conversion_Rate_%'] = np.where(df['clicks'] > 0, (df['conversions'] / df['clicks']) * 100, 0).round(2)
df['ROAS'] = np.where(df['ad_spend'] > 0, df['revenue'] / df['ad_spend'], 0).round(2)


# ==========================================
# PHASE 4: CAMPAIGN STATUS CLASSIFICATION
# ==========================================
# Rule-based business logic for recommendations:
# - Continue: ROAS >= 2.5 (High return)
# - Pause: 1.0 <= ROAS < 2.5 (Moderate/Break-even return)
# - Discontinue: ROAS < 1.0 (Loss-making)
def classify_campaign(row):
    if row['ad_spend'] == 0:
        return 'No Spend'
    elif row['ROAS'] >= 2.5:
        return 'Continue'
    elif row['ROAS'] >= 1.0:
        return 'Pause'
    else:
        return 'Discontinue'

df['Campaign_Status'] = df.apply(classify_campaign, axis=1)


# ==========================================
# PHASE 5: EXPORT & INSPECT SUMMARY
# ==========================================
# Save the cleaned dataset to CSV
df.to_csv("meta_ads_cleaned_final.csv", index=False)

# Optional: Save to Excel (requires openpyxl installed via pip install openpyxl)
try:
    df.to_excel("meta_ads_cleaned_final.xlsx", index=False)
    print("\nSuccessfully exported cleaned data to CSV and Excel!")
except Exception:
    print("\nSuccessfully exported cleaned data to CSV (Excel export skipped - install openpyxl if needed).")

# Display breakdown results in the console
print("\n" + "="*40)
print(" CAMPAIGN STATUS RECOMMENDATION BREAKDOWN")
print("="*40)
print(df['Campaign_Status'].value_counts())

print("\n" + "="*40)
print(" PREVIEW OF CLEANED DATA (First 5 Rows)")
print("="*40)
print(df[['campaign_type', 'country', 'ad_spend', 'revenue', 'ROAS', 'Campaign_Status']].head())
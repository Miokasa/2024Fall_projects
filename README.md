# 2024Fall_projects
# Final Project: IS 597 PR
# Analyzing Cryptocurrency data (Bitcoin), and its connection with laws and regulations passed
### Overview
This project investigates the relationship between Bitcoin price fluctuations and the introduction of laws and regulations related to cryptocurrency. By analyzing Bitcoin's historical price data alongside key legal events, the goal is to uncover insights into how legal frameworks influence the cryptocurrency market.
### Team Members
[Ananyaa Tanwar](mailto:atanwar2@illinois.edu)  
[Danni Wu](mailto:miokasa@illinois.edu)

[Mengyao Wang](mailto:mengyao66666@illinois.edu)  

### Datasets Used

## Hypotheses 
## Hypothesis 1: Crypto price volatility increases substantially in the days following the implementation of regulatory policies.
Cryptocurrencies are assets that can be influenced by various factors, 
including regulatory interventions. This hypothesis posits that regulatory actions 
introduce uncertainty into the market, resulting in heightened volatility in the days 
following such events. Volatility is assessed using metrics like the standard deviation of 
price changes, daily high-low price ranges, and normalized percentage price changes.

---

### Analysis and Observations

#### 1. **Volatility Metrics**
- **Overall Average Volatility (2017-2024):**
  - During event periods: **0.1**
  - General periods: **0.101**
- These values indicate minimal differences, suggesting that on a broader timescale, volatility during regulatory event periods does not significantly differ from general market conditions.

#### 2. **Price Range**
- **Average Daily Price Range (2017-2024):**
  - During event periods: **1300.539**
  - General periods: **1092.913**
- This highlights more pronounced price fluctuations within single days during regulatory events, supporting the idea that regulatory announcements create short-term market uncertainty.

#### 3. **Normalized Price Change**
- **Average Normalized Price Change (2017-2024):**
  - During event periods: **0.011**
  - General periods: **0.007**
- This indicates slightly more aggressive price movements during regulatory periods.

#### 4. **Yearly Trends**
- While a yearly comparison of average volatility showed no strong or consistent patterns, other charts demonstrated increases in **percentage price change** 
during regulatory event periods. This suggests localized volatility spikes during certain regulatory events, 
even if they do not significantly impact annual averages.

---

### Conclusion
The data provides partial support for the hypothesis:
- **Daily price ranges** and **percentage price changes** are notably higher during regulatory event periods.
- However, the minimal difference in broader volatility metrics suggests that the hypothesis may need refinement.

#### **Revised Hypothesis**
*"Crypto price fluctuations and short-term volatility increase immediately following the implementation of regulatory policies, though the long-term impact on overall market volatility remains minimal."*

This revision better reflects the observed trends, emphasizing **short-term impacts** while acknowledging the lack of significant long-term effects.

---

## (Danni) Hypothesis 2: Bill passed in house has more impact on Bitcoin price trends than a bill that has only been introduced.

---

## Hypothesis 5: Crypto prices react more to bills introduced in Q3 and Q4, compared with Q1 and Q2.
This hypothesis is based on the assumption that end-of-year activities, such as profit-taking, or year-end settlements, could lead to higher volumes and price volatility.​
Effect of bills is assessed using OLS regression model (residuals in OLS equation) and average normalized volume.

---

### Analysis and Observations

#### 1. **Average Residuals**
- **Quaterly Average Residuals (2017-2024):**
  - Q1: **-0.005426**
  - Q2: **-0.003440**
  - Q3: **-0.000717**
  - Q4: **0.007165**
- These values indicate .

#### 2. **Average Volume**
- **Quaterly Average Volumn (2017-2024):**
  - Q1: **0.095791**
  - Q2: **0.082698**
  - Q3: **0.070697**
  - Q4: **0.098344**
- This highlights .

#### 3. **Quarterly Trends**
- The trends are consistent. Both average residual and average volume peak in Q1 and Q4, while they are significantly lower in Q2 and Q3.

---

### Conclusion
The data provides partial support for the hypothesis:
- **Avergae Residuals** and **Average Volume** are notably higher in Q4.
- However, bills introduced in Q1 have a greater impact than Q3. This is because investors might engage in new financial strategies or market expectations for the new year, which could drive higher trading activity.​

#### **Revised Hypothesis**
*"Crypto price fluctuated more in Q1 and Q4, due to the investor behavior."*

This revision better reflects the seasonal trends.

---

## Hypothesis 6: Crypto prices react more to regulations than to supportive bills.​
This hypothesis is based on the assumption that investors are more likely to be influenced by negative information.​ Effect of bills is assessed using average mean and average votatility 14 days before and after the event date.

---

### Analysis and Observations

#### 1. **Type Defination**
- **Quaterly Average Residuals (2017-2024):**
  - Neither type: **..**
  - Potential regulation type: **..**
  - Potential support: **..**
  - Regulation: **..**
  - Support: **..**

#### 2. **Change of Average Return**
- **Quaterly Average Residuals (2017-2024):**
  - Neither type: **-0.010230**
  - Potential regulation type: **-0.000778**
  - Potential support: **0.001275**
  - Regulation: **0.000511**
  - Support: **-0.002650**
- These values .

#### 3. **Average Volatility**
- **14 days before the events:**
  - Neither type: **12.121968**
  - Potential regulation type: **10.823646**
  - Potential support: **12.314108**
  - Regulation: **8.701134**
  - Support: **26.497265**
- This highlights.
- **14 days after the events:**
  - Neither type: **11.117225**
  - Potential regulation type: **17.541913**
  - Potential support: **14.437661**
  - Regulation: **36.847663**
  - Support: **15.045157**
- This highlights.

---

### Conclusion
The data provides partial support for the hypothesis:
- both regulation and potential regulation events have a significant impact on the market, with returns increasing markedly after the events, accompanied by a substantial rise in volatility.​
- Also, Regulatory policies have a positive impact on the market, while supportive policies, on the contrary, have a negative impact. Both direct regulatory bills and potential regulatory bills cause market volatility.
- However, only direct supportive bills result in market fluctuations.​


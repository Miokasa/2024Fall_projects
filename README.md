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
## (Ananyaa) Hypothesis 1: Crypto price volatility increases substantially in the days following the implementation of regulatory policies.
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


## (Danni) Hypothesis 2: Bill passed in house has more impact on Bitcoin price trends than a bill that has only been introduced.
## (Mengyao) Hypothesis 5: Crypto prices react more to bills introduced in Q3 and Q4, compared with Q1 and Q2.
This hypothesis is based on the assumption that end-of-year activities, such as profit-taking, or year-end settlements, could lead to higher volumes and price volatility.​
Effect of bills is assessed using OLS regression model (residuals in OLS equation) and average normalized volume.

---

### Analysis and Observations

#### 1. **Average Residuals**
- **Quaterly Average Residuals (2017-2024):**
  - Q1: **0.1**
  - Q2: **0.101**
  - Q3: **0.101**
  - Q4: **0.101**
- These values indicate minimal differences, suggesting that on a broader timescale, volatility during regulatory event periods does not significantly differ from general market conditions.

#### 2. **Average Volume**
- **Quaterly Average Volumn (2017-2024):**
  - Q1: **1300.539**
  - Q2: **1092.913**
  - Q3: **1092.913**
  - Q4: **1092.913**
- This highlights more pronounced price fluctuations within single days during regulatory events, supporting the idea that regulatory announcements create short-term market uncertainty.

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
## (Mengyao) Hypothesis 6: Crypto prices react more to regulations than to supportive bills.​
This hypothesis is based on the assumption that Investors are more likely to be influenced by negative information.​

---

### Analysis and Observations

#### 1. **Average Residuals**
- **Quaterly Average Residuals (2017-2024):**
  - Q1: **0.1**
  - Q2: **0.101**
  - Q3: **0.101**
  - Q4: **0.101**
- These values indicate minimal differences, suggesting that on a broader timescale, volatility during regulatory event periods does not significantly differ from general market conditions.

#### 2. **Average Volume**
- **Quaterly Average Volumn (2017-2024):**
  - Q1: **1300.539**
  - Q2: **1092.913**
  - Q3: **1092.913**
  - Q4: **1092.913**
- This highlights more pronounced price fluctuations within single days during regulatory events, supporting the idea that regulatory announcements create short-term market uncertainty.

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

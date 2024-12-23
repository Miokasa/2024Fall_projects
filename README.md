# 2024Fall_projects
# Final Project: IS 597 PR
# Analyzing Cryptocurrency data (Bitcoin), and its connection with laws and regulations passed
### Overview
This project investigates the relationship between Bitcoin price fluctuations and the introduction of laws and regulations related to cryptocurrency. By analyzing Bitcoin's historical price data alongside key legal events, the goal is to uncover insights into how legal frameworks influence the cryptocurrency market.
Please look at final_version_crypto_analysis.ipynb for the final version of the code.
### Team Members
[Ananyaa Tanwar](mailto:atanwar2@illinois.edu)  
[Danni Wu](mailto:miokasa@illinois.edu)
[Mengyao Wang](mailto:mengyao66666@illinois.edu)  

### Links for Datasets 
1. For historical bitcoin price: https://finance.yahoo.com/quote/BTC-USD/history/

2. For historical S&P500 price: https://finance.yahoo.com/quote/%5EGSPC/history/

3. For US laws' data: www.congress.gov

### Datasets Preparation
1. For historical bitcoin price: 

   Use yfinance API to get historical data from yahoo finance. 
   ![image](https://github.com/user-attachments/assets/ca8de19a-d777-4da4-9a7a-6bf582206e65)

2. For historical S&P500 price: 

   Use yfinance API to get historical data from yahoo finance. 

3. For US data: 

   Firstly, filter and download raw data from www.congress.gov. Specifically, we navigated to the "Advanced Searches" feature on the website and applied the following filters:
   1. Congress: Selected all years from 2013 to 2024.
   2. Words and Phrases: Chose the "Only these fields" option and searched within "Title" and "Summaries" using keywords like cryptocurrency, blockchain, and bitcoin.
   3. Legislation Types: Included all legislation types.
   4. Actions/Status: Allowed any action status.
   ![image](https://github.com/user-attachments/assets/b5707f0b-37a0-4111-8758-09b52821934d)
   ![image](https://github.com/user-attachments/assets/312bed47-c214-4a94-aa5b-11fc57c4d64b)
   ![image](https://github.com/user-attachments/assets/23333a9b-543c-41c8-97df-617ca3ce4655)
   
   Secondly, filter the progress (in the results_US.csv, 'Progress' column), the types of themes (in the results_US.csv, 'Type' column), and the types of support or regulate (in the US_types.csv, 'Type 1' column) of bills manually.
   1. Progress: Check the 'tracker' line under the detailed description of each bill.
   ![image](https://github.com/user-attachments/assets/1060d6ab-a659-46aa-ab21-848dda7d2634)
   3. Types of themes: Search the content of each bill and make a judgment based on the first sentence of the bill's detailed description.
   4. Types of support or regulation:  Search the content of each bill and make a judgment based on the following criteria:
      - Neither type: neither related to crypto nor related to blockchain or cybersecurity.
      - Potential regulation type: directly related to blockchain or cybersecurity & tend to regulate.
      - Potential support: directly related to blockchain or cybersecurity & tend to support.
      - Regulation: directly related to crypto & tend to regulate.
      - Support: directly related to crypto & tend to support.



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


## (Danni) Hypothesis 2: Bills that have passed the House have a greater impact on Bitcoin volatility during the date of introduction period compared to those that are only introduced.
This hypothesis is based on the assumption that regulatory bills that have passed the House are seen as more likely to be enacted, which may create greater market certainty or uncertainty.
analyzes how Bitcoin price changes (%PriceChange) are influenced by U.S. legislative events related to cryptocurrency, specifically during a time window around the introduction or passage of laws.
Using bootstrap resampling to estimate the distribution of mean differences between the impacts of two types of legislative events: "Introduced" and "Passed House."
---

### Analysis and Observations

#### 1. **Bootstrap mean difference**
- **%PriceChange**
  -  mean difference:0.146
- This indicates that the market reacts more strongly (positively or with greater volatility) when legislation is first introduced compared to passed House .

#### 2. **Confidence level**
- **Confidence Interval for the mean difference**
  -  95% CI:(0.113, 0.182) > 0
- The entire interval is positive (above 0), it suggests that "Introduced" events have a greater positive impact on %PriceChange than "Passed House" events.

#### 3. **Coefficients**
- **Passed_House**
  -  Coefficient = 0.0079, p-value = 0.501
- **Passed_House_Squared**
  -   Coefficient = 0.0065, p-value = 0.584
- **Interaction term**
  -   Passed_House_unrelated:-0.2398,p<0.001
  -   Passed_house_related to cryptocurrencies:-0.0946,p=0.017
- This suggests that the relationship between the date of introduction and Bitcoin volatility, once squared (to account for non-linearity), is still not significant. However, the interaction terms, such as Passed_House_unrelated and Passed_House_related to cryptocurrencies, have a statistically significant reduction in volatility.

---

### Conclusion
- Based on the analysis, Hypothesis 2 is partially supported. 
- While **introduced bills** have a greater immediate impact on Bitcoin **volatility**, as indicated by the positive mean difference and significant confidence interval, the passage of bills by the House does not show a significant effect on volatility. 
- The **interaction terms** suggest that the impact of passed bills depends on their content, especially those related to cryptocurrency. 

### Limitations:
- The relatively low R-squared suggests the model captures only part of the factors influencing Bitcoin volatility, indicating room for improvement.
- Variables like market sentiment, global economic conditions, or unrelated cryptocurrency events could play critical roles but are absent here.


## (Danni) Hypothesis 3: Time to the next regulatory action does not have a significant effect on market volatility
This hypothesis is based on the assumption that anticipation or proximity of a regulatory event might not necessarily impact market participants' behavior or trading decisions significantly. By analyzing the correlation between the time to the next action and volatility, and testing for statistical significance through p-values and regression coefficients

---

### Analysis and Observations

#### **Coefficients**
- **Time_to_Next_Action**
  -  Coefficient = 0.0128, and p-value = 0.000
- **Time_to_Next_Action_Squared**
  -   Coefficient = -7.24e-08, and p-value = 0.000
- This indicates that the time leading up to the next regulatory action has a positive and statistically significant impact on Bitcoin volatility.
- The negative coefficient suggests that as time to the next action increases, the volatility's impact diminishes at a decreasing rate and significant non-linear effect.

---

### Conclusion
- Hypothesis 3 is not supported by the data. 
- The analysis shows that the time to the next regulatory action does have a significant effect on Bitcoin volatility, with a positive impact indicated by the coefficient for Time_to_Next_Action. 
- The non-linear relationship, suggested by the negative coefficient for Time_to_Next_Action_Squared, indicates that while the impact of time on volatility is positive, its effect decreases as time progresses.

### Revised hypothesis
*The revised hypothesis could state: "The time to the next regulatory action significantly affects Bitcoin volatility, with the impact diminishing as the time to the next action increases.* 

The revised hypothesis is based on the observed data, which shows that the time to the next regulatory action has a statistically significant impact on Bitcoin volatility. The positive coefficient for Time_to_Next_Action suggests that as the time to the next action increases, volatility tends to rise. However, the negative coefficient for Time_to_Next_Action_Squared indicates a diminishing effect over time, meaning the impact of time on volatility decreases as the time progresses. This supports the revised hypothesis that the effect diminishes over time, making it more accurate to describe the relationship as non-linear.

### Limitations
- The non-linear effect may not be fully captured by the squared term, suggesting that a more complex model could better explain the relationship.
- The analysis assumes that only the proximity of regulatory actions affects volatility, but other market factors may also play a role.


## (Danni) Hypothesis 4: Regulation types don't influence market volatility.
This hypothesis is based on the assumption that market participants react primarily to the overall existence or progress of regulations rather than the specific category or type of the regulation. By comparing volatility across categories such as anti-money laundering and cybersecurity, analyzing the statistical significance of regulation type variables in the regression model.

---

### Analysis and Observations

#### **Regulation types coefficient**
- **Directly related to anti-money laundering**
  -  Coefficient = -0.1647, and p-value = 0.000
- **Directly related to cryptocurrencies**
  -   Coefficient = 0.0184 and p-value = 0.136 
- **Unrelated regulations**
  -  Coefficient = 0.0662, and p-value = 0.000
- **Directly related to cybersecurity**
  -   Coefficient =  -0.0042, and p = 0.798

---

### Conclusion
- Based on the analysis, the hypothesis  is rejected. 
- Some regulation types show statistically significant impacts on volatility. Specifically, "directly related to anti-money laundering" and "unrelated regulations" are both significant, with p-values less than 0.05. However, the regulation type "directly related to cryptocurrencies" is not statistically significant (p-value = 0.136), and "directly related to cybersecurity" has no significant impact (p-value = 0.798).

### Revised hypothesis
*Certain types of regulations, such as those related to anti-money laundering and unrelated regulations, have a significant influence on Bitcoin market volatility, while others, like those related to cryptocurrencies and cybersecurity, do not*

The data analysis shows that some regulation types, particularly those related to anti-money laundering, are statistically significant in influencing market volatility, while others (cryptocurrencies, cybersecurity) are not. Therefore, it's more accurate to specify which regulations affect volatility rather than assuming all regulation types have no impact.

### Limitations
- TLimited scope of regulation types: The study only considers a subset of regulation types, and other types of regulation could have different effects on volatility.
- Potential for omitted variables: There may be other unobserved factors that influence volatility, which are not captured in the model.
- Model assumptions: The assumptions underlying the regression model, such as linearity and no omitted variables, may not fully hold in this case, which could affect the results.


## (Mengyao) Hypothesis 5: Crypto prices react more to bills introduced in Q3 and Q4, compared with Q1 and Q2.
This hypothesis is based on the assumption that end-of-year activities, such as profit-taking, or year-end settlements, could lead to higher volumes and price volatility.​
The effect of bills is assessed using the OLS regression model (average residual in OLS equation 7 days after the event) and average normalized volume (7 days after the event).
Reasons for using residuals: To eliminate the influence of other known factors. Bitcoin prices and returns are affected by various factors, including macroeconomic indicators and market events (e.g., news and regulatory changes). By using residuals, we can control for known influencing factors, and isolate the independent impact of the policy, focusing on what is left unexplained by the model.

---

### Analysis and Observations

#### 1. **Average Residuals**
- **Quarterly Average Residuals (2017-2024):**
  - Q1: **-0.005426**
  - Q2: **-0.003440**
  - Q3: **-0.000717**
  - Q4: **0.007165**
- Bills impact bitcoin prices most in Q1 and Q4.

#### 2. **Average Volume**
- **Quarterly Average Volumn (2017-2024):**
  - Q1: **0.095791**
  - Q2: **0.082698**
  - Q3: **0.070697**
  - Q4: **0.098344**
- Average volume peaks in Q1 and Q4.

#### 3. **Quarterly Trends**
- The trends are consistent. Both average residual and average volume peak in Q1 and Q4, while they are significantly lower in Q2 and Q3.
- The similarity indicates that residuals effectively capture the indirect impact of policies, particularly through trading behavior.
- Trading behavior mediates the policy's impact on prices.

---

### Conclusion
The data provides partial support for the hypothesis:
- **Avergae Residuals** and **Average Volume** are notably higher in Q4.
- However, bills introduced in Q1 have a greater impact than Q3. This is because investors might engage in new financial strategies or market expectations for the new year, which could drive higher trading activity.​

#### **Revised Hypothesis**
*"Crypto price fluctuated more in Q1 and Q4, due to the investor behavior."*

This revision better reflects the seasonal trends.


## (Mengyao) Hypothesis 6: Crypto prices react more to regulations than to supportive bills.​
This hypothesis is based on the assumption that investors are more likely to be influenced by negative information.​ The effect of bills is assessed using average mean and volatility 14 days before and after the event date. The positivity or negativity of **Change of Average Return** represents investors' confidence in the bills, while the magnitude of **Volatility** reflects investors' expectations of the bills.

---

### Analysis and Observations

#### 1. **Type Definition**
- **Quarterly Average Residuals (2017-2024):**
  - Neither type: **neither related to crypto nor related to blockchain or cybersecurity**
  - Potential regulation type: **directly related to blockchain or cybersecurity & tend to regulate**
  - Potential support: **directly related to blockchain or cybersecurity & tend to support**
  - Regulation: **directly related to crypto & tend to regulate**
  - Support: **directly related to crypto & tend to support**

#### 2. **Change of Average Return**
- **Quarterly Average Residuals (2017-2024):**
  - Neither type: **-0.010230**
  - Potential regulation type: **-0.000778**
  - Potential support: **0.001275**
  - Regulation: **0.000511**
  - Support: **-0.002650**
- From a common-sense perspective, the market reaction to supportive policies should be positive. However, the actual reaction is negative, indicating a lack of investor confidence in the supportive policies.

#### 3. **Volatility**
- **14 days before the events:**
  - Neither type: **12.121968**
  - Potential regulation type: **10.823646**
  - Potential support: **12.314108**
  - Regulation: **8.701134**
  - Support: **26.497265**
- Before the bills were introduced, investors' expectations for directly supportive policies were the highest. Investors' expectations for potentially supportive bills were the second highest.
- Investors generally have positive expectations for supportive bills before they are introduced.
- **14 days after the events:**
  - Neither type: **11.117225**
  - Potential regulation type: **17.541913**
  - Potential support: **14.437661**
  - Regulation: **36.847663**
  - Support: **15.045157**
- After the bills were introduced, investors' expectations for directly regulated policies were the highest. Investors' expectations for potentially regulated bills were the second highest.
- Investors generally have positive expectations for negative bills after they are introduced.
  
---

### Conclusion
The data provides partial support for the hypothesis:
- Crypto prices react more to regulations than to regulatory bills after the events.​
- However, Crypto prices react more to supportive bills before the events.​
- Also, investors have lost confidence in supportive policies but are highly receptive to restrictive policies.

#### **Revised Hypothesis**
*"Crypto prices react more to regulations than to regulatory bills after the bills were introduced."*

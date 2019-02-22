# python-test

The project analysis the NSE index values for NIFTY during a sample time period(could be extended to real time datasets), which in return
would help new stockholders in making decisions related to stock market   

  --> average closing price fluctuations over weeks.
  --> rolling window methhodology to see data variations.
  --> Handling unequal time series due to stock market holidays.
  --> creation of dummy time series against original time series data in order to guide decision making during a shock(in various parameters
      handled individually)
  --> Creating timeseries plot of close prices of stocks/indices with the following features:
  
         -->  Color timeseries in simple blue color.
         -->  Color timeseries between two volume shocks in a different color (Red)
         -->  Gradient color in blue spectrum based on difference of 52 week moving average.
         -->  Mark closing Pricing shock without volume shock to identify volumeless price movement.
         -->  Hand craft partial autocorrelation plot for each stock/index on upto all lookbacks on bokeh 

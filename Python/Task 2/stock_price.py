# Request Module is used to get the fetch the data from the Http Method
import requests


# Function to get live stock data and store in the csv file
def get_stock_data():
    """
    Description : Get Stock function is used to get data from api and store in the csv file

    Approach : In this Api is used to get the stock data and after it will filter the data and store in the csv file
    """
    url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&outputsize=full&apikey=demo" # This is the url Which is used to get the data
    response = requests.get(url) # Request function used to fetch the data from the particular url
    data=response.text # Fetching the text data from the from the url
    data=eval(data) # Decoded the string data
    try: # Checking the status code
        stock_file=open("stock_price.csv",'w') # Opening the Stock Price .csv file in the write mode 
        stock_file.write("Time Series,1. Open,2. High,3. Low,4. Close,5. Volume\n") # Writing the Headings in the csv file
        for keys in data['Time Series (5min)'].keys(): # Iterating by number of keys present in the data['Time Series (5min)']
            stock_file.write(f"{keys},") # Writing the keys in the csv file
            for values in data['Time Series (5min)'][keys].values(): # iterating Each to store its values
                stock_file.write(f"{values},") # Writing the Values of each keys in the csv file
            stock_file.write('\n')
        stock_file.close() # Closing the CSV file
    except Exception as exception: # Handling the error if status code is not ok
        print(f"Error: {exception}") # Displaying the error code

# Calling the Get Stock function
get_stock_data()
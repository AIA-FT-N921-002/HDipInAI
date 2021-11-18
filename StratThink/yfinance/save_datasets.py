import yfinance as yf

company = "AAPL"
interval = "60m"
start = "2019-11-20"
end = "2021-11-17"
file_name = f'datasets/{company}_{interval}_{start}_{end}.csv'


try:
    csv_file = open(file_name, "r")    
    csv_file.close()
    print(f'File \'{file_name}\' already exists')    
except(FileNotFoundError):
    print(f'Saving {file_name}...')
    
    data = yf.download(company, interval=interval, start=start, end=end)
    csv_file = open(file_name, "w")    
    csv_file.write(data.to_csv(line_terminator='\n'))
    csv_file.close()
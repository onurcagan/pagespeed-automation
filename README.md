# PageSpeed Performance Tester

This script allows you to test the performance of a web page using Google's PageSpeed Insights API. You can run the test multiple times and calculate the average performance score for both mobile and desktop strategies.

## Requirements

- Python 3.x
- Requests library (`pip install requests`)

## Usage

1. Edit the `url_to_test` and `strategy` variables inside the `main()` function to set the URL you want to test and the strategy (either `'mobile'` or `'desktop'`).
2. Run the script using the command `python3 pagespeed-automation.py`.

The script will then perform the specified number of runs (default is 10) and print the individual and average performance scores.

## Code Structure

- `fetch_score(url)`: Fetches the performance score for the given URL using the PageSpeed Insights API.
- `build_url(url_to_test, strategy)`: Constructs the API URL with the given web page URL and strategy.
- `main()`: The main function where you can set the URL, strategy, and number of runs, and where the testing process is initiated.

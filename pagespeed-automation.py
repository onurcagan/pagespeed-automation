import requests
import concurrent.futures

def build_url(url_to_test, strategy):
    return f'https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={url_to_test}&strategy={strategy}'

def fetch_score(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Will raise an HTTPError if the HTTP request returned an unsuccessful status code
        data = response.json()
        score = data['lighthouseResult']['categories']['performance']['score']
        return score
    except Exception as e:
        print(f"An error occurred while fetching the score: {e}")
        return None

def main():
    url_to_test = 'https://tesla.com'
    strategy = 'mobile'
    url = build_url(url_to_test, strategy)
    num_runs = 10

    with concurrent.futures.ThreadPoolExecutor(max_workers=num_runs) as executor:
        results = executor.map(fetch_score, [url] * num_runs)

        scores = [score for score in results if score is not None]
        for i, score in enumerate(scores):
            print(f"Run {i+1} Performance Score: {score}")

        average_score = sum(scores) / len(scores) if scores else 0
        print(f"Average Performance Score: {average_score} for {url_to_test}")

if __name__ == '__main__':
    main()
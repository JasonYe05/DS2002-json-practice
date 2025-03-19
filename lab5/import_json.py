import json
import pandas as pd
import os



try:
    with open('C:/Users/jason/DS2002-json-practice/data/schacon.repos.json', 'r') as file:
        data = json.load(file)

    
    repos_list = []
    for i, repo in enumerate(data):
        if i >= 5:  
            break
        repos_list.append({
            'name': repo['name'],
            'html_url': repo['html_url'],
            'updated_at': repo['updated_at'],
            'visibility': repo['visibility']
        })
    

    for repo in repos_list:
        print(f"{repo['name']},{repo['html_url']},{repo['updated_at']},{repo['visibility']}")
    

    df = pd.DataFrame(repos_list)
    df.to_csv('chacon.csv', index=False, header=False)
    print(f"CSV file created at: {os.path.abspath('chacon.csv')}")
    
except FileNotFoundError:
    print(f"ERROR: Could not find the file at {file_path}")
    print("Please check if the path is correct or if you need to adjust permissions")
except Exception as e:
    print(f"An error occurred: {str(e)}")  
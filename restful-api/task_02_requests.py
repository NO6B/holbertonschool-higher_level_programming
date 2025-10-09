import requests
import csv


def fetch_and_print_posts():
    reponse = requests.get("https://jsonplaceholder.typicode.com/posts")
    print("Status Code:", reponse.status_code)
    if reponse.status_code == 200:
        posts = reponse.json()
        for post in posts:
            print(post['title'])


def fetch_and_save_posts():

    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    if response.status_code == 200:
        posts = response.json()

        csv_post = []
        for post in posts:
            csv_post.append({
                "id": post["id"],
                "title": post["title"],
                "body": post["body"]
            })

        with open("posts.csv", "w", newline='', encoding='utf-8') as csvfile:
            fieldnames = ["id", "title", "body"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(csv_post)

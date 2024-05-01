def list_youtube_videos():
    pass


def add_youtube_video(videos):
    pass

def update_youtube_video(videos):
    pass

def delete_youtube_video(videos):
    pass

    videos =[]

def main():
    while True:
        print("\n Youtube Maager App | Choose an option")
        print("1. List all Youtube  Videos")
        print("2. Add a Youtube Video")
        print("3. Update a Youtube Video")
        print("4. Delete a Youtube Video")
        print("5. Exit")

        choice = input("Enter your choice (1/2/3/4/5): ")

    match choice:
        case "1":
            list_youtube_videos(videos)
        case "2":
            add_youtube_video(videos)
        case "3":
            update_youtube_video(videos)
        case "4":
            delete_youtube_video(videos)
        case "5":
            exit()
        case _:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()
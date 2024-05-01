import json

def  load_data():
    try:
        with open("youtube.txt","r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_data_helper(videos):
    with open('youtube.txt',"w") as file: 
        json.dump(videos,file)
def list_youtube_videos(videos):
    print("\n \t\t\tList of all youtube videos")
    print("*" *70)
    for index,video in enumerate(videos,start= 1):
        print(f"{index}. Name : {video['name']} | Duration : {video['time']}" ) 
    print("*" *70)

def add_youtube_video(videos):
    name = input("Enter the youtube video :")
    time = input("Enter the video time : ")
    videos.append({"name":name,"time":time})
    save_data_helper(videos)

def update_youtube_video(videos):
    list_youtube_videos(videos)
    index = int(input("Enter the video number you want to update : "))
    if 1<= index <= len(videos):
        new_video =input("Enter the new name : ")
        new_time = input("Enter the new time : ")
        videos[index-1]= {"name":new_video,"time":new_time}
        save_data_helper(videos)
        print("Video updated successfully")
    else:
        print("Invalid choice. Please try again.")
    

def delete_youtube_video(videos):
    list_youtube_videos(videos)
    input_index = int(input("Enter the video number you want to delete : "))
    if 1<= input_index <= len(videos):
        del videos[input_index-1]
        print("Video deleted successfully")
        save_data_helper(videos)
        
    else:
        print("Invalid choice. Please try again.")

def main():
    videos =load_data()
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
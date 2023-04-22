class RemoteImage:
    def __init__(self, url):
        self.url = url

    def display_image(self):
        # 向伺服器加載並顯示圖片
        print("Displaying image from URL:", self.url)


def main():
    image = RemoteImage("http://example.com/image.jpg")
    image.display_image()


if __name__ == "__main__":
    main()

# 這樣的做法會導致每次圖片顯示的重複加載。

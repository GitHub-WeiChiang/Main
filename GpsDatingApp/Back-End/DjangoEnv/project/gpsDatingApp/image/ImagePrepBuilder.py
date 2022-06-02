import io
from typing import Pattern

from wand.image import Image
from django.core.files.uploadedfile import InMemoryUploadedFile

# Builder Pattern (變形版)
# 快速使用呼叫順序: .format().sample().save().close().getInMemoryImage()

class ImagePrepBuilder:

    # 類別屬性
    # 原圖格式陣列
    origFormatArr: list = ["jpg", "png", "gif", "jpeg", "heic"]
    # 暫存名稱陣列
    tempNameArr: list = ["temp.jpg", "temp.png", "temp.gif", "temp.jpeg"]
    # 暫存格式陣列
    tempFormatArr: list = ["image/jpeg", "image/png", "image/gif", "image/jpeg"]

    # 物件屬性
    # 原圖格式索引
    origFormatIdx: int = -1
    # 暫存相關索引
    tempFormatIdx: int = -1
    # 處理時圖片
    wandImage = None
    # 緩衝暫存位置
    bytesIO = None
    # 輸出圖片
    inMemoryImage = None

    def __init__(self, image):
        # 抓取原圖格式
        self.origFormatIdx = ImagePrepBuilder.origFormatArr.index(image.name.split(".")[-1].lower())
        self.tempFormatIdx = self.origFormatIdx
        # 轉換圖檔屬性
        self.wandImage = Image(file = image)

    # 轉檔 HEIC to JPG
    def format(self):
        if self.origFormatIdx != len(ImagePrepBuilder.origFormatArr) - 1:
            return self

        self.wandImage.format = 'jpg'
        self.tempFormatIdx = 0

        return self

    # 壓縮
    # 目標: 將大邊壓縮至 1000 ~ 1999 為原則
    # 例: >= 2000 -> * 0.5
    #     >= 3000 -> * 0.33
    #     >= 4000 -> * 0.25
    def sample(self):
        # 抓取大邊
        bigEdge = self.wandImage.width if self.wandImage.width > self.wandImage.height else self.wandImage.height

        # 沒有超過 2000 不壓縮
        if bigEdge < 2000:
            return self

        # 壓縮 sample 效能勝於 resize
        self.wandImage.sample(
            int(self.wandImage.width * (1 / int(bigEdge / 1000))),
            int(self.wandImage.height * (1 / int(bigEdge / 1000)))
        )

        return self

    def save(self):
        self.bytesIO = io.BytesIO()
        self.wandImage.save(file = self.bytesIO)

        return self

    def close(self):
        self.wandImage.close()

        return self

    def getInMemoryImage(self):
        self.bytesIO.seek(0)
        self.bytesIO.read()
        size = self.bytesIO.tell()
        self.bytesIO.seek(0)

        self.inMemoryImage = InMemoryUploadedFile(
            self.bytesIO,
            None,
            ImagePrepBuilder.tempNameArr[self.tempFormatIdx],
            ImagePrepBuilder.tempFormatArr[self.tempFormatIdx],
            size,
            None
        )

        return self.inMemoryImage
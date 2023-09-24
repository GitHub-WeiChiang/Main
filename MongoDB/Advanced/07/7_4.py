import pymongo
import pprint

client = pymongo.MongoClient()

db = client.opendata

cursor = db.AQI_geo.find({
    "geometry": {
        # $geoWithin + $box: 查詢從對角線矩形範圍內有多少點座標資料
        "$geoWithin": {
            "$box": [
                [
                    121.52164820995671,
                    25.035613353746356
                ],
                [
                    121.23744562228472,
                    24.850289879333857
                ]
            ]
        }
    }
})

pprint.pprint(list(cursor))


cursor = db.AQI_geo.find({
    "geometry": {
        # $geoWithin + $centerSphere: 查詢某個半徑範圍內的點資料。
        "$geoWithin": {
            "$centerSphere": [
                [
                    121.18799380575814,
                    24.837600387388264
                ],
                # "50 / 6378.1" 是一個數學計算，用於計算地球表面上的一個圓形區域的半徑，
                # 此示例代碼將其用作地理空間查詢的參數查詢某個半徑範圍內的點資料，
                # 具體來說 6378.1 是地球的平均半徑 (以千米為單位)，
                # 當 50 除以 6378.1 時會得到的結果是一個小數，
                # 表示地球表面上的一個圓形區域的半徑，
                # 此半徑被用來定義一個圓形區域以查詢包含在這個區域內的地理點數據，
                # 簡而言之 "50 / 6378.1" 表示要查詢位於以指定座標為中心半徑約為 50 公里的地理點數據。
                50 / 6378.1
            ],
        }
    }
})

pprint.pprint(list(cursor))


cursor = db.AQI_geo.find(
    {
        "geometry": {
            # $geoWithin + $polygon: 搜尋在這個幾何區域內有哪些點座標資料。
            "$geoWithin": {
                "$polygon": [
                    [
                        121.30693703451834,
                        25.144471966881355
                    ],
                    [
                        120.9881317257607,
                        25.064473653568157
                    ],
                    [
                        120.8050427394694,
                        24.753260912464654
                    ],
                    [
                        120.96892658733844,
                        24.67649878218785
                    ],
                    [
                        121.35687038346543,
                        25.035475853133605
                    ],
                    [
                        121.30821736612972,
                        25.145630970343475
                    ]
                ]
            }
        },
    },
    {
        "SiteName": 1,
        "AQI": 1,
        "_id": 0
    }
)

pprint.pprint(list(cursor))


cursor = db.AQI_geo.find(
    {
        "geometry": {
            # $nearSphere + $geometry: 查詢距離該座標點多遠的資料。
            "$nearSphere": {
                "$geometry": {
                    "type": "Point",
                    "coordinates": [
                        121.37353816201767,
                        24.94805722437809
                    ]
                },
                # $minDistance 與 $maxDistance 為可選參數，
                # 此處以超過 5 公里且不到 10 公里為例。
                "$minDistance": 5 * 1000,
                "$maxDistance": 10 * 1000
            }
        }
    },
    {
        "SiteName": 1,
        "AQI": 1,
        "_id": 0
    }
)

pprint.pprint(list(cursor))

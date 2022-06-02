# Singleton

from gpsDatingApp.dao.RegisterInfoDaoSingleton import RegisterInfoDaoSingleton
from gpsDatingApp.models import registerInfo

import threading
lock = threading.Lock()

class ListInitConfig():

    __instance = None
    __isFirstInit: bool = False

    # 開發團隊 email
    DEV_TEAM_EMAIL: set = {
        "albert0425369@gmail.com",
        "nocvi111@gmail.com",
        "nocvi111@feversocial.com",
    }

    # 開發團隊 userId
    DEV_TEAM_USERID: set = set()

    # 事前預約計數地點
    REZ_CNTR_INFO_INIT_FORMAT: dict = {
        # 北部地區
        "臺北市": 0,
        "新北市": 0,
        "基隆市": 0,
        "桃園市": 0,
        "新竹市": 0,
        "新竹縣": 0,
        "苗栗縣": 0,
        # 中部地區
        "臺中市": 0,
        "彰化縣": 0,
        "南投縣": 0,
        # 南部地區
        "雲林縣": 0,
        "嘉義市": 0,
        "嘉義縣": 0,
        "臺南市": 0,
        "高雄市": 0,
        "屏東縣": 0,
        # 東部地區
        "宜蘭縣": 0,
        "花蓮縣": 0,
        "臺東縣": 0,
        # 離島地區
        "澎湖縣": 0,
        "金門縣": 0,
        "連江縣": 0,
        # 以上以外地區
        "其他": 0
    }

    # 國家
    ADV_INFO_CY: set = {
        "",
        # 當前支援
        "TW"
    }

    # 城市
    ADV_INFO_CITY: set = {
        "",
        # 城市代碼
        "KLU", "TPH", "TPE", "TYC", "HSH",
        "HSC", "MAC", "MAL", "TXG", "CWH",
        "CWS", "NTC", "NTO", "YLH", "CHY",
        "CYI", "TNN", "KHH", "IUH", "PTS",
        "ILN", "ILC", "HWA", "HWC", "TTC",
        "TTT", "PEH", "GNI", "KYD", "KMN",
        "MZW", "LNN"
    }

    # 學校
    ADV_INFO_SCH: set = {
        "",
        # 國立大學
        "NTU", "NCHU", "NTNU", "NCKU", "NCCU", "TUN", "NTHU", "NCU", "NTOU", "NKNU",
        "NCUE", "NSYSU", "CCU", "NIU", "NTUE", "TNUA", "NTTU", "NTSU", "NUTN", "NTCU",
        "NTUA", "NDHU", "NCNU", "NTUS", "TNNUA", "NUU", "NCYU", "NUK", "NQU", "UTP",
        "NPTU", "NYCU",
        # 私立大學
        "SCU", "KMU", "THU", "CYCU", "TKU", "CMU", "TMU", "FJU", "FCU", "PCCU",
        "PU", "TTU", "CSMU", "ISU", "CGU", "YZU", "MCU", "HFU", "CHU", "DYU",
        "SHU", "USC", "CJCU", "AU", "TCU", "NHU", "HCU", "KNU", "FGU", "TSU",
        "UKN", "AU", "MDU",
        # 學院
        "CTBC", "MMC", "DILA",
        # 國立科大
        "NTUST", "NTUT", "NYUST", "NPUST", "NFU", "NKUHT", "NUTC", "NCUT", "NPU", "NTUB",
        "NTUNHS", "NKUST",
        # 技術學院
        "TCPA",
        # 專科
        "NTIN", "NTC",
        # 私立科大
        "CYUT", "KSU", "CNU", "STUST", "FYU", "TUT", "MUST", "HKU", "MITUST", "STU",
        "CTUST", "LHU", "KYU", "JUST", "MCUT", "LTU", "YUMT", "CSU", "CTU", "TJU",
        "WZU", "FEU", "SJU", "HWAI", "CUST", "VNU", "TCUST", "YDU", "UCH", "OCU",
        "WFU", "CUTE", "TMUST", "HUST", "HWU", "CLUT", "MEIHO", "CCUST", "AEUST", "TNU",
        "TPCU", "TWU", "NKUT", "HDUT", "CGUST", "TF", "CUFA", "HWH", "TUMT",
        # 技術學院
        "DAHAN", "NANYA", "CKU", "LIT", "TTC",
        # 專科
        "JENTE", "MKC", "TZUHUI", "SZMC", "CTCN", "YUHING", "MHCHCM", "HSC", "SMC", "CJC",
        # 軍警大學
        "CNA", "CAFA", "CMA", "CPU", "NDU",
        # 軍警學院
        "NDMCTSGH",
        # 軍警技術學院
        "AFATS",
        # 軍警專科
        "TPA", "AAROC",
        # 空中大學
        "NOU", "OUK",
        # 其他教育部立案學校法人
        "TBCS", "CCT", "IKTC", "TGST", "IKTCDS", "TTCS"
    }

    # 類組
    ADV_INFO_DEPT: set = {
        "",
        # 18 學群
        "文史哲", "外語", "法政", "社會與心理", "大眾傳播",
        "藝術", "教育", "財經", "管理", "數理化學",
        "工程", "資訊", "地球與環境", "建築與設計", "醫藥衛生",
        "生命科學", "生物資源", "遊憩與運動"
    }

    def __new__(cls):
        if not cls.__instance:
            with lock:
                if not cls.__instance:
                    ListInitConfig.__instance = super().__new__(cls)
        return cls.__instance
    
    def __init__(self):
        if not self.__isFirstInit:
            ListInitConfig.__isFirstInit = True

    def devTeamUserId(self):
        for devEmail in self.DEV_TEAM_EMAIL:
            unit: registerInfo = RegisterInfoDaoSingleton().findByEmail(devEmail)
            if unit == None:
                continue
            self.DEV_TEAM_USERID.add(unit.userId)

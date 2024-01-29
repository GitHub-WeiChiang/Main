LDAP3
=====
```
# 安裝啦
pip install ldap3
```
```
from ldap3 import Server, Connection, SIMPLE, SYNC, ALL
from ldap3.core.exceptions import LDAPBindError, LdapSocketOpenError

# AD 伺服器組態
AD_HOST = "your_ad_server"
SEARCH_BASE = "DC=...,DC=...,DC=..."

user_name = "your_username"
user_password = "your_password"

# 實例化 Server 配置類別
SERVER = Server(host=AD_HOST, get_info=ALL)

# 以使用者身分進行連線 (透過遠端 AD 進行使用者密碼驗證)
try:
    user_conn = Connection(SERVER, user=user_name, password=user_password, auto_bind=True)
    print("Authentication successful")
except LDAPBindError:
    print("Authentication failed: Invalid credentials or user not found.")
except LdapSocketOpenError:
    print("LDAP socket error: Unable to connect to the server.")
```
```
# 查詢用戶對象
dsquery user -name [user_name]

# 我是誰
ad_user_info = connection.extend.standard.who_am_i()

CN: Common Name
DC: Domain Component
OU: Organizational Unit
```
```
# 導入 ldap3 (Lightweight Directory Access Protocol) 輕量級目錄訪問協議基礎模組
from ldap3 import Server, Connection, ALL
# 導入 ldap3 (Lightweight Directory Access Protocol) 輕量級目錄訪問協議例外模組
from ldap3.core.exceptions import LDAPBindError, LdapSocketOpenError

# AD 伺服器組態
AD_HOST = ...
AD_ADMIN_USER = ...
AD_ADMIN_PW = ...

# 掃描入口 (由此開始向下遞歸搜索)
SEARCH_BASE = "DC=...,DC=...,DC=..."

# 組織搜索過濾器
ORG_SEARCH_FILTER = "(CN={})"
# 群組搜索過濾器
GRP_SEARCH_FILTER = "(member={})"
# 所有使用者搜索過濾器
ALL_USER_SEARCH_FILTER = "(objectclass=user)"
# 所有組織搜索過濾器
ALL_ORG_SEARCH_FILTER = "(objectclass=organizationalUnit)"

# 實例化 Server 配置類別
SERVER = Server(host=AD_HOST, get_info=ALL)

user_name = ...
user_password = ...

# 以管理員身分進行連線
try:
    conn = Connection(SERVER, user=AD_ADMIN_USER, password=AD_ADMIN_PW, auto_bind=True)
except LDAPBindError:
    ...
except LdapSocketOpenError:
    ...

# 搜尋指定使用者基本資訊
has_basic_info = conn.search(search_base=SEARCH_BASE, search_filter=ORG_SEARCH_FILTER.format(user_name))

# 搜尋失敗
if not has_basic_info:
    ...

# 取得使用者基本資訊 (含所在組織)
try:
    user_basic_info = json.loads(conn.response_to_json())["entries"][0]
except IndexError:
    ...

# 生成使用者所在組織
user_org = [items.split("=")[-1] for items in user_basic_info["dn"].split(",") if "OU" in [items][0]]

# 搜尋指定使用者進階資訊
has_adv_info = conn.search(search_base=SEARCH_BASE, search_filter=GRP_SEARCH_FILTER.format(user_basic_info["dn"]))

# 搜尋失敗
if not has_adv_info:
    ...

# 取得使用者進階資訊 (含所在群組)
user_adv_info = [entry["dn"] for entry in json.loads(conn.response_to_json())["entries"] if "dn" in entry]

user_grp = list()

# 生成使用者所在群組
for entry in user_adv_info:
    user_grp.append([items.split("=")[-1] for items in entry.split(",") if "CN" in items][0])

# 以使用者身分進行連線 (透過遠端 AD 進行使用者密碼驗證)
try:
    conn = Connection(SERVER, user=user_name, password=user_password, auto_bind=True)
except LDAPBindError:
    ...
except LdapSocketOpenError:
    ...
```
<br />

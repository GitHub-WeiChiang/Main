LDAP3
=====
```
pip install ldap3
```
```
dsquery user -name [user_name]

ad_user_info = connection.extend.standard.who_am_i()

CN: Common Name
DC: Domain Component
OU: Organizational Unit
```
```
from ldap3 import Server, Connection, ALL
from ldap3.core.exceptions import LDAPBindError, LdapSocketOpenError

AD_HOST = ...
AD_ADMIN_USER = ...
AD_ADMIN_PW = ...

SEARCH_BASE = "DC=...,DC=...,DC=..."

ORG_SEARCH_FILTER = "(CN={})"
GRP_SEARCH_FILTER = "(member={})"
ALL_USER_SEARCH_FILTER = "(objectclass=user)"
ALL_ORG_SEARCH_FILTER = "(objectclass=organizationalUnit)"

SERVER = Server(host=AD_HOST, get_info=ALL)

user_name = ...
user_password = ...

try:
    conn = Connection(SERVER, user=AD_ADMIN_USER, password=AD_ADMIN_PW, auto_bind=True)
except LDAPBindError:
    ...
except LdapSocketOpenError:
    ...

has_basic_info = conn.search(search_base=SEARCH_BASE, search_filter=ORG_SEARCH_FILTER.format(user_name))

if not has_basic_info:
    ...

try:
    user_basic_info = json.loads(conn.response_to_json())["entries"][0]
except IndexError:
    ...

user_org = [items.split("=")[-1] for items in user_basic_info["dn"].split(",") if "OU" in [items][0]]

has_adv_info = conn.search(search_base=SEARCH_BASE, search_filter=GRP_SEARCH_FILTER.format(user_basic_info["dn"]))

if not has_adv_info:
    ...

user_adv_info = [entry["dn"] for entry in json.loads(conn.response_to_json())["entries"] if "dn" in entry]

user_grp = list()

for entry in user_adv_info:
    user_grp.append([items.split("=")[-1] for items in entry.split(",") if "CN" in items][0])

try:
    conn = Connection(SERVER, user=user_name, password=user_password, auto_bind=True)
except LDAPBindError:
    ...
except LdapSocketOpenError:
    ...
```
<br />

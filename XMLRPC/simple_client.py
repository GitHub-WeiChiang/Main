import xmlrpc.client
import datetime


if __name__ == '__main__':
    proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")

    today = proxy.today()

    converted = datetime.datetime.strptime(today.value, "%Y%m%dT%H:%M:%S")
    print("Today: %s" % converted.strftime("%d.%m.%Y, %H:%M"))

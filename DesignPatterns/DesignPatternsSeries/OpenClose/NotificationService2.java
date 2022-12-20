public class NotificationService2 {
    public static void main(String[] args) {
        NotificationService2 ns = new NotificationService2();
        // 依照需求傳入各個實作訊息傳遞的類別
        ns.sendNotification(new EmailService(), "helo");
        ns.sendNotification(new MessageService(), "hello");
        ns.sendNotification(new WechatService(), "hello");
    }

    // 透過多型，執行每一個類別的方法。
    public void sendNotification(NotificationService ns, String info) {
        ns.sendNotification(info);
    }
}

// 新增一個接口 (抽象類別)
interface NotificationService {
    public void sendNotification(String info);
}

// 各個通知類型需實作該接口
class EmailService implements NotificationService {
    public void sendNotification(String info) {
        System.out.printf("Email: %s\n", info);
    }
}

// 各個通知類型需實作該接口
class MessageService implements NotificationService {
    public void sendNotification(String info) {
        System.out.printf("Message: %s\n", info);
    }
}

// 各個通知類型需實作該接口
class WechatService implements NotificationService {
    public void sendNotification(String info) {
        System.out.printf("Wechat: %s\n", info);
    }
}

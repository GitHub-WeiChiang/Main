// 使用寄送功能的服務類別
public class NotificationService1 {
    public static void main(String[] args) {
        NotificationService1 ns = new NotificationService1();
        ns.sendNotification("email", "helo");
        ns.sendNotification("message", "hello");
    }

    public void sendNotification(String serviceType, String info) {
        // 因為沒有抽象化的父類別，導致需要進行判斷
        if (serviceType == "email") {
            // 呼叫各自的執行代碼
            sendEmail(info);
        } else if (serviceType == "message") {
            // 呼叫各自的執行代碼
            sendMessage(info);
        }
    }

    public void sendEmail(String info) {
        EmailService es = new EmailService();
        es.sendNotification(info);
    }

    public void sendMessage(String info) {
        MessageService ms = new MessageService();
        ms.sendNotification(info);
    }
}

// 寄送 Email 的功能類別
class EmailService {
    public void sendNotification(String info) {
        System.out.printf("Email: %s\n", info);
    }
}

// 寄送 Message 的功能類別
class MessageService {
    public void sendNotification(String info) {
        System.out.printf("Message: %s\n", info);
    }
}

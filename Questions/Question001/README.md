Question001 - 什麼是 Timing Attack ?
=====
* ### 程式一
* ### Compare two strings using the same time whether they are equal.
* ### This function should be used to mitigate timing attacks.
    ```
    private boolean safeEqual(String a, String b) {
        if (a.length() != b.length()) {
            return false;
        }

        int equal = 0;

        // time-constant comparison.
        for (int i = 0; i < a.length(); i++) {
            // if (a.charAt(i) == b.charAt(i)) {
            //     equal++;
            // }
            equal |= a.charAt(i) ^ b.charAt(i);
        }

        return equal == 0;
    }
    ```
* ### 程式二
* ### 這個方法容易會被計時攻擊破解，透過逐一迭代每一個字元並統計回傳時間。
    ```
    private boolean safeEqual(String a, String b) {
        if (a.length() != b.length()) {
            return false;
        }

        for (int i = 0; i < a.length(); i++) {
            int equal = a.charAt(i) ^ b.charAt(i);
            if (equal != 0) {
                return false;
            }
        }

        return true;
    }
    ```
* ### 有時候不必這麼累，用這個 !
* ### Return True if strings or bytes-like objects a and b are equal, otherwise False, using a “constant-time compare” to reduce the risk of timing attacks.
    ```
    import secrets


    def safe_compare(s1, s2):
        return secrets.compare_digest(s1, s2)


    string1 = "password"
    string2 = "password"

    if safe_compare(string1, string2):
        print("字符串相同")
    else:
        print("字符串不相同")
    ```
<br />

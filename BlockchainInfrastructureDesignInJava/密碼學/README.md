密碼學
=====
3.1 加密與解密
-----
* ### 編碼的過程即加密的過程，加密模塊把可讀信息(明文)處理成代碼形式(密文)。
* ### 解碼的過程即解密的過程，解密模塊把代碼形式(密文)轉換回可讀信息(明文)。
* ### 加解密過程中，密鑰為關鍵角色。
* ### 加密技術: 對稱加密、不對稱加密、不可逆加密。
	* ### 對稱加密: 早期加密算法，加解密密鑰相同，對稱密鑰技術基本類型為分組密碼和序列密碼。
		* ### 算法公開、計算量小、加密速度快、加密效率高。
		* ### 交易雙方使用相同密鑰、安全性無保證。
		* ### 廣泛使用的對稱加密算法: DES、3DES、IDEA、AES(取代DES)
	* ### 不對稱加密: 使用兩把完全不同但又完全匹配的一對鑰匙，即公鑰與私鑰。
		* ### RSA 算法、DSA 算法。
		* ### 數位簽章(Digital Signature)以不對稱加密算法為基礎。
		* ### 安全性高、加密速度慢、效率低。
	* ### 不可逆加密: 加密過程無需密鑰，輸入明文後由系統直接經過加密算法處理成密文，加密後的數據無法解密，必須重新輸入密文，並再次經過相同不可逆加密算法處理，若得到相同加密密文並被系統重新識別，才能真正解密。
		* ### RSA 算法、MD5 算法、SHS 算法。
* ### Java 中 Cipher 類主要提供加密和解密功能， public class Cipher extends Object，構成 Java Cryptographic Extension(JCE) 框架核心。
	* ### Cipher c = Cipher.getInstance("DES/CBC/PKCS5Padding");
	* ### Cipher 類中常用的常量:
		* ### ENCRYPT_MODE: 加密模式。
		* ### DECRYPT_MODE: 解密模式。
		* ### WRAP_MODE: 為密鑰包裝模式。
		* ### UNWRAP_MODE: 為密鑰解包裝模式。
		* ### PUBLIC_KEY: 要解包的密鑰為公鑰。
		* ### PRIVATE_KEY: 要解包的密鑰為私鑰。
		* ### SECRET_KEY: 鑰解包的密鑰為秘密密鑰。
	* ### Cipher 建構式
		* ### protected Cipher (CipherSpi cipherSpi, Provider provider, String transformation)
	* ### 核心方法
		* ### 

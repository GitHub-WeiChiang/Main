/**
 * 
 * @author ChiangWei
 * @date 2022/03/17
 *
 */

package com.example.demo.util;

// A private key. The purpose of this interface is to group (and provide type safety for) all private key interfaces.
import java.security.PrivateKey;
// A public key. This interface contains no methods or constants. It merely serves to group (and provide type safety for) all public key interfaces.
import java.security.PublicKey;
// Testing framework for Java
import org.testng.util.Strings;

// 字符集工具類
import cn.hutool.core.util.CharsetUtil;
// 字符串工具類
import cn.hutool.core.util.StrUtil;
// 安全相關工具類，加密分為三種:
// 1、對稱加密（symmetric），例如：AES、DES等
// 2、非對稱加密（asymmetric），例如：RSA、DSA等
// 3、摘要加密（digest），例如：MD5、SHA-1、SHA-256、HMAC等
import cn.hutool.crypto.SecureUtil;
// 密鑰類型
import cn.hutool.crypto.asymmetric.KeyType;
// RSA公鑰/私鑰/簽名加密解密
// 由於非對稱加密速度極其緩慢，一般文件不使用它來加密而是使用對稱加密，非對稱加密算法可以用來對對稱加密的密鑰加密，這樣保證密鑰的安全也就保證了數據的安全
import cn.hutool.crypto.asymmetric.RSA;
// AES加密算法實現
// 高級加密標準（英語：Advanced Encryption Standard，縮寫：AES），在密碼學中又稱Rijndael加密法對於Java中AES的默認模式是：AES/ECB/PKCS5Padding，如果使用CryptoJS，請調整為：padding: CryptoJS.pad.Pkcs7
import cn.hutool.crypto.symmetric.AES;
// DES加密算法實現
// DES全稱為Data Encryption Standard，即數據加密標準，是一種使用密鑰加密的塊算法Java中默認實現為：DES/CBC/PKCS5Padding
import cn.hutool.crypto.symmetric.DES;
// 對稱算法類型
import cn.hutool.crypto.symmetric.SymmetricAlgorithm;

// 基於 Hutool 工具類的加密解密類
public class DeEnCoderHutoolUtil {
	// 構建 RSA 對象
	private static RSA rsa = new RSA();
	// 獲得私鑰
	private static PrivateKey privateKey = rsa.getPrivateKey();
	// 獲得公鑰
	private static PublicKey publicKey = rsa.getPublicKey();
	
	/**
	 * function RSA 加密通用方法: 不對稱加密解密
	 * 
	 * @param originalContent: 明文
	 * @return 密文
	 */
	public static String rsaEncrypt(String originalContent) {
		// 明文為空時
		if (Strings.isNullOrEmpty(originalContent)) {
			return null;
		}
		
		// 公鑰加密，之後私鑰解密
		return rsa.encryptBase64(originalContent, KeyType.PublicKey);
	}
	
	/**
	 * function RSA 解密通用方法: 不對稱加密解密
	 * 
	 * @param ciphertext 密文
	 * @return 明文
	 */
	public static String rsaDecrypt(String ciphertext) {
		// 密文為空時
		if (Strings.isNullOrEmpty(ciphertext)) {
			return null;
		}
		
		return rsa.decryptStr(ciphertext, KeyType.PrivateKey);
	}
	
	/**
	 * function DES 加密通用方法: 對稱加密解密
	 * 
	 * @param originalContent: 明文
	 * @param key 加密密鑰
	 * @return 密文
	 */
	public static String desEncrypt(String originalContent, String key) {
		// 明文或加密密鑰為空時
		if (Strings.isNullOrEmpty(originalContent) || Strings.isNullOrEmpty(key)) {
			return null;
		}
		
		// 還可以隨機生成密鑰
		// byte[] key = SecureUtil.generateKey(SymmetricAlgorithm.DES.getValue()).getEncoded();
		
		// 構建
		DES des = SecureUtil.des(key.getBytes());
		
		// 加密
		return des.encryptHex(originalContent);
	}
	
	/**
	 * function DES 解密通用方法: 對稱加密解密
	 * 
	 * @param ciphertext 密文
	 * @param key DES 解密密鑰(同加密密鑰)
	 * @return 明文
	 */
	public static String desDecrypt(String ciphertext, String key) {
		// 密文或解密密鑰為空時
		if (Strings.isNullOrEmpty(ciphertext) || Strings.isNullOrEmpty(key)) {
			return null;
		}
		
		// 還可以隨機生成密鑰
		// byte[] key = SecureUtil.generateKey(SymmetricAlgorithm.DES.getValue()).getEncoded();
		
		// 構建
		DES des = SecureUtil.des(key.getBytes());
		
		// 解密
		return des.decryptStr(ciphertext);
	}
}

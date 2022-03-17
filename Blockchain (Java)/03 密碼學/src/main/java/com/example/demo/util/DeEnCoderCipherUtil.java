/**
 * 
 * @author ChiangWei
 * @date 2022/03/15
 *
 */

package com.example.demo.util;

// This class provides a cryptographically strong random number generator (RNG).
import java.security.SecureRandom;

// This class provides the functionality of a cryptographic cipher for encryption and decryption. It forms the core of the Java Cryptographic Extension (JCE) framework.
import javax.crypto.Cipher;
// This interface contains no methods or constants. Its only purpose is to group (and provide type safety for) secret keys
import javax.crypto.SecretKey;
// This class represents a factory for secret keys.
import javax.crypto.SecretKeyFactory;
// This class specifies a DES key.
import javax.crypto.spec.DESKeySpec;

// Testing framework for Java
import org.testng.util.Strings;

// This class consists exclusively of static methods for obtaining encoders and decoders for the Base64 encoding scheme.
// Base64 是一種能將任意 Binary 資料用 64 種字元組合成字串的方法，而這個 Binary 資料和字串資料彼此之間是可以互相轉換的，十分方便。在實際應用上，Base64 除了能將 Binary 資料可視化之外，也常用來表示資料加密過後的內容。
import java.util.Base64;
// This class implements an encoder for encoding byte data using the Base64 encoding scheme as specified in RFC 4648 and RFC 2045.
import java.util.Base64.Encoder;
// This class implements a decoder for decoding byte data using the Base64 encoding scheme as specified in RFC 4648 and RFC 2045.
import java.util.Base64.Decoder;

// 基於 Cipher 實現的加密和解密工具
public class DeEnCoderCipherUtil {
	// 加密、解密模式
	private final static String CIPHER_MODE = "DES";
		
	// DES 密鑰
	public static String DEFAULT_DES_KEY = "區塊鏈是分布式數據儲存、點對點傳輸、共識機制、加密算法等計算機技術的新型應用模式";
	
	/**
	 * function 加密通用方法
	 * 
	 * @param originalContent 明文
	 * @param key 加密密鑰
	 * @return 密文
	 */
	public static String encrypt(String originalContent, String key) {
		// 明文或加密密鑰為空時
		if (Strings.isNullOrEmpty(originalContent) || Strings.isNullOrEmpty(key)) {
			return null;
		}
		
		// 明文或加密密鑰不為空時
		try {
			byte[] byteContent = encrypt(originalContent.getBytes(), key.getBytes());
			Encoder encoder = Base64.getEncoder();
			String result = encoder.encodeToString(byteContent);
			return result;
		} catch (Exception e) {
			e.printStackTrace();
		}
		return null;
	}
	
	/**
	 * function 解密通用方法
	 * 
	 * @param ciphertext 密文
	 * @param key DES 解密密鑰(同加密密鑰)
	 * @return 明文
	 */
	public static String decrypt(String ciphertext, String key) {
		// 密文或加密密鑰為空時
		if (Strings.isNullOrEmpty(ciphertext) || Strings.isNullOrEmpty(key)) {
			return null;
		}
		
		// 密文或加密密鑰不為空時
		try {
			Decoder decoder = Base64.getDecoder();
			byte[] bufCiphertext = decoder.decode(ciphertext);
			byte[] contentByte = decrypt(bufCiphertext, key.getBytes());
			return new String(contentByte);
		} catch (Exception e) {
			e.printStackTrace();
		}
		return null;
	}
	
	/**
	 * function 字節加密方法
	 * 
	 * @param originalContent 明文
	 * @param key 加密密鑰的byte數組
	 * @return 密文的byte數組
	 */
	private static byte[] encrypt(byte[] originalContent, byte[] key) throws Exception {
		// step1: 生成可信任的隨機數源
		SecureRandom secureRandom = new SecureRandom();
		
		// step2: 基於密鑰數據創建 DESKeySpec 對象
		DESKeySpec desKeySpec = new DESKeySpec(key);
		
		// step3: 創建密鑰工廠，將 DESKeySpec 轉換成 SecretKey 對象來保存對稱密鑰
		SecretKeyFactory keyFactory = SecretKeyFactory.getInstance(CIPHER_MODE);
		SecretKey securetKey = keyFactory.generateSecret(desKeySpec);
		
		// step4: Cipher 對象實際完成加密操作，指定其支持指定的加密和解密算法
		Cipher cipher = Cipher.getInstance(CIPHER_MODE);
		
		// step5: 用密鑰初始化 Cipher 對象，ENCRYPT_MODE 表示加密模式
		cipher.init(Cipher.ENCRYPT_MODE, securetKey, secureRandom);
		
		// 返回密文
		return cipher.doFinal(originalContent);
	}
	
	/**
	 * function 字節解密方法
	 * 
	 * @param ciphertextByte 字節密文
	 * @param key 解密密鑰(同加密密鑰)byte數組
	 * @return 明文byte數組
	 */
	private static byte[] decrypt(byte[] ciphertextByte, byte[] key) throws Exception {
		// step1: 生成可信任的隨機數源
		SecureRandom secureRandom = new SecureRandom();
		
		// step2: 從原始密鑰數據創建 DESKeySpec 對象
		DESKeySpec desKeySpec = new DESKeySpec(key);
		
		// step3: 創建密鑰工廠，將 DESKeySpec 轉換成 SecretKey 對象來保存對稱密鑰
		SecretKeyFactory keyFactory = SecretKeyFactory.getInstance(CIPHER_MODE);
		SecretKey securetKey = keyFactory.generateSecret(desKeySpec);
		
		// step4: Cipher 對象實際完成解密操作，指定其支持響應的加密和解密算法
		Cipher cipher = Cipher.getInstance(CIPHER_MODE);
		
		// step5: 用密鑰初始化Cipher對象，DECRYPT_MODE 表示解密模式
		cipher.init(Cipher.DECRYPT_MODE, securetKey, secureRandom);
		
		// 返回明文
		return cipher.doFinal(ciphertextByte);
	}
}

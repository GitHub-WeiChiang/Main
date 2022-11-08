/**
 * 
 * @author ChiangWei
 * @date 2022/03/29
 *
 */

package com.example.demo.util;

// The Character Encoding is not supported.
import java.io.UnsupportedEncodingException;
// provides applications the functionality of a message digest algorithm, such as SHA-1 or SHA-256.
import java.security.MessageDigest;
// This exception is thrown when a particular cryptographic algorithm is requested but is not available in the environment.
import java.security.NoSuchAlgorithmException;
// Converts hexadecimal Strings. The Charset used for certain operation can be set, the default is set in DEFAULT_CHARSET_NAME This class is thread-safe.
import org.apache.commons.codec.binary.Hex;
// 摘要算法工具類
import cn.hutool.crypto.digest.DigestUtil;

public class SHAUtil {
	
	/**
	 * 利用 Apache commons-codec 的工具類實現 SHA - 256 加密
	 * 
	 * @param originalStr 加密前的報文 / 封包 (報文是網路中交換與傳輸的數據單元，即站點一次性要發送的數據塊。報文包含了將要發送的完整的數據信息，其長短很不一致，長度不限且可變。)
	 * @return String 加密後的報文
	 */
	public static String getSHA256BasedMD(String originalStr) {
		MessageDigest messageDigest;
		String encdeStr = "";
		try {
			messageDigest = MessageDigest.getInstance("SHA-256");
			byte[] hash = messageDigest.digest(originalStr.getBytes("UTF-8"));
			encdeStr = Hex.encodeHexString(hash);
		} catch (NoSuchAlgorithmException e) {
			e.printStackTrace();
		} catch (UnsupportedEncodingException e) {
			e.printStackTrace();
		}
		return encdeStr;
	}
	
	/**
	 * 利用 Hutool 的工具類實現 SHA - 256 加密
	 * 
	 * @param originalStr 加密前的報文
	 * @return String 加密後的報文
	 */
	public static String sha256BasedHutool(String originalStr) {
		return DigestUtil.sha256Hex(originalStr);
	}
}

/**
 * 
 * @author ChiangWei
 * @date 2020/4/26
 *
 */

import java.io.IOException;
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
import java.util.Base64;
// This class implements an encoder for encoding byte data using the Base64 encoding scheme as specified in RFC 4648 and RFC 2045.
import java.util.Base64.Encoder;
// This class implements a decoder for decoding byte data using the Base64 encoding scheme as specified in RFC 4648 and RFC 2045.
import java.util.Base64.Decoder;

// ��� Cipher ��{���[�K�M�ѱK�u��
public class DeEnCoderCipherUtil {
	// �[�K�B�ѱK�Ҧ�
	private final static String CIPHER_MODE = "DES";
	
	// DES �K�_
	public static String DEFAULT_DES_KEY = "�϶���O�������ƾ��x�s�B�I���I�ǿ�B�@�Ѿ���B�[�K��k���p����޳N���s�����μҦ�";
	
	/**
	 * function �[�K�q�Τ�k
	 * 
	 * @param originalContent ����
	 * @param key �[�K�K�_
	 * @return �K��
	 */
	public static String encrypt(String originalContent, String key) {
		// ����Υ[�K�K�_���Ů�
		if (Strings.isNullOrEmpty(originalContent) || Strings.isNullOrEmpty(key)) {
			return null;
		}
		
		// ����Υ[�K�K�_�����Ů�
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
	 * function �ѱK�q�Τ�k
	 * 
	 * @param ciphertext �K��
	 * @param key DES �ѱK�K�_(�P�[�K�K�_)
	 * @return ����
	 */
	public static String decrypt(String ciphertext, String key) {
		// �K��Υ[�K�K�_���Ů�
		if (Strings.isNullOrEmpty(ciphertext) || Strings.isNullOrEmpty(key)) {
			return null;
		}
		
		// �K��Υ[�K�K�_�����Ů�
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
	 * function �r�`�[�K��k
	 * 
	 * @param originalContent ����
	 * @param key �[�K�K�_��byte�Ʋ�
	 * @return �K�媺byte�Ʋ�
	 */
	private static byte[] encrypt(byte[] originalContent, byte[] key) throws Exception {
		// step1: �ͦ��i�H�����H���Ʒ�
		SecureRandom secureRandom = new SecureRandom();
		
		// step2: ���K�_�ƾڳЫ�DESKeySpec��H
		DESKeySpec desKeySpec = new DESKeySpec(key);
		
		// step3: �ЫرK�_�u�t�A�NDESKeySpec�ഫ��SecretKey��H�ӫO�s��٥[�K
		SecretKeyFactory keyFactory = SecretKeyFactory.getInstance(CIPHER_MODE);
		SecretKey secretKey = keyFactory.generateSecret(desKeySpec);
		
		// step4: Cipher��H��ڧ����[�K�ާ@�A���w�������w���[�K�M�ѱK��k
		Cipher cipher = Cipher.getInstance(CIPHER_MODE);
		
		// step5: �αK�_��l��Cipher��H�AENCRYPT_MODE��ܥ[�K�Ҧ�
		cipher.init(Cipher.ENCRYPT_MODE, secretKey, secureRandom);
		
		// ��^�K��
		return cipher.doFinal(originalContent);
	}
}

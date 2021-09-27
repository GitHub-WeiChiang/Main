/**
 * 
 * @author ChiangWei
 * @date 2020/4/27
 *
 */

// A private key. The purpose of this interface is to group (and provide type safety for) all private key interfaces.
import java.security.PrivateKey;
// A public key. This interface contains no methods or constants. It merely serves to group (and provide type safety for) all public key interfaces.
import java.security.PublicKey;
//Testing framework for Java
import org.testng.util.Strings;

// �r�Ŷ��u����
import cn.hutool.core.util.CharsetUtil;
// �r�Ŧ�u����
import cn.hutool.core.util.StrUtil;
// �w�������u�����A�[�K�����T��:
// 1�B��٥[�K�]symmetric�^�A�Ҧp�GAES�BDES��
// 2�B�D��٥[�K�]asymmetric�^�A�Ҧp�GRSA�BDSA��
// 3�B�K�n�[�K�]digest�^�A�Ҧp�GMD5�BSHA-1�BSHA-256�BHMAC��
import cn.hutool.crypto.SecureUtil;
// �K�_����
import cn.hutool.crypto.asymmetric.KeyType;
// RSA���_/�p�_/ñ�W�[�K�ѱK
// �ѩ�D��٥[�K�t�׷���w�C�A�@���󤣨ϥΥ��ӥ[�K�ӬO�ϥι�٥[�K�A�D��٥[�K��k�i�H�Ψӹ��٥[�K���K�_�[�K�A�o�˫O�ұK�_���w���]�N�O�ҤF�ƾڪ��w��
import cn.hutool.crypto.asymmetric.RSA;
// AES�[�K��k��{
// ���ť[�K�зǡ]�^�y�GAdvanced Encryption Standard�A�Y�g�GAES�^�A�b�K�X�Ǥ��S��Rijndael�[�K�k���Java��AES���q�{�Ҧ��O�GAES/ECB/PKCS5Padding�A�p�G�ϥ�CryptoJS�A�нվ㬰�Gpadding: CryptoJS.pad.Pkcs7
import cn.hutool.crypto.symmetric.AES;
// DES�[�K��k��{
// DES���٬�Data Encryption Standard�A�Y�ƾڥ[�K�зǡA�O�@�بϥαK�_�[�K������kJava���q�{��{���GDES/CBC/PKCS5Padding
import cn.hutool.crypto.symmetric.DES;
// ��ٺ�k����
import cn.hutool.crypto.symmetric.SymmetricAlgorithm;

// ��� Hutool �u�������[�K�ѱK��
public class DeEnCoderHutoolUtil {
	// �c�� RSA ��H
	private static RSA rsa = new RSA();
	// ��o�p�_
	private static PrivateKey privateKey = rsa.getPrivateKey();
	// ��o���_
	private static PublicKey publicKey = rsa.getPublicKey();
	
	/**
	 * function RSA �[�K�q�Τ�k: ����٥[�K�ѱK
	 * 
	 * @param originalContent: ����
	 * @return �K��
	 */
	public static String rsaEncrypt(String originalContent) {
		// ���嬰�Ů�
		if (Strings.isNullOrEmpty(originalContent)) {
			return null;
		}
		
		// ���_�[�K�A����p�_�ѱK
		return rsa.encryptBase64(originalContent, KeyType.PublicKey);
	}
	
	/**
	 * function RSA �ѱK�q�Τ�k: ����٥[�K�ѱK
	 * 
	 * @param ciphertext �K��
	 * @return ����
	 */
	public static String rsaDecrypt(String ciphertext) {
		// �K�嬰�Ů�
		if (Strings.isNullOrEmpty(ciphertext)) {
			return null;
		}
		
		return rsa.decryptStr(ciphertext, KeyType.PrivateKey);
	}
	
	/**
	 * function DES �[�K�q�Τ�k: ��٥[�K�ѱK
	 * 
	 * @param originalContent: ����
	 * @param key �[�K�K�_
	 * @return �K��
	 */
	public static String desEncrypt(String originalContent, String key) {
		// ����Υ[�K�K�_���Ů�
		if (Strings.isNullOrEmpty(originalContent) || Strings.isNullOrEmpty(key)) {
			return null;
		}
		
		// �٥i�H�H���ͦ��K�_
		// byte[] key = SecureUtil.generateKey(SymmetricAlgorithm.DES.getValue()).getEncoded();
		
		// �c��
		DES des = SecureUtil.des(key.getBytes());
		
		// �[�K
		return des.encryptHex(originalContent);
	}
	
	/**
	 * function DES �ѱK�q�Τ�k: ��٥[�K�ѱK
	 * 
	 * @param ciphertext �K��
	 * @param key DES �ѱK�K�_(�P�[�K�K�_)
	 * @return ����
	 */
	public static String desDecrypt(String ciphertext, String key) {
		// �K��θѱK�K�_���Ů�
		if (Strings.isNullOrEmpty(ciphertext) || Strings.isNullOrEmpty(key)) {
			return null;
		}
		
		// �٥i�H�H���ͦ��K�_
		// byte[] key = SecureUtil.generateKey(SymmetricAlgorithm.DES.getValue()).getEncoded();
		
		// �c��
		DES des = SecureUtil.des(key.getBytes());
		
		// �ѱK
		return des.decryptStr(ciphertext);
	}
}

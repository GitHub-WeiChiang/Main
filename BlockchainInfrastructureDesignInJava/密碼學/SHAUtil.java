/**
 * 
 * @author ChiangWei
 * @date 2020/5/7
 *
 */

// The Character Encoding is not supported.
import java.io.UnsupportedEncodingException;
// provides applications the functionality of a message digest algorithm, such as SHA-1 or SHA-256.
import java.security.MessageDigest;
// This exception is thrown when a particular cryptographic algorithm is requested but is not available in the environment.
import java.security.NoSuchAlgorithmException;
// Converts hexadecimal Strings. The Charset used for certain operation can be set, the default is set in DEFAULT_CHARSET_NAME This class is thread-safe.
import org.apache.commons.codec.binary.Hex;
// �K�n��k�u����
import cn.hutool.crypto.digest.DigestUtil;

public class SHAUtil {
	
	/**
	 * �Q�� Apache commons-codec ���u������{ SHA - 256 �[�K
	 * 
	 * @param originalStr �[�K�e������ / �ʥ] (����O�������洫�P�ǿ骺�ƾڳ椸�A�Y���I�@���ʭn�o�e���ƾڶ��C����]�t�F�N�n�o�e�����㪺�ƾګH���A����u�ܤ��@�P�A���פ����B�i�ܡC)
	 * @return String �[�K�᪺����
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
}

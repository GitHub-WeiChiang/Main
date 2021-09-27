/**
 * 
 * @author ChiangWei
 * @date 2020/4/28
 *
 */

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

//�w�������u�����A�[�K�����T��:
//1�B��٥[�K�]symmetric�^�A�Ҧp�GAES�BDES��
//2�B�D��٥[�K�]asymmetric�^�A�Ҧp�GRSA�BDSA��
//3�B�K�n�[�K�]digest�^�A�Ҧp�GMD5�BSHA-1�BSHA-256�BHMAC��
import cn.hutool.crypto.SecureUtil;
//��ٺ�k����
import cn.hutool.crypto.symmetric.SymmetricAlgorithm;

class DeEnCoderHutoolUtilTest {

	@Test
	void testDesEncrypt() {
		// case1: String originalContent = null, String key = null
		String originalContent = null, key = null;
		assertEquals(DeEnCoderHutoolUtil.desEncrypt(originalContent, key), null);
		
		// case2: String originalContent != null, String key = null
		originalContent = "2019���ն�۸u�}�Ұ�!";
		assertEquals(DeEnCoderHutoolUtil.desEncrypt(originalContent, key), null);
		
		// case3: String originalContent = null, String key != null
		originalContent = null;
		key = "2019���ն�۸u�}�Ұ�!����²�����L�ӧr!";
		assertEquals(DeEnCoderHutoolUtil.desEncrypt(originalContent, key), null);
		
		// case4: String originalContent != null, String key != null
		originalContent = "2019���ն�۸u�}�Ұ�!";
		key = new String(SecureUtil.generateKey(SymmetricAlgorithm.DES.getValue()).getEncoded());
		assertNotNull(DeEnCoderHutoolUtil.desEncrypt(originalContent, key));
	}
	
	@Test
	public void testDesDecrypt() {
		// case1: String ciphertext = null, String key = null
		String ciphertext = null, key = null;
		assertEquals(DeEnCoderHutoolUtil.desDecrypt(ciphertext, key), null);
		
		// case2: String ciphertext != null, String key = null
		String originalContent = "2019���ն�۸u�}�Ұ�!";
		String keyTmp = new String(SecureUtil.generateKey(SymmetricAlgorithm.DES.getValue()).getEncoded());
		ciphertext = DeEnCoderHutoolUtil.desEncrypt(originalContent, keyTmp);
		assertEquals(DeEnCoderHutoolUtil.desDecrypt(ciphertext, key), null);
		
		// case3: String ciphertext = null, String key != null
		ciphertext = null;
		key = new String(SecureUtil.generateKey(SymmetricAlgorithm.DES.getValue()).getEncoded());
		assertEquals(DeEnCoderHutoolUtil.desDecrypt(ciphertext, key), null);
		
		//case4: String ciphertext != null, String key != null
		ciphertext = DeEnCoderHutoolUtil.desEncrypt(originalContent, key);
		assertNotNull(DeEnCoderHutoolUtil.desDecrypt(ciphertext, key));
	}
}

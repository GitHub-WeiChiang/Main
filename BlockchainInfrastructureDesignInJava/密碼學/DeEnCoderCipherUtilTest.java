/**
 * 
 * @author ChiangWei
 * @date 2020/4/27
 *
 */

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

class DeEnCoderCipherUtilTest {
	private static String ciphertextGlobal;
	
	@Test
	void testEncrypt() {
		// case1: originalContent = null; key = null;
		String originalContent = null;
		String key = null;
		assertEquals(DeEnCoderCipherUtil.encrypt(originalContent, key), null);
		
		// case2: originalContent != null; key = null;
		originalContent = "2019©¡®Õ¶é©Û¸u¶}±Ò°Õ!";
		key = null;
		assertEquals(DeEnCoderCipherUtil.encrypt(originalContent, key), null);
		
		// case3: originalContent = null; key != null;
		originalContent = null;
		key = "2019©¡®Õ¶é©Û¸u¶}±Ò°Õ!¤º±ÀÂ²¾ú¥µ¹L¨Ó§r!";
		assertEquals(DeEnCoderCipherUtil.encrypt(originalContent, key), null);
		
		// case4: originalContent != null; key != null;
		originalContent = "2019©¡®Õ¶é©Û¸u¶}±Ò°Õ!";
		key = "2019©¡®Õ¶é©Û¸u¶}±Ò°Õ!¤º±ÀÂ²¾ú¥µ¹L¨Ó§r!";
		ciphertextGlobal = DeEnCoderCipherUtil.encrypt(originalContent, key);
		assertEquals(ciphertextGlobal, "Gt3qUbOkIX2460sXmyCIB4skE3SrCegg");
	}
	
	@Test
	void testDecrypt() {
		// case1: String ciphertext = null, String key = null
		String ciphertext = null, key = null;
		assertEquals(DeEnCoderCipherUtil.decrypt(ciphertext, key), null);
		
		// case2: String ciphertext != null, String key = null
		ciphertext = ciphertextGlobal;
		assertEquals(DeEnCoderCipherUtil.decrypt(ciphertext, key), null);
		
		// case2: String ciphertext = null, String key != null
		ciphertext = null;
		key = "2019©¡®Õ¶é©Û¸u¶}±Ò°Õ!¤º±ÀÂ²¾ú¥µ¹L¨Ó§r!";
		assertEquals(DeEnCoderCipherUtil.decrypt(ciphertext, key), null);
		
		// case2: String ciphertext != null, String key != null
		ciphertext = ciphertextGlobal;
		key = "2019©¡®Õ¶é©Û¸u¶}±Ò°Õ!¤º±ÀÂ²¾ú¥µ¹L¨Ó§r!";
		assertEquals(DeEnCoderCipherUtil.decrypt(ciphertext, key), "2019©¡®Õ¶é©Û¸u¶}±Ò°Õ!");
	}
}

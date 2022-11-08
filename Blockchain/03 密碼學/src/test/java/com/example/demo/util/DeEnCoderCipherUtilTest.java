/**
 * 
 * @author ChiangWei
 * @date 2022/03/16
 *
 */

package com.example.demo.util;

import org.testng.annotations.Test;
import org.testng.Assert;

public class DeEnCoderCipherUtilTest {
	private static String ciphertextGlobal;
	
	@Test
	void testEncrypt() {
		// case1: originalContent = null; key = null;
		String originalContent = null;
		String key = null;
		Assert.assertEquals(DeEnCoderCipherUtil.encrypt(originalContent, key), null);
		
		// case2: originalContent != null; key = null;
		originalContent = "2019屆校園招聘開啟啦!";
		key = null;
		Assert.assertEquals(DeEnCoderCipherUtil.encrypt(originalContent, key), null);
		
		// case3: originalContent = null; key != null;
		originalContent = null;
		key = "2019屆校園招聘開啟啦!內推簡歷扔過來呀!";
		Assert.assertEquals(DeEnCoderCipherUtil.encrypt(originalContent, key), null);
		
		// case4: originalContent != null; key != null;
		originalContent = "2019屆校園招聘開啟啦!";
		key = "2019屆校園招聘開啟啦!內推簡歷扔過來呀!";
		ciphertextGlobal = DeEnCoderCipherUtil.encrypt(originalContent, key);
		Assert.assertEquals(ciphertextGlobal, "Gt3qUbOkIX2460sXmyCIB4skE3SrCegg");
	}
	
	@Test(dependsOnMethods = {"testEncrypt"})
	void testDecrypt() {
		// case1: String ciphertext = null, String key = null
		String ciphertext = null, key = null;
		Assert.assertEquals(DeEnCoderCipherUtil.decrypt(ciphertext, key), null);
		
		// case2: String ciphertext != null, String key = null
		ciphertext = ciphertextGlobal;
		Assert.assertEquals(DeEnCoderCipherUtil.decrypt(ciphertext, key), null);
		
		// case2: String ciphertext = null, String key != null
		ciphertext = null;
		key = "2019屆校園招聘開啟啦!內推簡歷扔過來呀!";
		Assert.assertEquals(DeEnCoderCipherUtil.decrypt(ciphertext, key), null);
		
		// case2: String ciphertext != null, String key != null
		ciphertext = ciphertextGlobal;
		key = "2019屆校園招聘開啟啦!內推簡歷扔過來呀!";
		Assert.assertEquals(DeEnCoderCipherUtil.decrypt(ciphertext, key), "2019屆校園招聘開啟啦!");
	}
}

/**
 * 
 * @author ChiangWei
 * @date 2022/03/17
 *
 */

package com.example.demo.util;

import org.testng.annotations.Test;
import org.testng.Assert;

// 安全相關工具類，加密分為三種:
// 1、對稱加密（symmetric），例如：AES、DES等
// 2、非對稱加密（asymmetric），例如：RSA、DSA等
// 3、摘要加密（digest），例如：MD5、SHA-1、SHA-256、HMAC等
import cn.hutool.crypto.SecureUtil;
// 對稱算法類型
import cn.hutool.crypto.symmetric.SymmetricAlgorithm;

public class DeEnCoderHutoolUtilTest {
	@Test
	public void testDesEncrypt() {
		// case1: String originalContent = null, String key = null
		String originalContent = null, key = null;
		Assert.assertEquals(DeEnCoderHutoolUtil.desEncrypt(originalContent, key), null);
		
		// case2: String originalContent != null, String key = null
		originalContent = "2019屆校園招聘開啟啦!";
		Assert.assertEquals(DeEnCoderHutoolUtil.desEncrypt(originalContent, key), null);
		
		// case3: String originalContent = null, String key != null
		originalContent = null;
		key = "2019屆校園招聘開啟啦!內推簡歷扔過來呀!";
		Assert.assertEquals(DeEnCoderHutoolUtil.desEncrypt(originalContent, key), null);
		
		// case4: String originalContent != null, String key != null
		originalContent = "2019屆校園招聘開啟啦!";
		key = new String(SecureUtil.generateKey(SymmetricAlgorithm.DES.getValue()).getEncoded());
		Assert.assertNotNull(DeEnCoderHutoolUtil.desEncrypt(originalContent, key));
	}
	
	@Test
	public void testDesDecrypt() {
		// case1: String ciphertext = null, String key = null
		String ciphertext = null, key = null;
		Assert.assertEquals(DeEnCoderHutoolUtil.desDecrypt(ciphertext, key), null);
		
		// case2: String ciphertext != null, String key = null
		String originalContent = "2019屆校園招聘開啟啦!";
		String keyTmp = new String(SecureUtil.generateKey(SymmetricAlgorithm.DES.getValue()).getEncoded());
		ciphertext = DeEnCoderHutoolUtil.desEncrypt(originalContent, keyTmp);
		Assert.assertEquals(DeEnCoderHutoolUtil.desDecrypt(ciphertext, key), null);
		
		// case3: String ciphertext = null, String key != null
		ciphertext = null;
		key = new String(SecureUtil.generateKey(SymmetricAlgorithm.DES.getValue()).getEncoded());
		Assert.assertEquals(DeEnCoderHutoolUtil.desDecrypt(ciphertext, key), null);
		
		//case4: String ciphertext != null, String key != null
		ciphertext = DeEnCoderHutoolUtil.desEncrypt(originalContent, key);
		Assert.assertNotNull(DeEnCoderHutoolUtil.desDecrypt(ciphertext, key));
	}
}

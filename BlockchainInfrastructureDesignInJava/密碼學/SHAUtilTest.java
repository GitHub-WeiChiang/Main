/**
 * 
 * @author ChiangWei
 * @date 2020/5/9
 * @other SHAUtil 測試類
 *
 */

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

class SHAUtilTest {

	// 測試 getSHA256 方法
	@Test
	void testGetSHA256() {
		String originalStr = "區塊鏈是分布式數據結構、點對點傳輸、共識機制、加密算法等計算機技術的新型應用模式。";
		assertEquals("46a3f742aacd4aadbeee27a210072894d03c43e90955827cf2b7be843d841b91", SHAUtil.getSHA256BasedMD(originalStr));
	}
	
	// 測試 getSHA256 方法
	@Test
	void testSha256BasedHutool() {
		String originalStr = "區塊鏈是分布式數據結構、點對點傳輸、共識機制、加密算法等計算機技術的新型應用模式。";
		assertEquals("46a3f742aacd4aadbeee27a210072894d03c43e90955827cf2b7be843d841b91", SHAUtil.sha256BasedHutool(originalStr));
	}
}

/**
 * 
 * @author ChiangWei
 * @date 2020/5/9
 * @other SHAUtil ������
 *
 */

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

class SHAUtilTest {

	// ���� getSHA256 ��k
	@Test
	void testGetSHA256() {
		String originalStr = "�϶���O�������ƾڵ��c�B�I���I�ǿ�B�@�Ѿ���B�[�K��k���p����޳N���s�����μҦ��C";
		assertEquals("46a3f742aacd4aadbeee27a210072894d03c43e90955827cf2b7be843d841b91", SHAUtil.getSHA256BasedMD(originalStr));
	}
	
	// ���� getSHA256 ��k
	@Test
	void testSha256BasedHutool() {
		String originalStr = "�϶���O�������ƾڵ��c�B�I���I�ǿ�B�@�Ѿ���B�[�K��k���p����޳N���s�����μҦ��C";
		assertEquals("46a3f742aacd4aadbeee27a210072894d03c43e90955827cf2b7be843d841b91", SHAUtil.sha256BasedHutool(originalStr));
	}
}

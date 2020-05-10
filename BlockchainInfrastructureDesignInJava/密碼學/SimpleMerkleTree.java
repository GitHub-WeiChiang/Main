/**
 * 
 * @author ChiangWei
 * @date 2020/5/10
 *
 */

import java.util.ArrayList;
import java.util.List;

// ²�ƪ� Merkle ��ڸ`�I����ȭp��
public class SimpleMerkleTree {
	
	// �� Merkle ���Q�p���`�I���ƭ�
	public static String getTreeNodeHash(List<String> hashList) {
		if(hashList == null || hashList.size() == 0) {
			return null;
		}
		
		while (hashList.size() != 1) {
			hashList = getMerkleNodeList(hashList);
		}
		
		return hashList.get(0);
	}
	
	// �� Merkle ���Q�p���`�I���ƭ�
	public static List<String> getMerkleNodeList(List<String> contentList) {
		List<String> merkleNodeList = new ArrayList<String>();
		
		if (contentList == null || contentList.size() == 0) {
			return merkleNodeList;
		}
		
		int index = 0, length = contentList.size();
		while (index < length) {
			// ������Ĥl�`�I�ƾ�
			String left = contentList.get(index++);
			
			// ����k�Ĥl�`�I�ƾ�
			String right = "";
			if (index < length) {
				right = contentList.get(index++);
			}
			
			// �p�⥪�k�Ĥl�`�I�����`�I���ƭ�
			String sha2HexValue = SHAUtil.sha256BasedHutool(left + right);
			merkleNodeList.add(sha2HexValue);
		}
		return merkleNodeList;
	}
	
}

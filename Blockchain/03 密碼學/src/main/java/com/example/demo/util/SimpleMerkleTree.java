/**
 * 
 * @author ChiangWei
 * @date 2022/03/30
 *
 */

package com.example.demo.util;

import java.util.ArrayList;
import java.util.List;

// 簡化的 Merkle 樹根節點雜湊值計算
public class SimpleMerkleTree {
	// 按 Merkle 樹思想計算跟節點哈希值
	public static String getTreeNodeHash(List<String> hashList) {
		if(hashList == null || hashList.size() == 0) {
			return null;
		}
		
		while (hashList.size() != 1) {
			hashList = getMerkleNodeList(hashList);
		}
		
		return hashList.get(0);
	}
	
	// 按 Merkle 樹思想計算跟節點哈希值
	public static List<String> getMerkleNodeList(List<String> contentList) {
		List<String> merkleNodeList = new ArrayList<String>();
		
		if (contentList == null || contentList.size() == 0) {
			return merkleNodeList;
		}
		
		int index = 0, length = contentList.size();
		while (index < length) {
			// 獲取左孩子節點數據
			String left = contentList.get(index++);
			
			// 獲取右孩子節點數據
			String right = "";
			if (index < length) {
				right = contentList.get(index++);
			}
			
			// 計算左右孩子節點的父節點哈希值
			String sha2HexValue = SHAUtil.sha256BasedHutool(left + right);
			merkleNodeList.add(sha2HexValue);
		}
		return merkleNodeList;
	}
}

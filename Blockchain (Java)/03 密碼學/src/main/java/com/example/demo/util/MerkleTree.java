/**
 * 
 * @author ChiangWei
 * @date 2022/03/30
 *
 */

package com.example.demo.util;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

// MerkleTree 建構、生成根節點哈希值的工具類
public class MerkleTree {
	// TreeNode List
	private List<TreeNode> list;
	// 根結點
	private TreeNode root;
	
	// 構造函數
	public MerkleTree(List<String> contents) {
		createMerkleTree(contents);
	}
	
	// 建構 Merkle Tree
	private void createMerkleTree(List<String> contents) {
		// 輸入為空則不進行任何處理
		if (contents == null || contents.size() == 0) {
			return;
		}
		
		// 初始化
		list = new ArrayList<>();
		
		// 根據數據創建葉子節點
		List<TreeNode> leafList = createLeafList(contents);
		list.addAll(leafList);
		
		// 創建父節點
		List<TreeNode> parents = createParentList(leafList);
		list.addAll(parents);
		
		// 循環創建各級父節點至根節點
		while (parents.size() > 1) {
			List<TreeNode> temp = createParentList(parents);
			list.addAll(temp);
			parents = temp;
		}
		
		root = parents.get(0);
	}
	
	// 創建父節點列表
	private List<TreeNode> createParentList(List<TreeNode> leafList) {
		List<TreeNode> parents = new ArrayList<>();
		
		// 空檢驗
		if (leafList == null || leafList.size() == 0) {
			return parents;
		}
		
		int length = leafList.size();
		for (int i = 0; i < length - 1; i += 2) {
			TreeNode parent = createParentNode(leafList.get(i), leafList.get(i + 1));
			parents.add(parent);
		}
		
		// 奇數個節點時，單獨處理最後一個節點
		if (length % 2 != 0) {
			TreeNode parent = createParentNode(leafList.get(length - 1), null);
			parents.add(parent);
		}
		
		return parents;
	}
	
	// 創建父節點
	private TreeNode createParentNode(TreeNode left, TreeNode right) {
		TreeNode parent = new TreeNode();
		
		parent.setLeft(left);
		parent.setRight(right);
		
		// 如果 right 為空，責父節點的哈希值為 left 的哈希值
		String hash = left.getHash();
		if (right != null) {
			hash = SHAUtil.sha256BasedHutool(left.getHash() + right.getHash());
		}
		// hash 字段和 data 字段同值
		parent.setData(hash);
		parent.setHash(hash);
		
		if (right != null) {
			parent.setName("(" + left.getName() + "和" + right.getName() + "的父節點)");
		} else {
			parent.setName("(繼承節點{" + left.getName() + "}成為父節點)");
		}
		
		return parent;
	}
	
	// 構建葉子節點列表
	private List<TreeNode> createLeafList(List<String> contents) {
		List<TreeNode> leafList = new ArrayList<>();
		
		// 空檢驗
		if (contents == null || contents.size() == 0) {
			return leafList;
		}
		
		for (String content : contents) {
			TreeNode node = new TreeNode(content);
			leafList.add(node);
		}
		
		return leafList;
	}
	
	// 遍歷樹
	public void traverseTreeNodes() {
		Collections.reverse(list);
		TreeNode root = list.get(0);
		traverseTreeNodes(root);
	}
	
	private void traverseTreeNodes(TreeNode node) {
		System.out.println(node.getName());
		
		if (node.getLeft() != null) {
			traverseTreeNodes(node.getLeft());
		}
		
		if (node.getRight() != null) {
			traverseTreeNodes(node.getRight());
		}
	}
	
	public List<TreeNode> getList() {
		if (list == null) {
			return list;
		}
		Collections.reverse(list);
		return list;
	}
	
	public void setList(List<TreeNode> list) {
		this.list = list;
	}
	
	public TreeNode getRoot() {
		return root;
	}
	
	public void setRoot(TreeNode root) {
		this.root = root;
	}
}
